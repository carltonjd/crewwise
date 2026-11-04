---
target: full home page
total_score: 22
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 6
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:b601560e79a53824366709e6fd110246c64e56257ed953de8901a873a3a8f3ba"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T07-55-26Z
slug: src-pages-index-astro
---
Method: dual-agent (A: design review sub-agent · B: detector sub-agent)

# Critique: Crewwise home page (src/pages/index.astro), full page

## Design Health Score
| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Demo play/Replay and the pinned day card respond well. On mobile the demo timeline sits below a ~1,300px transcript. |
| 2 | Match system / real world | 3 | Speaks the customer's day. Minor jargon ("No-cool call"). |
| 3 | User control and freedom | 3 | SlipAway forces ~3,400px of scroll with no skip. |
| 4 | Consistency and standards | 2 | Two visual systems: cut-paper above, white card plus blue shadow below. Pillars .tile-meta looks like links. "Free audit" and "free 30-minute call" read as two offers. |
| 5 | Error prevention | 3 | Fake-link affordance invites dead taps. |
| 6 | Recognition rather than recall | 3 | SlipAway closing refers to times several screens back. |
| 7 | Flexibility and efficiency | n/a | Single-path Persuade page. |
| 8 | Aesthetic and minimalist design | 2 | Heavy repetition, one heading rhythm, ~13,200px on a 390 phone. |
| 9 | Error recovery | 3 | No forms. FAQ email fallback present. |
| 10 | Help and documentation | n/a | Marketing surface. |
| **Total** | | **22/32 (69%)** | **Acceptable, just under Good** |

Clarity 8/10. Premium 6/10 (hero 9, lower page 5 to 6). Wow 5/10. Ship-ready: no.

## Design Specificity Verdict
LLM: The page belongs to Crewwise down to the Demo. From Pillars on, it is a well-made generic AI-receptionist template: white rounded cards with an 8px blue offset shadow, a 4-step stepper, two audience cards, a FAQ and a CTA band with one blank tilted slab. The brief's STORY says the cut-paper language carries "through the demo, services and close". It stops at the demo.

Deterministic scan: CLI found 58 advisories (41 design-system-font-size, 17 design-system-radius). All rely on the outdated DESIGN.md, so they are noise. Browser detector (headless, no user-visible overlay): 18 findings at 1440 and 17 at 390. text-occlusion (15/14) is on the hero phone's stacked SVG scene layers, which is a false positive. tight-leading (3) comes from SlipAway p.moment at 36px with line-height 1.2. This is real but minor.

## Repetition count
- 13 timestamped rows/cards in 5 of 9 sections.
- About 10 "booked" confirmations with 6 different booking times.
- 7 "Example" chips.
- 4 phone mockups.
- "Flagged urgent" x3. "No legal advice" x3. "2:14 PM on a job" in Demo and SlipAway.
- SlipAway 7:30 PM "Web form, new client" is followed in the next section by AfterHours 7:32 PM "New client enquiry".
- Every H2 is 68px/820, left-aligned, with 134px padding, in 8 sections.

## Per-section verdict
- Hero: Polished and owns the world. Scored lightly. Fine.
- Demo: The strongest lower section and the real proof. It is an inset rounded panel under a big white heading block, not a full-bleed continuation of the hero. On mobile it is ~1,845px tall.
- Pillars: Clear message and the only price. It is a bento of shadow cards, with crude mini-phones and blue .tile-meta lines that look like links but are not.
- SlipAway: The best idea below the demo. Problems:
  - It is ~3,400px long with empty columns.
  - The time is said twice per step.
  - On mobile the pinned card clips the step's time label.
  - Row 4's "kept" has no marker.
- AfterHours: A good band change, but it reuses the timestamp-row device and nearly duplicates the 7:30 PM enquiry. There is no cut-paper on navy.
- HowItWorks: A generic stepper. The connector line dangles past step 4. Step 3's "1 to 3 weeks" pulls against "about two weeks". There is no CTA on the audit step.
- WhoFor: Two cards of unequal fill. It is the third retelling of the demo examples, and the blue H3s act as eyebrows.
- Faq: Clean and the right density. The left column is mostly empty.
- FinalCta: Strong headline, but the CTA is detached in a middle column and the only art is an empty slab. The page ends weaker than it starts.

## What's working
1. Demo tabs: one home-service call and one law-firm call, a live transcript and a timestamped "what it did" log.
2. SlipAway's pinned lost-to-kept day card is the right "first few minutes" story.
3. Voice discipline holds: plain sentences, labelled examples, one price, no banned constructions.

## Priority issues
1. [P1] The lower page leaves the hero's world. Pillars, AfterHours, WhoFor and FinalCta all use white rounded card plus blue shadow (global.css .card / --shadow-object). Fix: carry hero vocabulary down the page. Use navy cut-paper shapes with hard #1749B0 shadows on blue or navy grounds, use white slips only as payoff objects, and use typographic layouts where a card is not an object. Command: /impeccable bolder, then /impeccable layout.
2. [P1] The same story is told five times. Merge AfterHours into the SlipAway day or give it a different device (a navy cut-paper lock screen with stacked notifications). Drop or replace the WhoFor example slips. Command: /impeccable distill.
3. [P1] Mobile length (~13,200px) and SlipAway. SlipAway.astro .step min-height 62vh/55vh gives ~3,400px; reduce to about 40vh/35vh. The mobile .pin covers the step time label (m390-slip-step2.png): add an opaque backing with a bottom fade, or pad the step text below the card. Drop the duplicate time eyebrow. Command: /impeccable adapt.
4. [P1] CTA path gap. There is no audit action between the hero and FinalCta. Add "Get my free audit" to HowItWorks step 1 and after the Demo. Make Pillars .tile-meta real links to /free-audit/ or mute them. Command: /impeccable layout.
5. [P2] The close underdelivers. In FinalCta.astro, put the CTA under the heading, replace the empty .slab with a hero callback (phone at rest plus white slip), and enlarge the reassurance line. Command: /impeccable delight.

## Full fix list
P1
- Pillars, AfterHours, WhoFor .card plus global.css --shadow-object: one repeated card device. Bring in cut-paper vocabulary.
- index.astro AfterHours 7:32 PM entry against the SlipAway 7:30 PM moment: merge or re-device. Copy change needs owner approval.
- SlipAway.astro .step min-height: reduce, and enlarge the desktop step type.
- SlipAway.astro mobile .pin clips .step-time: add an opaque pin backing, or padding-top on steps.
- HowItWorks.astro step 1: add a primary "Get my free audit".
- Pillars.astro .tile-meta: make it a link or mute it. Aligning "free audit" with "30-minute call" needs owner approval.

P2
- Demo.astro .stage: make it a full-bleed blue continuation of the hero.
- Demo mobile: transcript scrolls inside the phone, or timeline interleaved with the lines.
- Pillars.astro .mini-phone x2: replace with a cut-paper browser or search result. Keep the PO/invoice match.
- HowItWorks.astro .stops::before: end the line at the last dot.
- HowItWorks step 3: carrier detail goes to an FAQ (owner approval). The "About 7 to 10 days" label duplicates the body text.
- WhoFor.astro: make it a two-column typographic split with no cards.
- FinalCta.astro .foot and .slab, per issue 5.
- All bands: vary the H2 scale and alignment.

P3
- SlipAway row 4 "kept": add a neutral done mark.
- WhoFor H3s: set them in navy, not blue.
- "No-cool call, booked" is jargon (owner approval).
- SlipAway p.moment line-height: raise to 1.25 to 1.3 on phone.
- Demo desktop: the timeline card hangs short beside the phone.

## Persona red flags
- Jordan: "Free audit" and "free 30-minute call" look like two products, and the blue Pillars lines do nothing when tapped.
- Riley: 6 different booking times and the 7:30/7:32 duplicate read as filler. "Two weeks" against "1 to 3 weeks" reads like small print.
- Casey: 13k px of page, a 3,400px pinned story that clips text, and the nearest body CTA ~11,000px down.
- Law-firm partner: SlipAway is all trades, and the bubbly cards feel consumer-grade.
- Plumber owner: reads the same booked story five times.

## Questions to consider
1. What does each of SlipAway, AfterHours and WhoFor prove that the demo has not?
2. What would Pillars look like as three cut-paper objects without cards?
3. Should the last image be the phone at rest with a slip reading "Your free audit, booked"?
