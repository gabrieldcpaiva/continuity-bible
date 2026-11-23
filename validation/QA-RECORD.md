# QA record — v1.0, checked 23 November 2026

What was actually run, what it covered, and what it could not cover. Anything not listed here was not
checked.

## 1. Automated checks on the worked example

`python3 src/check_example.py` — **86 assertions, 86 passed, 0 failed.** Exit code 0.

Coverage, by group:

| Group | What it asserts |
| --- | --- |
| Structure | Six shots, numbered 1–6 in order, every shot has a slug and a length. |
| Inheritance | Every row after shot 1 carries a non-empty “inherits” line; shot 1 is marked as establishing. |
| Codes | Every variant, light state and prop state code used in the table is declared in its register, and every declared code is used. |
| Contiguity | Variant and light runs are contiguous — no code appears, disappears and reappears. |
| Status | A row marked C contains a change; a row marked F contains none; every U also appears in the open-items list. |
| Frame sides | Door and ON AIR lamp always frame-right; mug always frame-left; pencil always in the left hand. |
| Bookend | Shot 6 matches shot 1 on framing size and camera position, and the mug state has moved on. |
| Prop runs | Mug state (upright full → tipped with ring) changes once and never reverts; the ring never lands on the paper. |
| Absences | No clock anywhere in the prop register or the shot text; no promise language (“guaranteed”, “never drifts”) in any of the seven documents. |
| Schema coverage | Every field in `src/schema.py` appears in the example. |

This is a consistency proof, not a quality proof: it cannot tell whether the scene is any good, only that it
does not contradict itself.

## 2. Automated checks on the offline form

`node tools/tests/test-form.mjs` (jsdom, file:// URL) — **35 checks, 35 passed, 0 failed.**

Covered: the page builds all fields; six shot blocks and fifteen preflight items exist; every input has a
label or an accessible name; a realistic six-shot fill-in exports text containing every value typed, with
no `undefined` or `null`; empty fields degrade to an em dash; the build button writes the text into the
page; the file loads no external script, style or image, over `file://`.

**Not covered:** visual rendering. No browser or headless Chromium was available in the build environment,
so the form's appearance, responsive behaviour and print stylesheet were written carefully but **not seen**.
The layout is plain CSS grid with a system font stack; the risk is cosmetic, not functional. First real
check should be: open it in Chrome, Firefox and Safari, at 100 % zoom and on a phone, and print it to PDF.

## 3. PDF checks

- **43 pages**, A4 (595 × 842 pt), 18 mm margins, produced by `python3 src/build_pdf.py`.
- Fonts: Inter (5 weights), Source Serif 4 (2), JetBrains Mono (2) — **all embedded as subsets**. The only
  base-14 reference left in the file is an empty `Tf` operator that draws no text.
- Text extraction with pypdf: **16 100+ words**, no missing-glyph boxes.
- Every page rendered to an image with pypdfium2 and inspected: no clipped text, no table overflowing the
  frame, no heading stranded at the foot of a page, no page below ~3 % ink except the deliberately blank
  floor-plan sheet.
- Page-by-page ink measurement (`sparsity.py`): the lowest-ink pages are blank templates (the floor-plan
  sheet, the three panels, the shot card), which is expected for a fill-in page.
- Page furniture verified: cover (p.1), contents (p.2), part openers at p.3, 9, 16, 19, 24, 30, 33,
  colophon (p.43).

**Not covered:** a commercial print proof, colour-managed output, PDF/X validation, and printing on paper.
The file is RGB, not CMYK, and should be proofed by the printer before a short run.

## 4. Files, names and handoff

- Every file in `product/` opens: the seven Markdown files parse as UTF-8 text, the PDF opens in two
  independent readers (pypdf, pypdfium2), the three CSVs parse with Python's `csv` module.
- Names are descriptive and numbered in reading order; the PDF is versioned in its filename.
- The editable source, the print edition and the CSVs are generated from the same content, so they cannot
  disagree about a field name or a value.

## 5. What was not tested, and must not be implied

- **No filmmaker has read, filled in or used any of this.**
- **No one has been asked about price.** US$29 is a test price with no evidence behind it.
- No comparison against a real sequence was made by a second person; there is no inter-rater check.
- No accessibility audit by a screen-reader user; the PDF is tagged only by reading order, not as a
  fully tagged PDF, and the HTML form has labels and focus styles but no automated audit (axe or similar
  was not available offline).

## 6. Re-running these checks

```bash
python3 src/check_example.py        # expects 86 passed, 0 failed
npm install --no-save jsdom
node tools/tests/test-form.mjs      # expects 35 passed, 0 failed
python3 src/build_pdf.py            # expects "pages 43"
```
