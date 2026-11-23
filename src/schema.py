"""The Continuity Bible — field schema (single source of truth).

Everything the buyer edits is defined here once: the field dictionary, the blank
templates, the worked-example tables and the HTML form all read from this module.

Three layers, deliberately kept separate:

  IDENTITY  what must stay the same for the whole sequence (character, location)
  VARIANT   an intentional, authorised change, given a code (V1, V2 ... / L1 ... / P-01a)
  SHOT STATE the exact state of one shot, plus the handoff line to its neighbour

Status markers (never colour alone — the letters travel with the values):
  F      fixed
  C      changed intentionally (always followed by the variant code that authorises it)
  U      unresolved (needs a decision before generating)
  N/A    not applicable to this shot
"""

PRODUCT = {
    "name": "The Continuity Bible",
    "tagline": "A six-shot handoff system for independent AI filmmakers",
    "version": "v1.0",
    "edition_date": "November 2026",
    "price_line": "Test price US$29 (unvalidated)",
    "model_note": (
        "Written to be generation-model independent. Where a technical term appears "
        "(lens feel, camera height, frame side) it is marked optional: use the parts "
        "your workflow can control, and keep the rest as a note to yourself."
    ),
}

STATUS = [
    {
        "code": "F",
        "name": "Fixed",
        "color": "#1D6B4A",
        "means": "Locked for the whole sequence. Copy it into every shot word for word.",
        "when": "The field is part of identity, or a variant is in force and this field is not changing.",
    },
    {
        "code": "C",
        "name": "Changed intentionally",
        "color": "#A4562A",
        "means": "This shot deliberately differs from the one before it. The change has a code.",
        "when": "Wardrobe, condition, props, light or dressing shift on purpose. Never write C without the code.",
    },
    {
        "code": "U",
        "name": "Unresolved",
        "color": "#8A5A11",
        "means": "You have not decided yet. It is allowed to stay open, but not silently.",
        "when": "A choice is deferred. Write what you will accept if the generation makes its own choice.",
    },
    {
        "code": "N/A",
        "name": "Not applicable",
        "color": "#5B6673",
        "means": "The field does not apply to this shot. Say why in three words.",
        "when": "No face in an insert, no prop in frame, no second character in the scene.",
    },
]

# ---------------------------------------------------------------------------
# Field definitions. `key` is the machine name used by the HTML form and the
# CSV export; `label` is what the buyer reads. `lines` is writing space in the
# printed template (0 = single short line).
# ---------------------------------------------------------------------------

CHARACTER_FIELDS = [
    dict(key="char_id", layer="Identity", label="Character ID", lines=0,
         records="A short code you will repeat in every table row, e.g. CH-01.",
         stays="The code itself, for the whole sequence.",
         changes="Never. A new code means a different character.",
         inherit="Copy the code into the shot table, never the character's name."),
    dict(key="name_in_script", layer="Identity", label="Name in the script", lines=0,
         records="The name used in your notes and prompts. One spelling only.",
         stays="Spelling and capitalisation.",
         changes="Only if the script is rewritten.",
         inherit="Use this exact spelling in every prompt."),
    dict(key="role_in_scene", layer="Identity", label="Role in the scene (one line)", lines=1,
         records="Who this person is and what they want in this scene, in one sentence.",
         stays="The sentence, for the whole scene.",
         changes="Per scene, not per shot.",
         inherit="Read it before every generation; it keeps behaviour in range."),
    dict(key="age_read", layer="Identity", label="Age read", lines=0,
         records="How old the person reads on screen, not their birth year. e.g. 'mid-40s'.",
         stays="The band. Do not let it float between shots.",
         changes="Only for a deliberate time jump, logged as a variant.",
         inherit="Quote the same words in every prompt."),
    dict(key="build_posture", layer="Identity", label="Build and posture", lines=1,
         records="Height read, build, and the one posture habit that makes them them.",
         stays="The silhouette. This is the first thing that drifts when you only describe a face.",
         changes="Only if they sit, stand or undress as part of the action (log it).",
         inherit="Repeat the posture habit in shots where they are seated."),
    dict(key="face_anchors", layer="Identity", label="Five face anchors", lines=5,
         records="Five features, in plain words, that a stranger could check at a glance. Not a portrait description.",
         stays="All five, in every shot where the face is visible.",
         changes="Nothing. If one anchor changes, it is a different character.",
         inherit="Copy all five, word for word, into every prompt. Do not summarise or re-order them."),
    dict(key="hair_fixed", layer="Identity", label="Hair (fixed styling)", lines=2,
         records="Length, colour read, part, and exactly how it is worn: tucked where, falling where.",
         stays="Part, tuck, length and colour.",
         changes="Only as a logged variant (e.g. hair wet, hat on).",
         inherit="Say where it is tucked, not just 'short hair'."),
    dict(key="skin_complexion", layer="Identity", label="Skin and complexion", lines=1,
         records="Tone read, undertone, and any marks you want kept (freckles, shine, a mole).",
         stays="Tone and the marks you name.",
         changes="Condition can change by variant (sweat, dirt, blood) — log it.",
         inherit="Keep the same words; avoid inventing new descriptors."),
    dict(key="eyes", layer="Identity", label="Eyes", lines=0,
         records="Eye colour read, and whether they wear glasses or not. 'No glasses' is information.",
         stays="Colour and the glasses decision.",
         changes="Only as a logged variant.",
         inherit="Write 'no glasses' when there are no glasses, so they do not appear."),
    dict(key="wardrobe_baseline", layer="Variant", label="Baseline wardrobe (V1)", lines=3,
         records="The default garment set, fit, colours, and the fastening state. This is your V1.",
         stays="Garment set and colour while V1 is in force.",
         changes="A new variant code takes over; V1 is never edited afterwards.",
         inherit="Copy the V1 line verbatim until a later code replaces it."),
    dict(key="signature_item", layer="Variant", label="Signature item (optional)", lines=1,
         records="One carried or worn object worth tracking through the sequence (mug, badge, ring).",
         stays="Presence, side and state until a prop state changes.",
         changes="Prop states get their own codes (P-01a, P-01b).",
         inherit="Name the hand that holds it."),
    dict(key="never_change", layer="Identity", label="Never-change list (three items)", lines=3,
         records="If you only hold three things, hold these. Your personal drift tripwires.",
         stays="All three.",
         changes="Nothing.",
         inherit="This is the list you read out loud before pressing generate."),
    dict(key="voice_optional", layer="Identity", label="Voice quality (optional)", lines=1,
         records="Pace, pitch and texture, for anyone working with generated audio.",
         stays="The description.",
         changes="Per scene.",
         inherit="Optional: skip it if your workflow is silent."),
]

CHARACTER_VARIANT_FIELDS = [
    dict(key="variant_code", label="Code", width=0.08),
    dict(key="what_changes", label="What changes (structural, glanceable)", width=0.26),
    dict(key="first_shot", label="From shot", width=0.09),
    dict(key="motivation", label="Caused by", width=0.19),
    dict(key="glanceable_at", label="Readable at", width=0.14),
    dict(key="ends_at", label="Ends at", width=0.12),
    dict(key="reversal", label="Reversal rule", width=0.12),
]

LOCATION_FIELDS = [
    dict(key="loc_id", layer="Identity", label="Location ID", lines=0,
         records="Short code repeated in every table row, e.g. LOC-01.",
         stays="The code.",
         changes="Never.",
         inherit="Copy the code, not the place name."),
    dict(key="loc_name", layer="Identity", label="Location name", lines=0,
         records="The name used in the script and in prompts. One spelling.",
         stays="Spelling.",
         changes="Never within a sequence.",
         inherit="Use the same words every time."),
    dict(key="story_function", layer="Identity", label="Story function (one line)", lines=1,
         records="What this room is for in the scene: pressure, comfort, exposure.",
         stays="For the whole sequence.",
         changes="Per scene.",
         inherit="It guides light and framing choices, not facts."),
    dict(key="room_read", layer="Identity", label="Room read", lines=2,
         records="Shape, approximate size, ceiling height, and how many ways in or out.",
         stays="Everything here. This is the room's skeleton.",
         changes="Never within a sequence.",
         inherit="Repeat it in wide shots; it is the cheapest way to keep a room recognisable."),
    dict(key="fixed_landmarks", layer="Identity", label="Fixed landmarks (up to five)", lines=5,
         records="Five objects or features that never move, each with its frame position and one identifying detail.",
         stays="Position, count and identifying detail.",
         changes="Nothing. If a landmark moves, the room has changed — log it as a location variant.",
         inherit="Name at least two landmarks per shot with their frame side."),
    dict(key="palette_materials", layer="Identity", label="Palette and materials", lines=2,
         records="The three to five surface colours and textures that make the room read as one room.",
         stays="Colour relationships, not exact hex values.",
         changes="Only with a logged lighting variant.",
         inherit="Quote the same colour words; do not invent new ones."),
    dict(key="light_sources_fixed", layer="Identity", label="Light sources that exist in the room", lines=3,
         records="Every practical light and where it comes from. This is the physics of the room, not the look.",
         stays="Which sources exist and their direction.",
         changes="Whether each source is on, off or dimmed — that is a light state code.",
         inherit="State the light state code, not a mood word."),
    dict(key="time_band", layer="Identity", label="Time band", lines=0,
         records="The clock window the sequence sits inside, e.g. 02:40–02:52, deep night, no daylight possible.",
         stays="The whole sequence.",
         changes="Only across a scene break.",
         inherit="Repeat it every shot: it rules out windows, sun, and street light."),
    dict(key="sound_optional", layer="Identity", label="Sound bed (optional)", lines=1,
         records="Room tone and the recurring sounds, for anyone cutting real audio later.",
         stays="Room tone description.",
         changes="Events can enter and leave.",
         inherit="Optional: skip if you are not working with generated audio."),
    dict(key="geography_rules", layer="Identity", label="Geography rules", lines=3,
         records="Two or three hard rules that keep the room readable: what is always frame-left, always frame-right, which side the camera stays on.",
         stays="The rules. They are the point of the sheet.",
         changes="Never within a sequence.",
         inherit="Check them as rules, not as descriptions. They catch mirroring."),
    dict(key="never_change", layer="Identity", label="Never-change list (three items)", lines=3,
         records="The three details that prove it is the same room.",
         stays="All three.",
         changes="Nothing.",
         inherit="Read out loud with the character's list before generating."),
]

LOCATION_VARIANT_FIELDS = [
    dict(key="variant_code", label="Code", width=0.08),
    dict(key="what_changes", label="What changes", width=0.30),
    dict(key="first_shot", label="From shot", width=0.10),
    dict(key="motivation", label="Caused by", width=0.20),
    dict(key="glanceable_at", label="Readable at", width=0.16),
    dict(key="reversal", label="Reversal rule", width=0.16),
]

SHOT_FIELDS = [
    dict(key="shot_no", layer="Shot state", label="Shot", lines=0,
         records="The shot number and a slug you will recognise, e.g. '3 — INSERT, CUE SHEET'.",
         stays="The number. Never renumber mid-sequence.",
         changes="n/a",
         inherit="Rows are read in order; the row above is always the shot before."),
    dict(key="action_pose", layer="Shot state", label="Action and pose", lines=2,
         records="What happens in one sentence, plus the body position that makes it readable.",
         stays="Nothing — this is what changes between shots.",
         changes="Every shot.",
         inherit="Write it so the previous shot's ending pose flows into this shot's opening pose."),
    dict(key="screen_position", layer="Shot state", label="Screen position and facing", lines=1,
         records="Where the person sits in the frame and which way the body faces, e.g. 'centre-right, front-on, 3/4 to frame-left'.",
         stays="Frame side, for as long as the camera stays on one side of the line.",
         changes="Only if the camera crosses the line — which you should log.",
         inherit="Copy the frame side from the previous row unless you have crossed the line on purpose."),
    dict(key="gaze", layer="Shot state", label="Where they look", lines=1,
         records="The target of the eyes in frame terms: off-lens frame-right, down at the paper, at camera.",
         stays="Gaze direction within a beat.",
         changes="Per beat.",
         inherit="If the gaze has to continue across the cut, say so on both rows."),
    dict(key="props_hands", layer="Shot state", label="Props and hands", lines=2,
         records="Which hand holds what, and what the other hand does.",
         stays="The hand assignment, once chosen.",
         changes="State changes are logged as prop codes.",
         inherit="Name the hand every time. 'The mug' is not enough; 'the mug, right hand' is."),
    dict(key="prop_states", layer="Shot state", label="Prop states (codes)", lines=1,
         records="The active state of each tracked prop, e.g. P-01a upright and full.",
         stays="A state holds until a new code starts.",
         changes="Only by an authorised prop code, with a stated cause.",
         inherit="Carry the previous row's prop state forward unless a code changes it."),
    dict(key="set_dressing_delta", layer="Shot state", label="Set dressing changes", lines=1,
         records="Anything in the room that differs from the location sheet in this shot. Usually nothing.",
         stays="'None' is a good answer.",
         changes="Rarely — and always logged.",
         inherit="If it is not written here, it does not change."),
    dict(key="framing", layer="Shot state", label="Framing and camera", lines=2,
         records="Framing size, camera height, angle, lens feel and movement.",
         stays="The axis and the height band.",
         changes="Every shot — but the axis should hold.",
         inherit="Keep the camera on the same side of the line unless you log a reason."),
    dict(key="light_state", layer="Shot state", label="Light state (code)", lines=0,
         records="Which light state code is in force, e.g. L1.",
         stays="The code, until it changes on purpose.",
         changes="By a logged light code.",
         inherit="Never describe lighting twice; quote the code and the register does the rest."),
    dict(key="inherits_from", layer="Shot state", label="Inherits from the previous shot", lines=2,
         records="The state this shot receives unchanged: look, props, geography, light, gaze.",
         stays="It is literally the previous row's handoff line.",
         changes="Never edited after the fact — if it changed, it went in the wrong field.",
         inherit="Copy the previous shot's handoff line here before writing anything else."),
    dict(key="changes_in_shot", layer="Shot state", label="Changes in this shot", lines=2,
         records="Every intentional difference, each with its code. 'None' is the most common answer.",
         stays="Nothing.",
         changes="Here.",
         inherit="If you cannot give a change a code, it is drift waiting to happen."),
    dict(key="hands_off", layer="Shot state", label="Hands off to the next shot", lines=2,
         records="What the next shot must inherit exactly. This is the line the next row starts from.",
         stays="Nothing.",
         changes="Every shot.",
         inherit="Write it as an instruction to your future self, not a summary."),
    dict(key="hazards", layer="Shot state", label="Watch-outs", lines=1,
         records="The two or three things this shot is most likely to get wrong.",
         stays="Until fixed.",
         changes="Per shot.",
         inherit="These become the first lines of the preflight check."),
    dict(key="status", layer="Shot state", label="Row status", lines=0,
         records="One marker for the row: F, C, U or N/A. A row with any C is a C row.",
         stays="n/a",
         changes="As the shot resolves.",
         inherit="A C row must name its code. A U row must appear in the open-items list."),
]

PREFLIGHT = [
    ("Row check", "The shot number and slug match the row I am working from.",
     "Wrong row is the most common cause of a wrong shot."),
    ("Identity", "The five face anchors are pasted word for word, in the same order.",
     "Paraphrasing anchors is how faces drift."),
    ("Never-change list", "The three character items and three location items are in the prompt.",
     "Your personal tripwires."),
    ("Variant code", "The variant in force matches the previous shot, or the change has a code and a cause.",
     "An uncoded change is drift you have not noticed yet."),
    ("Wardrobe", "Same garment set, same fastening state, same sleeve length as the row says.",
     "Sleeves and buttons are the first thing to flip."),
    ("Hair", "Same part, same tuck, same length.",
     "Hair tuck changes read as a different person at wide framing."),
    ("Hands and props", "Correct hand, correct prop state code, other hand accounted for.",
     "Models love to swap hands."),
    ("Prop state", "Mug, paper, tools and carried items are in the state the row records.",
     "A prop that resets is a continuity break the audience feels."),
    ("Geography", "Two landmarks named with their frame side; nobody has been mirrored.",
     "Mirroring is invisible until the cut."),
    ("The line", "The camera is on the same side of the line as the previous shot.",
     "If it is not, the shot needs a written reason."),
    ("Light state", "The light code matches the register, including anything that is off.",
     "An unlit practical is continuity too."),
    ("Time band", "Same time band; nothing in frame records an impossible time.",
     "No clocks, no screens with times, no phone lock screens."),
    ("Framing", "Framing size, height, angle and movement match the row.",
     "Height drift is subtle and expensive."),
    ("Handoff", "I have read the handoff line aloud: this shot must hand off — to shot —.",
     "Saying it out loud catches what skimming misses."),
    ("Open items", "Any U mark in this row is decided, or its accepted risk is written down.",
     "Allowed to stay open. Not allowed to stay silent."),
]

# Columns of the wide spreadsheet tracker (CSV), grouped to match the three panels.
TRACKER_COLUMNS = [
    ("Group", "Shot number"),
    ("Group", "Shot slug"),
    ("Anchors", "Character ID"),
    ("Anchors", "Location ID"),
    ("Anchors", "Variant in force (character)"),
    ("Anchors", "Light state (location)"),
    ("Anchors", "Identity anchors to hold"),
    ("Action", "Action and pose"),
    ("Action", "Screen position and facing"),
    ("Action", "Where they look"),
    ("Action", "Props and hands"),
    ("Action", "Prop states (codes)"),
    ("Action", "Set dressing changes"),
    ("Camera", "Framing size"),
    ("Camera", "Camera height"),
    ("Camera", "Lens feel (optional)"),
    ("Camera", "Movement"),
    ("Handoff", "Inherits from previous shot"),
    ("Handoff", "Changes in this shot (code)"),
    ("Handoff", "Hands off to next shot"),
    ("Handoff", "Watch-outs"),
    ("Status", "Row status (F / C / U / N/A)"),
]


# --------------------------------------------------------------- teaching lines
# One weak handoff line and one strong one. Used by the PDF (Part 1) and the site,
# so the two editions cannot drift apart.
HANDOFF_WEAK = "same look as shot 3, a bit darker, she is tense"

HANDOFF_STRONG_LINES = [
    "CH-01, V1 cardigan buttoned to the third button, sleeves at the wrist",
    "L1 lamp lit red, corridor strip dark, door frame-right",
    "P-01a mug upright left of the script, headphones on, pencil out of shot",
    "camera south of the desk at (0.65, 0.45), medium close-up, she looks off-lens",
    "frame-right · hands off to shot 4: same frame, mug still full",
]

# Fill-in template a user can copy into their notes. Blanks are deliberate.
HANDOFF_SKELETON = (
    "CH-01 · V1 [the fastening state] · L1 [what is lit, what is off] · "
    "P-01a [prop state, frame side] · [hands: which one holds what] · "
    "[two landmarks with their frame side] · camera [side of the line] · "
    "[framing size] · [where they look] · hands off to shot [N]: [what must be identical]"
)
