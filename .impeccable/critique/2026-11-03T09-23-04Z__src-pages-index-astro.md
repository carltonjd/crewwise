---
target: Crewwise home page full review
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 1
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:211de4dfe6d970b9f97cf203bca57fefcf77ee4bfd1f1466a49cba4647603b35"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T09-23-04Z
slug: src-pages-index-astro
---
Method: dual-agent (A: design review sub-agent · B: detector/browser sub-agent), parent ran ban-list audit and captures.

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Demo auto-switches Home-service to Law firm tab unannounced; SlipAway progress only via 0.38 dimming |
| 2 | Match System / Real World | 3 | Strong real-day copy; "Handled by AI front desk" drops "the" |
| 3 | User Control and Freedom | 3 | Replay, Esc, focus trap good; Demo auto-advance takes control mid-read |
| 4 | Consistency and Standards | 2 | Five audit-link looks (incl. banned "→"), WhoFor h2 smaller than its h3s, mobile bar has no CTA, three different phone drawings |
| 5 | Error Prevention | 3 | All anchors resolve, no dead links |
| 6 | Recognition Rather Than Recall | 3 | SlipAway close recalls 8:41/2:14/7:30 from ~2,500px above |
| 7 | Flexibility and Efficiency | n/a | single-action marketing page |
| 8 | Aesthetic and Minimalist Design | 3 | SlipAway ~3,000px mostly dimmed; WhoFor redundant |
| 9 | Error Recovery | 3 | no forms on home; no-JS/reduced-motion get final states |
| 10 | Help and Documentation | n/a | marketing surface |
| **Total** | | **23/32 (72%)** | **Good** |

Clarity 8/10 · Premium 7/10 · Wow 7/10. Verdict: not ship-ready (1 P1 + craft-floor bans), about a day of fixes.

## Ban-list violations (craft-floor)
1. Hard zero-blur offset shadow: Hero.astro z0 `.sh` phone copy `<g transform="translate(10 10)">` fill #1749B0 (lines 79-84, CSS 655-668, JS 1169/1389) and Call now `rect.cbs` 3px offset (line 148-157, anim 828). Visible at phone bottom-right in every hero capture.
2. Eyebrow above heading: HowItWorks `.when` above `h3` ("Within two business days" etc.). Also free-audit aside "First/Then" labels above lines; SlipAway `.step-time` above step text (borderline).
3. Section numbers without meaning: Header.astro:77 mobile menu `<em>01..04</em>`.
4. Tracking below -0.04em floor: h1 -0.045em (all pages), `.display` h2s -0.048em (demo, slip, close), `.h2` -0.042em, `.price` -0.045em.
5. Identical entrance on every section from an invisible default: global.css:479 `.js [data-rise]{opacity:0;translateY(12px)}` on Pillars, SlipAway, HowItWorks, WhoFor, FAQ, FinalCta.
6. Unicode glyph as icon: Pillars.astro:247 `.meta-link::after{content:'→'}`.
7. Borderline: two equal plate+heading+text items in Pillars `.pair`; pricing three soft-shadowed white cards on soft grey; footer giant full-width wordmark (category trope); FAQ rounded soft cards with + discs.
PASS: gradient text, glass/backdrop, side stripes on cards (WhoFor 3px top rule is a column rule), system display face (Hanken self-hosted), emoji, fake stats, centred-everything (only route title centred), floating pill nav (full-width bar), browser surfaces themed (selection, caret, accent, scrollbar), no horizontal overflow, one H1 per page, no en/em dashes, 404 returns 404.

## Brief conflicts
- Surface brief line 11 "blue offset shadow on cards" contradicts its own line 18 and the craft floor. Delete.
- Surface brief line 22 "fingertip tap on Call now" contradicts owner "no finger imagery" (build uses ripples only). Reword.
- DESIGN.md 135/143/154/158/209/215-221/247-248/266 Hard Shadow Rule and offset vocabulary: banned; DESIGN.md is stale (day rail, appointment book, "refuses split hero with phone mockup" line 139/276 contradicts the chosen G2a hero). Regenerate via /impeccable document.
- PRODUCT.md 65 "eyebrow labels over every heading" implies eyebrows are fine sometimes; the craft floor bans all eyebrows. Reword to "no eyebrow labels".
- Source comments still describe hard shadows: Hero.astro:6,148,655,1169,1389; Demo.astro:350; HowItWorks.astro:74; global.css:18,396; legacy token names --shadow-booking*.

## Priority issues
- [P1] Hero hard offset shadows (phone `.sh` z0 copy, `.cbs`). Fix: delete the z0 `.sh` svg and `.cbs`; depth from the existing blue-deep plane or `filter: var(--drop-paper)`; animate press with scale/fill. /impeccable polish
- [P2] Craft-floor bans: HowItWorks `.when` eyebrows, menu 01-04, tracking below -0.04em, uniform data-rise fade from opacity 0, "→" glyph. /impeccable polish + typeset + animate
- [P2] Mobile solid bar has no CTA (Header.astro `.side .cta{display:none}` under 62.5rem). Show compact "Free audit" pill when `[data-solid]`. /impeccable adapt
- [P2] SlipAway too long/dim, no CTA at resolution (`.step` min-height 40vh, opacity 0.38; mobile row layers overlap mid-transition). Trim to ~28vh, raise to 0.55, button in `.step-close`. /impeccable distill
- [P2] WhoFor inverted hierarchy (`.who-title` step-2 < `.aud-title` 2.75rem) and redundant. /impeccable distill
- [P2] Header `.rule` scaleX goes negative in JS fallback/reduced motion (stub at left gutter). Clamp with max(0,…).
- [P2] Footer thin (Pricing, Free audit only; no services, no Book a call) and giant wordmark generic; `.mark` border-radius curls the hairline.

## Persona red flags
Jordan: "AI front desk" never defined plainly; "Example call" outlined pill reads as a button; Demo switches itself. Riley: reduced-motion hairline stub; footer rule curl; close slip says "Free audit booked" before anything is booked. Casey: no CTA in the bar or thumb zone after the hero; tall Demo phone scrolls inside the page. Plumber owner: hero proof is a law firm; price first appears in Pillars; "PO 1042 / Invoice 1042" reads office.

## Detector
Source: exit 0, 76 advisory (63 design-system-font-size, 13 design-system-radius). dist: 178 findings (cramped-padding 67 mostly FP on full-bleed wrappers; low-contrast 12 incl. :hover #1a4fbd on navy 2.4:1 to check; nested-cards 6 FP; side-tab 3; tight-leading 3 at 1.28; dark-glow 4 on roofing FP; layout-transition 1; shape-assembled-illustration 1; pulsing-dot 1 intentional). Browser overlay: home 23, roofing 5/4 (oversized hero headline), others 0. The detector did not catch the SVG hard offsets; the ban audit did.

## Questions
1. Does the page need both Demo and SlipAway? 2. Should the hero alternate a trade firm with Harbor & Lane? 3. End on the booking slip instead of the logo?
