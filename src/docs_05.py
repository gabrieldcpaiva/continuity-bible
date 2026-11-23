"""Document 05 — Shot preflight checklist template."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, fill,
                 checklist, pagebreak, formula, spacer)
from schema import PRODUCT, PREFLIGHT

GROUPS = [
    ("Row and identity", 0, 3),
    ("Wardrobe, hair, hands and props", 3, 8),
    ("Geography, light and time", 8, 12),
    ("Framing, handoff and open items", 12, 15),
]

BLOCKS = [
    table(["Shot no.", "Slug", "Generated from row", "Date / time"],
          [["", "", "", ""]], widths=[0.14, 0.40, 0.26, 0.20], dense=True, heights=[24]),
    lead(
        "Read this with your hand on the button. It takes about a minute, and it is the only part of the system you use on every "
        "single shot."
    ),
]

for name, a, b in GROUPS:
    BLOCKS.append(h2(name))
    BLOCKS.append(checklist([(t, hint) for t, _, hint in PREFLIGHT[a:b]]))

BLOCKS.append(p(
    "Each check names the failure it prevents, because a check whose purpose you cannot remember is a check you will skip. "
    "Tick the box, or leave it blank and write why — a blank box is information too."
))

BLOCKS += [
    h1("The line to read out loud"),
    p(
        "Before generating, say this sentence with the shot numbers filled in. It is the single habit that catches the most mistakes, "
        "because it forces you to name what the next shot is relying on."
    ),
    formula([
        "“This shot inherits  ______________________________________________",
        " from shot ____ , changes ________________________________________ ,",
        " and must hand off ______________________________________________",
        " to shot ____ .”",
    ]),
    fill([
        dict(label="Watch-outs for this shot", hint="the two or three things most likely to go wrong — copy them from the table", lines=3),
        dict(label="Open items affecting this shot", hint="any U mark, and the risk you are accepting", lines=2),
    ], tight=True),

    h2("After generating"),
    p("Three short answers. Two lines is enough; this is a working note, not a report."),
    fill([
        dict(label="What came out", hint="describe the frame, not your feelings about it", lines=2),
        dict(label="Verdict", hint="kept · drift outside the frame · drift in the anchors · rejected", lines=1),
        dict(label="Action", hint="re-framed · re-cut to match this shot · re-generated with anchors first · accepted as-is", lines=2),
    ], tight=True),
    callout(
        "rule", "If you keep it, the table changes",
        "A shot you keep is now the truth. If it differs from the row, edit the row — and if it differs from the previous shot, either "
        "re-generate it or add the change to the next row's ledger with a code. Never leave the document describing a shot you did not make."
    ),

    pagebreak(),
    h1("The fifteen checks, and the failure each one prevents"),
    table(["#", "Check", "The failure it prevents"],
          [[str(i), t, f] for i, (t, _, f) in enumerate(PREFLIGHT, 1)],
          widths=[0.05, 0.50, 0.45], dense=True),
    callout(
        "tip", "If you only have time for five",
        "Run checks 2, 4, 7, 9 and 14: the five anchors, the variant code, the hands, the geography, and the handoff line read aloud. "
        "Those five catch most of what makes six shots look like six films."
    ),
    h2("Printing this checklist"),
    p(
        "Print six copies for a six-shot scene and write the shot number at the top of each. If you are working entirely on screen, copy "
        "the checklist into your notes app once and duplicate it per shot. The boxes work either way: [ ] becomes [x]."
    ),
]


DOC = doc(
    title="Shot preflight checklist",
    subtitle="Fifteen checks for the minute before you generate, and three notes for the minute after",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 6 of 7 · Editable template. Print one per shot.",
    ],
    blocks=BLOCKS,
    filename="product/05-shot-preflight-checklist.md",
)
