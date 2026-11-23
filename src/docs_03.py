"""Document 03 — Location sheet template (blank, printable, with a floor plan)."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, fill, keep,
                 pagebreak, stageplan, formula, spacer)
from schema import PRODUCT, STATUS

BLANK_PLAN = r"""
                 NORTH
      +----------------------------------------------+
      |                                              |
      |                                              |
      |                                              |
      |                                              |
      |                                              |
      |                                              |
      |                                              |
      +----------------------------------------------+
                 SOUTH

   Fixed things to mark:   door [D]   window [W]   fixed furniture [#]
                           practical lights (o)   camera positions S1-S6
"""

BLOCKS = [
    table(["Sheet for", "Sequence / scene", "Date", "Version"],
          [["", "", "", ""]], widths=[0.30, 0.30, 0.20, 0.20], dense=True, heights=[26]),
    callout(
        "rule", "How to use this sheet",
        "Fill it in once per location, next to the character sheet. The floor plan is not decoration: it is the fastest way to see "
        "that you have put two cameras on opposite sides of your character, which is the mistake that makes a cut feel flipped."
    ),

    h1("1 · The room"),
    p("Identity layer. Everything here stays the same for the whole sequence unless a location variant says otherwise."),
    fill([
        dict(label="Location ID", hint="short code used in every table row", lines=1),
        dict(label="Location name", hint="one spelling, used in notes and prompts", lines=1),
    ], tight=True),
    fill([
        dict(label="Story function", hint="what this room does to the scene — pressure, comfort, exposure", lines=2),
        dict(label="Room read", hint="shape, approximate size, ceiling height, how many ways in or out", lines=4),
        dict(label="Palette and materials", hint="three to five surface colours and textures that make it one room", lines=4),
        dict(label="Time band", hint="the clock window, e.g. 21:10-21:22 · and what light is impossible because of it", lines=2),
        dict(label="Ceiling and floor", hint="what is up there and down there · what must never appear if the camera tilts", lines=2),
    ], tight=True),

    pagebreak(),
    h2("Fixed landmarks — five, no more"),
    p(
        "Five objects or features that never move. For each one, write its position in frame terms and one identifying detail that "
        "would prove it is the same room. Position plus detail is what makes a landmark checkable."
    ),
    fill([dict(label="Landmarks", hint="name · frame position · one identifying detail", lines=5)], numbered=True),

    h2("Light sources that exist in the room"),
    p(
        "The physics, not the look: every practical light, where it comes from, and what colour it reads. Whether each one is on is "
        "recorded later as a light state code."
    ),
    fill([dict(label="Light sources", hint="lamp — warm, from the desk's east end · window — cool, from frame-left · none", lines=3)]),

    h2("What must never appear in this room"),
    p(
        "The mirror image of a landmark: things a model likes to add that would break the scene. A wall clock is the common one, "
        "because it records a time you did not choose. Write the ban, not the wish."
    ),
    fill([dict(label="Banned", hint="no wall clock · no window · no brand marks · no second door", lines=4)]),

    pagebreak(),
    h1("2 · Floor plan"),
    p(
        "Draw the room from above, with north marked. Put a circle where you plan to stand for each shot and label it S1 to S6. "
        "Then draw the line your character faces along — every camera should be on the same side of it."
    ),
    stageplan(
        BLANK_PLAN,
        caption="Copy this outline into any drawing app, or print the page and draw on it. What matters is where the cameras are, "
                "not how neat the plan is.",
        data={"kind": "blank", "height": 320},
    ),

    callout(
        "tip", "The two-second check",
        "Look at the circles. If any circle is on the opposite side of the character from the others, either move it or write "
        "down why you crossed the line — the next person to open this file, including you in three days, will not remember."
    ),

    pagebreak(),
    keep(
        h2("Camera positions"),
        table(["Shot", "Position in the room", "Height", "Direction", "Framing / lens feel (optional)"],
              [[str(i), "", "", "", ""] for i in range(1, 7)],
              widths=[0.08, 0.30, 0.10, 0.24, 0.28],
              heights=[30] * 6, dense=True),
    ),

    h2("Geography rules"),
    p(
        "Two or three hard rules written as rules. These are the ones you check in one glance while a generation runs. "
        "Examples: “the door is always frame-right”; “every camera stays on the south side of the desk”; “the window is never in shot”."
    ),
    fill([dict(label="Rule 1", lines=2), dict(label="Rule 2", lines=2), dict(label="Rule 3", lines=2)], tight=True),

    pagebreak(),
    h1("3 · Light states"),
    p(
        "One row per distinct lighting state. A state is what is on and what is off — not how it feels. Most scenes need one or two."
    ),
    table(["Code", "What is lit, what is off", "Shots", "Caused by"],
          [["L1", "", "", ""], ["L2", "", "", ""], ["L3", "", "", ""]],
          widths=[0.09, 0.47, 0.12, 0.32], heights=[30, 30, 30], dense=True),
    p("Add rows if you need them. If you need more than four light states in one scene, check whether two of them are really the same state."),

    h2("Location variants"),
    p(
        "Physical changes to the room: a broken window, furniture moved, weather on a skylight. Lighting changes belong above, as light "
        "states. Many scenes have no location variants at all."
    ),
    table(["Code", "What changes", "From shot", "Caused by", "Readable at", "Reversal rule"],
          [["", "", "", "", "", ""], ["", "", "", "", "", ""]],
          widths=[0.08, 0.30, 0.10, 0.20, 0.15, 0.17], heights=[28, 28], dense=True),

    h2("Sound bed (optional)"),
    p("Room tone and recurring sounds, for anyone cutting audio later. Skip it if you are not. "),
    fill([dict(label="Sound", hint="room tone · recurring sounds · what must not be heard", lines=2)]),

    h2("Three never-change items"),
    p("The three details that prove it is the same room."),
    fill([dict(label="Never-change list", lines=3)], numbered=True),

    h2("Before you move on"),
    ul([
        "Does every landmark have a frame position, not just a name?",
        "Is there a rule that stops the room mirroring between shots?",
        "Does the floor plan show one side of the line that all six cameras stay on?",
        "Is there anything in the room that records time — a clock, a screen, a phone — that you have not decided about?",
        "Do you know which light is the key, and which lights are off in the shot you are about to generate?",
    ]),
]


DOC = doc(
    title="Location sheet",
    subtitle="One page per location: five fixed landmarks, one floor plan, every light state coded",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 4 of 7 · Editable template. Print one per location.",
    ],
    blocks=BLOCKS,
    filename="product/03-location-sheet.md",
)
