---
target: Crewwise home page
total_score: 25
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:e2f7c0e17ffc862ce1b47c31ff19291628972fd127d44d2b84c05e3259310c4b"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-01T12-36-50Z
slug: src-pages-index-astro
---
Method: dual-agent (A: design review, B: detector + browser overlay)

## Design Health Score (7 and 10 n/a: single-page Persuade surface)
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Call timer and Today tag good; day-rail now-line never explained |
| 2 | Match system / real world | 4 | Trade language and appointment-book frame fit the audience |
| 3 | User control and freedom | 3 | No visible replay or pause on the call |
| 4 | Consistency and standards | 3 | Inner pages match; rail and gutter appear on some sections, not others |
| 5 | Error prevention | 3 | Audit form labels, optional markers, "I don't have one" |
| 6 | Recognition over recall | 3 | Services chips ("Booking button tapped") need decoding |
| 7 | Flexibility and efficiency | n/a | Persuade surface |
| 8 | Aesthetic and minimalist | 3 | Restrained, but voids (FAQ left column, padding) read unfinished |
| 9 | Error recovery | 3 | Form copy sound; submit states not re-tested |
| 10 | Help and documentation | n/a | Persuade surface |
| Total | | 25/32 (78%) | Good |

## Design specificity
Hero is authored for this product; below it the book becomes wallpaper and every section shares one skeleton (H2 left, hairline list right). Detector: 1 non-advisory (side-tab, roofing.astro:458, border-left 8px); 32 advisories (30 font-size, 2 radius off the DESIGN.md scale). Overlay counts: / 6, /pricing/ 3, /free-audit/ 3, /roofing/ 4.

## Priority issues
- [P1] Signature moment plays mostly off-screen on first visits (laptop, phone); CTA row zigzags. layout, animate.
- [P1] No second act after the hero; identical section rhythm, motion fades to reveals. bolder, animate.
- [P2] The ending fizzles: cryptic "Your free audit / Open" slot, no reassurance by the final button. clarify, delight.
- [P2] Thin trust layer: Octalogic is one paragraph; facts not set as book entries. shape.
- [P2] Professional firms get one small card; nothing in the first screens for a law-firm partner; no "never gives legal advice" line. clarify.
- [P3] Polish: translucent header ghosts content; gantt bars repeat step titles; "New enquiry" repeated 4x; roofing side-tab border. polish.

## Persona red flags
Jordan: gutter numbers and now-line puzzling; audit cost unknown until the form. Riley: cannot replay the call; 7-to-6 rail vs 7:30 PM content. Casey: sees one caller bubble, scrolls past before the booking lands. Dana (law partner): hero is all HVAC, firm proof buried, no legal-advice line.

## Questions
If the visitor never sees Thursday fill, does the page have a hero? Why does the book stop telling a story after the first screen? What does a law-firm partner see that is meant for them?
