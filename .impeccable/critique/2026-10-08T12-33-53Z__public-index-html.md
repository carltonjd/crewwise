---
target: homepage
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:D:\\Work\\Projects\\tradeapp\\public\\index.html"
target_fingerprint: "sha256:f39132593115c3b136dfd077d7c7b1f79da82a116480b4c582facdf2a6c60829"
target_path: "D:\\Work\\Projects\\tradeapp\\public\\index.html"
timestamp: 2026-10-08T12-33-53Z
slug: public-index-html
---
Method: dual-agent (A: design review sub-agent · B: detector sub-agent)

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 3 | Route shows progress well; paused state is invisible (hover/touch freezes silently) |
| 2 | Match System / Real World | 3 | Roofer vocabulary strong; eyebrow says "home-service businesses" while every example is roofing |
| 3 | User Control and Freedom | 3 | Replay, skip link, cancel anytime; no deliberate pause; Calendly opens a new tab unannounced |
| 4 | Consistency and Standards | 3 | Typed arrows break the no-typed-glyph rule; Replay icon reads as "C"; radii 4/8/12/16 off the scale |
| 5 | Error Prevention | 3 | Inline validation; Company required; phone placeholder reads like a value |
| 6 | Recognition Rather Than Recall | 3 | "Busy days" nav label opaque on the homepage |
| 7 | Flexibility and Efficiency | n/a | One-visit marketing page |
| 8 | Aesthetic and Minimalist Design | 3 | Clean; dead space in hero top-right, half-empty end cards, empty blue under "covers all five" |
| 9 | Error Recovery | 3 | Plain errors and "Wrong number? Change it" |
| 10 | Help and Documentation | n/a | Kept n/a as in earlier runs (reviewer scored 3: good FAQ, missing recording consent and minute allowance) |
| **Total** | | **24/32** | **Good (75%)** |

## Design Specificity Verdict
Specific in the cards, generic in the frame. The route, busy-day queue, hail slot and Lead Recovery Report speak roofer; the shell (tight grotesk on white, faint grid, yellow pill, repeated split header, blue band, 3-step how-it-works, one-price, FAQ, giant footer wordmark) is the current SaaS template. The Site Plan north star shows only as a faint grid.

Detector: 17 CLI findings per page (cramped-padding 6, design-system-radius 4, design-system-color 2, dark-glow 2, clipped-overflow 1, nested-cards 1, codex-grid-background 1); browser 21 desktop / 20 phone (bounce-easing x15 from the --spring token, heading-rhythm x4, dark-glow, grid background, oversized h1 at 1440). False positives: heading-rhythm (space comes from previous section padding), navy dark-glow (normal elevation shadow), cramped-padding on section.dark and .faq-col, body overflow-x guard. Real: blue zero-offset halo on .signal/.mtip, off-scale radii, --spring overshoot, off-token #17244B and #2B3B68. Grid background is the user's chosen plan grid (deliberate).

## Priority Issues
1. [P1] Hero route states look broken: empty dashed boxes before play (the only product on the phone first screen), silent hover/touch pause, a swipe that starts on the route pauses it, end cards about half empty on desktop. Fix: ghosted real content for future steps, drop touch toggle or show a paused chip, size cards to content. /impeccable harden
2. [P1] Trust valley at the decision: "What does it sound like?" deferred to the demo; nobody behind the product; first company detail is the footer address. Fix: labelled example audio clip; short "who you'll talk to" block. /impeccable shape
3. [P1, deliberate] Homepage identity split: home-service framing with all-roofing examples; "More trades coming soon" is a dead end. User chose this positioning; at most add a waitlist path. /impeccable clarify
4. [P2] Desktop hero composition: CTA stranded right under an empty grid quadrant. Fix: CTA under the lead with a "$499 a month, no contract" microline. /impeccable layout
5. [P2] Phone path: price ~13 screens down, sticky bar only offers Calendly, report chart scrolls sideways and clips the storm peak, two yellow demo buttons together at pricing. /impeccable adapt

## Persona Red Flags
Jordan: home-service vs roofing; "Busy days" label; unexplained call-minute allowance.
Riley: allowance has no number or overage; setup fee amount unstated; recording consent not addressed; hover/touch freezes hero; Company required.
Casey: first screen is headline plus skeleton boxes; swipe can pause demo; ~17 screens; sideways chart; two identical yellow buttons.
Roofing owner on phone between jobs: lands on "home-service"; price far down; muted 13-15px captions wash out in sun; "call me back" is at the bottom while the sticky bar opens a calendar; "We'll call you soon" has no time window.

## Minor Observations
Replay icon reads as C; text peeks above the floating phone header; "Example report" pill wraps on phone; no CTA in the blue band after its strongest line; split-header leads sit at inconsistent offsets; orphan "sent." in closing card; busy-day FAQ repeats section copy; DESIGN.md still describes the pinned scroll scene; blue halo on .signal/.mtip breaks the no-glow rule; --spring overshoot used 15 times.

## Questions to Consider
- Who is `/` meant to convert, and what does a plumber do on it today?
- Why make a roofer book a meeting to hear the product when a labelled 30-second clip could answer it?
- Should the Site Plan drawing language carry the whole page, or give way to something with weather and material in it?
