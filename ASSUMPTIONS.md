# Assumptions

Everything below was decided during the build without asking, because the brief asked for an autonomous
run. Each entry says what was assumed, why, and what would reverse it. If you disagree with one, it is a
one-line change in `src/schema.py` or `src/example.py`, followed by a rebuild.

## Product decisions

| # | Assumption | Why | Cost if wrong |
| --- | --- | --- | --- |
| 1 | **Name: "The Continuity Bible", subtitle "A six-shot handoff system for independent AI filmmakers".** | Short, says what it is, no trademark search done. | Rename is a find-and-replace in `src/schema.py` (`PRODUCT`) and the file names. |
| 2 | **A4 page size, 18 mm margins, print-and-write primary use.** | The reader is one person at a desk; A4 is the default outside the US, and the sheets have to be writable. | US Letter would need a page-size change plus re-testing of every table width. |
| 3 | **Seven separate documents, not one long book.** | The brief asked for six components; a seventh (the field dictionary) was added because "what stays fixed vs what may change" needs one page per field. | Merge or split is a change in `src/build_pdf.py`, not in the content. |
| 4 | **Identity / Variant / Shot state, with letters F, C, U, N/A.** | The brief named the three layers and asked for non-colour markers. Letters survive photocopying and greyscale printing. | Any other marker set is a constant in `src/schema.py`. |
| 5 | **Codes: `V1..Vn` (wardrobe/variant), `L1..Ln` (light), `P-01a/b` (prop states), `CH-01`, `LOC-01`.** | Short enough to paste into a prompt, ordered enough to sort. | Low. |
| 6 | **Scope: scenes of about four to eight shots; the templates are built for six.** | Where drift starts to be expensive, and small enough to hold in the head; also what the brief specified. | Longer sequences need one table per scene, which is stated in the product. |
| 7 | **Free for everyone.** The earlier one-off test price is dropped. | Decided on 26 Nov 2026. The cover line comes from `PRODUCT["price_line"]` in `src/schema.py`. | Putting a price back on would need a different page, a checkout, and a fresh decision. |
| 8 | **English only, plain-language register, no unexplained abbreviations.** | The brief's accessibility bar; second-language readers are part of the audience. | Translation is a separate job. |
| 9 | **No external visual assets. Only one drawing, generated as vector paths from `src/plan.py`.** | The brief preferred no external assets and forbade generated imagery as content. | The floor plan is the only thing to redraw. |
| 10 | **Distribution is the free static page (`site/`, Vercel) plus the files in the repo.** | No store and no payment. | A later paid edition would be a different page, not this one. |
| 11 | **No refund policy, because nothing is sold.** | A refund is a commercial commitment, and there is no sale. | If a price ever returns, write the policy before anyone is asked to pay. |

| 24 | **Type: Inter for text, Source Serif 4 for titles, JetBrains Mono for the code blocks — all SIL OFL, all embedded.** | Reportlab needs a TTF to embed; licence-clean faces were required for a file you can publish. |

## Content decisions

| # | Assumption | Why |
| --- | --- | --- |
| 12 | **The worked example is an invented scene: "Night Signal", Scene 14, "The Third Caller", six shots, one character, one room.** | Needed a scene with a prop state, a light change and a natural reason to change wardrobe, without depicting a real person or a real production. |
| 13 | **The example's intentional change is a wardrobe variant plus a prop spill at shot 5, caused by an on-screen event.** | A change with a visible cause teaches the "C" marker better than a change with no reason. |
| 14 | **The "clock ghost" is an empty landmark marked N/A.** | Demonstrates that N/A is a real answer, and that a wall clock is the classic accidental continuity error in a generated room. |
| 15 | **Camera positions are recorded as plan coordinates (`camera_xy`) as well as words.** | Words drift; a coordinate does not. It also let the floor plan be drawn from the same data. |
| 16 | **No model is named anywhere as required; where an example needs a concrete act, it says "generate" and describes the frame, not the tool.** | Model-agnostic brief requirement; also keeps the product from ageing with any one vendor. |
| 17 | **The bundle includes the source Markdown and a CSV tracker, not just the PDF.** | The brief asked for an editable core product; a PDF alone is not editable. |
| 18 | **The optional HTML form is a single file with inline CSS and JS, and one export function.** | Offline, no dependencies, no network, no account; testable without a browser window. |

## Claims and evidence

| # | Assumption | Status |
| --- | --- | --- |
| 19 | Boords and Milanote prices quoted anywhere in this repo | **Verified** on the vendors' pages on 23 Nov 2026; see `research/`. |
| 20 | Practitioner claims about continuity being a workflow problem | **Verified as published opinion**, four 2026 guides, quoted in `research/`. Not a controlled finding. |
| 21 | That anyone would pay for the document | **Retired.** The product is free for everyone. The commercial stop/go test is retired and must not be run. |
| 22 | That the sheets are usable without the guide | **Untested.** This is precisely what the two-person usability test is for. |
| 23 | The example is free of accidental contradictions | **Checked mechanically** (86 assertions) and read through; not checked by an independent filmmaker. |

## What was deliberately not done

- No image or video generation, no video hosting, no collaboration features, no model integration.
- No interviews, no outreach, no purchases, no publication. No participant, customer, quote or endorsement
  is claimed anywhere.
- No paid prompt databases, courses or template packs were read or paraphrased from.
- No legal, tax or consumer-protection advice is given; the licence wording is a plain permission statement,
  not a lawyer-reviewed agreement.
- Two validation activities were prepared rather than performed, because performing them requires contacting
  people, which was out of scope without authorisation.
