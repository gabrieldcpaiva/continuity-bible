# Contributing to The Continuity Bible

Thank you for taking an interest. This project is meant to be used, questioned, and improved in public.

## Ways to help

- Use the sheets on a real scene and tell us what got in the way.
- [Open an issue](https://github.com/gabrieldcpaiva/continuity-bible/issues) if a field is confusing, missing, or wrong.
- Open a pull request for a fix or a small improvement.

You do not need a perfect write-up. A short note about what you tried, and where it broke, is enough.

## Before you change the files

`src/schema.py` is the source of the fields, markers, and checklists. The Markdown in `product/`, the spreadsheets, the PDF, and the website are generated from it.

Edit the schema and the builders in `src/`, then rebuild. A hand-edit to a generated Markdown file will be overwritten on the next build.

## Rebuild and test

```bash
python3 -m pip install -r requirements.txt
python3 src/check_example.py
python3 src/build_md.py
python3 src/build_pdf.py
python3 src/build_site.py
npm install --no-save jsdom
node tools/tests/test-form.mjs
node tools/tests/test-site.mjs
```

The PDF build needs the fonts in `assets/fonts/`.

## Licence of contributions

The guide and other written content are under [CC BY-NC 4.0](LICENSE). The build and test scripts listed in [LICENSE-CODE](LICENSE-CODE) are under MIT. By offering a contribution, you agree that it can be included under the same terms as the files you change.

## A note on tone

Write in plain language. Keep the product honest: this paper names what the next shot must keep, and it does not stop a model from drifting. Prefer words over colour, and make the sheets usable in print as well as on screen.
