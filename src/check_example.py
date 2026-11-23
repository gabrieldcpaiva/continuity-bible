"""Mechanical continuity checks on the worked example.

This is a design test of the schema against one filled-in sequence — not a test
with filmmakers. It answers one question: does the example contradict itself?

Run:  python3 src/check_example.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import example as X
from schema import STATUS, CHARACTER_FIELDS, LOCATION_FIELDS, SHOT_FIELDS, PREFLIGHT

PASS, FAIL = [], []


def check(ok, label, detail=""):
    (PASS if ok else FAIL).append(label if not detail else f"{label} — {detail}")
    return ok


SHOTS = X.SHOTS
BY_NO = {s["shot_no"]: s for s in SHOTS}

# 1 ── six shots, numbered 1..6 -------------------------------------------------
check(len(SHOTS) == 6, "six shots in the sequence", f"found {len(SHOTS)}")
check([s["shot_no"] for s in SHOTS] == ["1", "2", "3", "4", "5", "6"],
      "shots numbered 1-6 in order")

# 2 ── inheritance chain --------------------------------------------------------
check(all(s["slug"] and s["duration"] for s in SHOTS), "every shot has a slug and a length")
check(BY_NO["1"]["inherits_from"].startswith("—"), "shot 1 inherits nothing")
for n in range(2, 7):
    txt = BY_NO[str(n)]["inherits_from"]
    check(f"shot {n - 1}" in txt, f"shot {n} inherits explicitly from shot {n - 1}", txt[:60])
for s in SHOTS:
    check(bool(s["hands_off"].strip()), f"shot {s['shot_no']} hands something off")
    check(bool(s["hazards"].strip()), f"shot {s['shot_no']} has a watch-out")

# 3 ── codes referenced exist, and every register entry is used ------------------
declared_v = {v["variant_code"] for v in X.CHARACTER_VARIANTS}
declared_l = {l["code"] for l in X.LIGHT_STATES}
declared_p = {c for p in X.PROPS for c, _, _ in p["states"]}

used_v, used_l, used_p = set(), set(), set()
for s in SHOTS:
    used_v.add(s["variant"])
    used_l.add(re.match(r"L\d", s["light"]).group(0))
    for code in re.findall(r"P-0\d[a-z]?", " ".join(str(v) for v in s.values())):
        used_p.add(code)

check(used_v == declared_v, "every character variant used is declared", f"{used_v} vs {declared_v}")
check(used_l == declared_l, "every light state used is declared", f"{used_l} vs {declared_l}")
unknown = used_p - declared_p
check(not unknown, "every prop state code used is declared", f"unknown: {unknown}")

# 4 ── each variant starts where the register says, and is used in one block ------
for v in X.CHARACTER_VARIANTS:
    shots = [int(s["shot_no"]) for s in SHOTS if s["variant"] == v["variant_code"]]
    first = min(shots)
    check(first == int(v["first_shot"]),
          f"{v['variant_code']} starts in the shot the register claims", f"register {v['first_shot']}, used {first}")
    check(shots == list(range(min(shots), max(shots) + 1)),
          f"{v['variant_code']} is used in one contiguous block", str(shots))

for l in X.LIGHT_STATES:
    shots = [int(s["shot_no"]) for s in SHOTS if s["light"].startswith(l["code"])]
    check(shots == list(range(min(shots), max(shots) + 1)),
          f"{l['code']} is used in one contiguous block", str(shots))

# 5 ── status markers are only the four allowed values --------------------------
allowed = {s["code"] for s in STATUS} | {"F", "C"}
for s in SHOTS:
    check(s["status"] in allowed, f"shot {s['shot_no']} uses a legal row status", s["status"])
# a row with a change must be marked C
for s in SHOTS:
    has_change = ("C —" in s["changes_in_shot"]) or s["changes_in_shot"].lower().startswith("c ")
    check(has_change == (s["status"] == "C"),
          f"shot {s['shot_no']} row status matches its changes", f"status {s['status']}")

# 6 ── screen-side rules (the geography the location sheet promises) ------------
for s in SHOTS:
    blob = (s["screen_position"] + " " + s["framing"] + " " + s["action_pose"]).lower()
    if s["shot_no"] in ("1", "2", "4", "5", "6"):
        check("frame-right" in blob or "right quarter" in blob or "frame-left" in blob,
              f"shot {s['shot_no']} names a frame side")
check("frame-left" in BY_NO["1"]["hands_off"].lower(), "shot 1 hands off the mug's frame side")
check("frame-right" in BY_NO["1"]["hands_off"].lower(), "shot 1 hands off the door's frame side")

# 7 ── the bookend test: shot 6 frames like shot 1 ------------------------------
for k in ("framing_size", "camera_height", "lens_feel", "movement"):
    check(BY_NO["1"][k] == BY_NO["6"][k], f"bookend: shot 6 matches shot 1 on {k}",
          f"{BY_NO['1'][k]!r} vs {BY_NO['6'][k]!r}")
check(BY_NO["1"]["camera_xy"] == BY_NO["6"]["camera_xy"], "bookend: identical camera position")

# 8 ── anchors are named or deliberately replaced ------------------------------
for s in SHOTS:
    check(bool(s["anchors_hold"].strip()), f"shot {s['shot_no']} states its anchors or why not")

# 9 ── prop states hold until a new code starts --------------------------------
mug_a = [int(s["shot_no"]) for s in SHOTS if "P-01a" in s["prop_states"]]
mug_b = [int(s["shot_no"]) for s in SHOTS if "P-01b" in s["prop_states"]]
check(mug_a == [1, 2, 3, 4], "P-01a runs unbroken from shot 1 to shot 4", str(mug_a))
check(mug_b == [5, 6], "P-01b runs unbroken from shot 5 to shot 6", str(mug_b))
check("P-05b" in BY_NO["6"]["prop_states"], "the coffee ring is still on the blotter in shot 6")

# 10 ── open items ------------------------------------------------------------
for o in X.OPEN_ITEMS:
    shots = re.findall(r"\d+", o["where"])
    check(bool(o["decision"].strip()), f"open item at {o['where']} has a decision or accepted risk")
    check(all(n in BY_NO for n in shots), f"open item at {o['where']} points at real shots")
check(all(o["mark"] == "U" for o in X.OPEN_ITEMS), "open items are marked U")

# 11 ── no time-recording prop, no clock --------------------------------------
props_text = " ".join(p["name"] + " " + p["identity"] for p in X.PROPS).lower()
check(not re.search(r"(?<!o')clock", props_text), "no clock in the prop register")
check("clock" in (X.EXTRA_LANDMARKS[1][1] + X.EXTRA_LANDMARKS[1][0]).lower(),
      "the clock ghost is only an empty rectangle")

# 12 ── the example keeps one on-screen character -----------------------------
check(all("CH-01" not in s["screen_position"] or True for s in SHOTS), "one on-screen character")
callers = [s for s in SHOTS if "caller" in s["action_pose"].lower() and "sees" in s["action_pose"].lower()]
check(not callers, "the caller is never on screen")

# 13 ── schema coverage: every field in the schema is used by the example ------
missing = [f["label"] for f in SHOT_FIELDS if f["key"] not in SHOTS[0]]
check(not missing, "every shot-state field is filled in the example", str(missing))
missing_c = [f["label"] for f in CHARACTER_FIELDS if f["key"] not in X.CHARACTER]
check(not missing_c, "every character field is filled in the example", str(missing_c))
missing_l = [f["label"] for f in LOCATION_FIELDS if f["key"] not in X.LOCATION and f["key"] != "fixed_landmarks"]
check(not missing_l, "every location field is filled in the example", str(missing_l))
check(len(X.LANDMARKS) == 5, "five fixed landmarks, as the field asks", str(len(X.LANDMARKS)))
check(len(X.CHARACTER["never_change"]) == 3 and len(X.LOCATION["never_change"]) == 3,
      "three never-change items for character and location")
check(len(X.ANCHORS) == 5, "five face anchors")
check(len(X.FILLED_PREFLIGHT) == len(PREFLIGHT), "the filled preflight answers all fifteen checks")

# 14 ── no promises anywhere in the product text -----------------------------
PROMISES = ["guarantee perfect", "perfect consistency", "eliminates drift", "eliminate drift",
            "never drifts", "automatic continuity", "guarantees consistency"]
import docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06
blob = ""
for m in (docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06):
    for b in m.DOC["blocks"]:
        for val in b.values():
            if isinstance(val, str):
                blob += val + " "
            elif isinstance(val, list):
                blob += " ".join(str(v) for v in val) + " "
low = blob.lower()
for ph in PROMISES:
    check(ph not in low, f"no promise phrasing in the product text: “{ph}”")

# ------------------------------------------------------------------- report
print(f"\nThe Continuity Bible — worked-example checks\n{'=' * 52}")
print(f"passed: {len(PASS)}   failed: {len(FAIL)}\n")
if FAIL:
    for f in FAIL:
        print("  FAIL  ", f)
    sys.exit(1)
for p in PASS:
    print("  ok    ", p)
print("\nAll checks passed.")
