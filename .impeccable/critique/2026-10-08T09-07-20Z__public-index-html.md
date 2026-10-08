---
target: homepage
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\public\\index.html"
target_fingerprint: "sha256:727bea581fc25e8fafd0a04aef656bcee083ea20db1c7409fa89936e9b028c1a"
target_path: "D:\\Work\\Projects\\tradeapp\\public\\index.html"
timestamp: 2026-10-08T09-07-20Z
slug: public-index-html
---
Method: dual-agent (A: design review · B: detector + browser)

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | System status | 3 | Scene rail good; no sense of scroll remaining; swallowed phone tap on Call me back |
| 2 | Real world | 3 | Roofer examples fluent; "Busy days", "opportunity value" opaque |
| 3 | User control | 2 | Pinned scene 340vh/300vh, no skip; phone explanation after the scene |
| 4 | Consistency | 3 | Beat 2 left-aligned vs centred beats; "Inspection booked" vs "Booked Mon 9:00 AM" |
| 5 | Error prevention | 3 | Placeholder reads as value |
| 6 | Recognition | 3 | Roofing (the only product sold) not in nav/menu/footer |
| 7 | Flexibility | n/a | Landing page |
| 8 | Minimalist | 3 | Same Oak Ridge call shown 4 times |
| 9 | Error recovery | 3 | Swallowed tap loses summary and Company error |
| 10 | Help | n/a | Landing page |
| Total | | 23/32 | Good (72%) |

Specificity: content specific (scene, leak map, storm queue, report sheet); frame still the SaaS kit (H2-left/intro-right x6, connectors, footer wordmark).
Detector: 12 CLI findings, all deliberate/false positives except .signal/.mtip blurred glow; browser: bounce-easing token, oversized h1 desktop, heading-rhythm false positives.

Priority issues
1. [P1] Phone: sub + buttons + roofing link buried after 300vh scene; dead space at top of pin. /adapt
2. [P1] Roofing page undiscoverable (no nav/menu/footer link). /clarify
3. [P2] One example replayed four times; What it does should show other moments. /distill
4. [P2] Desktop scene: no product on first screen, long pin, inconsistent staging, no skip. /animate
5. [P2] No reassurance under hero CTA; $72,000 still the visual peak. /clarify
Also: phone tap on Call me back swallowed when the error message pushes the button (bug).
