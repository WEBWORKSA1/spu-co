#!/usr/bin/env python3
"""Generate the SPU.co static site. Usage: python3 build/build.py (from repo root)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import page, SITE
import pages_core, pages_more, pages_guides  # noqa: F401 (registers pages)
from pages_core import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for path, title, desc, body, kw in PAGES:
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(path, title, desc, body, **kw))
    print("wrote", path)

urls = [p for p, *_ in PAGES if p != "404.html"]
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        pri = "1.0" if u == "index.html" else ("0.9" if u in ("get-quotes.html", "calculator.html") else "0.7")
        f.write(f"  <url><loc>{loc}</loc><lastmod>2026-09-20</lastmod><priority>{pri}</priority></url>\n")
    f.write("</urlset>\n")
print("wrote sitemap.xml with", len(urls), "urls")
