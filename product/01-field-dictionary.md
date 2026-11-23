<!--
  Field dictionary — The Continuity Bible v1.0
  Editable Markdown. Lines of underscores (________) are writing space: type over them.
  Part 2 of 7. Full contents: product/README-first.md
  You may edit, rename and reprint this file for your own productions.
-->

# Field dictionary

*What every field records, what stays fixed, what may change, and how each shot inherits*

**The Continuity Bible** · v1.0 · November 2026
Part 2 of 7 · Reference. You do not need to read it before you start; keep it open while you fill in your first scene.

---

Every field below is one of three things: a piece of identity you protect, a variant you allow, or the state of a single shot. The layer is written next to each field. When in doubt about a field, check its layer first.

The tables answer four questions for each field: what you write in it, what has to stay the same, what is allowed to change, and how the next shot receives it. Read one row at a time; the whole point is that no single field needs a paragraph of explanation on the sheet itself.

## The four status markers

Markers are letters, not colours. Every marker below is written as a letter in the sheets, in the tables and on the printed page, so the information survives a black-and-white print, a photo of a page, and colour-blind eyes.

| Code | Name | What it means | When you use it |
|---|---|---|---|
| F | Fixed | Locked for the whole sequence. Copy it into every shot word for word. | The field is part of identity, or a variant is in force and this field is not changing. |
| C | Changed intentionally | This shot deliberately differs from the one before it. The change has a code. | Wardrobe, condition, props, light or dressing shift on purpose. Never write C without the code. |
| U | Unresolved | You have not decided yet. It is allowed to stay open, but not silently. | A choice is deferred. Write what you will accept if the generation makes its own choice. |
| N/A | Not applicable | The field does not apply to this shot. Say why in three words. | No face in an insert, no prop in frame, no second character in the scene. |

One row-level rule keeps the markers honest: **the row's status is its strongest marker** — C if anything in the row changed, otherwise U if anything is unresolved, otherwise F. Any U that sits inside a C row is also written into the open-items box, so nothing unresolved can hide inside a row that looks finished.

# Character sheet

One sheet per on-screen character. It is deliberately short: five face anchors, three never-change items, and one baseline look. A second page of description makes the sheet harder to use, not more accurate.

| Field | What it records | What stays fixed | What may change | How it is inherited |
|---|---|---|---|---|
| Character ID | A short code you will repeat in every table row, e.g. CH-01. | The code itself, for the whole sequence. | Never. A new code means a different character. | Copy the code into the shot table, never the character's name. |
| Name in the script | The name used in your notes and prompts. One spelling only. | Spelling and capitalisation. | Only if the script is rewritten. | Use this exact spelling in every prompt. |
| Role in the scene (one line) | Who this person is and what they want in this scene, in one sentence. | The sentence, for the whole scene. | Per scene, not per shot. | Read it before every generation; it keeps behaviour in range. |
| Age read | How old the person reads on screen, not their birth year. e.g. 'mid-40s'. | The band. Do not let it float between shots. | Only for a deliberate time jump, logged as a variant. | Quote the same words in every prompt. |
| Build and posture | Height read, build, and the one posture habit that makes them them. | The silhouette. This is the first thing that drifts when you only describe a face. | Only if they sit, stand or undress as part of the action (log it). | Repeat the posture habit in shots where they are seated. |
| Five face anchors | Five features, in plain words, that a stranger could check at a glance. Not a portrait description. | All five, in every shot where the face is visible. | Nothing. If one anchor changes, it is a different character. | Copy all five, word for word, into every prompt. Do not summarise or re-order them. |
| Hair (fixed styling) | Length, colour read, part, and exactly how it is worn: tucked where, falling where. | Part, tuck, length and colour. | Only as a logged variant (e.g. hair wet, hat on). | Say where it is tucked, not just 'short hair'. |
| Skin and complexion | Tone read, undertone, and any marks you want kept (freckles, shine, a mole). | Tone and the marks you name. | Condition can change by variant (sweat, dirt, blood) — log it. | Keep the same words; avoid inventing new descriptors. |
| Eyes | Eye colour read, and whether they wear glasses or not. 'No glasses' is information. | Colour and the glasses decision. | Only as a logged variant. | Write 'no glasses' when there are no glasses, so they do not appear. |
| Baseline wardrobe (V1) | The default garment set, fit, colours, and the fastening state. This is your V1. | Garment set and colour while V1 is in force. | A new variant code takes over; V1 is never edited afterwards. | Copy the V1 line verbatim until a later code replaces it. |
| Signature item (optional) | One carried or worn object worth tracking through the sequence (mug, badge, ring). | Presence, side and state until a prop state changes. | Prop states get their own codes (P-01a, P-01b). | Name the hand that holds it. |
| Never-change list (three items) | If you only hold three things, hold these. Your personal drift tripwires. | All three. | Nothing. | This is the list you read out loud before pressing generate. |
| Voice quality (optional) | Pace, pitch and texture, for anyone working with generated audio. | The description. | Per scene. | Optional: skip it if your workflow is silent. |

### The five-anchor rule

Five is a limit, not a minimum. Anchors must be checkable by a stranger in one glance at the framing you will actually generate: a scar, a mole, a hair tuck, an eyebrow shape, a seated habit. Colour alone is a weak anchor; structure is a strong one. If you cannot check it at the shot's widest framing, it belongs in “Watch-outs”, not in the anchors.

## Character variant register

Every deliberate change to a character gets a code, a cause and an end. Codes are never reused and never edited after a shot has been generated with them: if the look needs to change again, that is V3.

| Code | What changes (structural, glanceable) | From shot | Caused by | Readable at | Ends at | Reversal rule |
|---|---|---|---|---|---|---|
| V1 | Charcoal cardigan buttoned to the third button, sleeves at the wrists. | 1 | Starting look. | Wide and medium. | 4 | Never return to V1. |
| V2 | Cardigan open, sleeves pushed to the elbows. | 5 | The spill during the ellipsis. She pushed a wet sleeve up. | Medium and wide. | next scene | Do not return to V1. |

*Two example rows, from the worked example. A real register usually has one row.*

**Readable at** is the field that keeps variants honest. A change nobody can see at the framing you are generating is not a variant, it is a hope. Write the framing where the change actually reads, and do not rely on it in shots tighter than that.

# Location sheet

One sheet per location. It does the job the character sheet does, for the space: five fixed landmarks, three never-change items, a floor plan, and the geography rules that stop a room from mirroring between shots.

| Field | What it records | What stays fixed | What may change | How it is inherited |
|---|---|---|---|---|
| Location ID | Short code repeated in every table row, e.g. LOC-01. | The code. | Never. | Copy the code, not the place name. |
| Location name | The name used in the script and in prompts. One spelling. | Spelling. | Never within a sequence. | Use the same words every time. |
| Story function (one line) | What this room is for in the scene: pressure, comfort, exposure. | For the whole sequence. | Per scene. | It guides light and framing choices, not facts. |
| Room read | Shape, approximate size, ceiling height, and how many ways in or out. | Everything here. This is the room's skeleton. | Never within a sequence. | Repeat it in wide shots; it is the cheapest way to keep a room recognisable. |
| Fixed landmarks (up to five) | Five objects or features that never move, each with its frame position and one identifying detail. | Position, count and identifying detail. | Nothing. If a landmark moves, the room has changed — log it as a location variant. | Name at least two landmarks per shot with their frame side. |
| Palette and materials | The three to five surface colours and textures that make the room read as one room. | Colour relationships, not exact hex values. | Only with a logged lighting variant. | Quote the same colour words; do not invent new ones. |
| Light sources that exist in the room | Every practical light and where it comes from. This is the physics of the room, not the look. | Which sources exist and their direction. | Whether each source is on, off or dimmed — that is a light state code. | State the light state code, not a mood word. |
| Time band | The clock window the sequence sits inside, e.g. 02:40–02:52, deep night, no daylight possible. | The whole sequence. | Only across a scene break. | Repeat it every shot: it rules out windows, sun, and street light. |
| Sound bed (optional) | Room tone and the recurring sounds, for anyone cutting real audio later. | Room tone description. | Events can enter and leave. | Optional: skip if you are not working with generated audio. |
| Geography rules | Two or three hard rules that keep the room readable: what is always frame-left, always frame-right, which side the camera stays on. | The rules. They are the point of the sheet. | Never within a sequence. | Check them as rules, not as descriptions. They catch mirroring. |
| Never-change list (three items) | The three details that prove it is the same room. | All three. | Nothing. | Read out loud with the character's list before generating. |

### The geography rules are the point

Most “these shots don't cut together” problems come from a mirrored frame, not a wrong wall colour. Two or three hard rules written as rules — “the door is always frame-right”, “every camera stays south of the desk” — are checkable in one glance, where a paragraph of description is not.

## Location variant register

| Code | What changes | From shot | Caused by | Readable at | Reversal rule |
|---|---|---|---|---|---|
| V-A | Rain on the skylight; the room reads darker and blue. | 1 | Weather change in the scene. | Wide only. | Never reversed in this scene. |

*An example of a location variant. The worked example has none — the room never changes, and that is a legitimate, and common, register.*

Most lighting changes are better recorded as light state codes (L1, L2) than as location variants. A light state says what is switched on, which is what you can actually control; a location variant is for a physical change to the room.

## Light and time register

Light changes are the ones most often left in someone's head, and they are the easiest to record: a code, a description of what is lit and what is off, and the shots the code covers.

| Code | What is lit, what is off | Shots | Caused by |
|---|---|---|---|
| L1 | ON AIR lamp lit red; corridor strip under the door dark. | 1–5 | The show is on air. |
| L2 | ON AIR lamp fully dark, no red wash; a thin warm corridor strip appears under the door. | 6 | She takes the show off air. |

> **Tip — Say what is off**  
> The strongest light information in a shot is usually what has been switched off. “No red wash on the door wall” is a checkable instruction; “moody lighting” is not.

# Six-shot state table

This is the heart of the system: one row per shot, three panels. The panels exist because a single table wide enough to hold every field cannot be printed, read or filled in by hand. Panel A holds what must not move. Panel B is the inheritance ledger. Panel C is the state of the shot itself.

| Panel | What it holds | The question it answers |
|---|---|---|
| A — Anchors and variants | Character, location, the variant in force, the light state, the anchors to hold. | What must not move in this shot? |
| B — Inheritance ledger | Inherits from, changes in this shot, hands off to the next. | What came in, what changed, what must go out? |
| C — Shot state | Action and pose, screen position, gaze, props and hands, framing, watch-outs. | What exactly am I generating? |

| Field | What it records | What stays fixed | What may change | How it is inherited |
|---|---|---|---|---|
| Shot | The shot number and a slug you will recognise, e.g. '3 — INSERT, CUE SHEET'. | The number. Never renumber mid-sequence. | n/a | Rows are read in order; the row above is always the shot before. |
| Action and pose | What happens in one sentence, plus the body position that makes it readable. | Nothing — this is what changes between shots. | Every shot. | Write it so the previous shot's ending pose flows into this shot's opening pose. |
| Screen position and facing | Where the person sits in the frame and which way the body faces, e.g. 'centre-right, front-on, 3/4 to frame-left'. | Frame side, for as long as the camera stays on one side of the line. | Only if the camera crosses the line — which you should log. | Copy the frame side from the previous row unless you have crossed the line on purpose. |
| Where they look | The target of the eyes in frame terms: off-lens frame-right, down at the paper, at camera. | Gaze direction within a beat. | Per beat. | If the gaze has to continue across the cut, say so on both rows. |
| Props and hands | Which hand holds what, and what the other hand does. | The hand assignment, once chosen. | State changes are logged as prop codes. | Name the hand every time. 'The mug' is not enough; 'the mug, right hand' is. |
| Prop states (codes) | The active state of each tracked prop, e.g. P-01a upright and full. | A state holds until a new code starts. | Only by an authorised prop code, with a stated cause. | Carry the previous row's prop state forward unless a code changes it. |
| Set dressing changes | Anything in the room that differs from the location sheet in this shot. Usually nothing. | 'None' is a good answer. | Rarely — and always logged. | If it is not written here, it does not change. |
| Framing and camera | Framing size, camera height, angle, lens feel and movement. | The axis and the height band. | Every shot — but the axis should hold. | Keep the camera on the same side of the line unless you log a reason. |
| Light state (code) | Which light state code is in force, e.g. L1. | The code, until it changes on purpose. | By a logged light code. | Never describe lighting twice; quote the code and the register does the rest. |
| Inherits from the previous shot | The state this shot receives unchanged: look, props, geography, light, gaze. | It is literally the previous row's handoff line. | Never edited after the fact — if it changed, it went in the wrong field. | Copy the previous shot's handoff line here before writing anything else. |
| Changes in this shot | Every intentional difference, each with its code. 'None' is the most common answer. | Nothing. | Here. | If you cannot give a change a code, it is drift waiting to happen. |
| Hands off to the next shot | What the next shot must inherit exactly. This is the line the next row starts from. | Nothing. | Every shot. | Write it as an instruction to your future self, not a summary. |
| Watch-outs | The two or three things this shot is most likely to get wrong. | Until fixed. | Per shot. | These become the first lines of the preflight check. |
| Row status | One marker for the row: F, C, U or N/A. A row with any C is a C row. | n/a | As the shot resolves. | A C row must name its code. A U row must appear in the open-items list. |

## Preflight: fifteen checks, one minute

The checklist is not part of the record; it is the thing you read with your hand on the button. Each check names the failure it prevents, because a check whose purpose you cannot remember gets skipped.

| # | Check | What it prevents |
|---|---|---|
| 1 | Row check | Wrong row is the most common cause of a wrong shot. |
| 2 | Identity | Paraphrasing anchors is how faces drift. |
| 3 | Never-change list | Your personal tripwires. |
| 4 | Variant code | An uncoded change is drift you have not noticed yet. |
| 5 | Wardrobe | Sleeves and buttons are the first thing to flip. |
| 6 | Hair | Hair tuck changes read as a different person at wide framing. |
| 7 | Hands and props | Models love to swap hands. |
| 8 | Prop state | A prop that resets is a continuity break the audience feels. |
| 9 | Geography | Mirroring is invisible until the cut. |
| 10 | The line | If it is not, the shot needs a written reason. |
| 11 | Light state | An unlit practical is continuity too. |
| 12 | Time band | No clocks, no screens with times, no phone lock screens. |
| 13 | Framing | Height drift is subtle and expensive. |
| 14 | Handoff | Saying it out loud catches what skimming misses. |
| 15 | Open items | Allowed to stay open. Not allowed to stay silent. |

After generating, three short fields go in the drift log: what came out, the verdict, and the action you took. Two lines per rejected attempt is enough, and it is the only record that teaches you your own failure patterns.

# What changed while testing this against a full sequence

The schema was drafted, used to plan an original six-shot scene, and then revised where a field proved ambiguous, redundant or too slow to fill in. These are the changes that survived, and the reasons — they are the most useful part of this document if you plan to adapt the sheets to your own workflow.

### Cut

- **Mood and emotion.** Not checkable at a glance, and it duplicated “action and pose”. Emotion that matters is a body position.
- **Lighting mood words.** “Warm, lonely, cold” drifts between shots and cannot be verified. Replaced by light state codes plus the fixed list of sources that physically exist in the room.
- **A prompt box.** It would have made this a prompt pack tied to one model, and it goes stale faster than the decisions do. The anchor lines and change codes are what feed a prompt; where they go is your workflow's business.
- **Exact colour values.** Nobody checks a hex code in a generated frame. Replaced by three colour words plus a negative: “charcoal, never black, never navy”.
- **A risk score per row.** Subjective, unused, and it made finished rows look unfinished.
- **A separate “screen direction” field.** Merged into framing and movement, because for a locked-off six-shot scene it was a field that almost always read “none”.

### Merged

- **Character condition and wardrobe.** Combined into the variant register, because a torn sleeve and a rolled sleeve are the same kind of change and deserve the same code.
- **Camera position, height and lens feel.** Kept in the shot state but pulled together on one printed line, so the whole camera decision is readable in one movement of the eye.
- **“What the next shot needs” and “what carries forward”.** These were two fields saying the same thing. Now there is one handoff line, and the next row starts by copying it.

### Added after the sequence was filled in

- **Watch-outs, one line per shot.** There was no obvious place to write “the mug must not stand up again”, and without it that instruction lived in someone's head. It is now the field that stops the most expensive mistakes.
- **Readable at, in the variant register.** A variant that cannot be seen at the framing you are generating is not worth a code, and the register now makes you say which framing proves it.
- **Reversal rule.** Changes tend to leak backwards into earlier shots when you re-generate. One line — “never return to V1 in this scene” — closes that hole.
- **The open-items box.** U marks were being written and then forgotten. Anything marked U now also has to appear in one list, with the risk you are accepting.
- **Three panels instead of one table.** A single table with every field was 29 columns: unprintable, unreadable, and impossible to fill in by hand. Splitting it into three panels of six rows is the change that made the system usable on paper.

> **Note — How this was tested**  
> The schema was applied to the original six-shot scene in part 7 and checked mechanically: every change carries a code that exists, every code has a start shot and no gaps, every shot inherits from the one before, and the bookend frames match. That is a design test against a worked example, not a test with other filmmakers — see the validation notes for what is still unproven.

## The five rules the schema encodes

1. **Identity is copied, not re-described.** The same words, in the same order, in every shot. Paraphrase is drift.
2. **A change needs a code, a cause and an end.** No code, no change: that is drift you have not noticed yet.
3. **Every shot starts with the previous shot's handoff line.** Inheritance is explicit or it does not exist.
4. **Record what is off.** Dark lamps, empty hands, missing props and absent characters are continuity too.
5. **When the document and the frame disagree, the document changes.** Otherwise the system quietly stops describing the film.
