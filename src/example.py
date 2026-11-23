"""Worked example — an original fictional sequence used to test the schema.

Film: "Night Signal" (fictional short). Scene 14 — "The Third Caller".
Everything here is invented for this product. It is a teaching example, not a
record of a real production or a real generation session.

The example is stored as data so that (a) the Markdown and PDF editions cannot
drift apart and (b) src/check_example.py can test the continuity itself.
"""

FILM = {
    "title": "Night Signal",
    "scene": "Scene 14 — “The Third Caller”",
    "logline": (
        "A late-night radio host takes a call from someone who describes the room she is "
        "sitting in. She keeps the show on air for eleven more seconds, then takes it off."
    ),
    "why_this_scene": (
        "It is one room, one on-screen character and one continuous time band, so every "
        "continuity decision is visible. It also contains the three kinds of change a real "
        "sequence usually needs: a wardrobe change, a prop state change (a spill) and a "
        "lighting change (going off air)."
    ),
    "sequence_time": "02:40–02:52, deep night, no windows in the room",
    "shot_count": 6,
}

# --- Character -------------------------------------------------------------

ANCHORS = [
    ("brow_scar", "Right eyebrow split by a small pale scar", "brow scar, right"),
    ("mole", "Dark mole 2 cm below the outer corner of the left eye", "mole, left cheek"),
    ("hair", "Chin-length bob, silver at both temples, tucked behind the right ear only",
     "silver temples, bob tucked right ear only"),
    ("brows", "Heavy straight eyebrows set close together", "heavy close-set brows"),
    ("posture", "Sits with her weight on her left forearm, never on both", "weight on left forearm"),
]

CHARACTER = {
    "char_id": "CH-01",
    "name_in_script": "RAE",
    "role_in_scene": "Night-shift host at a small AM station, eleven minutes from the end of her show.",
    "age_read": "Mid-40s",
    "build_posture": "Average height (1.7 m), broad-shouldered, unhurried. Seated for the whole scene; weight always on her left forearm.",
    "hair_fixed": "Chin-length bob, dark brown with silver at both temples. Tucked behind the right ear only; the left side falls forward across the cheekbone.",
    "skin_complexion": "Deep brown skin, warm undertone. A faint shine on the nose and forehead from the desk lamp — keep it; it is how the room's key light reads on her.",
    "eyes": "Dark brown. No glasses at any point in the scene.",
    "wardrobe_baseline": "V1 — charcoal grey fine-knit cardigan buttoned to the third button, cream crew-neck tee at the neckline, sleeves at the wrists. Olive canvas trousers (waist-up only in frame). Matte black broadcast headphones on both ears, coiled cable over her right shoulder.",
    "signature_item": "P-03 pencil, always in her LEFT hand. A thin silver band on her left ring finger, visible in the insert.",
    "never_change": [
        "The brow scar on her right eyebrow — it is the fastest way to check you have the right face.",
        "The bob tucked behind the right ear only; the left side always falls forward.",
        "The cardigan is charcoal, never black, never navy.",
    ],
    "voice_optional": "Low, close-mic'd, unhurried. Slight vocal fry at the end of sentences.",
}

CHARACTER_VARIANTS = [
    dict(
        variant_code="V1",
        what_changes="Baseline look: charcoal cardigan buttoned to the third button, cream tee at the neckline, sleeves at the wrists, headphones on both ears.",
        first_shot="1",
        motivation="Starting look of the scene.",
        glanceable_at="Wide and medium.",
        ends_at="Shot 4 (last shot in V1).",
        reversal="Never return to V1 inside scene 14.",
    ),
    dict(
        variant_code="V2",
        what_changes="Cardigan open, sleeves pushed to the elbows, cream tee fully visible. Headphones unchanged. The colour and the garment set do not change.",
        first_shot="5",
        motivation="The spill during the 30-second ellipsis: she pushed the wet right sleeve up and pulled the cardigan open.",
        glanceable_at="Medium and wide. Not readable in the insert.",
        ends_at="Carries forward into scene 15.",
        reversal="Do not return to V1 in this scene. V2 is the look from here on.",
    ),
]

CHARACTER["face_anchors"] = [label for _, label, _ in ANCHORS]

# --- Props -----------------------------------------------------------------

PROPS = [
    dict(
        prop_id="P-01", name="Mug",
        identity="Cream stoneware mug, 9 cm tall, handle on her right (east) side, a small chip on the lip at 10 o'clock. Always frame-left of her.",
        states=[
            ("P-01a", "Upright, full, thin steam rising. Handle east.", "Shots 1–4"),
            ("P-01b", "On its side on the blotter, handle toward frame-left, coffee pooled in a 20 cm dark ring, still wet.", "Shots 5–6"),
        ],
    ),
    dict(
        prop_id="P-02", name="Cue sheet",
        identity="A4 cue sheet on a brown clipboard, top clip visible, eight ruled lines of handwriting. Never legible in any framing — do not attempt readable words.",
        states=[("P-02", "Flat on the blotter, clip at the top.", "Shots 1–6")],
    ),
    dict(
        prop_id="P-03", name="Pencil",
        identity="Standard yellow pencil, sharpened, point down, in her LEFT hand in every shot.",
        states=[("P-03", "Held in the left hand, point resting on the paper.", "Shots 1–6")],
    ),
    dict(
        prop_id="P-04", name="Headphones",
        identity="Matte black broadcast headphones, one narrow silver band across the crown, coiled cable over her right shoulder. Worn on both ears in every shot of the scene.",
        states=[("P-04", "On both ears, cable over the right shoulder.", "Shots 1–6")],
    ),
    dict(
        prop_id="P-05", name="Desk blotter",
        identity="Dark green desk blotter, 60 × 40 cm, under the mug and the clipboard. One identifying detail: a pale scratch along the near edge.",
        states=[
            ("P-05", "Clean, no ring, scratch along the near edge.", "Shots 1–4"),
            ("P-05b", "Holds the 20 cm coffee ring from P-01b. Ring never touches the paper.", "Shots 5–6"),
        ],
    ),
]

# --- Location --------------------------------------------------------------

LANDMARKS = [
    ("Desk", "Free-standing oak desk, 1.6 × 0.7 m, long side east–west, centre of the room. Its near edge crosses the bottom third of every desk-axis frame."),
    ("Mixer", "Grey broadcast mixer on the desk's north edge, eight faders, two red-lit buttons at the right end."),
    ("Gooseneck lamp", "Brass lamp clamped at the desk's east end, head tilted down-west, warm pool across the clipboard."),
    ("Door", "East wall, 0.9 m wide, frosted half-glass with no lettering, painted the same dull green as the wall. Always frame-right."),
    ("ON AIR lamp", "Red box lamp above the door, inside the room. Always frame-right, always above the door."),
]

EXTRA_LANDMARKS = [
    ("Corkboard", "North wall, west end: eleven overlapping gig flyers, one corner curled. Reads small, top frame-left."),
    ("Clock ghost", "Pale unfaded rectangle on the north wall where a clock used to hang. No clock in the room, in any shot."),
    ("Ceiling stain", "Tea-coloured water stain in the second ceiling tile from the door. Only readable in the wide shots."),
]

LOCATION = {
    "loc_id": "LOC-01",
    "loc_name": "Studio B — KDLT 1140 AM",
    "story_function": "A room she controls, until the caller proves otherwise.",
    "room_read": "A converted insurance office: 4.2 m east–west by 3.2 m north–south, acoustic-tile ceiling at 2.5 m, one door, no windows.",
    "palette_materials": "Dull green-grey walls; off-white acoustic tiles; dark red-brown lino, scuffed; oak desk; grey mixer; brass lamp. Nothing in the room is blue except the corridor light.",
    "light_sources_fixed": "Gooseneck lamp (warm, 2700 K, key light on the desk and hands); two overhead fluorescents (cool, one tube dimmer at its end — do not animate the flicker in stills); corridor light under the door (cool, thin); ON AIR lamp glow on the wall above the door (red, soft).",
    "time_band": "02:40–02:52. Deep night. No windows, so no daylight is possible in any shot.",
    "sound_optional": "Low room tone, a hum from the mixer, the gooseneck lamp's faint buzz when lit.",
    "geography_rules": [
        "Every camera stays on the south side of the desk. Nothing crosses the line.",
        "The door and the ON AIR lamp are always frame-right. The mug is always frame-left.",
        "The clipboard always sits east of the mixer, under the lamp.",
    ],
    "never_change": [
        "Dull green-grey walls, and the door painted the same colour.",
        "Eleven flyers on the corkboard; one curled corner, front right.",
        "The clock ghost stays empty: no clock ever appears in this room.",
    ],
}

LIGHT_STATES = [
    dict(code="L1",
         description="ON AIR lamp lit red above the door, a soft red wash on the wall around it. The corridor strip under the door is dark.",
         shots="1–5",
         caused="The show is on air."),
    dict(code="L2",
         description="ON AIR lamp fully dark, no red wash anywhere on the door wall. A thin warm-amber corridor strip appears under the door.",
         shots="6",
         caused="She takes the show off air at the end of shot 6."),
]

CAMERA_POSITIONS = [
    ("1", "South-west corner, 0.7 m from both walls", "1.45 m", "North-north-east, across the room", "24 mm feel — optional"),
    ("2", "1.5 m south of the desk, slightly west of centre", "1.30 m", "North, at her chest", "40 mm feel — optional"),
    ("3", "Directly above the desk", "1.25 m", "Straight down", "35 mm feel — optional"),
    ("4", "South-east of her chair, over her left shoulder", "1.50 m", "North-east, past her shoulder to the door", "50 mm feel — optional"),
    ("5", "2 m south of her chair, slightly west of centre", "1.40 m", "North, at her face", "85 mm feel — optional"),
    ("6", "Same as shot 1", "1.45 m", "Same as shot 1", "24 mm feel — optional"),
]

# --- Six shots -------------------------------------------------------------

SHOTS = [
    dict(
        shot_no="1", slug="ROOM, FIRST LIGHT", duration="6 s",
        variant="V1", light="L1", status="F",
        anchors_hold="silhouette, hair tuck and cardigan only — the face is too small in a wide to judge",
        action_pose=(
            "Rae is mid-sentence at the mic, sitting upright with her weight on her left forearm. "
            "Her left hand holds the pencil on the cue sheet; her right hand rests around the mug. "
            "Nothing else in the room moves."
        ),
        screen_position="Centre-right, on the far side of the desk, front-on and 3/4 to frame-left. The desk's near edge crosses the bottom third.",
        gaze="Down at the cue sheet, then a small lift to the mic at frame-centre.",
        props_hands="Right hand around the mug (P-01a). Left hand holding the pencil (P-03), point down on the clipboard (P-02).",
        prop_states="P-01a · P-02 · P-03 · P-04 · P-05 (blotter clean)",
        set_dressing_delta="None. This shot establishes the room read.",
        framing_size="Wide — whole room, her seated",
        camera_height="1.45 m",
        lens_feel="24 mm feel",
        movement="Static",
        framing="Wide, 24 mm feel, 1.45 m, static. Door and red lamp in the right quarter; corkboard small at top frame-left; ceiling stain visible.",
        light_state="L1",
        inherits_from="— (first shot of the sequence; this row is what the other five answer to)",
        changes_in_shot="Establishes V1, P-01a and L1. Nothing changes inside the shot.",
        hands_off="Room geography (door and lamp frame-right, mug frame-left), V1 wardrobe, headphones on both ears with the cable over her right shoulder, paper illegible.",
        hazards="Do not mirror the room: door stays frame-right. Keep the paper illegible.",
        camera_xy=(0.65, 0.45),
    ),
    dict(
        shot_no="2", slug="CUE SHEET, PENCIL DOWN", duration="5 s",
        variant="V1", light="L1", status="F",
        anchors_hold="all five anchors",
        action_pose=(
            "Still talking, she leans 15 cm further in and tips her head down to underline one line "
            "of the cue sheet with the pencil."
        ),
        screen_position="Centre, chest-up, 3/4 to frame-left. The mug sits at the bottom frame-left and stays in shot.",
        gaze="Down and slightly right, at the clipboard.",
        props_hands="Left hand: pencil (P-03), point down on the paper. Right hand: off the mug, flat on the blotter beside it.",
        prop_states="P-01a · P-02 · P-03 · P-04 · P-05 (blotter clean)",
        set_dressing_delta="None.",
        framing_size="Medium — waist-up",
        camera_height="1.30 m",
        lens_feel="40 mm feel",
        movement="Slow 5% push",
        framing="Medium, waist-up, 40 mm feel, 1.30 m, slow 5% push.",
        light_state="L1",
        inherits_from="Everything from shot 1: V1 wardrobe, L1 light, mug upright at frame-left, door frame-right, headphones on, paper illegible.",
        changes_in_shot="None. The pencil was already in her left hand in shot 1 — if it appears for the first time here, that is an uncoded change.",
        hands_off="Pencil still in the left hand, mug still upright at frame-left, sleeves still at the wrists, door still frame-right.",
        hazards="The pencil must not switch hands. Keep the mug in frame — it is the prop that shot 5 changes.",
        camera_xy=(1.55, 0.75),
    ),
    dict(
        shot_no="3", slug="INSERT, CUE SHEET AND MUG", duration="4 s",
        variant="V1", light="L1", status="F",
        anchors_hold="N/A for the face — hands only. Hold the silver ring on her left hand and the pencil in the same hand.",
        action_pose=(
            "Only her hands are in frame. The pencil drags a short underline; her right hand lifts the "
            "mug three centimetres off the blotter and sets it back down in the same place."
        ),
        screen_position="Straight down over the desk. The clipboard fills the right two-thirds; the mug enters at the left edge.",
        gaze="N/A — no face in frame.",
        props_hands="Left hand: pencil, point down, mid-stroke. Right hand: around the mug handle, thumb up.",
        prop_states="P-01a (lifted, still upright, still full) · P-02 · P-03 · P-04 · P-05 (blotter clean)",
        set_dressing_delta="None.",
        framing_size="Overhead insert — hands and desk",
        camera_height="1.25 m",
        lens_feel="35 mm feel",
        movement="Static",
        framing="Overhead insert, 35 mm feel, 1.25 m directly above the desk, static. The gooseneck lamp rakes in from frame-right.",
        light_state="L1 (plus the fixed gooseneck key from frame-right)",
        inherits_from="From shot 2: pencil in the left hand, mug upright at frame-left, green blotter, lamp pool from frame-right.",
        changes_in_shot="None. The camera axis changes; the state does not.",
        hands_off="The mug goes back down where it was lifted. The blotter is still clean. The pencil is still in the left hand.",
        hazards="No coffee ring on the blotter in this shot — the ring is a later prop state. The paper stays illegible.",
        camera_xy=(2.0, 1.75),
    ),
    dict(
        shot_no="4", slug="OVER HER SHOULDER TO THE DOOR", duration="5 s",
        variant="V1", light="L1", status="F",
        anchors_hold="back of the head only: bob tuck, silver temples. The face is turned away — do not invent a face here.",
        action_pose=(
            "She stops talking. Her head turns 20° toward the door; her right hand drops off the desk "
            "and hangs out of frame. Her left shoulder and the back of her head hold frame-left."
        ),
        screen_position="Over her left shoulder. She occupies frame-left; the door and the red lamp occupy centre-right.",
        gaze="Off-lens, toward the door at frame-right.",
        props_hands="Left hand still on the clipboard with the pencil. Right hand empty, off the desk.",
        prop_states="P-01a (upright and full, out of frame behind her shoulder) · P-02 · P-03 · P-04 · P-05 (clean)",
        set_dressing_delta="None.",
        framing_size="Over-the-shoulder medium",
        camera_height="1.50 m",
        lens_feel="50 mm feel",
        movement="Static",
        framing="Over-the-shoulder medium, 50 mm feel, 1.50 m, static. Door frame-right; corridor strip under the door dark.",
        light_state="L1",
        inherits_from="From shot 3: mug upright and full on the blotter, pencil in the left hand, V1 with sleeves at the wrists, L1 light.",
        changes_in_shot="None in state. This is the last shot in V1 — the change happens in the ellipsis after it.",
        hands_off="Hand-off to shot 5, 30 seconds later off-screen: mug tipped (P-01b) with the coffee ring on the blotter, cardigan open with sleeves pushed to the elbow (V2). The lamp is still L1.",
        hazards="Her head must not cover the ON AIR lamp. Nothing may be visible through the frosted glass.",
        camera_xy=(2.5, 0.9),
    ),
    dict(
        shot_no="5", slug="THE CALLER, CLOSE", duration="8 s",
        variant="V2", light="L1", status="C",
        anchors_hold="all five anchors",
        action_pose=(
            "She listens, still. Chin lifted a centimetre, shoulders squared. Her right hand rests flat "
            "on the desk beside the tipped mug; she does not touch it."
        ),
        screen_position="Centre, chest-up, front-on and slightly 3/4 to frame-left. The tipped mug and the coffee ring sit at the bottom frame-left.",
        gaze="Off-lens to frame-right, holding on the door. Never at camera.",
        props_hands="Right hand: empty and flat on the desk near the mug. Left hand: out of frame below the desk edge, still holding the pencil.",
        prop_states="P-01b (mug on its side, handle frame-left, 20 cm dark ring, still wet) · P-02 · P-03 · P-04 · P-05b",
        set_dressing_delta="None. The spill is a prop state, not a set change.",
        framing_size="Medium close-up — chest-up",
        camera_height="1.40 m",
        lens_feel="85 mm feel",
        movement="Static",
        framing="Medium close-up, 85 mm feel, 1.40 m, static. Her eyeline runs out of frame-right.",
        light_state="L1 (unchanged)",
        inherits_from="From shot 4: room read, L1 lamp still lit, headphones on both ears, door frame-right, V1 up to the ellipsis.",
        changes_in_shot="C — V2 (cardigan open, sleeves to the elbow). C — P-01b (mug tipped, coffee ring on the blotter). Both caused by the spill during the 30-second ellipsis, both logged before generating.",
        hands_off="V2 stays to the end of the scene. P-01b stays. The lamp is still L1. Her gaze keeps holding toward frame-right.",
        hazards="The mug must not stand up again. The ring stays on the blotter, never on the paper. Do not add a visible stain to the cardigan at this framing.",
        camera_xy=(1.95, 0.6),
    ),
    dict(
        shot_no="6", slug="OFF AIR", duration="7 s",
        variant="V2", light="L2", status="C",
        anchors_hold="silhouette, hair tuck and cardigan — same as shot 1, in the same framing",
        action_pose=(
            "She leans back 10 cm, presses the left of the mixer's two red buttons with her right hand, "
            "and looks at the door. She does not look at camera."
        ),
        screen_position="Wide, same framing as shot 1: centre-right, front-on and 3/4 to frame-left, desk's near edge across the bottom third.",
        gaze="Off-lens to frame-right, on the door.",
        props_hands="Right hand: index finger on the mixer button. Left hand: pencil still in it, resting on the clipboard.",
        prop_states="P-01b · P-02 · P-03 · P-04 · P-05b",
        set_dressing_delta="None.",
        framing_size="Wide — whole room, her seated",
        camera_height="1.45 m",
        lens_feel="24 mm feel",
        movement="Static",
        framing="Wide, 24 mm feel, 1.45 m, static — identical to shot 1. Door and lamp in the right quarter.",
        light_state="L2",
        inherits_from="From shot 5: V2 wardrobe, P-01b tipped mug with the ring, lamp still lit, headphones on, door frame-right.",
        changes_in_shot="C — L2. She takes the show off air: the lamp above the door goes dark and the corridor strip lights under the door.",
        hands_off="End of sequence. Scene 15 inherits V2 wardrobe and the P-01b prop state; the lamp stays dark until she is back on air.",
        hazards="No red glow left on the wall above the door. The framing must match shot 1 exactly — this is the bookend test.",
        camera_xy=(0.65, 0.45),
    ),
]

OPEN_ITEMS = [
    dict(
        mark="U", where="Shot 6 — mixer buttons",
        issue="Which of the mixer's two red buttons takes her off air is undecided.",
        decision="She presses the left one. If a generation produces a different layout, accept it provided two red buttons remain and her finger lands on one of them.",
        risk="Low: the button is 12 px across in a wide shot.",
    ),
    dict(
        mark="U", where="Shots 4 and 6 — corridor beyond the door",
        issue="The colour of the corridor light is unresolved.",
        decision="Never resolve it. The frosted glass stays opaque and the strip under the door stays a thin warm-amber line.",
        risk="Accepted: nothing may ever be legible through the door.",
    ),
]

DRIFT_LOG = [
    dict(shot="5", attempt="1", what="Cardigan stayed buttoned and the mug stood upright. The coffee ring did appear on the blotter.",
         verdict="Broke V2 and P-01b", action="Re-ran with the V2 and P-01b lines only, anchors untouched. Attempt 2 used."),
    dict(shot="4", attempt="2", what="Door appeared frame-left, so the room mirrored.",
         verdict="Geography break", action="Re-ran with the geography rule as the first line of the prompt. Attempt 1 was the keeper."),
    dict(shot="2", attempt="1", what="Pencil moved to the right hand.",
         verdict="Hand rule broken", action="Re-ran with “left hand” placed before the action sentence, where it is read first."),
]

FILLED_PREFLIGHT = {
    "Row check": "Yes — row 5, “THE CALLER, CLOSE”.",
    "Identity": "All five anchors pasted, same order.",
    "Never-change list": "Three character items and three location items all in.",
    "Variant code": "V2 with a cause (the spill in the ellipsis). P-01b logged at the same time.",
    "Wardrobe": "Cardigan open, sleeves to the elbow. Colour unchanged.",
    "Hair": "Bob, right ear only.",
    "Hands and props": "Right hand empty on the desk; pencil stays in the left hand, out of frame.",
    "Prop state": "Mug on its side, handle frame-left, ring 20 cm, still wet.",
    "Geography": "Door frame-right; mixer north; mug frame-left. No mirroring.",
    "The line": "Same south-of-the-desk camera as shots 1–4.",
    "Light state": "L1 — lamp still lit. It only goes dark in shot 6.",
    "Time band": "02:40–02:52. No clock in the room.",
    "Framing": "MCU, 85 mm feel, 1.40 m, static.",
    "Handoff": "Read aloud: hands off V2 and P-01b to shot 6.",
    "Open items": "Two U items accepted and written down: mixer button, corridor colour.",
}
