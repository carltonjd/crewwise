---
target: Crewwise full home page (H4 hero) and inner-page ban sweep
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:7d94156a176204fcf13288d702e096dae0d52a0b7b968573ec2767d2337fb732"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T14-12-36Z
slug: src-pages-index-astro
---
Method: dual-agent (A: isolated design-review sub-agent · B: isolated detector sub-agent; A finished before B's output was read). The parent also ran its own checks: DPR 2 screenshots at 5 viewports, the ban-list DOM sweep across 8 URLs, the form states and reduced motion.

# Full home page critique (src/pages/index.astro), H4 hero

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | The demo tabs, timeline, accordion and header states all work. The hero tap ripple is invisible (`.pc` undefined), and the mobile hero does not play in the first viewport. |
| 2 | Match System / Real World | 3 | The "customer's day" copy is excellent. The order runs solution, then problem (SlipAway), then solution again. |
| 3 | User Control and Freedom | 3 | Tabs, Replay, the accordion and Esc on the menu all work. |
| 4 | Consistency and Standards | 3 | "Replay example call" appears twice (Hero and Demo). The "Example call" tag sits next to Replay and reads as a link. |
| 5 | Error Prevention | 3 | Fine. |
| 6 | Recognition Rather Than Recall | 3 | Fine. |
| 7 | Flexibility and Efficiency | n/a | Persuade. |
| 8 | Aesthetic and Minimalist Design | 2 | Three phones (Hero, Demo, FinalCta) and four check-slips. The FinalCta repeats the hero's copy-left, device-right split. The hero has a dead lower-left quadrant. The heading blocks in Pillars, HowItWorks and WhoFor leave the right half empty. |
| 9 | Error Recovery | 4 | The audit form summary links to each field, the fixes are specific, and a network error keeps the input. |
| 10 | Help and Documentation | n/a | Persuade. |
| **Total** | | **24/32 (75%)** | **Good** |

- **Clarity 7/10, Premium 7/10, Wow 6/10.**
- **Verdict:** ship-ready on design once the two P1s are fixed. There is no P0. Launch is still gated on the owner's legal items.
- **Trend:** 26 to 24. The drop comes from H8, because the new hero's empty quadrant adds to the existing below-fold repetition. Reviewer variance is about ±1.

## Ban-list audit (8 URLs, DOM sweep and screenshots)

**VIOLATION:**
- **Split hero.** H4 is still a split at desktop. The headline ends 12-38px left of the phone box, and the copy sits off the floor. This is owner-fixed, so it is logged as a conflict.
- **Motion craft.** The hero `.pc` origin bug.

**BORDERLINE:**
- **Persuade action.** The CTA is a button, not the working form. This is the recorded exception.
- **Equal tiles.** Pillars has two equal plate tiles, and WhoFor has two equal cards.
- **Metric stack.** The /roofing/ storm report has a 180/40/24/30/12 metric column (roofing.astro:174).
- **Label above the title.** The /roofing/ head slip puts "Monday 9:00 AM" above "Inspection booked" (roofing.astro:55), and the stamp repeats "Inspection booked".
- **Placeholder screens.** The FinalCta and /roofing/ close phones, and the Pillars website plate, use skeleton bars standing in for content.
- **Small targets.** Several targets are under 44px: email links are 22-25px, the free-audit "privacy policy" link is 20px (inline), and the inner logo is 36px.
- **Sheet #143a8a.** Craft-floor passes it, but it conflicts with the brief's palette.

**PASS:**
- No eyebrows. The DOM sweep found 0 on all 8 URLs.
- Section numbers are real sequences (route 1-4, legal clauses).
- No gradient text, no glass, and no side stripes (the detector's side-tab hit is the 3px top rule).
- No hard offset shadows, no mono costume, and no glyph or emoji icons (all checks and warnings are SVG).
- Hanken is self-hosted. Tracking is at least -0.04em everywhere, and display text is at most 92px.
- Light mode, chosen from the use scene.
- One H1 per page, and no horizontal overflow at 1440 or 390.
- Copy checks:
  - no en or em dashes, arrows or buzzwords;
  - no clinic words and no Octalogic;
  - "$299" is the only price;
  - the only middot is the fixed footer legal line.
- The 404 returns a 404 status, with noindex and no canonical.

## Priority issues

- **[P1] The hero tap beat is broken.** Hero.astro `.pc` has no rule. Add `.pc { transform-box: fill-box; transform-origin: center; }`.
- **[P1] The mobile hero does not play in the first viewport.** The threshold is 0.4 (Hero.astro:1108). Fix: lower it to 0.15 and tighten `.art` and `--pw`.
- **[P2] The hero dead quadrant, the tangency, the crossing lips and the mobile sheet seam.** All are in Hero.astro.
- **[P2] Repetition below the fold.**
  - FinalCta.astro repeats the hero split and puts a third phone on a placeholder screen.
  - Fix: build the close from the audit deliverable itself, for example a paper report showing "what we found".
- **[P2] DESIGN.md and the surface brief are out of date.** Regenerate both for H4, and decide on the #143a8a token.
- **[P3] Polish.**
  - Rename one "Replay example call" (Hero or Demo.astro).
  - Make the Demo's "Example call" tag look like a tag.
  - Raise the inactive SlipAway headlines from opacity .6 to about .75.
  - Bring email link targets up to 44px.
  - Fix the /roofing/ slip duplicate.
  - Resolve the 56 font-size, 15 radius and 1 colour token drifts.

## Inner pages

- **/pricing/:** the price plate is now in the fold at 1440 (fixed). The blue band is still empty on its right half.
- **/free-audit/:** the error, network and success states are all strong, and the stamp is gone (fixed). The empty right half of the head band remains.
- **/roofing/:** the proof slip is in the head band and the FAQ is down to 6 (fixed). The slip's label above the title, the duplicate, the metric column and the close that copies the home close remain.
- **/privacy/, /terms/, /refunds/:** clean, one H1, a good measure. The "Last updated" date is October 6, 2026 (owner item).
- **404:** correct status and robots, and it offers recovery (the audit and home).

## Detector

- **Source:** 72 unique advisories (56 font-size, 15 radius, 1 colour). Exit 0. All are token drift.
- **Browser findings:**
  - home at 1440: 11;
  - home at 390: 8;
  - pricing: 1 (cramped-padding on #plans; intentional);
  - roofing: 1 (dark-glow on `.report`; navy paper shadow, so a false positive);
  - free-audit, privacy and 404: 0.
- **Home false positives:**
  - buried-raster (the logo crossfade);
  - low-contrast (white numerals on navy markers);
  - side-tab (top rule);
  - shape-assembled (the brand SVG);
  - clipped-overflow (hero clip).
- **Home true positive (minor):** tight-leading on `p.moment` (1.25 at 36px).

## Persona red flags

- **Casey:** the mobile hero is static until scrolled. The CTA is in the upper half. Email targets are 22px.
- **Riley:** Replay is inert before play. The "Example call" tag looks clickable. "Two business days" is unconfirmed.
- **Jordan:** "Hear it answer a call" leads to a transcript.
- **Plumber:** the hero proof is law only, and the trade appears one screen down.
- **Law partner:** there is no team or people shown (Octalogic is hidden), and the price only appears mid-page.
