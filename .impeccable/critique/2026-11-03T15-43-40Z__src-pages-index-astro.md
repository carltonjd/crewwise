---
target: Crewwise full home page round 6 (premium pass)
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 4
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
target_fingerprint: "sha256:7d94156a176204fcf13288d702e096dae0d52a0b7b968573ec2767d2337fb732"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\pages\\index.astro"
timestamp: 2026-11-03T15-43-40Z
slug: src-pages-index-astro
---
Method: dual-agent (A: isolated design-review sub-agent · B: isolated detector sub-agent; A finished before B's output was read). The parent added its own evidence:
- DPR 2 captures at 1440, 1280, 390 and 360;
- a 14-frame hero entrance timeline;
- SlipAway scrub frames at 0, 25, 50, 75 and 100% in Chromium, Firefox (rAF fallback, `story is-scrub`) and WebKit (`story is-native`);
- header hide and show states;
- micro-interaction states;
- no-JS, reduced motion and print emulation;
- form states and inner pages at 1440 and 390.

# Full home page critique (src/pages/index.astro), round 6 after the "studio-level" premium pass

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | The tap ripple is fixed. The mobile story plays in the first screen. Scroll-spy, tabs and FAQ all give feedback. The new regression is that 15 of 17 `[data-enter]` elements compute to opacity 0 until scrolled, in print as well. |
| 2 | Match System / Real World | 3 | The "customer's day" copy is strong. SlipAway puts the "After you clock off" heading before the 6:40 and 7:30 moments, so the narrative order is muddled. |
| 3 | User Control and Freedom | 3 | Tabs, Replay, the accordion and the menu all work. The header returns on scroll up. |
| 4 | Consistency and Standards | 3 | Two Replay controls (hero and Demo). The inner pages drop the cut-paper world. The press colour #8c3105 is off-token. |
| 5 | Error Prevention | 3 | Fine. |
| 6 | Recognition Rather Than Recall | 3 | Fine. |
| 7 | Flexibility and Efficiency | n/a | Persuade surface. |
| 8 | Aesthetic and Minimalist Design | 2 | The page is 9,694px on desktop and 11,637px on mobile. There are 6+ "Get my free audit" CTAs. SlipAway repeats each moment twice (left narrative plus ledger). The hero's lower-left floor holds only the caption row. FinalCta has about 250px of empty blue under the sheet. |
| 9 | Error Recovery | 4 | The audit form's summary links to each field, gives specific fixes, and shows inline messages with icons (verified with an empty submit at 1440 and 390). |
| 10 | Help and Documentation | n/a | Persuade surface. |
| **Total** | | **24/32 (75%)** | **Good** |

- **Clarity 8/10. Premium 7/10:** hero 8, below the fold 6.5. **Wow 6/10.**
- **Trend:** 24 to 24. Craft went up (the illustration set, the motion tokens, the fixed hero beats and the scrubbed story). The heuristics stayed flat: the length, the repetition and the dead zones are unchanged, and the new view-timeline entrances hide content by default.

## Design specificity verdict

- **LLM:** the hero (Harbor & Lane Law phone, a tap, the AI front desk answering, the booked slip), the Demo transcript with its event log, and the SlipAway lost/kept ledger are authored for this product. Below the hero the skeleton is the category stack: demo, 3 services, how-it-works, who-for, FAQ, CTA. The cut-paper world appears in plates and the skyline, not in the page structure. The inner pages are a blue banner with an empty right half.
- **Detector:** source has 63 findings, all `design-system-*` token drift against a DESIGN.md being regenerated: 43 font sizes, 18 radii, and 2 uses of the undocumented #8c3105 (Header.astro:327, FinalCta.astro:193). `dist/` has 141 findings, mostly jsdom noise (81 cramped-padding, 11 white-on-white on transparent containers). The browser overlay found 6 on `/`: tight line height x2, a clipped positioned child, side-tab x2 (`.aud::before`) and an organic clip-path. Inner pages had 1 or 2 each.
- **False positives:** organic-clip-path (the deliberate nicked corner), the 2.4:1 hover (overridden by the `:where(.band-navy, …) a:hover { color: inherit }` rule in global.css), pulsing-dot (a functional typing indicator), and dark-glow on roofing (the paper shadow has blur).

## Ban-list audit (/, /pricing/, /free-audit/, /roofing/, /privacy/, /terms/, /refunds/, 404)

**VIOLATION**
- **Content visible by default (craft-floor Motion, animate.md):** the `[data-enter]` keyframes start at `opacity: 0` with `animation-fill-mode: both` (global.css:483-545).
  - Unscrolled, 15 of 17 elements compute to opacity 0. Print emulation gives the same result, because the `@media print` block (global.css:589) does not reset them.
  - The full-page capture shows a blank Demo phone and log, plates, route markers, audience plates, FAQ rows and the audit sheet.
  - The hero CTA and sub-line are also invisible for roughly the first 0.7 to 1.0s.
  - Fix:
    - keep opacity out of the keyframes for text-bearing elements (FAQ `details`, the Demo `.phone` and `.log`, the close sheet), so they are transform-only from a visible state;
    - add `@media print { [data-enter], .aud::before { animation: none !important; } }`;
    - start the hero sub-line and CTA visible at t=0, and choreograph only the headline and the phone.
- **One authored moment (craft-floor; overdrive's "never layer competing moments"):** the page now has about 8 motion systems. They are:
  - the hero entrance and story;
  - the Demo playback;
  - the SlipAway scrub;
  - the close-sheet slide with ticks;
  - the header hide/show with scroll-spy;
  - 17 `[data-enter]` entrances over 6 sections;
  - the tab pill;
  - the FAQ height animation.

  The verbs are varied, but the effect is still per-section entrance motion. Fix: keep the hero and SlipAway as the authored pair. Limit `[data-enter]` to the plates, drop it from the FAQ rows and the log, and make the close sheet static with only the ticks drawing.

**BORDERLINE**
- **Split-hero test (mode-persuade):** at 1440 the h1 ends at x=964 and the stage starts at x=949. That is copy on the left and the product on the right, with no badge row. The full-width floor and the slip bridging onto it are the only things breaking the split. H4 is owner-fixed, but impeccable reads it as a split.
- **The phone has a 2D `rotate(-5deg)`** (`.hs`, Hero.astro:761). This is not 3D tilt, so it is within the owner rule, but it contradicts the "flat phone, no tilt" description.
- **WhoFor:** two equal tiles, each a plate plus heading plus text under a 3px navy top rule (`.aud::before`). This is the icon-card scaffold.
- **HowItWorks:** four equal columns. The sequence numbers carry information, so they are allowed.
- **The compact header's hand-cut bottom edge** reads as a render wobble rather than a cut.

**PASS**
- No eyebrows or kickers on any page. The roofing `hero.eyebrow` field is not rendered.
- No gradient text, glass, side stripes, hard offset shadows, monospace costume or system display face.
- Icons are SVG; no unicode or emoji glyphs.
- No em/en dashes and no "→" in copy. No uppercase. A middle dot appears only in the fixed footer legal line.
- No modal. Tracking minimum is exactly -0.04em.
- `::selection`, `scrollbar-color`, caret and accent colours, and `:focus-visible` are all themed.
- Tap targets are at least 44px at 390. There is no horizontal overflow at any width.
- The 404 page returns status 404. The form states are strong.

## What's working
1. The hero sequence is product-proof motion. Across 14 frames it runs website, tap ripple, Calling, Answered at 0:02, 0:11, ended at 0:14, then the slip. It reads cleanly at 1440 and plays in the first 390 screen.
2. The illustration set is genuinely bespoke: hand-cut polygons, tonal light, and unequal Pillars tiles. SlipAway's sun-to-moon turn and ground shift work in all three engines.
3. Craft details: 92px/900 at -0.04em, orange used only for action, a themed focus ring, a clean drawn link underline, and a sliding tab pill.

## Priority issues
- **[P1] Content hidden by default (view-timeline entrances and the hero copy beat).**
  - Why: it breaks print, full-page captures, link previews and any engine without scroll, and it contradicts craft-floor.
  - Fix: see the Ban-list fix above. Suggested commands: /impeccable animate, /impeccable harden.
- **[P1] Too many motion moments, none deep.**
  - Fix: demote everything except the hero and SlipAway. Add one continuity move instead: the hero slip reappears as the first ledger row, or as the close sheet. Suggested command: /impeccable animate.
- **[P1] The SlipAway "scene" is a strip.**
  - At 1440 the town is a band about 300px tall in the right column above the ledger. The left column is six equal text blocks that duplicate the ledger.
  - At 390 the sticky skyline covers the tops of the ledger cards (story-chromium-390-050.png).
  - Fix: make the town and sky the full-bleed section ground, cut the left copy to the heading, lead and closing, and offset the cards by the sticky band height on mobile. Suggested commands: /impeccable layout, /impeccable distill.
- **[P1] Hero lower-left dead zone at 1440.** Between y≈390 and 900 css, the floor holds only a 12px caption row.
  - Fix: pull the caption and Replay up under the note, raise the slip further left onto the floor, or reduce the hero height. Suggested command: /impeccable layout.
- **[P2] Hierarchy and length below the fold.**
  - The Pillars h3 is about 24px under a 70px h2.
  - The FinalCta has about 250px of empty blue under the sheet.
  - There are 6+ identical CTAs.
  - The inner pages are a banner with an empty right half.
  - Suggested commands: /impeccable typeset, /impeccable distill, /impeccable bolder.

## Persona red flags
- **Jordan (first-timer):** "Hear it answer a call" lands on a transcript, not audio. The website offer is about 3,000px down. Two Replay links appear.
- **Riley (stress tester):** print or PDF of the home page blanks most of the proof. Without JS, the Demo tabs are `hidden`, so the law-firm scene is unreachable.
- **Casey (mobile):** the page is 11.6k px. The sticky skyline covers the ledger card tops. The Menu sits top right.

## Minor observations
- The pressed button is a muddy #8c3105. Use orange-press #A93B06.
- The "Example" tag appears 8+ times in different styles.
- Fine print is 12px on blue-deep.
- The `.typing i` infinite animation should pause offscreen.
- Reconcile the 63 token-drift hits once DESIGN.md is regenerated.

## Inner pages
- **/pricing/:** clear "From $299/month" on a navy plate. The banner's right half is empty and it is the only paper moment.
- **/free-audit/:** the best inner page functionally (the error summary and inline errors are excellent). Visually it is a plain white form card.
- **/roofing/:** the only inner page with a slip. That slip floats small in empty blue, so the hero is weak next to home.
- **/privacy/, /terms/, /refunds/:** a good reading measure under a plain blue banner. Consistent, with no world.
- **404:** correct status and a clear CTA, with an empty right half and no personality.

## Questions to consider
- What if the hero's booking slip were the one object that travels the page (the hero, the ledger, the audit sheet)?
- What would the page be at 65% of its height?
- Does the motion budget belong in eight places or two?
