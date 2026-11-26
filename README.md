# The Continuity Bible

Six generated shots can look like six different films. The usual cause is not the model. Nobody wrote down what has to survive the cut.

This is that piece of paper. A character sheet, a location sheet, a six-shot state table, a fifteen-point preflight, a field dictionary, and one complete worked example, so six separately generated shots can be made to feel like one scene.

It is free for everyone. No account, no signup, no payment.

**Use it free:** https://continuity-bible.vercel.app

**Version 1.0 · November 2026**

> Continuity is a production judgment supported by a written record. This product does not eliminate continuity drift, and nothing in it claims to.

## Who it's for

Independent AI filmmakers who generate a scene as separate shots and need those shots to cut together. Any model, any tool. If you can write a sentence and check a frame, you can use it.

## What's inside

| Layer | Where it lives | Question it answers |
| --- | --- | --- |
| **Identity** | character sheet, location sheet | What must never change? |
| **Variant** | variant and light-state registers | What changed on purpose, and why? |
| **Shot state** | six-shot table | What exactly is true in this shot? |
| **Handoff** | inherits / changes / hands off | What does the next shot receive? |

Every field in the dictionary answers four questions: what it records, what stays fixed, what may change, and how an intentional change is recorded. Status markers are **F** fixed, **C** changed intentionally, **U** unresolved, **N/A** not applicable — letters with words, never colour alone.

Open `product/README-first.md` for the reading order. The print edition is `product/The-Continuity-Bible-v1.0.pdf` (A4, 43 pages). To type instead of write, open `tools/continuity-form.html` in any browser. One file, offline, no account. It exports plain text. Unsaved text is lost on reload. A saved draft stays only in that browser.

## Where the words come from

`src/schema.py` is the source. The Markdown in `product/`, the spreadsheets, the PDF and the website are generated from it. Edit the schema and the document builders in `src/`, then rebuild. A hand-edit to a generated Markdown file is overwritten the next time you build. Lines of underscores in those files are writing space for the person filling in the sheet.

## Rebuild

```bash
python3 -m pip install -r requirements.txt
python3 src/check_example.py        # 86 mechanical checks on the worked example
python3 src/build_md.py             # writes product/*.md and product/spreadsheets/*.csv
python3 src/build_pdf.py            # writes product/The-Continuity-Bible-v1.0.pdf
python3 src/build_site.py           # writes site/index.html and site/files/*
```

`requirements.txt` pins `reportlab==5.1.2` and `pypdf==7.1.1`. The PDF needs `assets/fonts/*.ttf` in place. Nothing else is downloaded at build time.

The form and site tests need Node and jsdom:

```bash
npm install --no-save jsdom
node tools/tests/test-form.mjs
node tools/tests/test-site.mjs
```

## Honest limits

- It will not stop a model from drifting. It is the record that judgment works from, and a way to notice a problem before the shot is wasted.
- It will not make six shots match by itself. You still look at the frames.
- It is written for scenes of about four to eight shots. Longer work wants one table per scene.
- It is new. The worked example was checked by a script for contradictions. A two-person usability session is written in `validation/` and not yet run. If a field is wrong when you use it, feedback is welcome.
- The old commercial price test is retired. The work is free.

## Put the page online

Vercel serves the `site/` folder as a static site. `vercel.json` points the output at that folder. No build command, no environment variables. See `site/README.md`. Replace `https://continuity-bible.vercel.app` above once the deployment has a URL.

## Repository layout

```
product/                     generated book, plus README-first.md
src/schema.py                source of every field, marker and checklist item
src/                         builders (Python 3 + reportlab)
site/                        free one-page site, generated
tools/continuity-form.html   offline form
validation/                  usability session, still to run; commercial test retired
launch/                      posts for sharing the free page
requirements.txt             pinned build libraries
vercel.json                  static deploy of site/
```

## License

The guide, the PDF, the templates, the site, and the other written content are Copyright 2026 Gabriel Paiva, under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). The legal code is in `LICENSE`. You may share and adapt that work for non-commercial use if you give credit. Don't sell it.

The build and test scripts are Copyright (c) 2026 Gabriel Paiva, under the MIT licence in `LICENSE-CODE`:

- `src/build_md.py`, `src/build_pdf.py`, `src/build_site.py`, `src/check_example.py`
- `src/dsl.py`, `src/plan.py`, `src/typeset.py`
- `tools/tests/test-form.mjs`, `tools/tests/test-site.mjs`

`src/schema.py`, `src/example.py`, and `src/docs_00.py` through `src/docs_06.py` are the written source of the guide, so they stay under CC BY-NC 4.0. The typefaces in `assets/fonts/` stay under the SIL Open Font License.
