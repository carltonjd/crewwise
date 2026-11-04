---
target: Crewwise full home page round 8 (fix verification)
total_score: 27
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 0
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:a9ced63bf100f948fd52b9044c78f5a776ac16982ba4441584bf7ec9e0be4833"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T16-27-25Z
slug: src-pages-index-astro
---
DEGRADED: single-context (lean review requested by caller; no sub-agents, browser overlay skipped). CLI detect run once on src/pages/index.astro: 0 findings.

# Full home page critique (src/pages/index.astro), round 8 after the fix round

Verdict: APPROVE WITH NOTES. Every item from round 7 has landed, and the one blocker (the skyline running through the close) is gone at all four scrub points and both widths, with 0 measured text/town intersections. I would sign this off for launch. It is not yet a studio showcase piece: SlipAway still leaves half its stage empty at 1440, and the inner pages drift out of the cut-paper material.

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 4 | The Demo arrives finished. 0 hidden on load and in print. The hero wipe never hides the sub-line or CTA. |
| 2 | Match System / Real World | 4 | The day reads in order, and the close now sits below the town. |
| 3 | User Control and Freedom | 3 | Fine. |
| 4 | Consistency and Standards | 3 | Inner-page cards use rounded corners (free-audit .covers 16px, roofing .slotted 12px, pricing 12px) against cut-paper slips everywhere else. There are still two Replay controls. |
| 5 | Error Prevention | 3 | Fine. |
| 6 | Recognition Rather Than Recall | 3 | Fine. |
| 7 | Flexibility and Efficiency | n/a | Persuade surface. |
| 8 | Aesthetic and Minimalist Design | 3 | 9,247px at 1440 (was 9,537). Pillars is 1,478px. The left half of the SlipAway stage is empty at 30–50%. The HowItWorks slips have empty bottoms of about 35%. The roofing head plate is empty above its slip. |
| 9 | Error Recovery | 4 | The audit form is unchanged. |
| **Total** | | **27/32 (84%)** | **Good** |

Clarity 8.5. Premium 8 (hero 8.5, below the fold 7.5). Wow 7. Trend 26 to 27.

## Previous asks
- SlipAway skyline collision: DONE. .stage is in place, the town is at 4009+194 and the close starts at 4769. There is no overlap at 0, 30, 50 or 100% at either 1440 or 390.
- Empty free-audit head plate: DONE. The checklist sheet sits on the plate. Its content now duplicates the "What your audit covers" aside below.
- Demo arriving empty: DONE. The finished transcript and log show on entry.
- Hero entrance overlap: DONE. The clip-path wipe at t=0.3 keeps line 2 out of the sub-line.
- Hero floor dead space: PARTLY. The hero is 722px, but about 110px of blue-deep floor remains below the caption at 1440.
- Paper world coverage: DONE. HowItWorks is a blue strip with slips. The FAQ is a paper sheet with a blue-deep aside.
- Pillars length: DONE. 2,039 to 1,478.

## Priority issues
- [P2] SlipAway dead left column at 1440, 30–50% scrub. Make the lead (h2 + lede) sticky in the left column through the scrub, or put a running time-of-day there.
- [P2] Roofing head: the top 60% of the navy plate is empty and the slip sits at its foot. Centre .slotted on the plate, or stack a call slip above it.
- [P2] Material drift on inner pages. free-audit .covers (16px radius), roofing .slotted (12px) and the pricing head card (12px) should take the slip's cut corner and edge instead of a radius.
- [P3] HowItWorks slips: equal-height columns leave empty bottoms. Use align-items:start with a small stagger.
- [P3] Pricing shows "From $299/month" twice in the first viewport (head card and plate).
- [P3] The moon touches the right edge at 390. The WhoFor h2 sits off the left edge every other h2 shares.

## Questions
- Could the SlipAway left column carry a clock that moves from 2:14 to 7:30 as the slips land?
- Should the free-audit head sheet replace the "covers" aside rather than repeat it?
