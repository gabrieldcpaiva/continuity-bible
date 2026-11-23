"""Document 01 — Field dictionary: every field, what it holds, and how it inherits."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, pagebreak,
                 formula, spacer)
from schema import (PRODUCT, STATUS, CHARACTER_FIELDS, CHARACTER_VARIANT_FIELDS,
                    LOCATION_FIELDS, LOCATION_VARIANT_FIELDS, SHOT_FIELDS,
                    PREFLIGHT)


def field_table(fields):
    rows = []
    for f in fields:
        rows.append([f["label"], f["records"], f["stays"], f["changes"], f["inherit"]])
    return table(
        ["Field", "What it records", "What stays fixed", "What may change", "How it is inherited"],
        rows,
        widths=[0.145, 0.235, 0.20, 0.185, 0.235],
        dense=True,
    )


STATUS_ROWS = [[s["code"], s["name"], s["means"], s["when"]] for s in STATUS]

BLOCKS = [
    lead(
        "Every field below is one of three things: a piece of identity you protect, a variant you allow, or the state "
        "of a single shot. The layer is written next to each field. When in doubt about a field, check its layer first."
    ),
    p(
        "The tables answer four questions for each field: what you write in it, what has to stay the same, what is allowed "
        "to change, and how the next shot receives it. Read one row at a time; the whole point is that no single field "
        "needs a paragraph of explanation on the sheet itself."
    ),

    h2("The four status markers"),
    p(
        "Markers are letters, not colours. Every marker below is written as a letter in the sheets, in the tables and on the "
        "printed page, so the information survives a black-and-white print, a photo of a page, and colour-blind eyes."
    ),
    table(["Code", "Name", "What it means", "When you use it"], STATUS_ROWS,
          widths=[0.09, 0.19, 0.38, 0.34],
          first_col_bold=True),
    p(
        "One row-level rule keeps the markers honest: **the row's status is its strongest marker** — C if anything in the row "
        "changed, otherwise U if anything is unresolved, otherwise F. Any U that sits inside a C row is also written into the "
        "open-items box, so nothing unresolved can hide inside a row that looks finished."
    ),

    h1("Character sheet"),
    p(
        "One sheet per on-screen character. It is deliberately short: five face anchors, three never-change items, and one "
        "baseline look. A second page of description makes the sheet harder to use, not more accurate."
    ),
    field_table(CHARACTER_FIELDS),
    h3("The five-anchor rule"),
    p(
        "Five is a limit, not a minimum. Anchors must be checkable by a stranger in one glance at the framing you will actually "
        "generate: a scar, a mole, a hair tuck, an eyebrow shape, a seated habit. Colour alone is a weak anchor; structure is a "
        "strong one. If you cannot check it at the shot's widest framing, it belongs in “Watch-outs”, not in the anchors."
    ),

    h2("Character variant register"),
    p(
        "Every deliberate change to a character gets a code, a cause and an end. Codes are never reused and never edited after "
        "a shot has been generated with them: if the look needs to change again, that is V3."
    ),
    table([f["label"] for f in CHARACTER_VARIANT_FIELDS],
          [["V1", "Charcoal cardigan buttoned to the third button, sleeves at the wrists.", "1",
            "Starting look.", "Wide and medium.", "4", "Never return to V1."],
           ["V2", "Cardigan open, sleeves pushed to the elbows.", "5",
            "The spill during the ellipsis. She pushed a wet sleeve up.", "Medium and wide.", "next scene",
            "Do not return to V1."]],
          widths=[f["width"] for f in CHARACTER_VARIANT_FIELDS], dense=True,
          caption="Two example rows, from the worked example. A real register usually has one row."),
    p(
        "**Readable at** is the field that keeps variants honest. A change nobody can see at the framing you are generating is "
        "not a variant, it is a hope. Write the framing where the change actually reads, and do not rely on it in shots tighter "
        "than that."
    ),

    h1("Location sheet"),
    p(
        "One sheet per location. It does the job the character sheet does, for the space: five fixed landmarks, three never-change "
        "items, a floor plan, and the geography rules that stop a room from mirroring between shots."
    ),
    field_table(LOCATION_FIELDS),
    h3("The geography rules are the point"),
    p(
        "Most “these shots don't cut together” problems come from a mirrored frame, not a wrong wall colour. Two or three hard rules "
        "written as rules — “the door is always frame-right”, “every camera stays south of the desk” — are checkable in one glance, "
        "where a paragraph of description is not."
    ),

    h2("Location variant register"),
    table([f["label"] for f in LOCATION_VARIANT_FIELDS],
          [["V-A", "Rain on the skylight; the room reads darker and blue.", "1",
            "Weather change in the scene.", "Wide only.", "Never reversed in this scene."]],
          widths=[f["width"] for f in LOCATION_VARIANT_FIELDS], dense=True,
          caption="An example of a location variant. The worked example has none — the room never changes, and that is a "
                  "legitimate, and common, register."),
    p(
        "Most lighting changes are better recorded as light state codes (L1, L2) than as location variants. A light state says "
        "what is switched on, which is what you can actually control; a location variant is for a physical change to the room."
    ),

    h2("Light and time register"),
    p(
        "Light changes are the ones most often left in someone's head, and they are the easiest to record: a code, a description "
        "of what is lit and what is off, and the shots the code covers."
    ),
    table(["Code", "What is lit, what is off", "Shots", "Caused by"],
          [["L1", "ON AIR lamp lit red; corridor strip under the door dark.", "1–5", "The show is on air."],
           ["L2", "ON AIR lamp fully dark, no red wash; a thin warm corridor strip appears under the door.", "6",
            "She takes the show off air."]],
          widths=[0.08, 0.52, 0.10, 0.30], dense=True),
    callout(
        "tip", "Say what is off",
        "The strongest light information in a shot is usually what has been switched off. “No red wash on the door wall” is a "
        "checkable instruction; “moody lighting” is not."
    ),

    h1("Six-shot state table"),
    p(
        "This is the heart of the system: one row per shot, three panels. The panels exist because a single table wide enough to "
        "hold every field cannot be printed, read or filled in by hand. Panel A holds what must not move. Panel B is the "
        "inheritance ledger. Panel C is the state of the shot itself."
    ),
    table(["Panel", "What it holds", "The question it answers"],
          [["A — Anchors and variants",
            "Character, location, the variant in force, the light state, the anchors to hold.",
            "What must not move in this shot?"],
           ["B — Inheritance ledger",
            "Inherits from, changes in this shot, hands off to the next.",
            "What came in, what changed, what must go out?"],
           ["C — Shot state",
            "Action and pose, screen position, gaze, props and hands, framing, watch-outs.",
            "What exactly am I generating?"]],
          widths=[0.22, 0.46, 0.32], dense=True),
    field_table(SHOT_FIELDS),

    h2("Preflight: fifteen checks, one minute"),
    p(
        "The checklist is not part of the record; it is the thing you read with your hand on the button. Each check names the "
        "failure it prevents, because a check whose purpose you cannot remember gets skipped."
    ),
    table(["#", "Check", "What it prevents"],
          [[str(i), title, hint] for i, (title, _, hint) in enumerate(PREFLIGHT, 1)],
          widths=[0.05, 0.55, 0.40], dense=True),
    p(
        "After generating, three short fields go in the drift log: what came out, the verdict, and the action you took. Two "
        "lines per rejected attempt is enough, and it is the only record that teaches you your own failure patterns."
    ),

    h1("What changed while testing this against a full sequence"),
    p(
        "The schema was drafted, used to plan an original six-shot scene, and then revised where a field proved ambiguous, redundant "
        "or too slow to fill in. These are the changes that survived, and the reasons — they are the most useful part of this "
        "document if you plan to adapt the sheets to your own workflow."
    ),
    h3("Cut"),
    ul([
        "**Mood and emotion.** Not checkable at a glance, and it duplicated “action and pose”. Emotion that matters is a body position.",
        "**Lighting mood words.** “Warm, lonely, cold” drifts between shots and cannot be verified. Replaced by light state codes plus the "
        "fixed list of sources that physically exist in the room.",
        "**A prompt box.** It would have made this a prompt pack tied to one model, and it goes stale faster than the decisions do. The "
        "anchor lines and change codes are what feed a prompt; where they go is your workflow's business.",
        "**Exact colour values.** Nobody checks a hex code in a generated frame. Replaced by three colour words plus a negative: “charcoal, "
        "never black, never navy”.",
        "**A risk score per row.** Subjective, unused, and it made finished rows look unfinished.",
        "**A separate “screen direction” field.** Merged into framing and movement, because for a locked-off six-shot scene it was a "
        "field that almost always read “none”.",
    ]),
    h3("Merged"),
    ul([
        "**Character condition and wardrobe.** Combined into the variant register, because a torn sleeve and a rolled sleeve are the same "
        "kind of change and deserve the same code.",
        "**Camera position, height and lens feel.** Kept in the shot state but pulled together on one printed line, so the whole camera "
        "decision is readable in one movement of the eye.",
        "**“What the next shot needs” and “what carries forward”.** These were two fields saying the same thing. Now there is one handoff "
        "line, and the next row starts by copying it.",
    ]),
    h3("Added after the sequence was filled in"),
    ul([
        "**Watch-outs, one line per shot.** There was no obvious place to write “the mug must not stand up again”, and without it that "
        "instruction lived in someone's head. It is now the field that stops the most expensive mistakes.",
        "**Readable at, in the variant register.** A variant that cannot be seen at the framing you are generating is not worth a code, "
        "and the register now makes you say which framing proves it.",
        "**Reversal rule.** Changes tend to leak backwards into earlier shots when you re-generate. One line — “never return to V1 in "
        "this scene” — closes that hole.",
        "**The open-items box.** U marks were being written and then forgotten. Anything marked U now also has to appear in one list, with "
        "the risk you are accepting.",
        "**Three panels instead of one table.** A single table with every field was 29 columns: unprintable, unreadable, and impossible to "
        "fill in by hand. Splitting it into three panels of six rows is the change that made the system usable on paper.",
    ]),
    callout(
        "note", "How this was tested",
        "The schema was applied to the original six-shot scene in part 7 and checked mechanically: every change carries a code that exists, "
        "every code has a start shot and no gaps, every shot inherits from the one before, and the bookend frames match. "
        "That is a design test against a worked example, not a test with other filmmakers — see the validation notes for what is still unproven."
    ),

    h2("The five rules the schema encodes"),
    ol([
        "**Identity is copied, not re-described.** The same words, in the same order, in every shot. Paraphrase is drift.",
        "**A change needs a code, a cause and an end.** No code, no change: that is drift you have not noticed yet.",
        "**Every shot starts with the previous shot's handoff line.** Inheritance is explicit or it does not exist.",
        "**Record what is off.** Dark lamps, empty hands, missing props and absent characters are continuity too.",
        "**When the document and the frame disagree, the document changes.** Otherwise the system quietly stops describing the film.",
    ]),
]


DOC = doc(
    title="Field dictionary",
    subtitle="What every field records, what stays fixed, what may change, and how each shot inherits",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 2 of 7 · Reference. You do not need to read it before you start; keep it open while you fill in your first scene.",
    ],
    blocks=BLOCKS,
    filename="product/01-field-dictionary.md",
)
