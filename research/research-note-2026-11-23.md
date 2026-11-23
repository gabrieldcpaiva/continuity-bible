# Research note — 23 November 2026

Focused research done **after** the core product was written and quality-checked, as the brief required.
Three questions only: the two competitor claims the brief flagged, and whether the product's central
argument (continuity is a workflow property, not a model setting) matches current practitioner guidance.

Access date for every source below: **23 November 2026**. Prices are list prices in US dollars as shown
on the page on that date; they change.

---

## 1. Boords pricing — verified on the vendor's own pricing page

**Source:** Boords, “Pricing”, https://boords.com/pricing (read 23 Nov 2026).

| Plan | Monthly list price | What the page states |
| --- | --- | --- |
| Free | $0, no card required | 5 active storyboards · 3 active scripts · 8 one-off sample AI image credits |
| Solo | $39/month | 1 user + unlimited clients · unlimited storyboards and scripts · 250 AI images a month |
| Pro | $75/month | up to 5 teammates · 1,000 AI images a month |
| Team | $125/month | up to 10 teammates · 2,000 AI images a month · client-hidden comments, project-level permissions |
| Agency | $250/month | up to 30 teammates · 3,000 AI images a month · priority support |
| Enterprise | Custom quote | SAML single sign-on, custom seats, audit trail |

The same page advertises “Save 33%” on yearly billing, a 30-day money-back guarantee on paid plans, and
unlimited no-signup client review on every paid tier.

**Caution about secondary sources.** Several third-party review pages currently describe Boords as
“Lite $19 / Standard $49 / Workflow $89”, or as “Standard $49 / Workflow $89–99”. Those numbers
contradict the vendor page and could not be reproduced from it, so they are not used anywhere in this
product. If you are buying or pricing against Boords, read boords.com/pricing itself.

**Status of the brief's claim:** the brief referred to “Boords pricing” without giving numbers, so there
was no supplied figure to confirm or refute. The figures above are verified from the vendor page on
23 Nov 2026 and should be re-checked before any future use.

## 2. Milanote free plan — verified on the vendor's own plans page

**Source:** Milanote, “Plans & pricing”, https://milanote.com/plans (read 23 Nov 2026).

- **Free**, “with no time limit”: **100 notes, images or links**, **10 file uploads**, **unlimited shared boards**.
- **Paid, per person:** $9.99/month billed annually, or $12.50 billed monthly — unlimited notes, images,
  links and file uploads.
- **Team:** $49/month billed annually for up to 10 people.

**Caveats seen in secondary sources and not confirmed on the vendor page:** one review claims PDF export
is unavailable on the free tier, while another says the free tier can export; one calls the team plan
“up to 10 members” and another “5 members”. These are unresolved, so the product makes no claim about
Milanote export or team size, only about the free-plan limits above, which the vendor page states plainly.

## 3. Does the product's argument match current practice guidance?

**Sources read on 23 Nov 2026:**

- Everypixel Journal, “AI Filmmaking Workflow: From Script to Final Cut (2026)”,
  https://journal.everypixel.com/ai-filmmaking-workflow-2026 (page date 12 Nov 2026).
- Domer, “From Idea to Short Film: Text-to-Video and Image-to-Video”,
  https://domer.io/blog/text-to-video-image-to-video-short-film-workflow (4 Oct 2026).
- Versely Studio, “How to Make an AI Short Film, Start to Finish”,
  https://www.versely.studio/blog/how-to-make-an-ai-short-film (3 Aug 2026).
- Flyaigh, “How to Make an AI Short Film (2026)”,
  https://www.flyaigh.com/blog/guide-make-ai-short-film (5 Jun 2026).

Four independently written guides from 2026 converge on the same three points, which is the part worth
recording:

1. **Continuity is a process problem, not a model setting.** Domer states it directly: “Continuity is
   where AI short films live or die, and it is entirely a process problem rather than a model problem.”
2. **The standard fix is a locked reference plus word-for-word reuse of the character description.**
   Domer: reuse “the same descriptive phrasing for the character attributes, word for word, in every
   prompt. Rewriting the description is the fastest way to get a different person.” This is the same rule
   the product encodes as “copy, do not paraphrase”.
3. **Nobody claims it is guaranteed.** Everypixel: “no method guarantees that every detail will remain
   unchanged”. Versely describes continuity as coming from “three techniques used together, not from any
   single model feature”.

**What this supports:** the product's central argument is consistent with current published guidance, and
the specific habits it enforces (identical wording, an approved anchor frame, an explicit change record)
are the ones practitioners describe.

**What this does not support:** nothing here is evidence that filmmakers will pay US$29 for a document.
It is evidence about method, not about demand. Adjacent tools exist — Boords sells storyboard software
from $39/month, Milanote sells a visual workspace from $9.99/month — and their existence shows the market
is real, not that this product fits inside it. That question is what the three-person commercial test in
`validation/` is for, and it is unvalidated.

## 4. Deliberately not used

- No paid prompt databases, prompt collections, courses or template packs were consulted, quoted or
  adapted. The schema, the example scene and all wording are original to this product.
- No claims are made about any video model's capability, and no model is named as required or recommended.
- One adjacent research paper (a 2026 multi-shot “entity memory” system) circulated in summaries during
  the research window. It was not read directly, so it is not cited as evidence here.

## 5. What still needs checking, if the product is ever sold

- Competitor prices at the moment of launch (they move; the 33% annual discount in particular).
- Whether the “independent AI filmmaker” segment treats US$29 as an impulse purchase or as a
  subscription-shaped decision — only the commercial test answers this.
- Whether buyers can use the sheets without the worked example in front of them — the two-person
  usability test in `validation/` is designed for exactly that question and has not been run.
