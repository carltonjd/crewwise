---
target: Crewwise home hero
total_score: 16
max_score: 24
na_heuristics: 5,7,9,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
target_fingerprint: "sha256:dd2f31941a29713269433a94d3300b4ff22f15e07f4dd740ed54e69e0c45399d"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
timestamp: 2026-11-02T07-57-19Z
slug: src-components-home-hero-astro
---
Method: dual-agent (A: design review, B: detector + contrast)
Scope: home hero ("the first minute"), before fixes.
Heuristics scored: 1 (3), 2 (3), 3 (2), 4 (3), 6 (3), 8 (2); others n/a. Total 16/24 (67%).
Verdict: specific idea, generic execution; timeline read as Step 1-2-3. Contrast all AA in hero (button 4.79 tightest). Detector: 0 non-advisory.
Priority issues: [P1] timeline not measured (moments at column edges, no ticks); [P1] phone: minute below the fold and played off-screen; [P2] CTA floated right off the reading path; [P2] cards heavy/template-like, booked card weakest; [P2] motion sequencing (pulse unseen, no answer beat); [P3] caption + Example pill acted as eyebrow/badge.
Applied: dots at true seconds with drop lines and 10s ticks; start on visibility; CTA under sub-line; lighter cards and a calendar-slot booked card; ringing to answered beat, staggered lines, drawn check; caption moved under the timeline as one quiet line; laptop compaction.
Open: plumber persona (Phase 2 switches), phone hero 1.63 screens vs 1.5 target, stopwatch alternative not explored.
