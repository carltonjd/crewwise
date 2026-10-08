---
target: homepage
total_score: 25
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\public\\index.html"
target_fingerprint: "sha256:b090bf3e6d3e3a7c4e4b9d088ce11f9759e588d2973847d1b081f53a1fbc2b8c"
target_path: "D:\\Work\\Projects\\tradeapp\\public\\index.html"
timestamp: 2026-10-08T05-33-36Z
slug: public-index-html
closed: true
---
Method: dual-agent (A: design review · B: detector + browser)

## Design Health Score
| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 3 | Phone hero cards start faded at the fold and read as disabled |
| 2 | Match System / Real World | 3 | Roofer examples fluent; "AI front desk", "opportunity value" unexplained |
| 3 | User Control and Freedom | 3 | Solid; Calendly opens new tab without cue |
| 4 | Consistency and Standards | 3 | Blue bold leak "fixes" look like links; "Everything in What it does" names a section that has no such label |
| 5 | Error Prevention | 3 | Strong form; no best-time field despite "around your jobs" |
| 6 | Recognition Rather Than Recall | 3 | "Busy days" nav label opaque to first-timers |
| 7 | Flexibility and Efficiency | n/a | Single-purpose landing page |
| 8 | Aesthetic and Minimalist Design | 3 | Desktop hero pushes H1 low; closing CTA floats far from its headline |
| 9 | Error Recovery | 4 | Field-level, plain, actionable, keeps input |
| 10 | Help and Documentation | n/a | Landing page; FAQ covers it |
| Total | | 25/32 | Good (78%) |

## Design Specificity Verdict
Content specific, frame generic. Hero call story, storm queue and estimate thread are roofer-specific; the skeleton (eyebrow+giant H1, KPI tile grid with dark hero tile, 3-step how-it-works, single price card, 2-col FAQ, giant footer wordmark) is the stock SaaS sequence. Headline/eyebrow could sit on any AI receptionist site.
Detector: 16 CLI findings per page (identical on /roofing/): thin-border-wide-shadow x6, cramped-padding x4, dark-glow x3, layout-transition x1 (header padding), clipped-overflow x1 (body overflow-x, false positive), flat-type-hierarchy x1 (h4 17px/h3 18px vs 16px body). Browser: 32 per view, mostly bounce-easing (one --spring token, 1.35 overshoot, repeated), heading-rhythm (3 of 4 false positives), oversized-h1 (88px, desktop).

## Priority Issues
1. [P1] Homepage invites trades that can't buy (deliberate per brief; decision needed). /clarify
2. [P1] Phone first screen is all text; proof starts faded at the fold. /adapt
3. [P2] Content contradiction: 1418 Maple Ct is "claim filed, booked Mon 9" in hero but "No claim yet, sent to you now" in queue. /clarify
4. [P2] Biggest objection unanswered: does it sound like a robot, will callers know it's AI, what if it's wrong. /clarify
5. [P2] $72,000 tile spends trust; disclaimer far below. /clarify or /quieter
6. [P2] Desktop composition: hero H1 starts ~y480; closing CTA ~600px from headline. /layout

## Persona Red Flags
Jordan: "Busy days" nav, "Everything in What it does", no description of the demo.
Riley: Maple Ct contradiction; Calendly slug shows personal name.
Casey: no thumb-zone CTA over ~16 screens; report chart needs sideways scroll; orphan tile; email wraps in contact list.
Roofer owner on phone: reads "home-service"; price 10 screens down; India address first seen in footer with no named person.

## Minor Observations
Flat type steps (h4 17 / h3 18 on 16 body); header animates padding (layout transition); glow on .signal/.mtip; "Your front desk while you're on the job" near-repeats H1; hero caption carries key trust lines at 13px grey; leakmap hidden on phone.

## Questions
- Why is / general when only roofers can buy?
- Would a 30s labelled example call recording beat all animated cards?
- What if the report's biggest element were the word "Example"?
