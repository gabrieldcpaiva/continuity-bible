# The Continuity Bible

A free continuity system for filmmakers and AI video makers who want separately generated shots to feel like one scene.

**Use it now, free, with no account:** [The Continuity Bible website](https://continuity-bible.vercel.app)

Version 1.0 · November 2026

## Start in 3 steps

1. Open [the free website](https://continuity-bible.vercel.app), or download [the print-ready PDF](product/The-Continuity-Bible-v1.0.pdf).
2. Fill in a character sheet and a location sheet, then the six-shot table. Each new shot starts by copying the previous shot's handoff line, not by remembering it.
3. Run the one-minute preflight before you generate, then look at the frames. You still make the call.

## What's inside

- **A live page** with a 15-point preflight you can tick in the browser. A saved draft stays only on that device.
- **A 43-page A4 PDF**, ready to print and write on.
- **The same seven documents as Markdown**, plus a CSV tracker, so you can type or keep your own copy.
- **An offline form** in [`tools/continuity-form.html`](tools/continuity-form.html). One file, no account, no network. It exports plain text. Unsaved text is lost on reload.
- **One complete worked example**, an invented six-shot scene, with a change traced from start to finish.

## How to use it

The paper does not stop the drift. It names what the next shot must keep. Continuity is still a production judgment. These sheets are the written record that judgment works from, so you can notice a problem before a shot is wasted.

Work in this order:

1. Read [the twenty-minute start guide](product/00-start-here.md).
2. Fill in the [character sheet](product/02-character-sheet.md) and the [location sheet](product/03-location-sheet.md).
3. Plan the scene in the [six-shot state table](product/04-six-shot-state-table.md).
4. Check the [shot preflight](product/05-shot-preflight-checklist.md) in the minute before you generate.

If you only have a short window, read the start guide and the first pages of [the worked example, The Third Caller](product/06-worked-example-the-third-caller.md). The full reading order is in [what's in the box](product/README-first.md).

Every field can be marked **F** (fixed), **C** (changed on purpose), **U** (unresolved), or **N/A**. The letter is the marker. Colour is never the only signal.

The sheets are built for scenes of about four to eight shots. Longer work wants one table per scene.

## Questions

**Will this stop my model from drifting?**
No. It is the record that judgment works from. You still look at the frames.

**Is it free?**
Yes. No account, no signup, no payment.

**Does it work with my tools?**
Yes. Any model, any tool. If you can write a sentence and check a frame, you can use it.

**Can I sell the guide or the templates?**
No. You may share and adapt the written work for non-commercial use if you give credit. Don't sell it.

**Is it proven in the field?**
It is new. The worked example was checked by a script for contradictions. A two-person usability session is written in [`validation/`](validation/) and has not been run yet. If a field is wrong when you use it, please say so.

## Licence

The guide, the PDF, the templates, the site, and the other written content are Copyright 2026 Gabriel Paiva, under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). The legal code is in [LICENSE](LICENSE). You may share and adapt that work for non-commercial use if you give credit. Don't sell it.

The build and test scripts are Copyright (c) 2026 Gabriel Paiva, under the MIT licence in [LICENSE-CODE](LICENSE-CODE):

- `src/build_md.py`, `src/build_pdf.py`, `src/build_site.py`, `src/check_example.py`
- `src/dsl.py`, `src/plan.py`, `src/typeset.py`
- `tools/tests/test-form.mjs`, `tools/tests/test-site.mjs`

`src/schema.py`, `src/example.py`, and `src/docs_00.py` through `src/docs_06.py` are the written source of the guide, so they stay under CC BY-NC 4.0. The typefaces in `assets/fonts/` stay under the SIL Open Font License.

## Credits

Made by Gabriel Paiva with his agent team, Coco and Ferro.

## Contributing

Issues and pull requests are welcome. If a field is confusing, or a sheet breaks on your scene, [open an issue](https://github.com/gabrieldcpaiva/continuity-bible/issues) or propose a change. A short guide is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Build the files yourself

`src/schema.py` is the source. The Markdown in `product/`, the spreadsheets, the PDF, and the website are generated from it. A hand-edit to a generated Markdown file is overwritten the next time you build.

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

The live site is a static export of the `site/` folder. Vercel is not hooked up to this repository, so a push does not redeploy the page. See [the site folder README](site/README.md).

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
