"""
LOCAL PREVIEW ONLY - not part of the real build pipeline.

Renders the generated _reports/_products/_categories collections into static
HTML under _preview_site/, mirroring what the real Jekyll layouts
(_layouts/*.html) would produce, so the site can be viewed without installing
Ruby/Jekyll. Run scripts/build_site_content.py first.

Run: python scripts/preview_render.py
Then serve _preview_site/ with any static file server.
"""
import os
import re
import shutil

import yaml

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "_preview_site")


def load_front_matter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    front_matter = yaml.safe_load(m.group(1)) or {}
    front_matter["_body"] = m.group(2).strip()
    return front_matter


def load_collection(dirname):
    docs = []
    d = os.path.join(ROOT, dirname)
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            fm = load_front_matter(os.path.join(d, fn))
            fm["_slug_from_filename"] = fn[:-3]
            docs.append(fm)
    return docs


def page_shell(title, body, categories, products, description=""):
    cats_sorted = sorted(categories, key=lambda c: c["title"])
    sections = {}
    for p in products:
        sections.setdefault(p["section"], []).append(p)
    sidebar_products = ""
    for section in sorted(sections):
        items = sorted(sections[section], key=lambda p: p["title"])
        sidebar_products += f"<h4>{section}</h4><ul>"
        for p in items:
            sidebar_products += f'<li><a href="/products/{p["slug"]}/">{p["title"]}</a></li>'
        sidebar_products += "</ul>"

    sidebar_cats = "".join(
        f'<li><a href="/categories/{c["slug"]}/">{c["title"]}</a></li>' for c in cats_sorted
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · IT Analytics Report Library</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<header class="site-header">
  <a class="site-title" href="/">IT Analytics Report Library</a>
  <div class="search-box">
    <input id="search-input" type="search" placeholder="Search reports…" autocomplete="off">
    <div id="search-results" class="search-results"></div>
  </div>
</header>
<div class="layout">
  <nav class="sidebar">
    <section><h3><a href="/categories/">Categories</a></h3><ul>{sidebar_cats}</ul></section>
    <section><h3><a href="/products/">Products</a></h3>{sidebar_products}</section>
  </nav>
  <main class="content">
    {body}
  </main>
</div>
<footer class="site-footer">
  <p>Community-contributed report templates. Provided as examples only; not officially supported.
  Report issues or contribute a template via GitHub.</p>
</footer>
<script src="/assets/js/search.js"></script>
</body>
</html>"""


def render_report_body(r):
    tags = ""
    for c in r.get("categories", []):
        tags += f'<a class="tag tag-category" href="/categories/{c["slug"]}/">{c["name"]}</a>'
    for p in r.get("products", []):
        tags += f'<a class="tag tag-product" href="/products/{p["slug"]}/">{p["name"]}</a>'

    rid = r["report_id"]
    actions = (
        f'<a class="btn btn-primary" href="/reports/{rid}/{r["rtd_name"]}" download>Download Template (.rtd)</a>'
        f'<a class="btn" href="/reports/{rid}/sample.html" target="_blank" rel="noopener">View Sample Output ↗</a>'
    )
    if r.get("has_video") and r.get("video_url"):
        actions += f'<a class="btn" href="{r["video_url"]}" target="_blank" rel="noopener">Watch Video ↗</a>'

    thumb = ""
    if r.get("thumbnail"):
        thumb = (
            '<h3>Report Designer Screen</h3>'
            f'<img class="report-thumb" src="/reports/{rid}/thumbnail.png" alt="Report designer / scoping screen">'
        )

    sample_frame = (
        '<h3>Report Preview</h3>'
        f'<iframe class="report-sample-frame" src="/reports/{rid}/sample.html" '
        f'title="Sample output for {r["title"]}" loading="lazy" '
        "onload=\"this.style.height = (this.contentWindow.document.body.scrollHeight + 20) + 'px'\"></iframe>"
    )

    desc = f'<p class="report-desc">{r["description"]}</p>' if r.get("description") else ""
    problem = f'<h3>Problem this solves</h3><p>{r["problem_statement"]}</p>' if r.get("problem_statement") else ""

    return f"""<article class="report">
  <h1>{r["title"]}</h1>
  <div class="report-tags">{tags}</div>
  <div class="report-actions">{actions}</div>
  {sample_frame}
  {thumb}
  {desc}
  {problem}
  <dl class="report-meta">
    <dt>Author</dt><dd>{r.get("author", "")}</dd>
    <dt>Last updated</dt><dd>{r.get("modified_date", "")}</dd>
    <dt>Downloads</dt><dd>{r.get("download_count", 0)}</dd>
  </dl>
</article>"""


def render_list_body(title, matching):
    items = "".join(f'<li><a href="{r["_url"]}">{r["title"]}</a></li>' for r in sorted(matching, key=lambda r: r["title"]))
    plural = "" if len(matching) == 1 else "s"
    return f"<h1>{title}</h1><p>{len(matching)} report{plural}</p><ul class=\"report-list\">{items}</ul>"


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    categories = load_collection("_categories")
    products = load_collection("_products")
    reports = load_collection("_reports")
    for r in reports:
        r["_url"] = f'/reports/{r["_slug_from_filename"]}/'

    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    if os.path.isdir(os.path.join(ROOT, "reports")):
        shutil.copytree(os.path.join(ROOT, "reports"), os.path.join(OUT, "reports"))

    def write(rel_path, html):
        full = os.path.join(OUT, rel_path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)

    # Home
    total = len(reports)
    home_body = f"""<h1>IT Analytics Report Library</h1>
<p>A collection of unique report templates created by the Veritas/Cohesity IT Analytics
community, available for all customers and partners. Reports can be downloaded and
used as-is or customized to suit your own environment.</p>
<p>Browse by <strong><a href="/categories/">Category</a></strong> or
<strong><a href="/products/">Product</a></strong> in the sidebar, or use the search
box above. Each report page has a <strong>Download Template</strong> button and a
<strong>View Sample Output</strong> link.</p>
<p>Currently listing <strong>{total}</strong> report templates.</p>"""
    write("index.html", page_shell("Home", home_body, categories, products))

    # Products index
    sections = {}
    for p in products:
        sections.setdefault(p["section"], []).append(p)
    body = "<h1>Browse by Product</h1>"
    for section in sorted(sections):
        body += f"<h2>{section}</h2><ul class=\"report-list\">"
        for p in sorted(sections[section], key=lambda p: p["title"]):
            body += f'<li><a href="/products/{p["slug"]}/">{p["title"]}</a></li>'
        body += "</ul>"
    write("products/index.html", page_shell("Products", body, categories, products))

    # Categories index
    body = "<h1>Browse by Category</h1><ul class=\"report-list\">"
    for c in sorted(categories, key=lambda c: c["title"]):
        body += f'<li><a href="/categories/{c["slug"]}/">{c["title"]}</a></li>'
    body += "</ul>"
    write("categories/index.html", page_shell("Categories", body, categories, products))

    # Individual product pages
    for p in products:
        matching = [r for r in reports if p["slug"] in r.get("product_slugs", [])]
        body = render_list_body(f'{p["section"]}: {p["title"]}', matching)
        write(f'products/{p["slug"]}/index.html', page_shell(p["title"], body, categories, products))

    # Individual category pages
    for c in categories:
        matching = [r for r in reports if c["slug"] in r.get("category_slugs", [])]
        body = render_list_body(c["title"], matching)
        write(f'categories/{c["slug"]}/index.html', page_shell(c["title"], body, categories, products))

    # Report pages
    for r in reports:
        body = render_report_body(r)
        write(f'reports/{r["_slug_from_filename"]}/index.html', page_shell(r["title"], body, categories, products, r.get("description", "")))

    print(f"Rendered {total} report pages, {len(products)} product pages, {len(categories)} category pages to {OUT}")


if __name__ == "__main__":
    main()
