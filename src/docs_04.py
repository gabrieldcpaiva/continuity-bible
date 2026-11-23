"""Document 04 — Six-shot state table template (blank)."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, fill,
                 pagebreak, formula, spacer)
from schema import PRODUCT, STATUS

ROWS_A = [[str(i)] + [""] * 4 for i in range(1, 7)]
ROWS_C = [[str(i)] + [""] * 5 for i in range(1, 7)]

BLOCKS = [
    table(["Scene", "Sequence", "Date", "Version"],
          [["", "", "", ""]], widths=[0.30, 0.30, 0.20, 0.20], dense=True, heights=[26]),
    callout(
        "rule", "How to use this table",
        "One row per shot, filled left to right. Row 1 is the anchor shot: it establishes everything and inherits nothing. Every row "
        "after it starts by copying the row above into “Inherits from”, and only then writes what is different."
    ),
    p(
        "The table is split into three panels because a table wide enough to hold every field cannot be printed or filled in by hand. "
        "Panel A is what must not move. Panel B is the handoff. Panel C is the shot itself. Use a shot card (last page) when you want "
        "one shot on its own in front of you."
    ),
    table(["Marker", "Meaning"], [[s["code"], f"{s['name']} — {s['means']}"] for s in STATUS],
          widths=[0.10, 0.90], dense=True),

    pagebreak(),
    h1("Panel A · Anchors and variants"),
    p("What must not move in this shot. Fill this in first: it is where you commit to the look before describing the action."),
    table(
        ["Shot", "Character / location", "Variant in force", "Light state", "Anchors to hold (or why not applicable)"],
        ROWS_A,
        widths=[0.07, 0.17, 0.16, 0.12, 0.48],
        heights=[44] * 6, dense=True,
        caption="Variant in force: the character code (V1, V2 …). Light state: the code from the location sheet (L1, L2 …).",
    ),
    callout(
        "tip", "N/A is a real answer",
        "In an insert with no face, the anchors are not checkable — write what replaces them (“hands only: ring on the left hand, "
        "pencil in the same hand”). A blank cell reads as “I forgot”; N/A reads as “I decided”."
    ),

    pagebreak(),
    h1("Panel B · Inheritance ledger"),
    p(
        "The handoff. Three lines per shot, and the middle one is usually the word “none”. This is the panel that makes six separate "
        "shots into one sequence, because every shot begins with what the last one handed it."
    ),
    table(
        ["Shot", "Inherits from the previous shot (copy it, do not rewrite it)",
         "Changes in this shot (code + what + cause)", "Hands off to the next shot"],
        [["1", "— first shot: this row establishes everything", "", ""]] + [[str(i), "", "", ""] for i in range(2, 7)],
        widths=[0.07, 0.31, 0.31, 0.31],
        heights=[20] + [48] * 5, dense=True,
    ),
    callout(
        "warn", "Two things that break the ledger",
        "Rewriting the inherited line in your own words, which hides the moment the state changed — and writing “none” in the changes "
        "column for a shot where something did change. Both are easy to spot: if a later shot cannot be explained by the chain, the "
        "chain is wrong."
    ),

    pagebreak(),
    h1("Panel C · Shot state"),
    p("The shot itself: what happens, where the body is, what the hands hold, how it is framed, and what usually goes wrong here."),
    table(
        ["Shot", "Action and pose", "Screen position, facing, gaze",
         "Props, hands and prop state codes", "Framing and camera", "Watch-outs"],
        ROWS_C,
        widths=[0.06, 0.22, 0.18, 0.19, 0.18, 0.17],
        heights=[46] * 6, dense=True,
    ),
    callout(
        "tip", "Write the watch-outs last, and write them as instructions",
        "“Mug must not stand up again” beats “cup is tipped”. An instruction tells your future self what to prevent; a description "
        "only tells them what you saw once."
    ),

    h1("Hero prop register"),
    p(
        "Only the props you would notice if they changed. Four or five is plenty. Give each a code and, where it changes, a state code: "
        "P-01a, P-01b. A prop with a state code is a prop your continuity depends on."
    ),
    table(["Prop ID", "Name", "What it always is (identity)", "States (code · what it is · shots)"],
          [["P-01", "", "", ""], ["P-02", "", "", ""], ["P-03", "", "", ""], ["P-04", "", "", ""]],
          widths=[0.09, 0.13, 0.32, 0.46], heights=[26, 26, 26, 26], dense=True),
    p("Props you do not list here still have to behave. Listing five is a promise to check five; listing twenty checks none."),

    h2("Open items"),
    p(
        "Every U mark in the panels above also appears here, with the decision you made or the risk you are accepting. This is the one "
        "place where “I will decide later” is allowed — as long as it is written down."
    ),
    table(["U#", "Where", "What is unresolved", "Decision or accepted risk"],
          [["U1", "", "", ""], ["U2", "", "", ""], ["U3", "", "", ""]],
          widths=[0.06, 0.16, 0.34, 0.44], heights=[26, 26, 26], dense=True),

    h2("Drift log"),
    p(
        "After each generation: two lines about what came out and what you did about it. This is the only record that will teach you "
        "your own failure patterns."
    ),
    table(["Shot", "Try", "What came out", "Verdict", "Action"],
          [["", "", "", "", ""] for _ in range(6)],
          widths=[0.07, 0.06, 0.40, 0.19, 0.28], heights=[30] * 6, dense=True),

    h2("What a useful entry looks like"),
    formula([
        "SHOT 5 · try 2",
        "  came out   cardigan still buttoned, mug upright, door frame-left",
        "  verdict    drift in the anchors",
        "  action     re-generated with the anchor line first, action last",
        "",
        "SHOT 2 · try 1",
        "  came out   perfect except a wall clock above the door",
        "  verdict    drift outside the frame's business",
        "  action     kept; cropped in the edit, logged so it is not repeated",
    ]),
    p(
        "Two entries are enough to see the pattern. The first is a state that slipped; the second is a decision you made on purpose "
        "and wrote down, which is why it is not drift."
    ),

    pagebreak(),
    h1("Shot card — one shot, on its own"),
    p(
        "Print this page six times, or copy the block into your notes, when you want the current shot in front of you instead of three "
        "panels. It holds the same information as one row of the table."
    ),
    table(["Shot no.", "Slug", "Duration / beat", "Row status"],
          [["", "", "", ""]], widths=[0.15, 0.40, 0.25, 0.20], dense=True, heights=[24]),
    fill([
        dict(label="Inherits from the previous shot", lines=2),
        dict(label="Character / location codes and variant in force", lines=1),
        dict(label="Anchors to hold", hint="the five anchors, verbatim — or what replaces them in this framing", lines=2),
        dict(label="Action and pose", lines=2),
        dict(label="Screen position, facing, gaze", lines=2),
        dict(label="Props, hands, prop state codes", lines=2),
        dict(label="Framing and camera", hint="size · height · angle · lens feel · movement", lines=1),
        dict(label="Light state code", lines=1),
        dict(label="Changes in this shot (code + cause)", lines=2),
        dict(label="Hands off to the next shot", lines=2),
        dict(label="Watch-outs", lines=2),
        dict(label="After generating: what came out, verdict, action", lines=2),
    ], tight=True),
]


DOC = doc(
    title="Six-shot state table",
    subtitle="Three panels and a handoff line: what must not move, what changed, and what the next shot inherits",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 5 of 7 · Editable template. Print double-sided if you can; keep Panel B next to you while generating.",
    ],
    blocks=BLOCKS,
    filename="product/04-six-shot-state-table.md",
)
