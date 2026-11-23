<!--
  Start here — The Continuity Bible v1.0
  Editable Markdown. Lines of underscores (________) are writing space: type over them.
  Part 1 of 7. Full contents: product/README-first.md
  You may edit, rename and reprint this file for your own productions.
-->

# Start here

*The twenty-minute workflow, and how a shot inherits from the shot before it*

**The Continuity Bible** · v1.0 · November 2026
Part 1 of 7 · Editable source file. Everything here is designed to be printed, written on, and edited.

---

Six generated shots can look like six different films. The usual cause is not the model. It is that nobody wrote down what has to survive the cut.

This system is that piece of paper. It has three layers — identity, variant, shot state — and one line between every pair of shots that says what the next shot must inherit. Fill it in once, before you generate anything, and you have a handoff you can follow shot by shot.

It is built for a scene of about six shots, which is the size where drift starts to be expensive and small enough to hold in your head. It works the same way for any generation workflow: text-to-video, image-to-video, a still frame you animate, or a shot you build from a reference image.

## What is in the box

| File | What it is for | When you use it |
|---|---|---|
| 02 Character sheet | One page per on-screen character: the features that must not change, plus the wardrobe variants. | Once per character, before the first shot. |
| 03 Location sheet | One page per location: the room's fixed landmarks, a floor plan, the light sources and the geography rules. | Once per location, before the first shot. |
| 04 Six-shot state table | The three panels that carry a shot from the previous one: anchors, inheritance ledger, shot state. | While planning, then in front of you while generating. |
| 05 Preflight checklist | Fifteen checks to run in the minute before you press generate, plus a drift log. | Every shot. Print six copies. |
| 01 Field dictionary | What each field records, what stays fixed, what may change, and how changes are coded. | When a field is unclear. Keep it nearby for the first scene. |
| 06 Worked example | A complete six-shot scene, filled in, with its changes traced end to end. | Read it once before you fill in your own. |

# The three layers

Every field in this system belongs to exactly one layer. If you can tell which layer you are writing in, you already know whether the thing you are describing is allowed to change.

| Layer | What it holds | How long it lasts | How you write it |
|---|---|---|---|
| Identity | What makes the person or room recognisable: face anchors, hair, build, fixed landmarks, wall colours, the time band. | The whole sequence. Longer, if it is the same character or room in the next scene. | Plain descriptive words, copied word for word into every shot. Never re-written from shot to shot. |
| Variant | An intentional change with a code: V1, V2 for characters, L1, L2 for light, P-01a, P-01b for prop states. | From the shot it starts in until the shot it ends in. It is a block, not a mood. | A short list of structural differences someone could see at a glance, plus what caused it. |
| Shot state | The exact state of one shot: action, pose, frame side, gaze, props and hands, framing, light code, and the handoff line. | One shot. | Short, factual, written so you can check it in thirty seconds while a generation runs. |

> **Rule — The one-line version**  
> Identity is what you protect. A variant is what you allow. Shot state is what you check.

Two smaller rules do most of the work, and both are about writing, not about generation:

1. **Copy, do not paraphrase.** The five face anchors and the never-change list go into every prompt in the same words, in the same order. Re-describing your character from memory each time is the single most common way a face drifts.
2. **Code every change.** If a shot differs from the one before it and you cannot point to a code that authorises the difference, it is not a change. It is drift you have not noticed yet.

There is a third rule about order, and it saves the most time: **generate the anchor shot first**. That is the shot that holds the most information — usually the wide, because it proves the room, the light and the wardrobe at once. Keep the frame that worked. Every later shot is checked against it, not against your memory.

# The twenty-minute workflow

Do this once per scene, before you generate anything. It is faster than repairing four broken shots later.

**Step 1 — Write six beats, one line each (5 minutes)** — _Not prompts. Beats: what happens, in order. If a beat needs two actions, it is two shots._  
Answer: ..............................................................
Answer: ..............................................................

**Step 2 — Cast and place (5 minutes)** — _Fill the character sheet and the location sheet. Five face anchors, five fixed landmarks, three never-change items each. Stop at five; more than five is a description, not a checklist._  
Answer: ..............................................................
Answer: ..............................................................

**Step 3 — Set the baseline and predict the change (2 minutes)** — _Write V1: the look in shot 1. Then write down the one change you expect the scene to need, even roughly. Naming it early is what stops it turning into three accidental changes._  
Answer: ..............................................................
Answer: ..............................................................

**Step 4 — Fill the table left to right (5 minutes)** — _One row per shot. Start row 1, then for every row after it copy the previous row's handoff line into “Inherits from”, and only then write what is different._  
Answer: ..............................................................
Answer: ..............................................................

**Step 5 — Draw the floor plan (2 minutes)** — _Sketch the room and mark where you plan to put the camera for each shot. If two cameras sit on opposite sides of your character, you have crossed the line and one of the shots will feel flipped._  
Answer: ..............................................................
Answer: ..............................................................

**Step 6 — Freeze and generate (start here)** — _Generate the anchor shot. Check it against the preflight list. Log what came out._  
Answer: ..............................................................

# Carrying continuity from one shot to the next

A shot inherits from a shot, not from a mood. Everything in this section is one loop, run six times.

## The loop

1. **Inherit.** Copy the previous row's handoff line into this row's “Inherits from” field. Do not rewrite it. If it is wrong, the previous shot was wrong, and that is where you fix it.
2. **Change.** Write only what is deliberately different, each with a code. Most rows will say “None”, and that is the healthiest answer in the document.
3. **Hand off.** Write one instruction to your future self: what the next shot must reproduce exactly. Name the things that are easy to lose — which hand holds what, what is on the floor, what is switched off.

In the table it looks like this, in three crossed-out-for-you words:

```
SHOT 4   inherits:  mug upright and full, pencil in the LEFT hand, sleeves at the wrists, lamp L1
         changes:   none
         hands off: 30 s later, off-screen: mug tipped (P-01b), cardigan open, sleeves to the elbow (V2)

SHOT 5   inherits:  room, L1 lamp still lit, headphones on, door frame-right
         changes:   C — V2 (cardigan open, sleeves to the elbow)
                    C — P-01b (mug tipped, coffee ring on the blotter)
         hands off: V2 and P-01b to the end of the scene; lamp still L1
```

> **Tip — Why the middle line matters**  
> The “changes” line in shot 5 is what stops the *next* shot from quietly agreeing with the wrong version. It is also the line you paste into the prompt, in this order: anchors first, then the change.

## Put changes in ellipses, not in shots

If a change would be hard to generate as visible action — a spill, an unbuttoning, a haircut, someone leaving and coming back — do not generate the transition. Put a time jump between two shots, record the change in the later row with its cause, and let the audience do the work. A change you never show is a change you never have to generate consistently.

The worked example does exactly this: the coffee is spilled in a thirty-second gap between shot 4 and shot 5. Neither shot has to animate it, and both shots are easy to describe.

## When a shot drifts

It will happen. The useful question is not “why did the model do that” but “what is the cheapest fix”. Three options, in order of cost:

| Response | When it is the right one | What you do |
|---|---|---|
| Re-frame | The drift is outside the frame you actually need. | Tighten or re-angle so the drifted detail is not in shot. Cheapest, and usually invisible. |
| Re-cut | The drifted shot is the weaker one and its neighbour is good. | Change this shot to match the neighbour, and update the row so the table stays true. Never leave the document describing a shot you did not make. |
| Re-generate | The drift is in the anchors — face, hair, room, wardrobe colour. | Re-run with the anchor lines first and the action last. If it drifts twice, the anchors are too vague: make them more structural (see below). |

> **Watch out — When the model will not hold a variant**  
> Most stubborn variants are described at the wrong scale. “A fine embroidered pattern on the pocket” will drift; “cardigan open over a cream tee, sleeves pushed to the elbow” will not. Describe change in structures a stranger could see from the other side of the room — shape, silhouette, colour block, what is open, what is off.

## A weak handoff line, and the same line made strong

The handoff line is the only sentence that crosses a cut. It is where most of the value is, and it is the first thing people write badly — as a mood, not as a list of things the next frame must contain.

```
WEAK      same look as shot 3, a bit darker, she is tense

STRONG    CH-01, V1 cardigan buttoned to the third button, sleeves at the wrist
          L1 lamp lit red, corridor strip dark, door frame-right
          P-01a mug upright left of the script, headphones on, pencil out of shot
          camera south of the desk at (0.65, 0.45), medium close-up, she looks off-lens
          frame-right · hands off to shot 4: same frame, mug still full
```

Both lines are true. Only one of them can be checked. Notice that the strong line has no adjectives about mood: mood is carried by the light code and the eyeline, which are the things a model can actually hold.

# What this system does and does not do

| It does | It does not |
|---|---|
| Give you one page per character and location that you copy from, instead of re-describing from memory. | Guarantee a consistent result. Continuity here is a production judgment supported by a written record. |
| Make every intentional change explicit, coded and traceable to a shot number. | Stop drift on its own. You still check each shot, and you still decide what to accept. |
| Give you a handoff line between shots that you can read out loud before generating. | Replace your eye. The document tells you where to look; it cannot see the frame for you. |
| Work with any generation model or pipeline, because it records decisions, not model settings. | Recommend a model, a prompt style or a paid tool. |

Two honest limits worth knowing on day one. First, a document cannot make a decision for you: where the generation is ambiguous, you decide, and the U mark is simply a way of writing down that you did. Second, the system is only as good as the shots you pick — a table full of rows describing frames you rejected is worse than no table, because it teaches you to trust it.

> **Rule — The habit that makes it work**  
> When the frame on screen and the document disagree, the document changes. Every time. A continuity document that quietly drifts from the real shots is the one failure mode this system cannot survive.

# Words used in this system

Defined once, here, so the sheets can stay short.

| Word | Plain meaning |
|---|---|
| Identity | The traits that make a character or room recognisable. They are meant to stay the same for the whole sequence. |
| Variant | A deliberate change, given a code (V1, V2 for a character; L1, L2 for light; P-01a, P-01b for a prop state). |
| Shot state | The exact condition of one shot: what happens, where the body is, what the hands hold, how it is framed, which light is on. |
| Handoff line | The sentence that says what the next shot must inherit exactly. Every shot row ends with one. |
| Anchor shot | The first shot you generate — usually the widest, because it proves the most. Later shots are checked against it. |
| Anchors | The five features on the character sheet that a stranger could check at a glance. Copied word for word, never paraphrased. |
| Drift | An unintentional difference between shots: a swapped hand, a changed hairline, a mug that refills. The opposite of a variant. |
| The line | The imaginary axis between two people, or between a person and a thing they face. Keep every camera on one side of it and the cut will read as one space. Crossing it without a reason makes a shot feel flipped. |
| Frame-left / frame-right | From the audience's point of view. “Mug frame-left” means it appears on the left side of the picture, whatever side of the room it is on. |
| Insert | A close shot of a detail — hands, paper, a screen — rather than a person's face. |
| Over-the-shoulder (OTS) | A shot framed past one person's head or shoulder, usually toward what they are looking at. |
| Medium, medium close-up (MCU), wide | How much of the body and room is in frame. A wide shows the room; a medium shows waist-up; a medium close-up shows chest-up. |
| Lens feel | Optional. The impression of a focal length — wide, normal, long. If your workflow cannot control it, record it as a note and check the framing size instead. |
| Time band | The clock window the sequence sits inside, e.g. 02:40–02:52. It rules out light that could not exist. |
| Ellipsis | A jump in time between two shots. The cheapest place to put a change you do not want to generate. |

---

# Frequently useful answers

### My scene has two characters. Do I need two sheets?

Yes — one character sheet each, and one extra pair of columns in the table, or two tables side by side. The worked example deliberately keeps to one on-screen character so the handoff is easy to read; the method is identical.

### How many shots should a table hold?

Six is the design size: enough to need a system, few enough to check in one sitting. For a longer scene, copy the table and continue the numbering — never restart at shot 1, or the handoff lines lose their place.

### What if I do not know a detail yet?

Mark it U, write what you will accept if the generation chooses for you, and move on. An honest U is worth more than a confident guess that you forget to check.

### What if the scene has no wardrobe change?

Then the variant register has one row, V1, and the register is short. That is a good sign, not a gap. Most drift comes from changes nobody asked for.

### Is this a prompt template?

No. It is a record of decisions, and it feeds whatever prompts or references your workflow uses. The anchor lines and the change codes are the parts that go into a prompt; the rest is for you.

### Do I have to fill in every field?

No. The minimum that works is five anchors, three never-change items per subject, one variant, one light state, and the handoff line on every row. Everything else is there for the shot where it matters — fill the rest in as you generate, not before.

### What do I do with the drift log at the end?

Keep it with the project, and read it before your next scene. Drift repeats in patterns: the same hand, the same prop, the same light. Six logged shots are enough to show which of your habits the model keeps breaking, which is more useful than any single fix.

### Can I use this on a phone or tablet?

The Markdown files read fine anywhere. For typing, copy them into any notes app or document editor. There is also an offline HTML form in the tools folder if you prefer fields to lines, but the printed sheets are the product.
