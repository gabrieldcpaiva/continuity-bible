"""Document 06 — The worked example, filled in end to end."""

from dsl import (doc, h1, h2, h3, p, lead, ul, ol, table, callout, fill,
                 pagebreak, stageplan, formula, spacer)
import example as X
from schema import PRODUCT, PREFLIGHT
from plan import ascii_plan

A = {k: (s, l) for k, l, s in X.ANCHORS}
ANCHOR_LINE = (
    "CH-01 RAE — " + " · ".join(s for _, _, s in X.ANCHORS) + ". "
    "Wearing V1: charcoal grey fine-knit cardigan buttoned to the third button, cream crew-neck tee at the "
    "neckline, sleeves at the wrists. Matte black broadcast headphones on both ears, coiled cable over the "
    "right shoulder. No glasses."
)

BEATS = [
    ["1", "ROOM, FIRST LIGHT", "6 s", "The room and her, mid-show. The anchor shot: it proves the room, the light and the wardrobe at once."],
    ["2", "CUE SHEET, PENCIL DOWN", "5 s", "She underlines a line on the cue sheet and keeps talking."],
    ["3", "INSERT, CUE SHEET AND MUG", "4 s", "Her hands only: the pencil, the paper, the mug lifted and set back down."],
    ["4", "OVER HER SHOULDER TO THE DOOR", "5 s", "She stops talking. Her head turns toward the door."],
    ["5", "THE CALLER, CLOSE", "8 s", "Thirty seconds later. She is listening. The mug is on its side."],
    ["6", "OFF AIR", "7 s", "She presses one button, leans back, and looks at the door. The lamp goes dark."],
]

CHAR_ROWS = [
    ["Character ID", X.CHARACTER["char_id"]],
    ["Name in the script", X.CHARACTER["name_in_script"]],
    ["Role in the scene", X.CHARACTER["role_in_scene"]],
    ["Age read", X.CHARACTER["age_read"]],
    ["Build and posture", X.CHARACTER["build_posture"]],
    ["Face anchors", "\n".join(f"{i}. {l}" for i, (_, l, _) in enumerate(X.ANCHORS, 1))],
    ["Hair (fixed styling)", X.CHARACTER["hair_fixed"]],
    ["Skin and complexion", X.CHARACTER["skin_complexion"]],
    ["Eyes", X.CHARACTER["eyes"]],
    ["Signature item", X.CHARACTER["signature_item"]],
    ["Never-change list", "\n".join(f"{i}. {t}" for i, t in enumerate(X.CHARACTER["never_change"], 1))],
    ["Voice (optional)", X.CHARACTER["voice_optional"]],
]

LOC_ROWS = [
    ["Location ID", X.LOCATION["loc_id"]],
    ["Location name", X.LOCATION["loc_name"]],
    ["Story function", X.LOCATION["story_function"]],
    ["Room read", X.LOCATION["room_read"]],
    ["Palette and materials", X.LOCATION["palette_materials"]],
    ["Light sources", X.LOCATION["light_sources_fixed"]],
    ["Time band", X.LOCATION["time_band"]],
    ["Sound (optional)", X.LOCATION["sound_optional"]],
    ["Geography rules", "\n".join(f"{i}. {r}" for i, r in enumerate(X.LOCATION["geography_rules"], 1))],
    ["Never-change list", "\n".join(f"{i}. {t}" for i, t in enumerate(X.LOCATION["never_change"], 1))],
]

LANDMARK_ROWS = [[n, d] for n, d in X.LANDMARKS] + [[n, d] for n, d in X.EXTRA_LANDMARKS]

VAR_ROWS = [[v["variant_code"], v["what_changes"], v["first_shot"], v["motivation"],
             v["glanceable_at"], v["ends_at"], v["reversal"]] for v in X.CHARACTER_VARIANTS]

PROP_ROWS = []
for pr in X.PROPS:
    states = "\n".join(f"**{c}** — {w} _({shots})_" for c, w, shots in pr["states"])
    PROP_ROWS.append([pr["prop_id"], pr["name"], pr["identity"], states])

LIGHT_ROWS = [[l["code"], l["description"], l["shots"], l["caused"]] for l in X.LIGHT_STATES]

PANEL_A = [[s["shot_no"], f"{X.CHARACTER['char_id']} / {X.LOCATION['loc_id']}",
            s["variant"], s["light"], s["anchors_hold"]] for s in X.SHOTS]

PANEL_B = [[s["shot_no"], s["inherits_from"], s["changes_in_shot"], s["hands_off"]] for s in X.SHOTS]

PANEL_C = [[s["shot_no"], s["action_pose"],
            s["screen_position"] + " **Look:** " + s["gaze"],
            s["props_hands"] + " **State:** " + s["prop_states"],
            s["framing"], s["hazards"]] for s in X.SHOTS]

CAMERA_ROWS = [[n, pos, h, d, lens] for n, pos, h, d, lens in X.CAMERA_POSITIONS]

OPEN_ROWS = [[o["mark"], o["where"], o["issue"], o["decision"], o["risk"]] for o in X.OPEN_ITEMS]

DRIFT_ROWS = [[d["shot"], d["attempt"], d["what"], d["verdict"], d["action"]] for d in X.DRIFT_LOG]

PREFLIGHT_ROWS = [[t, X.FILLED_PREFLIGHT[t]] for t, _, _ in PREFLIGHT]

BLOCKS = [
    lead(
        "One original six-shot sequence, planned with the sheets, with every field filled in. Read it once before you fill in "
        "your own scene: the fastest way to learn a template is to watch it used badly in a film you never have to make."
    ),
    callout(
        "note", "What this is, and is not",
        "“Night Signal” is a fictional short invented for this product, and the drift log below is an illustration of what a working "
        "log looks like — not a record of a real generation session, a real shoot, or testing with other filmmakers. No footage exists."
    ),

    h1("The scene"),
    table(["", ""],
          [["Film", X.FILM["title"]],
           ["Scene", X.FILM["scene"]],
           ["Logline", X.FILM["logline"]],
           ["Time", X.FILM["sequence_time"]],
           ["Why this scene", X.FILM["why_this_scene"]]],
          widths=[0.14, 0.86], first_col_bold=True, dense=True),

    h2("Six beats, before any field is filled in"),
    p(
        "Step one is always the beats, because the table is only as good as the shots it describes. These are written as beats, not "
        "prompts: what happens, in order."
    ),
    table(["Shot", "Slug", "Length", "The beat"], BEATS, widths=[0.07, 0.24, 0.09, 0.60], dense=True),
    p(
        "Two decisions are made here, before anything is generated. First, every camera will stay on the south side of the desk, so the "
        "six shots cut together as one space. Second, the one change the scene needs — the spill — happens in the thirty seconds between "
        "shot 4 and shot 5, where nobody has to generate it."
    ),

    h1("Character sheet, filled in"),
    table(["Field", "Rae"], CHAR_ROWS, widths=[0.22, 0.78], first_col_bold=True, dense=True),
    h2("The anchor line"),
    p("This is the line that goes at the start of every prompt for this character, before the action:"),
    formula([ANCHOR_LINE[i:i + 96] for i in range(0, len(ANCHOR_LINE), 96)]),
    callout(
        "tip", "Notice what the anchor line does not contain",
        "No mood, no lighting, no camera, no story. Those change per shot. Everything in this line must survive every shot, so it is "
        "kept to things that cannot quietly be different in shot 5 without you noticing."
    ),

    h2("Variant register"),
    table([f for f in ["Code", "What changes", "From shot", "Caused by", "Readable at", "Ends at", "Reversal rule"]],
          VAR_ROWS, widths=[0.07, 0.26, 0.09, 0.19, 0.13, 0.12, 0.14], dense=True,
          caption="Two rows, one change. The cardigan is the only thing about Rae that changes in the scene."),

    h1("Location sheet, filled in"),
    table(["Field", "Studio B"], LOC_ROWS, widths=[0.22, 0.78], first_col_bold=True, dense=True),

    h2("Landmarks"),
    p("Five fixed, three extra. Each one carries a frame position, because a landmark with no frame position cannot be checked."),
    table(["Landmark", "What makes it checkable"], LANDMARK_ROWS, widths=[0.18, 0.82], first_col_bold=True, dense=True),
]

BLOCKS += [
    h1("Floor plan"),
    p(
        "The plan is drawn from the numbers in the camera table, so the two cannot disagree. Every camera marker sits below the desk: "
        "the whole scene is shot from one side of the line, and nothing has to be re-established between shots."
    ),
    stageplan(ascii_plan(),
              caption="Studio B, north at the top. The room is 4.2 m by 3.2 m; the desk is free-standing so cameras can pass on the south "
                      "side. The PDF edition of this book prints the same plan as a drawn diagram.",
              data={"kind": "filled"}),
    h2("Camera positions"),
    table(["Shot", "Position in the room", "Height", "Direction", "Lens feel (optional)"],
          CAMERA_ROWS, widths=[0.07, 0.33, 0.10, 0.29, 0.21], dense=True, first_col_bold=True),

    h1("Light states and props"),
    h2("Light and time register"),
    table(["Code", "What is lit, what is off", "Shots", "Caused by"], LIGHT_ROWS,
          widths=[0.08, 0.52, 0.10, 0.30], dense=True, first_col_bold=True),
    p(
        "Two codes for six shots. The room's light is a constant with one switch at the end, which is why the change reads as an event "
        "rather than as drift."
    ),
    h2("Hero prop register"),
    table(["ID", "Prop", "What it always is", "States"], PROP_ROWS,
          widths=[0.07, 0.10, 0.43, 0.40], dense=True, first_col_bold=True),

    h1("Panel A · Anchors and variants"),
    p("What must not move, per shot. The variant column is the only place the look is allowed to differ."),
    table(["Shot", "Character / location", "Variant", "Light", "Anchors to hold (or why not applicable)"],
          PANEL_A, widths=[0.06, 0.15, 0.09, 0.07, 0.63], dense=True, first_col_bold=True),
    callout(
        "tip", "Two rows worth studying",
        "Shot 1 does not check the five anchors at all, because the face is too small in a wide to judge them — it checks the "
        "silhouette, the hair tuck and the cardigan instead. Shot 3 is an insert with no face, so it trades the anchors for the ring "
        "on the left hand and the pencil in the same hand. Both are N/A answers written as decisions rather than gaps."
    ),

    h1("Panel B · Inheritance ledger"),
    p(
        "The panel that turns six shots into one sequence. Read the left column downwards and you have the whole scene's continuity in "
        "six lines. Note that the middle column says “none” four times out of six — that is a healthy ledger, not a lazy one."
    ),
    table(["Shot", "Inherits from the previous shot", "Changes in this shot (code + cause)", "Hands off to the next shot"],
          PANEL_B, widths=[0.06, 0.30, 0.31, 0.33], dense=True, first_col_bold=True),

    h1("Panel C · Shot state"),
    p(
        "The same information a shot card would hold, kept in the table so the whole scene can be read at once. Split into two tables so "
        "the text stays at a readable size in print."
    ),
    table(["Shot", "Action and pose", "Screen position, facing, gaze",
           "Props, hands, prop states", "Framing and camera", "Watch-outs"],
          PANEL_C[:3], widths=[0.07, 0.20, 0.17, 0.19, 0.17, 0.20], dense=True, first_col_bold=True),
    table(["Shot", "Action and pose", "Screen position, facing, gaze",
           "Props, hands, prop states", "Framing and camera", "Watch-outs"],
          PANEL_C[3:], widths=[0.07, 0.20, 0.17, 0.19, 0.17, 0.20], dense=True, first_col_bold=True),

    h1("The change, end to end"),
    lead("One intentional change, three consequences, traced from the shot that starts it to the shot that ends it."),
    p(
        "In shot 4 she hears something and turns to the door. Thirty seconds pass off-screen. When we cut back in shot 5, three things "
        "are different, and each one is a code in the ledger:"
    ),
    table(["Code", "What it changes", "Starts", "Traced through", "Ends", "Why it is safe to generate"],
          [["V2", "Cardigan open, sleeves pushed to the elbows.",
            "Shot 5", "Panel A (variant column, shots 5–6); Panel B (shot 5 changes); Panel C (shot 5 action)",
            "Scene 15", "It is a silhouette change: open front, rolled sleeves, a bigger block of cream tee. Visible at medium and wide."],
           ["P-01b", "Mug on its side, 20 cm coffee ring on the blotter.",
            "Shot 5", "Prop register; Panel C (shots 5–6); the watch-out “the mug must not stand up again”",
            "Scene 15", "The state is described as an object lying in a specific place, not as an animation. Nothing has to be spilled on camera."],
           ["L2", "ON AIR lamp dark, corridor strip lit under the door.",
            "Shot 6", "Light register; Panel A (light column, shot 6); Panel B (shot 6 changes)",
            "Until she is back on air", "It is a switch, described as what is off. Dark is easier to generate than dark-and-red."]],
          widths=[0.07, 0.19, 0.08, 0.24, 0.11, 0.31], dense=True, first_col_bold=True),
    h3("How the handoff is written at the seam"),
    p(
        "The seam is where a change usually leaks. Here is the exact pair of cells that closes it — the last line of shot 4 and the "
        "first line of shot 5:"
    ),
    formula([
        "SHOT 4 · hands off  →  “…30 seconds later, off-screen: mug tipped (P-01b) with the coffee ring on",
        "                        the blotter, cardigan open with sleeves pushed to the elbow (V2). Lamp still L1.”",
        "",
        "SHOT 5 · changes    →  “C — V2 (cardigan open, sleeves to the elbow). C — P-01b (mug tipped, coffee ring",
        "                        on the blotter). Both caused by the spill during the 30-second ellipsis, both logged",
        "                        before generating.”",
    ]),
    p(
        "Shot 4 names the change before it happens, so nobody has to infer it from the picture. Shot 5 names the cause, so the change "
        "reads as a decision rather than a mistake. If the two cells disagreed — the classic version is a mug that is tipped in shot 5 "
        "and upright in shot 6 — the ledger would show the contradiction in one glance, which is the entire point of writing it down."
    ),
    callout(
        "rule", "The seam rule",
        "A change must be named in the shot *before* it appears, or in the shot where it appears, with a cause. Never in neither."
    ),

    h1("Preflight for shot 5, filled in"),
    p(
        "Shot 5 is the one with the change in it, so it is the one worth showing. This is what the checklist looks like one minute "
        "before generating."
    ),
    table(["Check", "Answer"], PREFLIGHT_ROWS, widths=[0.28, 0.72], first_col_bold=True, dense=True),
    callout(
        "tip", "The two answers that do the most work",
        "“Variant code: V2 with a cause” and “Prop state: mug on its side, handle frame-left, ring 20 cm, still wet”. The first stops "
        "the wardrobe reverting; the second stops the mug standing up again, which is the single most common break in a scene like this."
    ),

    h1("Open items and drift log"),
    h2("Open items"),
    p("Two U marks, both accepted in writing rather than left to chance."),
    table(["", "Where", "What is unresolved", "Decision or accepted risk", "Risk"],
          OPEN_ROWS, widths=[0.05, 0.16, 0.25, 0.38, 0.16], dense=True),
    h2("Drift log (illustrative)"),
    p(
        "What a working log looks like after a session. Two lines per rejected attempt is enough, and the pattern is the useful part: "
        "two of these three failures are hands and wardrobe, not faces."
    ),
    table(["Shot", "Try", "What came out", "Verdict", "Action"], DRIFT_ROWS,
          widths=[0.06, 0.06, 0.38, 0.20, 0.30], dense=True),

    h1("Six things this example shows"),
    ol([
        "**The anchor shot does the heavy lifting.** Shot 1 proves the room, the light and the wardrobe at once, and every later row is "
        "checked against it rather than against memory.",
        "**Most rows say “none”.** Four of six changes cells are “none”, and that is what a controlled sequence looks like. A ledger "
        "full of changes is a scene that will drift.",
        "**The change is authorised before it is seen.** Shot 4 hands off V2 and P-01b before shot 5 exists, so there is nothing to "
        "infer at the seam.",
        "**Changes live in ellipses.** The spill is described, not animated. The hardest thing in the scene is the one nobody has to generate.",
        "**Not applicable is a decision.** The insert has no face, so its anchor column says what replaces the face checks: the ring, the "
        "hand, the pencil.",
        "**The bookend test is free.** Shot 6 uses shot 1's framing exactly. If the room reads as the same room at both ends, the "
        "audience believes the middle.",
    ]),

    h2("Your turn, in three steps"),
    p("Take a scene you already have six loose shots for, and do only this much:"),
    ol([
        "Write the six beats. No prompts.",
        "Fill the five anchors and the three never-change items for your character, then write the anchor line as one sentence.",
        "Fill Panel B only — inherits, changes, hands off — for all six shots. If the middle column has more than two changes in it, you "
        "have found where your drift will come from.",
    ]),
    p(
        "That is about twenty minutes, and it is the part of this system that pays for itself first. The character and location sheets get "
        "better as you use them; the ledger is the piece that changes how the shots come out."
    ),

    h2("Where to go next"),
    ol([
        "**Run the preflight on your next shot.** Fifteen checks, one minute. It is the part of the system that survives a busy day.",
        "**Add a second character sheet** if your scene has two people on screen, and add two columns to the table — one per character. "
        "The method does not change; only the width does.",
        "**Copy the spreadsheet tracker** from the folder if you would rather work in rows than on paper. It holds the same fields as the "
        "three panels, in one wide table.",
        "**Keep the drift log.** After two or three scenes you will know your own failure patterns, and those are worth more than any "
        "general advice about continuity.",
    ]),
    callout(
        "note", "One last thing",
        "This system is a record of decisions, and its value comes from being true to the frames you actually keep. If you only use one part "
        "of it, use the inheritance ledger: a shot that starts from the previous shot's handoff line will cut with it far more often than "
        "one that starts from a fresh description.",
    ),
]


DOC = doc(
    title="Worked example",
    subtitle="“Night Signal”, scene 14: six connected shots, filled in, with the one change traced end to end",
    meta=[
        "**The Continuity Bible** · " + PRODUCT["version"] + " · " + PRODUCT["edition_date"],
        "Part 7 of 7 · Worked example. Fictional film, fictional generation log. Nothing here was shot or tested with other people.",
    ],
    blocks=BLOCKS,
    filename="product/06-worked-example-the-third-caller.md",
)
