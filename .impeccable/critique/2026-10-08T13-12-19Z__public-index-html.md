---
target: homepage
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\public\\index.html"
target_fingerprint: "sha256:02a96caa4ae6d1cc49b50b9279fc4d1f02bd8fe4d430eaab172d200c842baa23"
target_path: "D:\\Work\\Projects\\tradeapp\\public\\index.html"
timestamp: 2026-10-08T13-12-19Z
slug: public-index-html
---
Method: dual-agent (A: design review sub-agent · B: detector sub-agent)

| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of status | 3 | Hover pause note good; phone call sits faded until scrolled to, reads as disabled; nav keeps FAQ active over contact |
| 2 | Match real world | 3 | Roofer artifacts strong; generic hero copy and "generous allowance" |
| 3 | User control | 3 | Replay, pause, dialog Esc/close; no touch control of the call |
| 4 | Consistency | 3 | CTA labels vary (Book a demo / 15-min demo / Call me back / Join the list) |
| 5 | Error prevention | 3 | Required/optional clear; no phone format hint |
| 6 | Recognition | 3 | "Busy-day mode" in nav before it's explained |
| 7 | Flexibility | n/a | single-goal marketing page |
| 8 | Minimalist design | 3 | Middle feature run long, repeats pricing list and FAQ |
| 9 | Error recovery | 3 | Good inline errors; summary banner below the button |
| 10 | Help | n/a | kept comparable |
| **Total** | | **24/32** | Good (75%) |

Specificity: ~70% authored (call route, transcript, calendar, storm queue, report, connector line); generic: headline pattern, stock section heads, 3-step row, checklist pricing, giant footer wordmark.
Detector: CLI 11 home / 10 roofing; browser 9/8 desktop/phone. Previous real issues gone (blue glow, bounce easing); navy colours now tokens. Remaining real: oversized h1 hit (owner choice), thin-border wide-shadow on the join dialog (advisory). Others false positives.

Priority issues
1. [P1] Phone hero call never plays in the first screen and reads as disabled; 693px tall so Booked finishes off-screen. Fix: phone single card swapping in place with step pips, start at ~15% visible. /impeccable adapt
2. [P1] Trust gap: no voice, no person (pending owner material). /impeccable clarify
3. [P2] Hero action cluster: 4 links plus nav CTA; Join the list tap target 22px. /impeccable distill
4. [P2] "What happens after the phone rings" plateau: 9 feature rows repeated in pricing and FAQ. /impeccable layout
5. [P2] Pricing vagueness: minute allowance unquantified; no call-back window. /impeccable clarify

Minor: desktop header gap shows page text; Replay and pause note ~100px below cards; busy-day panel caught mid-sort; leak X marks partially drawn on fast scroll; pricing terms nearly as loud as $499; FAQ two-column zigzag; nav has no Contact item.
