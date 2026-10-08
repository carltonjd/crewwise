---
target: homepage
total_score: 25
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 1
target_identity: "file:D:\\Work\\Projects\\tradeapp\\public\\index.html"
target_fingerprint: "sha256:4105d17ed084903ea2d4bf24eab1251c5e82c9631c0b453156f56845e20726a8"
target_path: "D:\\Work\\Projects\\tradeapp\\public\\index.html"
timestamp: 2026-10-08T09-30-29Z
slug: public-index-html
---
Method: dual-agent (A: design review · B: detector + browser)

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | System status | 3 | Scene gives no sense of scroll left; reveal-gated cards sit empty at reading speed |
| 2 | Real world | 3 | Roofer language; "AI front desk", "Lead Recovery Report", "opportunity value" are coined |
| 3 | User control | 3 | Skip link, rail buttons; skip link small (77x22) |
| 4 | Consistency | 3 | Switch knobs drawn off while labelled On; "Sorted by urgency" before sorting |
| 5 | Error prevention | 3 | Phone placeholder reads as a value |
| 6 | Recognition | 3 | Price and "keep my number" hidden in FAQ / far down |
| 7 | Flexibility | n/a | Landing page |
| 8 | Minimalist | 3 | Page long (~19 phone screens); "Example. Names are made up." x7 |
| 9 | Error recovery | 4 | Field-level, keeps input, email fallback, change-number path |
| 10 | Help | n/a | Landing page (reviewer scored 3; excluded for like-for-like trend) |
| Total | | 25/32 | Good (78%) |

Specificity: content specific; skeleton still the stock SaaS order (split header x6, alternating rows, 3 steps, one price, 2-col FAQ, wordmark footer).
Detector: 10 CLI findings, all deliberate or false positive; browser adds desktop oversized-h1 (94px) as the only new candidate.

Priority issues
1. [P1] Qualified beat easiest to miss; scene scroll cost. (Beats reweighted and full autoplay added after this run.) /animate
2. [P2] Reveal-gated content empty at reading speed (How it works on phone, follow-ups, busy list); switches drawn off while "On". /animate, /polish
3. [P2] $72,000 still the loudest result-like number; show the formula. /clarify
4. [P2] No human presence (founder / who you'll talk to). /clarify
5. [P2] Phone ending: 12 FAQs then reach rows before the form; price late. /adapt, /distill
