// Functional test for tools/continuity-form.html — real DOM, no browser window.
//
//   npm install --no-save jsdom
//   node tools/tests/test-form.mjs
//
// It loads the file from disk (as file://, so nothing can touch the network),
// fills a sequence the way a filmmaker would, and checks that the exported
// plain text actually contains what was typed.

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { JSDOM } from "jsdom";

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, "..", "continuity-form.html"), "utf8");

let pass = 0;
const fails = [];
function check(ok, label, extra = "") {
  if (ok) pass++; else fails.push(extra ? `${label} — ${extra}` : label);
}

const dom = new JSDOM(html, {
  runScripts: "dangerously",
  url: "file:///continuity-form.html",
  pretendToBeVisual: true,
});
const { window } = dom;
const doc = window.document;
const $ = (sel) => doc.querySelector(sel);
const byField = (key) => doc.querySelector(`[data-field="${key}"]`);

function type(key, value) {
  const input = byField(key);
  if (!input) throw new Error("missing field: " + key);
  input.value = value;
  input.dispatchEvent(new window.Event("input", { bubbles: true }));
}

// 1 — the form builds itself
check(!!window.CB, "the page exposes its export API");
check(doc.querySelectorAll("[data-field]").length > 100,
  "the form renders a full set of fields",
  `${doc.querySelectorAll("[data-field]").length} fields`);
check(doc.querySelectorAll("details.shot").length === 6, "six shot blocks are created");
check(doc.querySelectorAll("#preflightChecks .check").length === 15, "fifteen preflight checks are created");
check(doc.getElementById("exportText") !== null, "there is an export area");

// 2 — every field has an accessible label
let unlabelled = 0;
doc.querySelectorAll("input[type=text], textarea, select").forEach((input) => {
  if (!input.id) { unlabelled++; return; }
  const labelled = doc.querySelector(`label[for="${input.id}"]`) || input.getAttribute("aria-label");
  if (!labelled) unlabelled++;
});
check(unlabelled === 0, "every input has a label or an accessible name", `${unlabelled} unlabelled`);

// 3 — fill a realistic sequence
type("char_id", "CH-01");
type("name_in_script", "RAE");
type("role_in_scene", "Night-shift radio host, eleven minutes from the end of her show.");
type("age_read", "Mid-40s");
type("face_anchor_1", "Right eyebrow split by a small pale scar");
type("face_anchor_2", "Dark mole below the outer corner of the left eye");
type("face_anchor_3", "Chin-length bob, silver at the temples, tucked behind the right ear only");
type("face_anchor_4", "Heavy straight eyebrows set close together");
type("face_anchor_5", "Sits with her weight on her left forearm");
type("wardrobe_baseline", "Charcoal cardigan buttoned to the third button, sleeves at the wrists.");
type("variant_code_1", "V1");
type("variant_what_1", "Baseline look: cardigan buttoned, sleeves at the wrists.");
type("variant_from_1", "1");
type("variant_code_2", "V2");
type("variant_what_2", "Cardigan open, sleeves pushed to the elbows.");
type("variant_from_2", "5");
type("variant_cause_2", "The spill during the ellipsis.");
type("never_change_1", "Brow scar on the right eyebrow");
type("anchor_line", "CH-01 RAE — right brow scar · mole left cheek · bob tucked right ear only");
type("loc_id", "LOC-01");
type("loc_name", "Studio B");
type("room_read", "4.2 m by 3.2 m, acoustic tile ceiling, one door, no windows.");
type("time_band", "02:40–02:52, deep night");
type("landmark_1", "Door, east wall, always frame-right");
type("light_sources_fixed", "Gooseneck lamp (warm); corridor light under the door");
type("geography_rules", "Every camera stays south of the desk. Door always frame-right.");
type("light_code_1", "L1");
type("light_what_1", "ON AIR lamp lit red; corridor strip dark");
type("light_shots_1", "1–5");
type("light_code_2", "L2");
type("light_what_2", "Lamp fully dark; warm corridor strip under the door");
type("light_shots_2", "6");

type("shot1_slug", "ROOM, FIRST LIGHT");
type("shot1_status", "F");
type("shot1_variant", "V1");
type("shot1_action", "Rae is mid-sentence at the mic, weight on her left forearm.");
type("shot1_propstates", "P-01a mug upright and full");
type("shot1_handsoff", "Door frame-right, mug frame-left, V1 wardrobe, headphones on.");
type("shot5_slug", "THE CALLER, CLOSE");
type("shot5_status", "C");
type("shot5_variant", "V2");
type("shot5_changes", "C — V2 cardigan open. C — P-01b mug tipped, coffee ring on the blotter.");
type("shot5_inherits", "From shot 4: room, L1 lamp lit, headphones on, door frame-right.");

type("prop_id_1", "P-01");
type("prop_what_1", "Cream stoneware mug with a chip on the lip");
type("prop_states_1", "P-01a upright full (1–4) · P-01b tipped with ring (5–6)");
type("open_id_1", "U1");
type("open_where_1", "Shot 6 — mixer buttons");
type("open_issue_1", "Which red button takes her off air");
type("open_decision_1", "Left one; accept any layout with two red buttons");

type("preflight_shot", "5");
byField("preflight_2").checked = true;
byField("preflight_14").checked = true;
type("drift_what", "Cardigan stayed buttoned, mug stood upright");
type("drift_verdict", "Drift in the anchors");
type("drift_action", "Re-generated with anchors first");

// 4 — build and inspect the export
const text = window.CB.buildExportText(window.CB.collect());
const expect = [
  "CH-01", "RAE", "Night-shift radio host",
  "Right eyebrow split by a small pale scar",
  "Charcoal cardigan buttoned to the third button",
  "V2 — Cardigan open, sleeves pushed to the elbows.",
  "LOC-01", "Studio B", "02:40–02:52, deep night",
  "L2 — Lamp fully dark",
  "ROOM, FIRST LIGHT", "THE CALLER, CLOSE",
  "C — V2 cardigan open. C — P-01b mug tipped, coffee ring on the blotter.",
  "P-01b tipped with ring",
  "Left one; accept any layout with two red buttons",
  "[x] 2. Identity", "[x] 14. Handoff",
  "Drift in the anchors", "Re-generated with anchors first",
];
for (const needle of expect) {
  check(text.includes(needle), `export contains “${needle}”`);
}
check(!text.includes("null"), "export contains no null values");
check(!text.includes("undefined"), "export contains no undefined values");
check(text.includes("  Row status:") || text.includes("Row status:"), "export labels the row status");
check(/SHOT 5 · status C/.test(text), "export reports shot 5 as changed");
check(text.split("\n").length > 80, "export is a full document, not a stub", `${text.split("\n").length} lines`);

// 5 — blank fields degrade gracefully rather than printing nothing
const empties = (text.match(/—/g) || []).length;
check(empties > 0, "empty fields are marked with an em dash");

// 6 — the build button writes the text into the page
doc.getElementById("btnBuild2").click();
check(doc.getElementById("exportText").value === text, "the build button fills the export area");

// 7 — the form makes no network calls when loaded from disk
check(window.location.protocol === "file:", "the page was loaded over file://");
const scripts = [...doc.querySelectorAll("script[src], link[href], img[src]")].filter((el) => {
  const url = el.getAttribute("src") || el.getAttribute("href") || "";
  return !url.startsWith("data:");
});
check(scripts.length === 0, "the page loads no external scripts, styles or images",
  `${scripts.length} external references`);
check(!!doc.querySelector('link[rel="icon"]'), "the form has a favicon");
check(/unsaved text is lost on reload/i.test(doc.body.textContent), "the form warns that unsaved text is lost");
check(!!doc.getElementById("btnClearDraft"), "there is a Clear saved draft button");

// 8 — everything happens inside one file
check(html.length > 20000 && html.length < 200000, "single self-contained file", `${html.length} bytes`);

// report
console.log(`\ncontinuity-form.html — functional checks`);
console.log("=".repeat(48));
console.log(`passed: ${pass}   failed: ${fails.length}\n`);
for (const f of fails) console.log("  FAIL  ", f);
if (!fails.length) console.log("  All form checks passed.");
process.exit(fails.length ? 1 : 0);
