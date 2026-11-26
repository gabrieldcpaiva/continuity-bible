# site/ — the free front door

One page. No build step at runtime, no frameworks, no fonts to download, no trackers, no network requests of
any kind. It carries the 60-second preflight as a working tool, the weak/strong handoff line, the seam from
the worked example, and direct downloads for the folder.

## Local preview

```bash
python3 -m http.server 8080 --bind 0.0.0.0 --directory site
# open http://localhost:8080
```

## Deploy on Vercel

The repo root has a `vercel.json` that serves this folder as a static site: no framework, no install, no build command, `outputDirectory` set to `site`. The page is meant to be indexed. Do not add an `X-Robots-Tag: noindex` header.

1. Import the Git repository in Vercel, or run `npx vercel` from the repo root.
2. Leave the build settings on what `vercel.json` already says.
3. Open the URL Vercel gives you. That URL replaces `[LIVE LINK]` in the README and the launch posts.

Nothing else to configure: no environment variables, no functions.

It also works from a USB stick or a `file://` open, except that **saved preflight state** needs
`localStorage`, which some browsers block for `file://` pages. The page degrades quietly — the checkboxes
still work, they just do not remember between visits.

## Rebuild after changing the product

The page is generated, not hand-maintained:

```bash
python3 src/build_site.py     # re-reads schema.py and example.py, re-copies the files, rewrites index.html
node tools/tests/test-site.mjs
```

`src/build_site.py` injects:

- the 15 preflight checks, from `schema.PREFLIGHT` — labels, lines and "why" text;
- the weak and strong handoff lines, from `schema.HANDOFF_WEAK` / `HANDOFF_STRONG_LINES` (the same
  constants the PDF prints, so the two cannot disagree);
- the copyable skeleton;
- the download table with real file sizes;
- the version and date.

If a marker is left unreplaced, the build fails rather than shipping a broken page.

## What lives in `files/`

| File | Source |
| --- | --- |
| `the-continuity-bible.pdf` | `product/The-Continuity-Bible-v1.0.pdf` (copy) |
| `templates-markdown.zip` | the seven `product/*.md` files, zipped at build time |
| `six-shot-continuity-tracker.csv`, `six-shot-tracker-blank.csv`, `status-markers.csv` | `product/spreadsheets/` |
| `continuity-form.html` | `tools/continuity-form.html` |

`files/` is disposable: delete it and rebuild.

## Editing the page itself

Content changes: `site/template.html` (the markers are listed above). Styling: the `<style>` block at the
top of the same file. There is no JavaScript framework — the whole script is ~90 lines at the bottom.

Two deliberate constraints, so the page stays honest and portable:

- **No external requests.** No CDN, no Google Fonts, no analytics. The icon is inline SVG.
- **Free for everyone.** The page does not mention a price. Keep it that way.
