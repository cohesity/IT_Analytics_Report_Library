"""
Turns export/reports.json + export/content/{id}/meta.json (locally-added
reports) + export/content/{id}/ (template/sample/thumbnail files) into the
Jekyll site: _reports/, _products/, _categories/, reports/, and
assets/search-index.json.

Idempotent: every write goes through write_if_changed/sync_dir, so re-running
this after a small edit (one report's description, one new report) only
touches the files that actually changed - this is what keeps the local Jekyll
dev server's rebuilds fast instead of reprocessing the whole site every time.

Product/category lists are hardcoded below rather than queried from a live
system, since the source Oracle environment (RTD_PRODUCT/RTD_CATEGORY) has
been deprecated. export/reports.json is now a frozen, committed snapshot of
the legacy Oracle-sourced reports; new reports are added via
scripts/new_report.py, which writes a self-contained
export/content/{id}/meta.json instead of touching that snapshot.

Optional per-report descriptions/{report_id}.md overlay is merged in as the
Jekyll page body if present - see README for the authoring workflow.

Run: python build_site_content.py
"""
import glob
import json
import os
import re
import shutil
import xml.etree.ElementTree as ET

ROOT = os.path.join(os.path.dirname(__file__), "..")
EXPORT_DIR = os.path.join(ROOT, "export")
DESCRIPTIONS_DIR = os.path.join(ROOT, "descriptions")

# (product_id, section, component, legacy_display_order). Excludes
# product_id 14 ("Drilldown Components / General") - an internal grouping
# not shown on the live public site's nav. The 4th field is the original
# RTD_PRODUCT.DISPLAY_ORDER value, captured for history but no longer used -
# build_products() computes each product's actual on-site display_order
# itself (PINNED_PRODUCTS first, then alphabetical within each section).
PRODUCTS = [
    (1, "Capacity Manager", "Host Probe Reports", 6),
    (2, "Capacity Manager", "General (All Storage Vendors)", 1),
    (3, "Capacity Manager", "EMC Reports", 2),
    (4, "Capacity Manager", "HDS Reports", 4),
    (5, "Virtualization", "VMware", 3),
    (6, "Backup Manager", "General (All Backup Vendors)", 2),
    (7, "Backup Manager", "EMC Avamar", 3),
    (8, "Backup Manager", "Veritas NetBackup", 7),
    (9, "Backup Manager", "IBM Spectrum Protect (TSM)", 9),
    (10, "Backup Manager", "EMC NetWorker (Legato)", 6),
    (11, "Public Cloud", "Azure", 5),
    (12, "Fabric Manager", "General", 6),
    (13, "Misc Utilities", "General", 21),
    (16, "Fabric Manager", "Brocade", 7),
    (17, "Fabric Manager", "Cisco", 8),
    (19, "Backup Manager", "HPDP", 6),
    (20, "Backup Manager", "CommVault", 4),
    (21, "File Analytics", "General", 12),
    (22, "Capacity Manager", "NetApp Reports (7 Mode)", 8),
    (23, "Backup Manager", "EMC Data Domain", 5),
    (24, "Capacity Manager", "HDS HNAS", 3),
    (25, "Capacity Manager", "HPE 3PAR", 5),
    (26, "Capacity Manager", "NetApp C-Mode", 7),
    (27, "Backup Manager", "Veeam", 9),
    (28, "Backup Manager", "Rubrik", 6),
    (29, "Backup Manager", "COHESITY", 4),
    (30, "Backup Manager", "Oracle RMAN", 7),
    (31, "Virtualization", "Microsoft Hyper-V", 2),
    (32, "Backup Manager", "Veritas Backup Exec", 9),
    (33, "Public Cloud", "AWS", 5),
    (34, "Backup Manager", "Veritas Flex Appliance", 8),
]

# Products pinned to the top of their section's list, ahead of the
# otherwise-alphabetical rest. (section, component) pairs.
PINNED_PRODUCTS = {
    ("Backup Manager", "General (All Backup Vendors)"),
}

CATEGORIES = [
    (1, "Consolidated Visibility"),
    (2, "Risk Mitigation/Ransomware"),
    (3, "Chargeback/Metering"),
    (4, "Utilization/Optimization"),
    (5, "Trending/Forecasting/Capacity Planning"),
    (6, "Auditing/Compliance/Governance"),
    (7, "OpsCenter Reports"),
]


def slugify(text):
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "misc"


def yaml_str(value):
    return json.dumps(value or "")


def _read_existing(path, binary):
    if not os.path.isfile(path):
        return None
    if binary:
        with open(path, "rb") as f:
            return f.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_if_changed(path, content):
    """content: str or bytes. Skips the write if the file already has this
    exact content, so unrelated files never have their mtime touched -
    that's what lets Jekyll's file watcher (and --incremental) see only the
    files that actually changed instead of the whole site every run."""
    binary = isinstance(content, bytes)
    if _read_existing(path, binary) == content:
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if binary:
        with open(path, "wb") as f:
            f.write(content)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    return True


def sync_dir(out_dir, desired):
    """desired: {filename: content (str or bytes)}. Writes only changed/new
    entries, then deletes any existing file in out_dir not present in
    desired (handles renames/removals with no special-casing). Returns
    (written, deleted) counts."""
    os.makedirs(out_dir, exist_ok=True)
    written = sum(
        write_if_changed(os.path.join(out_dir, name), content)
        for name, content in desired.items()
    )
    deleted = 0
    for existing in os.listdir(out_dir):
        path = os.path.join(out_dir, existing)
        if existing not in desired and os.path.isfile(path):
            os.remove(path)
            deleted += 1
    return written, deleted


def sync_tree(src_dir, dst_dir, skip=()):
    """Mirrors src_dir into dst_dir (recursively, for the images/ subfolders
    some reports have): writes changed/new files, then removes anything
    under dst_dir not present in src_dir. `skip` names (top-level only, e.g.
    "meta.json") are never copied into the public dst_dir. Returns
    (written, deleted)."""
    written = 0
    src_files = set()
    for dirpath, _dirnames, filenames in os.walk(src_dir):
        rel_dir = os.path.relpath(dirpath, src_dir)
        for filename in filenames:
            if rel_dir == "." and filename in skip:
                continue
            rel_path = filename if rel_dir == "." else os.path.join(rel_dir, filename)
            src_files.add(rel_path)
            with open(os.path.join(dirpath, filename), "rb") as f:
                content = f.read()
            if write_if_changed(os.path.join(dst_dir, rel_path), content):
                written += 1

    deleted = 0
    if os.path.isdir(dst_dir):
        for dirpath, _dirnames, filenames in os.walk(dst_dir, topdown=False):
            rel_dir = os.path.relpath(dirpath, dst_dir)
            for filename in filenames:
                rel_path = filename if rel_dir == "." else os.path.join(rel_dir, filename)
                if rel_path not in src_files:
                    os.remove(os.path.join(dirpath, filename))
                    deleted += 1
            if dirpath != dst_dir and not os.listdir(dirpath):
                os.rmdir(dirpath)

    return written, deleted


def build_products():
    lookup = {}
    desired = {}

    by_section = {}
    for product_id, section, component, _legacy_order in PRODUCTS:
        by_section.setdefault(section, []).append(component)

    for section, components in by_section.items():
        # PINNED_PRODUCTS entries first (in their declared order), then
        # everything else in this section alphabetically.
        pinned = [c for c in components if (section, c) in PINNED_PRODUCTS]
        rest = sorted((c for c in components if (section, c) not in PINNED_PRODUCTS), key=str.lower)
        for display_order, component in enumerate(pinned + rest):
            slug = slugify(f"{section}-{component}")
            key = f"{section} / {component}"
            lookup[key] = slug
            desired[f"{slug}.md"] = (
                "---\n"
                f"title: {yaml_str(component)}\n"
                f"section: {yaml_str(section)}\n"
                f"slug: {yaml_str(slug)}\n"
                f"display_order: {display_order}\n"
                "---\n"
            )

    written, deleted = sync_dir(os.path.join(ROOT, "_products"), desired)
    print(f"Products: {written} changed, {len(desired) - written} unchanged, {deleted} removed.")
    return lookup


def build_categories():
    lookup = {}
    desired = {}
    for category_id, name in CATEGORIES:
        slug = slugify(name)
        lookup[name] = slug
        desired[f"{slug}.md"] = (
            "---\n"
            f"title: {yaml_str(name)}\n"
            f"slug: {yaml_str(slug)}\n"
            "---\n"
        )
    written, deleted = sync_dir(os.path.join(ROOT, "_categories"), desired)
    print(f"Categories: {written} changed, {len(desired) - written} unchanged, {deleted} removed.")
    return lookup


def load_reports():
    with open(os.path.join(EXPORT_DIR, "reports.json"), encoding="utf-8") as f:
        reports = json.load(f)

    # Locally-added reports (no Oracle to export from anymore) each carry
    # their own meta.json alongside their content files instead of a shared
    # JSON entry, so adding one report is a self-contained diff. Merged in
    # here; everything downstream just sees a flat list of report dicts
    # regardless of where each one came from.
    for meta_path in sorted(glob.glob(os.path.join(EXPORT_DIR, "content", "*", "meta.json"))):
        with open(meta_path, encoding="utf-8") as f:
            reports.append(json.load(f))

    return reports


def load_overrides():
    """export/overrides.json: a single dict keyed by report_id (string),
    holding only reports that deviate from the defaults (cohesity_supported
    = false, ita_versions = unset) - e.g. {"1234": {"cohesity_supported":
    true}}. One small file rather than a directory of mostly-empty
    per-report files, since only a minority of reports will ever need an
    entry."""
    path = os.path.join(EXPORT_DIR, "overrides.json")
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


NO_SQL_SENTINEL = "No SQL, this is for documentation Purposes only."
RTD_ROOT_CLOSE_TAG = "</com.aptare.sc.dal.versioning.ObjectMap>"


def extract_sql(rtd_path):
    """The <string> sibling immediately following the <entry> whose key is
    "dataSource" (exactly one such entry per .rtd file, confirmed across all
    816 in the library). Other SQL-shaped text lives under sql/
    queryComboValues1/2/3 keys (combo-box population) and must not be
    mistaken for this. Returns (sql_text, has_sql); has_sql is False for the
    8 "documentation only" sentinel reports and for any malformed/missing
    file, so a build never fails - the SQL section on that page just doesn't
    render.

    About half the library's .rtd files have a trailing signature-like blob
    (e.g. ".HB2M40s...=") appended after the real XML document closes -
    presumably a content hash from the original report-designer tool. Strict
    XML parsing fails on any trailing content after the root element, so the
    file is truncated to the last real close tag before parsing."""
    try:
        with open(rtd_path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return "", False
    end = text.rfind(RTD_ROOT_CLOSE_TAG)
    if end != -1:
        text = text[:end + len(RTD_ROOT_CLOSE_TAG)]
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return "", False
    for entry in root.iter("entry"):
        children = list(entry)
        if len(children) == 2 and children[0].tag == "string" and children[0].text == "dataSource":
            value_el = children[1]
            if value_el.tag != "string" or not value_el.text:
                return "", False
            text = value_el.text.replace("\r\n", "\n").replace("\r", "\n")
            if text.strip() == NO_SQL_SENTINEL:
                return "", False
            return text, True
    return "", False


def dedupe_reports(reports):
    """RTD_REPORT carries ~400 pairs of true duplicates from a 2023-07-14 bulk
    re-save (same report_name, newer copy has a richer schema - reportGuid,
    reportVersion, etc). Keep the newest modify_date per report_name; log the
    rest to export/deduped_dropped.json for review rather than dropping
    silently."""
    best = {}
    for r in reports:
        name = r["report_name"]
        current = best.get(name)
        if current is None or (r.get("modify_date") or "") > (current.get("modify_date") or ""):
            best[name] = r
    kept_ids = {r["report_id"] for r in best.values()}
    dropped = [r for r in reports if r["report_id"] not in kept_ids]

    if dropped:
        print(f"Deduped {len(dropped)} older duplicate report(s) by report_name (kept newest modify_date).")
        with open(os.path.join(EXPORT_DIR, "deduped_dropped.json"), "w", encoding="utf-8") as f:
            json.dump(
                [{"report_id": r["report_id"], "report_name": r["report_name"],
                  "modify_date": r.get("modify_date")} for r in dropped],
                f, indent=2,
            )

    return list(best.values())


def build_reports(product_lookup, category_lookup):
    reports = dedupe_reports(load_reports())
    overrides = load_overrides()

    reports_out = os.path.join(ROOT, "_reports")
    downloads_out = os.path.join(ROOT, "reports")
    os.makedirs(downloads_out, exist_ok=True)

    desired_pages = {}
    search_index = []
    content_written = 0
    content_deleted = 0

    for r in reports:
        report_id = r["report_id"]
        slug = slugify(r["report_name"])

        product_entries = []
        for label in r["products"]:
            slug_p = product_lookup.get(label.strip())
            if slug_p:
                name = label.strip().split(" / ", 1)[-1]
                product_entries.append({"slug": slug_p, "name": name})

        category_entries = []
        for label in r["categories"]:
            slug_c = category_lookup.get(label.strip())
            if slug_c:
                category_entries.append({"slug": slug_c, "name": label.strip()})

        content_src = os.path.join(EXPORT_DIR, "content", str(report_id))
        content_dst = os.path.join(downloads_out, str(report_id))
        thumbnail = False
        has_sample = False
        sql_query = ""
        has_sql = False
        if os.path.isdir(content_src):
            written, deleted = sync_tree(content_src, content_dst, skip={"meta.json"})
            content_written += written
            content_deleted += deleted
            thumbnail = os.path.isfile(os.path.join(content_src, "thumbnail.png"))
            has_sample = os.path.isfile(os.path.join(content_src, "sample.html"))
            rtd_files = glob.glob(os.path.join(content_src, "*.rtd"))
            if rtd_files:
                sql_query, has_sql = extract_sql(rtd_files[0])

        override = overrides.get(str(report_id), {})
        cohesity_supported = bool(override.get("cohesity_supported", False))
        ita_versions = override.get("ita_versions") or ""

        desc_path = os.path.join(DESCRIPTIONS_DIR, f"{report_id}.md")
        explanation_body = ""
        if os.path.isfile(desc_path):
            with open(desc_path, encoding="utf-8") as f:
                explanation_body = f.read().strip()
            # new_report.py seeds a stub "<!-- TODO: ... -->" placeholder as
            # a landing spot for a not-yet-written explanation; strip HTML
            # comments before deciding there's real content, so a stub-only
            # file doesn't render an empty "How this report works" heading.
            explanation_body = re.sub(r"<!--.*?-->", "", explanation_body, flags=re.DOTALL).strip()

        front_matter = {
            "title": r["report_name"],
            "report_id": report_id,
            "rtd_name": r["rtd_name"],
            "description": r.get("report_desc") or "",
            "problem_statement": r.get("problem_stmt") or "",
            "author": r.get("author") or "",
            "modified_date": r.get("modify_date") or "",
            "download_count": r.get("rtd_download_count") or 0,
            "has_video": bool(r.get("has_video")),
            "video_url": r.get("video_url") or "",
            "cohesity_supported": cohesity_supported,
            "ita_versions": ita_versions,
            "thumbnail": thumbnail,
            "has_sample": has_sample,
            "has_sql": has_sql,
            "sql_query": sql_query,
            "has_explanation": bool(explanation_body),
            "products": product_entries,
            "categories": category_entries,
            "product_slugs": [p["slug"] for p in product_entries],
            "category_slugs": [c["slug"] for c in category_entries],
        }

        fm_yaml = "---\n"
        for key, value in front_matter.items():
            if isinstance(value, (list, dict)):
                fm_yaml += f"{key}: {json.dumps(value)}\n"
            elif isinstance(value, bool):
                fm_yaml += f"{key}: {str(value).lower()}\n"
            elif isinstance(value, int):
                fm_yaml += f"{key}: {value}\n"
            else:
                fm_yaml += f"{key}: {yaml_str(value)}\n"
        fm_yaml += "---\n"

        page_content = fm_yaml + (f"\n{explanation_body}\n" if explanation_body else "")

        # Prefixed with "report-" (not just the bare numeric id) so Jekyll's
        # post-style date-from-filename matcher can't misparse a filename
        # like "1139-80-20-rule-of-problematic-clients.md" as a date
        # (year 1139, "month" 80, day 20) and error out.
        filename = f"report-{report_id}-{slug}.md"
        desired_pages[filename] = page_content

        search_index.append({
            "title": r["report_name"],
            "url": f"/reports/report-{report_id}-{slug}/",
            "products": [p["name"] for p in product_entries],
            "categories": [c["name"] for c in category_entries],
            "product_slugs": [p["slug"] for p in product_entries],
            "category_slugs": [c["slug"] for c in category_entries],
            "sql_query": sql_query,
        })

    pages_written, pages_deleted = sync_dir(reports_out, desired_pages)

    current_ids = {str(r["report_id"]) for r in reports}
    dirs_removed = 0
    for existing in os.listdir(downloads_out):
        path = os.path.join(downloads_out, existing)
        if existing not in current_ids and os.path.isdir(path):
            shutil.rmtree(path)
            dirs_removed += 1

    write_if_changed(
        os.path.join(ROOT, "assets", "search-index.json"),
        json.dumps(search_index),
    )

    print(
        f"Reports: {pages_written} changed, {len(desired_pages) - pages_written} unchanged, "
        f"{pages_deleted} removed. Assets: {content_written} file(s) updated, "
        f"{content_deleted} removed, {dirs_removed} report folder(s) pruned."
    )


def main():
    product_lookup = build_products()
    category_lookup = build_categories()
    build_reports(product_lookup, category_lookup)


if __name__ == "__main__":
    main()
