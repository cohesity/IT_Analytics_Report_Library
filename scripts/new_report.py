"""
Adds a new, locally-authored report to the library - the replacement for the
old "export from Oracle" pipeline now that the source RTD_REPORT environment
is deprecated. Writes a self-contained export/content/{id}/ folder (the .rtd
template, a sample output, an optional thumbnail, and a meta.json) plus a
stub descriptions/{id}.md, so build_site_content.py picks the new report up
on its next run with no other changes needed.

New reports are assigned report_id >= 10000 (legacy Oracle-sourced ids top
out at 1297), auto-allocated as one past the current local max - no manual
bookkeeping, no collision risk with the frozen legacy export/reports.json.

Example:
  python new_report.py --rtd "My Report.rtd" --sample-html sample.html \\
      --name "My Report" --desc "What it shows." \\
      --problem-stmt "Why you'd run it." --author "you@example.com" \\
      --products "Backup Manager / Veritas NetBackup" \\
      --categories "Trending/Forecasting/Capacity Planning"

Or with a static image sample instead of pre-rendered HTML:
  python new_report.py --rtd "My Report.rtd" --sample-image chart.png ...

After this, run: python build_site_content.py
Then (optional but recommended): ask Claude to read the new report's .rtd/
sample and fill in descriptions/{id}.md with a user-friendly explanation.
"""
import argparse
import datetime
import glob
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_site_content import CATEGORIES, DESCRIPTIONS_DIR, EXPORT_DIR, PRODUCTS  # noqa: E402

VALID_PRODUCTS = {f"{section} / {component}" for _id, section, component, _order in PRODUCTS}
VALID_CATEGORIES = {name for _id, name in CATEGORIES}


def safe_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "template.rtd"


def next_local_id():
    max_id = 9999
    for meta_path in glob.glob(os.path.join(EXPORT_DIR, "content", "*", "meta.json")):
        with open(meta_path, encoding="utf-8") as f:
            report_id = json.load(f).get("report_id", 0)
        if report_id >= 10000:
            max_id = max(max_id, report_id)
    return max_id + 1


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rtd", required=True, help="Path to the .rtd template file")
    parser.add_argument("--sample-html", help="Path to a pre-rendered sample output HTML file")
    parser.add_argument("--sample-image", help="Path to a static sample output image (png/jpg/gif)")
    parser.add_argument("--thumbnail", help="Path to an optional designer/scoping screenshot")
    parser.add_argument("--name", required=True, help="Report title")
    parser.add_argument("--desc", default="", help="Short report description")
    parser.add_argument("--problem-stmt", default="", help="What problem this report solves")
    parser.add_argument("--author", default="", help="Author name or email")
    parser.add_argument("--video-url", default="")
    parser.add_argument(
        "--products", nargs="+", default=[], metavar="SECTION / COMPONENT",
        help=f"One or more of: {sorted(VALID_PRODUCTS)}",
    )
    parser.add_argument(
        "--categories", nargs="+", default=[], metavar="CATEGORY",
        help=f"One or more of: {sorted(VALID_CATEGORIES)}",
    )
    args = parser.parse_args()

    if not args.sample_html and not args.sample_image:
        parser.error("one of --sample-html or --sample-image is required")
    if args.sample_html and args.sample_image:
        parser.error("pass only one of --sample-html or --sample-image, not both")

    bad_products = [p for p in args.products if p not in VALID_PRODUCTS]
    if bad_products:
        parser.error(f"unknown product(s) {bad_products}; valid options: {sorted(VALID_PRODUCTS)}")
    bad_categories = [c for c in args.categories if c not in VALID_CATEGORIES]
    if bad_categories:
        parser.error(f"unknown categor(y/ies) {bad_categories}; valid options: {sorted(VALID_CATEGORIES)}")

    return args


def main():
    args = parse_args()
    report_id = next_local_id()
    out_dir = os.path.join(EXPORT_DIR, "content", str(report_id))
    os.makedirs(out_dir, exist_ok=True)

    rtd_name = os.path.basename(args.rtd)
    shutil.copyfile(args.rtd, os.path.join(out_dir, safe_filename(rtd_name)))

    if args.sample_html:
        shutil.copyfile(args.sample_html, os.path.join(out_dir, "sample.html"))
    else:
        ext = os.path.splitext(args.sample_image)[1].lstrip(".").lower() or "png"
        image_filename = f"output.{ext}"
        shutil.copyfile(args.sample_image, os.path.join(out_dir, image_filename))
        with open(os.path.join(out_dir, "sample.html"), "w", encoding="utf-8") as f:
            f.write(
                "<html><body style=\"margin:0\">"
                f"<img src=\"{image_filename}\" style=\"max-width:100%\">"
                "</body></html>"
            )

    if args.thumbnail:
        shutil.copyfile(args.thumbnail, os.path.join(out_dir, "thumbnail.png"))

    today = datetime.date.today().isoformat()
    meta = {
        "report_id": report_id,
        "report_name": args.name,
        "report_desc": args.desc,
        "problem_stmt": args.problem_stmt,
        "author": args.author,
        "create_date": today,
        "modify_date": today,
        "rtd_name": rtd_name,
        "has_video": bool(args.video_url),
        "video_url": args.video_url,
        "rtd_download_count": 0,
        "products": args.products,
        "categories": args.categories,
    }
    with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    os.makedirs(DESCRIPTIONS_DIR, exist_ok=True)
    desc_path = os.path.join(DESCRIPTIONS_DIR, f"{report_id}.md")
    if not os.path.isfile(desc_path):
        with open(desc_path, "w", encoding="utf-8") as f:
            f.write(f"<!-- TODO: ask Claude to draft a user-friendly explanation for \"{args.name}\" (report {report_id}) -->\n")

    print(f"Added report {report_id}: {args.name}")
    print(f"  {out_dir}")
    print(f"  {desc_path} (stub - fill in or ask Claude to draft it)")
    print("Next: python build_site_content.py")


if __name__ == "__main__":
    main()
