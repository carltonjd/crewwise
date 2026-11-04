---
target: Crewwise final site review (H3 hero)
total_score: 26
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 0
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:6bc77f2bec61fae1637e5a845822c380b784df264d7c5b172449acc7bc29e5c3"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T11-52-46Z
slug: src-pages-index-astro
---
DEGRADED (partial): Assessment A ran in the parent context because the caller required first-hand screenshot review. B (detector and browser overlay) ran as an isolated sub-agent, and its report arrived before A's synthesis was finished.

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | The form states are excellent. The Demo phone and the "What the AI front desk did" panel enter as about 1,100px of empty panels at 390. |
| 2 | Match System / Real World | 4 | "the" is fixed, the copy uses US spelling, the absolutes are softened, and "once texting is on" is qualified. |
| 3 | User Control and Freedom | 3 | Replay, tabs and Esc work. The menu closes. /roofing/ is about 9,300px at 390. |
| 4 | Consistency and Standards | 3 | /roofing/ is now in the same world. The copy-left, device-right skeleton repeats in the hero, the FinalCta and the closes on inner pages. "About two weeks" sits next to "7 to 10 days" and "1 to 3 weeks" for texting. |
| 5 | Error Prevention | 3 | Required and optional fields are flagged. "I don't have one" disables the website field. The phone number is formatted on blur. |
| 6 | Recognition Rather Than Recall | 3 | SlipAway is cut to 3 moments. The close restates the times. |
| 7 | Flexibility and Efficiency | n/a | Single-action marketing surface. |
| 8 | Aesthetic and Minimalist Design | 3 | The ruled rows clean up the FAQ and pricing. The /pricing/ and /roofing/ heroes leave half of the blue band empty. |
| 9 | Error Recovery | 4 | The summary is linked to each field, the fixes are specific (for example "That number has 2 digits..."), and the network error keeps the input and offers email. |
| 10 | Help and Documentation | n/a | Marketing surface. |
| **Total** | | **26/32 (81%)** | **Good** |

Clarity 8/10, Premium 8/10, Wow 7/10 (the hero alone is 8).

**Verdict:**
- **Home:** ship-ready on design. There are no craft-floor violations.
- **Site:** ship-ready on design (no P0 or P1 design issues). Launch is still gated on the owner's legal items.

## Ban-list audit (all 8 URLs)

**VIOLATION:** none.

**BORDERLINE:**
- **Split hero:** H3 is still a split hero under mode-persuade Comps. The copy is in the left track and the phone is in the right track (Hero.astro:494, `1fr | --pw | 0.6fr`). It is a stronger instance (life-size, bleeds off the fold, no badge row), but it is the same skeleton. It is owner-fixed, so this is a conflict, not a fix. FinalCta and the inner-page closes repeat the skeleton.
- **Persuade action:** the hero CTA links to /free-audit/ rather than putting the action in its working form.
- **Same-size tiles:** Pillars has two equal plate tiles (websites and automation).
- **Metric stack:** the /roofing/ storm report has a 180/40/24/30/12 number column (labelled illustrative).
- **Label above text:** the green "Audit request received" stamp sits above the success heading text.

**PASS:**
- **Eyebrows:** none. The time labels sit below their text.
- **Numbers:** the only numbers are real sequences (the route 1-4 and the automation 1-3).
- **Surfaces:**
  - No gradient text or radio gradient.
  - No glass or backdrop-filter.
  - No side stripes. The detector's side-tab hits are the WhoFor top rule and the menu chevron.
  - No hard offset shadows, no mono costume and no glyph or emoji icons (the FAQ + is SVG).
- **Fonts:** Hanken is self-hosted. Computed tracking is at least -0.04em on every page. Display is at most 88px.
- **Browser surfaces:** selection, caret, scrollbar, underline-offset, tabular-nums, balance and pretty are all themed.
- **Mode:** light mode, chosen from the use scene (daylight on a phone).
- **Page basics:**
  - One H1 per page.
  - No horizontal overflow at 360, 390, 1280 or 1440.
  - No en or em dashes, no arrows and no unresolved {{placeholders}}.
  - No clinic words, no Octalogic, and only the "$299" price.
  - The 404 returns 404 with noindex and no canonical.

## Conflicts

**Surface brief:**
- FIRST VIEWPORT and FORM still describe G2a, a "tilted phone, left copy, right phone" split hero. That is out of date (the hero is now H3) and conflicts with mode-persuade.
- It also calls for "faint paper grain", but Hero.astro:7 says no grain.

**PRODUCT.md:**
- "Not a metaphor world" contradicts the cut-paper world in the brief and in DESIGN.md.
- The /free-audit link as the single action conflicts with persuade's "action in working form".
- The "two business days" turnaround is listed as pending, but the site states it as fact.
- /refunds/ is missing from the list of Phase 1 pages.

**DESIGN.md is out of date:**
- **Hero layout:** it describes a "two-column grid, copy at 40%". The build uses three tracks: copy, phone and slip.
- **Hero depiction:** it describes a tilted phone with the slip "in front" and a touch dot. The build has a near-life-size phone with the slip hanging off its right edge.
- **Room index:** it describes a room index from 80rem. No page passes rooms (Base.astro:53), so RoomIndex is dead.
- **FAQ:** it describes soft 16px cards with an inset ring. The FAQs are now ruled rows (computed radius 0, transparent).
- **Missing patterns:** it does not document the ruled-row pattern or the navy pricing lead plate.
- **Tokens:** the font-size and radius ramp is incomplete (73 detector advisories, for example 0.9375rem, 0.875rem and the Demo radii).
- **Nothing banned:** DESIGN.md itself contains nothing impeccable bans.

## Priority issues

**P0, P1 (design):** none.

**[P1, owner-only] Legal and content blockers:**
- Recording-consent notice.
- SMS consent wording.
- Legal "updated" dates (2026-10-06 while the copy changed in 2026-11).
- The Calendly event is named "demo".
- "Hear it answer a call" points to a text transcript.

**[P2] Price below the fold on /pricing/:** at 1440x900 the blue band (pricing.astro head) is about 530px with the right half empty, so the price is below the fold. Pull the navy lead plate up into the band, or shorten the band and put "From $299/month" in it.

**[P2] Demo is empty on entry:** the Demo phone and the timeline (Demo.astro) reserve their full height and are empty when they enter (about 1,100px at 390). Render the first 2-3 events at rest, or cap the height on phones.

**[P2] DESIGN.md and the surface brief:** regenerate them for H3, ruled rows, the pricing plate and the full token ramp. Delete RoomIndex or the DESIGN.md mention of it.

**[P2] /roofing/:**
- The hero (roofing.astro hero band) has no proof in the first viewport. Bring the "One call" example slip into the band.
- At 390 the page is about 9,300px. Cut the FAQ from 11 to about 6.

**[P3] Polish:**
- **Tap targets:** these links are 20-25px tall, against the 44px claim:
  - Pillars `.more` links (171x20 and 218x20).
  - roofing "See an example" (133x25).
  - The inner-page logo link (130x30 at 390).
- **Success state:** drop the green stamp above the success text, or move it below.
- **Repeated layout:** vary the FinalCta composition so it does not echo the hero split.
- **Route heading:** "about two weeks" versus 7-10 days plus 1-3 weeks for texting. Qualify it or align it.
- **HowItWorks:** the heading is centred while every other band is left-aligned.

## Detector

**Source:** exit 0. 73 advisories (58 font-size, 15 radius) and 8 more from global.css. All are token drift.

**Browser:**
- Home: 25 at 1440 and 14 at 390.
- Roofing: 1 (dark-glow on `.report`).
- Pricing, free-audit, privacy and 404: 0.

**False positives:**
- text-occlusion: 15 SVG phone texts under `svg.fg`.
- buried-raster: the navy logo crossfade.
- low-contrast on the HowItWorks `<b>` numerals: they are white on a navy shape.
- side-tab: the 3px top rule and the chevron.
- tight-leading: `p.moment`, which is display-size.
- dark-glow: the paper shadow on navy (harmless).
- oversized-h1: 78px, within the 6rem cap, and owner-fixed copy.

## Persona red flags

- **Jordan:** fine. The AI front desk is defined in the Demo lead.
- **Riley:** the "two business days" promise is unconfirmed. A legal date predates the copy changes.
- **Casey:** the Demo has empty panels on scroll. The Pillars links are 20px targets.
- **Plumber:** the hero proof is a law firm. The price first appears in section 3 (a deliberate choice).
