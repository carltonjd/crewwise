---
target: Crewwise home page full review v3
total_score: 25
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 1
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:169a83008995d4f66ad420ab71cf09b539d535d3fcb37c3be04af9e8b9e0db96"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T09-58-04Z
slug: src-pages-index-astro
---
DEGRADED (partial): Assessment A ran in the parent context because the caller required first-hand verification. B ran as an isolated detector/browser sub-agent, and its report arrived before the synthesis of A was finished.

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Demo no longer auto-switches. SlipAway progress is shown only by dimming (0.6). |
| 2 | Match System / Real World | 3 | Hero phone says "Handled by AI front desk" and "Answered by AI front desk", missing "the". |
| 3 | User Control and Freedom | 3 | Replay, tabs, Esc and the focus trap work. The pinned SlipAway is still about 2,700px. |
| 4 | Consistency and Standards | 3 | Up from 2. The arrow is gone, the mobile CTA is in and WhoFor is fixed. /roofing/ is still the older soft-card world. |
| 5 | Error Prevention | 3 | All anchors resolve, and the form marks required and optional fields. |
| 6 | Recognition Rather Than Recall | 3 | SlipAway close restates times first shown about 2,000px above. |
| 7 | Flexibility and Efficiency | n/a | Single-action marketing page. |
| 8 | Aesthetic and Minimalist Design | 3 | Cleaner. SlipAway is long and the FAQ cards are generic. |
| 9 | Error Recovery | 3 | No forms on home. With no JS or with reduced motion, the final states render. |
| 10 | Help and Documentation | n/a | Marketing surface. |
| **Total** | | **25/32 (78%)** | **Good** |

Clarity 8/10, Premium 8/10, Wow 7/10.

Verdict:
- Home has no craft-floor ban violations left.
- The site is not ship-ready. Open items: the P1 privacy mismatch, the P2 roofing world split, and the FINISH step (DESIGN.md and the finish review).

## Ban-list audit (craft floor), all 8 URLs

**VIOLATION:** none.

**BORDERLINE:**
- **Split hero** (mode-persuade Comps): G2a is owner-fixed. This is a conflict, not a fix.
- **Same-size cards:**
  - Pillars has two equal plate tiles.
  - Pricing has three soft cards.
  - Roofing has five identical rounded leak rows and an 11-card FAQ.
  - The home FAQ is soft rounded cards.
- **Hero-metric look:**
  - Roofing storm stats 180, 40, 24, 30 and 12 (labelled illustrative).
  - Roofing "0:00 / +1 min / +2 weeks" tiles.
  - The 404 card: X disc, a big "404" and a small label.
- **Labels above content:**
  - The "Homeowner calls" label above the roofing rows.
  - The "New enquiry" micro-labels in the SlipAway cells.
- **Motion:** several distinct authored effects: hero, demo playback, SlipAway pin, the route line and the link-line. There is no uniform fade.
- **Green check too early:** the FinalCta "Your free audit" slip shows a green check before anything has been submitted.

**PASS:**
- **Eyebrows:**
  - HowItWorks .when and SlipAway .step-time now sit below their text.
  - The free-audit aside is now sentences.
- **Numbering:** the menu numbers are gone. The 1-4 route and pricing 1-3 are real sequences.
- **Shadows:** no zero-blur offsets in src, dist or computed styles.
- **Tracking:** the computed minimum is -0.04em on every page.
- **Other surface bans:** no gradient text, glass, side stripes, mono costume, glyph icons (no arrow, and the 404 X is SVG) or geometric masks.
- **Fonts and browser surfaces:** Hanken is self-hosted. Selection and caret are themed.
- **Page basics:**
  - One H1 per page.
  - No overflow at 360 or 1440.
  - No en or em dashes.
  - The 404 URL returns 404.

## Brief conflicts
- **Tracking:** surface brief line 18 and PRODUCT.md line 62 say "tight tracking". The build sits on the -0.04em floor. Reword both to "never tighter than -0.04em".
- **Eyebrows wording:** PRODUCT.md line 65 is a double negative ("Avoid: ... no eyebrow labels"). Reword it as a plain ban.
- **World:** PRODUCT.md line 63 says "not a metaphor world", but surface brief lines 16-18 describe the Saul Bass cut-paper world. The owner decides.
- **Price placement:** PRODUCT.md line 63 wants the price near the hero. The first price is in section 3. This is a gap between brief and build.
- **Middle dot:** PRODUCT.md line 66 bans middle-dot meta strings, but the fixed footer legal line uses one.
- **Split hero:** surface brief lines 22 and 24 (the G2a split hero) conflict with mode-persuade Comps. Owner-fixed.
- **Finish:** surface brief line 26 FINISH is still outstanding.

## Priority issues
- **[P1] Privacy copy:** /privacy/ claims the form collects "city and state, and a rough number of missed calls". The form does not ask for either. Rewrite it to match the real fields.
- **[P2] Roofing world:** /roofing/ is still the old soft-card world. Bring it into the cut-paper world.
- **[P2] SlipAway length:** SlipAway is about 2,700px on desktop. Cut it to three moments, or unpin it under 64rem.
- **[P2] Hero phone copy:** Hero.astro:320 and 330 are missing "the".
- **[P3] Polish:**
  - FinalCta .reassure is set heavier than the lead.
  - The green check shows before submission.
  - The "riley" class name and PRICE_RILEY leak into the DOM.

## Persona red flags
- **Jordan:** "AI front desk" is never defined in one plain line.
- **Riley:** the privacy policy promises data the form never collects.
- **Casey:** the bar CTA is fixed. The Demo phone is still tall at 390.
- **Plumber:** the hero proof is a law firm, and the price only appears in section 3.

## Detector
- **Source scan:** exit 0, with 76 advisories. These are DESIGN.md ramp checks, and DESIGN.md is being regenerated.
- **dist scan:** 194 findings, mostly false positives:
  - cramped-padding: 87.
  - Hover low-contrast: overridden by the scoped white rules and the :where(navy/blue) a:hover inherit rule.
  - White-on-white: on hidden layers.
  - dark-glow: this is the paper shadow.
  - side-tab: these are the menu chevron and the WhoFor top rule.
  - buried-raster: the logo crossfade.
  - Real or functional findings:
    - layout-transition: 1, real, needs checking.
    - pulsing-dot: the functional typing indicator.
- **Browser:**
  - Home: 27 findings at 1440 and 24 at 390. Mostly the 16 SVG text-occlusion false positives.
  - Roofing: 4 dark-glow findings.
  - Every other page is clean.

## Questions
1. Should /roofing/ be rebuilt now or left until Phase 2?
2. Should SlipAway be cut to three moments, or unpinned on phones?
3. Should "From $299/month" go into the hero note?
