"""
Reconciles images that never made it into RTD_REPORT but are referenced from
sample.html: chart GIFs generated on-the-fly by the old report engine, plus a
handful of shared skin icons (status dots, tapeLibrary/fileSystem) pulled in
via absolute URLs to now-decommissioned portal domains
(my.storageconsole.com, wow.aptare.com, storagescape.datalink.com, etc).
Run this after export_from_oracle.py, before build_site_content.py.

For relative references (src="./images/NAME") the file just needs to be
copied to export/content/{report_id}/images/{filename} - no HTML change.

For absolute references (url(https://dead-domain/skins/aptare/NAME) or
<img src="https://dead-domain/.../NAME">) sample.html is rewritten in place
to point at the same local images/{filename} path, since copying alone
wouldn't stop the browser from trying to load the dead external URL.

Run: python fetch_chart_images.py "C:\\NewReportLibrary\\Imbedded_images"
"""
import os
import re
import shutil
import sys

EXPORT_CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "export", "content")

RELATIVE_SRC_RE = re.compile(r'src=["\']\.?/?images/([^"\']+)["\']', re.IGNORECASE)
ABSOLUTE_URL_RE = re.compile(r'(https://[^\s"\')]+?/([^/\s"\')]+\.(?:gif|png|jpg|jpeg)))', re.IGNORECASE)


def process_sample_html(path, source_files):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    copied, missing, rewritten = [], [], False

    for filename in set(RELATIVE_SRC_RE.findall(text)):
        src = source_files.get(filename)
        if src is None:
            missing.append(filename)
            continue
        copy_image(path, filename, src)
        copied.append(filename)

    for full_url, filename in set(ABSOLUTE_URL_RE.findall(text)):
        src = source_files.get(filename)
        if src is None:
            missing.append(filename)
            continue
        copy_image(path, filename, src)
        copied.append(filename)
        text = text.replace(full_url, f"images/{filename}")
        rewritten = True

    if rewritten:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    return copied, missing


def copy_image(sample_path, filename, src):
    out_dir = os.path.join(os.path.dirname(sample_path), "images")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copy2(src, os.path.join(out_dir, filename))


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python fetch_chart_images.py <source_images_folder>")
    source_dir = sys.argv[1]
    if not os.path.isdir(source_dir):
        raise SystemExit(f"Not a directory: {source_dir}")

    source_files = {f: os.path.join(source_dir, f) for f in os.listdir(source_dir)
                     if os.path.isfile(os.path.join(source_dir, f))}
    print(f"Source folder has {len(source_files)} image files.")

    total_copied = 0
    all_missing = []
    reports_touched = 0

    for report_id in os.listdir(EXPORT_CONTENT_DIR):
        sample_path = os.path.join(EXPORT_CONTENT_DIR, report_id, "sample.html")
        if not os.path.isfile(sample_path):
            continue
        copied, missing = process_sample_html(sample_path, source_files)
        if copied or missing:
            reports_touched += 1
        total_copied += len(copied)
        all_missing.extend((report_id, f) for f in missing)

    print(f"Touched {reports_touched} report(s). Copied {total_copied} image(s).")
    if all_missing:
        print(f"{len(all_missing)} referenced image(s) not found in source folder:")
        for report_id, filename in all_missing[:50]:
            print(f"  report {report_id}: {filename}")
        if len(all_missing) > 50:
            print(f"  ... and {len(all_missing) - 50} more")


if __name__ == "__main__":
    main()
