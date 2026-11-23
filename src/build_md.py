"""Write the editable Markdown edition and the spreadsheet tracker."""

import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dsl import render_markdown
import docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06
import example as X
from schema import PRODUCT, TRACKER_COLUMNS, STATUS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = [docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06]

FRONT = (
    "<!--\n"
    "  {title} — The Continuity Bible {version}\n"
    "  Editable Markdown. Lines of underscores (________) are writing space: type over them.\n"
    "  Part {part} of 7. Full contents: product/README-first.md\n"
    "  You may edit, rename and reprint this file for your own productions.\n"
    "-->\n\n"
)


def main():
    written = []
    for i, m in enumerate(DOCS, 1):
        d = m.DOC
        path = os.path.join(ROOT, d["filename"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        md = render_markdown(d)
        header = FRONT.format(title=d["title"], version=PRODUCT["version"], part=i)
        with open(path, "w", encoding="utf-8") as f:
            f.write(header + md)
        written.append((d["filename"], len(md)))

    # Wide tracker CSV — one row per shot, for Google Sheets / Excel / Numbers.
    csv_path = os.path.join(ROOT, "product/spreadsheets/six-shot-continuity-tracker.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([c[1] for c in TRACKER_COLUMNS])
        # three example-filled rows, then three blank rows, as a starting point
        for s in X.SHOTS:
            w.writerow([
                s["shot_no"], s["slug"], X.CHARACTER["char_id"], X.LOCATION["loc_id"],
                s["variant"], s["light"], s["anchors_hold"],
                s["action_pose"], s["screen_position"], s["gaze"], s["props_hands"],
                s["prop_states"], s["set_dressing_delta"],
                s["framing_size"], s["camera_height"], s["lens_feel"], s["movement"],
                s["inherits_from"], s["changes_in_shot"], s["hands_off"], s["hazards"],
                s["status"],
            ])
        for _ in range(3):
            w.writerow([""] * len(TRACKER_COLUMNS))

    # Blank tracker, same columns, nothing filled in.
    blank_path = os.path.join(ROOT, "product/spreadsheets/six-shot-tracker-blank.csv")
    with open(blank_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([c[1] for c in TRACKER_COLUMNS])
        for i in range(1, 7):
            w.writerow([str(i)] + [""] * (len(TRACKER_COLUMNS) - 1))

    # Status marker reference, so the letters are never a mystery in the sheet.
    ref_path = os.path.join(ROOT, "product/spreadsheets/status-markers.csv")
    with open(ref_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Code", "Name", "What it means", "When you use it"])
        for s in STATUS:
            w.writerow([s["code"], s["name"], s["means"], s["when"]])

    for path, n in written:
        print(f"  wrote {path:58s} {n:>6d} chars")
    print("  wrote product/spreadsheets/*.csv")


if __name__ == "__main__":
    main()
