---
target: Crewwise full home page round 7 (fix verification)
total_score: 26
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 1
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:a9ced63bf100f948fd52b9044c78f5a776ac16982ba4441584bf7ec9e0be4833"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T16-08-18Z
slug: src-pages-index-astro
---
DEGRADED: single-context (lean review requested by caller; no sub-agents, browser overlay skipped). CLI detect run once on src/pages/index.astro.

# Full home page critique (src/pages/index.astro), round 7 after the fix round

Verdict: APPROVE WITH NOTES. The fix round landed: content visible by default, SlipAway is now a full-bleed day-to-night scene telling each moment once, and the middle tier and FinalCta are fixed. One real defect blocks launch: the skyline rides up through the closing copy mid-scrub. Below the hero the page is still a well-made agency page, not studio level.

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | 0 of 17 entrance elements hidden on load or in print. The Demo log is still an 80%-empty navy slab when you arrive. |
| 2 | Match System / Real World | 4 | SlipAway order fixed: heading, 2:14, 6:40, 7:30, then "After you clock off". |
| 3 | User Control and Freedom | 3 | Fine. |
| 4 | Consistency and Standards | 3 | Two Replay controls (hero and Demo). The free-audit head has an empty navy plate. |
| 5 | Error Prevention | 3 | Fine. |
| 6 | Recognition Rather Than Recall | 3 | Fine. |
| 7 | Flexibility and Efficiency | n/a | Persuade surface. |
| 8 | Aesthetic and Minimalist Design | 3 | 3 orange body CTAs plus 2 text links (was 6+). The length is barely changed: 9,537px on desktop and 11,466px on mobile. Pillars is 2,039px. There is a dead left column in SlipAway between the lead and the closing. |
| 9 | Error Recovery | 4 | The audit form is unchanged and strong. |
| **Total** | | **26/32 (81%)** | **Good** |

Clarity 8.5. Premium 7.5 (hero 8.5, below the fold 7). Wow 6.5. Trend 24 to 26.

## Previous asks
- Content visible by default: DONE. 0 hidden on load and in print. The hero sub-line and CTA are visible at t=0.3.
- Two authored motion moments: DONE. data-enter is down to 2 uses. The hero and SlipAway carry the motion; the Demo playback is product proof.
- SlipAway full-bleed, each moment once: DONE, with a collision defect (P1 below).
- Hero dead zone: PARTLY. The caption and Replay moved up, but about 170px of empty floor remains below Replay at 1440.
- Real middle hierarchy tier: DONE. Pillars h3 is 40px under a 68px h2.
- Asymmetric WhoFor: DONE. A large house plate against a small offset firm plate.
- 3 CTAs, not 6+: DONE for buttons (hero, story, close). Two quiet text links remain (route, faq).
- FinalCta dead space: DONE.
- Inner pages in the world: PARTLY. The pricing plate and card, the roofing slip and the 404 torn note are good. The free-audit head is an empty navy slab with nothing on it.

## Priority issues
- [P1] SlipAway skyline collides with the closing copy mid-scrub. At 1440, scrub 50%, the town band sits behind "Calls forward to the AI front desk..." with window lights and a light line cutting through the letters. At 390, scrub 50%, the buildings run behind "After you clock off" itself. Fix: give .story-close a bottom padding of at least var(--town-h) so the copy always clears the town. Or keep the town below the copy column (z-index under, with copy at its final y above .town top). Suggested command: /impeccable layout.
- [P2] The free-audit head plate is empty. Fix: put the "Your free audit" sheet (FinalCta) on the plate, or delete the plate.
- [P2] The Demo arrives empty. Fix: render the finished transcript and log as the default, then replay on tab or click. Or start playback at 40% when the section enters.
- [P2] Hero entrance: at t=0.3 the rising line 2 of the h1 overlaps the sub-line. Fix: animate the headline with clip/opacity only, or delay the sub-line so they never share pixels.
- [P3] Hero floor below Replay at 1440: reduce .hero min-height by about 120px, or bring the slip onto the floor further left.

## Questions
- Pillars is 2,039px. Could it be one plate per service at half the height?
- Could the cut-paper material reach HowItWorks and FAQ, which are plain white bands?
