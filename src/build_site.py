"""Build site/index.html plus its downloadable files.

One page, no dependencies, no external requests. Everything the page shows is read
from schema.py and example.py, so the site cannot drift away from the PDF.

    python3 src/build_site.py

Output:
    site/index.html
    site/files/the-continuity-bible-v1.0.pdf
    site/files/continuity-form.html
    site/files/*.csv
    site/files/templates-markdown.zip
"""

import html
import os
import shutil
import zipfile

import schema
from schema import PRODUCT, PREFLIGHT, HANDOFF_WEAK, HANDOFF_STRONG_LINES, HANDOFF_SKELETON

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCT_DIR = os.path.join(ROOT, "product")
SITE_DIR = os.path.join(ROOT, "site")
FILES_DIR = os.path.join(SITE_DIR, "files")
PDF_NAME = f"The-Continuity-Bible-{PRODUCT['version']}.pdf"


def kb(path):
    size = os.path.getsize(path)
    return f"{size // 1024} KB" if size >= 1024 else f"{size} B"


def preflight_rows():
    out = []
    for i, (label, line, why) in enumerate(PREFLIGHT, 1):
        out.append(
            '        <div class="check">\n'
            f'          <input type="checkbox" id="pf{i}" name="pf{i}">\n'
            f'          <label for="pf{i}">'
            f'<span class="t"><span class="n">{i:02d}</span>{html.escape(label)}</span>'
            f'<span class="d">{html.escape(line)}</span>'
            f'<span class="why">{html.escape(why)}</span>'
            "</label>\n"
            "        </div>"
        )
    return "\n".join(out)


def file_rows():
    rows = [
        (PDF_NAME, "The whole book: seven documents, 43 pages, print-ready A4.",
         "the-continuity-bible.pdf"),
        ("templates-markdown.zip", "The seven documents as editable Markdown. Print, edit, rename.",
         "templates-markdown.zip"),
        ("six-shot-continuity-tracker.csv", "The tracker as a spreadsheet: one row per shot, 22 columns.",
         "six-shot-continuity-tracker.csv"),
        ("six-shot-tracker-blank.csv", "The same columns, empty, to copy per sequence.",
         "six-shot-tracker-blank.csv"),
        ("status-markers.csv", "F / C / U / N/A and what each one obliges you to write.",
         "status-markers.csv"),
        ("continuity-form.html", "Offline form: same fields, one file, exports plain text.",
         "continuity-form.html"),
    ]
    out = []
    for name, what, path in rows:
        full = os.path.join(FILES_DIR, path)
        out.append(
            '        <div class="file">\n'
            f'          <a href="files/{path}" download>\n'
            f'            <div class="name">{html.escape(name)}</div>\n'
            f'            <div class="what">{html.escape(what)}</div>\n'
            "          </a>\n"
            f'          <span class="sz">{kb(full)}</span>\n'
            "        </div>"
        )
    return "\n".join(out)


def build_files():
    if os.path.isdir(FILES_DIR):
        shutil.rmtree(FILES_DIR)
    os.makedirs(FILES_DIR, exist_ok=True)
    shutil.copy2(os.path.join(PRODUCT_DIR, PDF_NAME),
                 os.path.join(FILES_DIR, "the-continuity-bible.pdf"))
    shutil.copy2(os.path.join(ROOT, "tools", "continuity-form.html"),
                 os.path.join(FILES_DIR, "continuity-form.html"))
    for csv_name in ("six-shot-continuity-tracker.csv", "six-shot-tracker-blank.csv",
                     "status-markers.csv"):
        shutil.copy2(os.path.join(PRODUCT_DIR, "spreadsheets", csv_name),
                     os.path.join(FILES_DIR, csv_name))

    zip_path = os.path.join(FILES_DIR, "templates-markdown.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(PRODUCT_DIR)):
            if name.endswith(".md"):
                z.write(os.path.join(PRODUCT_DIR, name), name)
        z.write(os.path.join(PRODUCT_DIR, "spreadsheets", "six-shot-tracker-blank.csv"),
                "spreadsheets/six-shot-tracker-blank.csv")
    return zip_path


def main():
    build_files()
    template = open(os.path.join(SITE_DIR, "template.html"), encoding="utf-8").read()
    pages = len(__import__("pypdf").PdfReader(
        os.path.join(PRODUCT_DIR, PDF_NAME)).pages)
    words = sum(len(open(os.path.join(PRODUCT_DIR, n), encoding="utf-8").read().split())
                for n in os.listdir(PRODUCT_DIR) if n.endswith(".md") and n[0].isdigit())

    page = (template
            .replace("__PREFLIGHT_ROWS__", preflight_rows())
            .replace("__FILE_ROWS__", file_rows())
            .replace("__HANDOFF_WEAK__", html.escape(HANDOFF_WEAK))
            .replace("__HANDOFF_STRONG__", html.escape("\n".join(HANDOFF_STRONG_LINES)))
            .replace("__SKELETON__", html.escape(HANDOFF_SKELETON))
            .replace("__CHECKS__", str(len(PREFLIGHT)))
            .replace("__PAGES__", str(pages))
            .replace("__WORDS__", f"{words:,}")
            .replace("__VERSION__", PRODUCT["version"].lstrip("v"))
            .replace("__DATE__", PRODUCT["edition_date"]))
    leftovers = [m for m in ("__PREFLIGHT_ROWS__", "__FILE_ROWS__", "__CHECKS__", "__PAGES__",
                             "__VERSION__", "__DATE__", "__SKELETON__", "__HANDOFF_") if m in page]
    if leftovers:
        raise SystemExit(f"unreplaced markers: {leftovers}")

    out = os.path.join(SITE_DIR, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)

    print(f"site/index.html                      {len(page):,} bytes")
    for name in sorted(os.listdir(FILES_DIR)):
        print(f"site/files/{name:<24} {kb(os.path.join(FILES_DIR, name)):>8}")
    print(f"pages: {pages}   words of editable source: {words:,}")


if __name__ == "__main__":
    main()
