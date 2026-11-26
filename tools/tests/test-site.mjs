// Functional test for site/index.html — loaded from disk, no browser window, no network.
//
//   npm install --no-save jsdom
//   node tools/tests/test-site.mjs
//
// Checks the things a page can break silently: missing download targets, the preflight
// counter, persistence, reset, and whether the two published lines match the PDF source.

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { JSDOM, VirtualConsole } from "jsdom";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..", "..");
const site = join(root, "site");

let pass = 0;
const fails = [];
const check = (ok, label, extra = "") =>
  ok ? pass++ : fails.push(extra ? `${label} — ${extra}` : label);

const page = readFileSync(join(site, "index.html"), "utf8");

// 1 — no external requests, no leftover template markers
check(!/(?:src|href)="https?:/.test(page), "the page makes no external requests");
check(!/__[A-Z_]+__/.test(page), "no unreplaced template markers");

// 2 — every download link resolves to a real file
const links = [...page.matchAll(/href="(files\/[^"]+)"/g)].map((m) => m[1]);
check(links.length >= 5, "at least five download links", `${links.length}`);
for (const l of new Set(links)) {
  check(existsSync(join(site, l)), `download exists: ${l}`);
}
const files = readdirSync(join(site, "files"));
check(files.length >= 5, "the files folder is populated", `${files.length} files`);

// 3 — the page loads and runs
const vc = new VirtualConsole(); // swallow jsdom CSS parse noise, surface nothing
const dom = new JSDOM(page, {
  runScripts: "dangerously",
  url: "https://continuity.test/",
  pretendToBeVisual: true,
  virtualConsole: vc,
});
const { window } = dom;
const doc = window.document;
const $ = (s) => doc.querySelector(s);
const boxes = [...doc.querySelectorAll("#checks input[type=checkbox]")];

check(boxes.length === 15, "fifteen preflight checks render", `${boxes.length}`);
check(!!window.CB_SITE, "the page exposes its preflight state");
check(doc.querySelector("#counter").textContent.startsWith("0 of 15"), "counter starts at 0 of 15");

// 4 — every checkbox has a label
const unlabelled = boxes.filter((b) => !doc.querySelector(`label[for="${b.id}"]`));
check(unlabelled.length === 0, "every check has a label", `${unlabelled.length} unlabelled`);

// 5 — ticking updates the counter and the done state
function tick(i) {
  boxes[i].checked = true;
  boxes[i].dispatchEvent(new window.Event("change", { bubbles: true }));
}
tick(0); tick(1); tick(2);
check(doc.querySelector("#counter").textContent.includes("3 of 15"), "counter follows the ticks",
  doc.querySelector("#counter").textContent);
check(boxes[0].closest(".check").classList.contains("done"), "a ticked row is marked done");
check(!boxes[3].closest(".check").classList.contains("done"), "an unticked row is not");

// 6 — state persists in localStorage under the documented key
const saved = window.localStorage.getItem("cb.preflight.v1");
check(!!saved, "state is saved to localStorage");
check(saved && JSON.parse(saved).checks && Object.values(JSON.parse(saved).checks).filter(Boolean).length === 3,
  "three checks are stored");

// 7 — completing all fifteen triggers the spoken-handoff prompt
boxes.forEach((_, i) => tick(i));
check(doc.querySelector("#counter").textContent.includes("15 of 15"), "counter reaches 15 of 15");
check(/handoff line out loud/i.test(doc.querySelector("#doneNote").textContent),
  "completion asks for the handoff line aloud");

// 8 — reset clears everything
$("#resetBtn").click();
check(doc.querySelector("#counter").textContent.startsWith("0 of 15"), "reset returns the counter to 0");
check(window.localStorage.getItem("cb.preflight.v1") === null, "reset clears the saved state");
check(boxes.every((b) => !b.checked), "reset unticks every box");

// 9 — the two handoff lines are the ones the book prints
const strong = $("#strongLine").textContent.trim();
check(strong.startsWith("CH-01, V1 cardigan buttoned"), "strong handoff line is the book's line");
check(/hands off to shot 4/.test(strong), "strong line ends with the handoff");
check(!/tense/.test(strong), "strong line carries no mood adjective");
check((doc.querySelector(".panel.bad pre").textContent || "").includes("tense"),
  "weak line is present as the counter-example");
check($("#skeleton").textContent.includes("hands off to shot"), "the copyable skeleton is on the page");

// 10 — the seam codes are the worked example's codes
const seam = doc.querySelector("#seam").textContent;
["V2", "P-01b", "L2"].forEach((c) => check(seam.includes(c), `seam section names ${c}`));

// 11 — honest claims only
const text = doc.body.textContent;
["guarantee that", "guaranteed consistent", "never drifts", "eliminates drift", "5 stars", "testimonial"].forEach((bad) => {
  check(!text.toLowerCase().includes(bad), `no banned claim: “${bad}”`);
});
check(/no trackers|no cookies|no analytics/i.test(text), "privacy claim is stated");
check(/not a prompt pack/i.test(text), "boundaries are stated on the page");
check(/The paper does not stop the drift\./.test(text), "the page states the book's limit in that sentence");
check(!/piece of paper that stops it/i.test(text), "the page does not claim the paper stops the drift");
check(!/\$29|US\$29|test price/i.test(text), "no price on the page");

// 12 — accessibility plumbing
check(!!doc.querySelector("a.skip"), "there is a skip link");
check(doc.querySelectorAll("h1").length === 1, "exactly one h1");
const h2s = doc.querySelectorAll("h2").length;
check(h2s >= 4, "sections are headed with h2", `${h2s} h2`);
check(doc.querySelector("#counter").getAttribute("aria-live") === "polite", "the counter is announced politely");

// report
console.log("\nsite/index.html — functional checks");
console.log("=".repeat(50));
console.log(`passed: ${pass}   failed: ${fails.length}\n`);
for (const f of fails) console.log("  FAIL  ", f);
if (!fails.length) console.log("  All site checks passed.");
process.exit(fails.length ? 1 : 0);
