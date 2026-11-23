"""Document 02 — Character sheet template (blank, printable)."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, fill,
                 pagebreak, spacer, formula, pdf_only)
from schema import PRODUCT, STATUS

STATUS_STRIP = " · ".join(f"{s['code']} = {s['name'].lower()}" for s in STATUS)


def header_block(kind):
    return table(
        ["Sheet for", "Sequence / scene", "Date", "Version"],
        [["", "", "", ""]],
        widths=[0.30, 0.30, 0.20, 0.20],
        dense=True, heights=[26],
    )


BLOCKS = [
    header_block("character"),
    callout(
        "rule", "How to use this sheet",
        "Fill it in once, before you generate this character's first shot. Ten minutes. Then copy the anchor line at the "
        "bottom of page 2 into every prompt, in the same words and the same order, and only change what the variant "
        "register authorises."
    ),

    h1("1 · Who this is"),
    p("Identity layer. Everything on this page stays the same for the whole sequence unless a variant says otherwise."),
    fill([
        dict(label="Character ID", hint="a short code you will repeat in every table row", lines=1),
        dict(label="Name in the script", hint="one spelling, used everywhere", lines=1),
    ], tight=True),
    fill([
        dict(label="Role in the scene", hint="who they are and what they want here, in one sentence", lines=2),
        dict(label="Age read", hint="how old they read on screen, not their birth year", lines=1),
        dict(label="Build and posture", hint="height read, build, and the one seated or standing habit that makes them them", lines=2),
    ], tight=True),

    h2("Five face anchors"),
    p(
        "Five features a stranger could check at a glance in the framing you will actually generate. Structure beats colour: a scar, "
        "a mole, a hair tuck, an eyebrow shape. Do not describe a portrait — list five tripwires."
    ),
    fill([dict(label="Face anchors — copy these five words into every shot", lines=5)], numbered=True),

    h2("Hair, skin, eyes"),
    fill([
        dict(label="Hair (fixed styling)", hint="length, colour read, part, and exactly where it is tucked or falling", lines=2),
        dict(label="Skin and complexion", hint="tone read, undertone, marks you want kept", lines=2),
        dict(label="Eyes", hint="colour read, and glasses or no glasses — write “no glasses” if there are none", lines=1),
    ], tight=True),

    h1("2 · Baseline look and variants"),
    p(
        "Variant layer. V1 is the look in the first shot; everything else is a change with a code. If you only need one look, "
        "you have one row, and that is normal."
    ),
    fill([
        dict(label="V1 — baseline wardrobe", hint="garment set, fit, colours, fastening state, sleeve length, footwear if visible", lines=3),
        dict(label="Signature item (optional)", hint="the one carried or worn object worth tracking, and which hand or side it lives on", lines=2),
    ], tight=True),

    h2("Variant register"),
    table(
        ["Code", "What changes (structural, glanceable)", "From shot", "Caused by", "Readable at", "Ends at", "Reversal rule"],
        [["V1", "", "", "", "", "", ""], ["V2", "", "", "", "", "", ""], ["V3", "", "", "", "", "", ""]],
        widths=[0.07, 0.27, 0.09, 0.18, 0.13, 0.12, 0.14],
        heights=[26, 26, 26], dense=True,
    ),
    callout(
        "tip", "What makes a good variant line",
        "Three to five structural differences someone could see from the other side of the room: what is open, what is pushed up, "
        "what is carried, what colour block has appeared. Fine detail drifts; silhouette holds."
    ),

    h2("Three never-change items"),
    p("The three details that prove it is the same person. If you only check three things, check these."),
    fill([dict(label="Never-change list", lines=3)], numbered=True),

    h2("Voice quality (optional)"),
    p("Only if your workflow involves generated audio. Skip it otherwise."),
    fill([dict(label="Voice", hint="pace, pitch, texture, one verbal habit", lines=1)]),

    h1("3 · The anchor line"),
    p(
        "One sentence that goes at the start of every prompt for this character, before the action. It is the five anchors plus the "
        "variant code in force. Copy it; do not retype it from memory."
    ),
    formula([
        "“CH-01 RAE — right brow scar · mole below the left eye · chin-length bob, silver temples,",
        "tucked behind the right ear only · heavy close-set brows · weight on the left forearm.",
        "Wearing V1: charcoal cardigan buttoned to the third button, cream tee at the neckline,",
        "sleeves at the wrists, broadcast headphones on both ears, cable over the right shoulder.”",
    ]),
    fill([dict(label="My anchor line", hint="write it once, here, and copy it verbatim from now on", lines=5)]),

    h2("Status markers used on this sheet"),
    table(["Marker", "Meaning"], [[s["code"], f"{s['name']} — {s['means']}"] for s in STATUS],
          widths=[0.10, 0.90], dense=True),

    h2("Before you move on"),
    ul([
        "Could a stranger with only this page tell whether the last frame was the same person? If not, written the anchors are not structural enough.",
        "Does every anchor survive a wide shot? Anything only visible in a close-up belongs in Watch-outs on the shot table.",
        "Is there exactly one V1 row, and does every later row have a cause you could actually shoot or skip?",
        "Does the anchor line name a frame side or a hand for anything that could flip? Left, right, east, west — pick one and stay with it.",
    ]),
]


DOC = doc(
    title="Character sheet",
    subtitle="One page per on-screen character: five anchors, one baseline look, every change coded",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 3 of 7 · Editable template. Print one per character. Fill in by hand or retype into any notes app.",
    ],
    blocks=BLOCKS,
    filename="product/02-character-sheet.md",
)
