---
target: Crewwise H4 stacked-stage hero
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
target_fingerprint: "sha256:efe051efeb7871e018586de56dadeaf26f26337b89176b187d966e1a839f2637"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
timestamp: 2026-11-03T14-12-36Z
slug: src-components-home-hero-astro
---
Method: dual-agent (A: isolated design-review sub-agent · B: isolated detector sub-agent; A finished before B's output was read). Parent ran its own DPR 2 screenshot, timeline, crispness and DOM ban sweep.

# Hero critique: H4 "Stacked stage" (src/components/home/Hero.astro)

## Design Health Score (Persuade; 7 and 10 n/a)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | The call reads clearly on desktop (Calling, timer, Call ended, grey dot). But the tap beat is broken (`.pc` undefined), and on a 390 phone nothing plays in the first viewport. |
| 2 | Match System / Real World | 3 | The call UI is realistic. "Hear it answer a call" promises audio and leads to a transcript (owner item). |
| 3 | User Control and Freedom | 3 | Replay works, reduced motion shows the final state, nothing traps the visitor. Replay is visible on phones before play and does nothing when pressed (Hero.astro:1085). |
| 4 | Consistency and Standards | 3 | Orange is used only on the action. "Replay example call" is duplicated in the Demo. |
| 5 | Error Prevention | 3 | The "fictional firm" label prevents a misread. |
| 6 | Recognition Rather Than Recall | 3 | Self-explanatory. |
| 7 | Flexibility and Efficiency | n/a | Persuade surface. |
| 8 | Aesthetic and Minimalist Design | 3 | Strong type. Problems: a dead lower-left floor quadrant of about 325px at 1440; "client." about 28px from the bezel; two pale cut lines crossing behind the phone; a mostly blank end-state screen. |
| 9 | Error Recovery | 3 | Little to recover from. |
| 10 | Help and Documentation | n/a | Persuade surface. |
| **Total** | | **24/32 (75%)** | **Good** |

- **Clarity 8/10, Premium 7/10, Wow 6/10.**
- **Ship verdict:** not yet. Fix `.pc` (a one-line P1) and the mobile play trigger (P1), then ship. Desktop is otherwise presentable.

## Crispness (DPR 2)

The screen text is sharp at rest, mid-wipe (2.15s), mid-crossfade (3.65s) and during mouse movement.
- Computed styles: no transform, perspective or will-change on `.stage`, `.dio` or `.lyr`.
- Filters sit only on the sheet `.fg` and on the sibling `.sh` shapes. The screen `.fg` has filter none.
- The blur fix holds.

## Design specificity

- **The story is specific.** A firm's site, then Call now, then Calling, then Answered by the AI front desk with a timer, then the booking slip.
- **The material is not.** The planes are ruler-straight quadrilaterals (`.floor` :46, `.sheet` :74). The brief promises slightly irregular hand-cut edges. Without the H&L screen this is the category's "phone mockup on brand blue".

## Split test (mode-persuade Comps)

**VIOLATION at desktop (owner-fixed direction, so this is logged as a conflict).**
- The headline glyphs end at x 929, 778 and 848 (1440, 1280, 1366). The phone's box starts at x 941, 813 and 886.
- The copy column and the device column never overlap. The floor starts below the note, so the copy does not stand on it.
- It is not the full template: there is no badge row, and the slip bridges the phone edge.
- **Mobile:** the generic stacked order (headline, sub-line, button, device).

**Fix within H4:** pick one of these.
- Let the phone overlap the end of headline line 2, with the headline in front.
- Raise the floor cut above the sub-line.
- Land the slip in the lower-left, beside the CTA row.

## Sheet #143a8a and its soft shadow

- **Craft-floor: PASS.** Its shadow (`drop-shadow(0 10px 22px rgb(15 27 51/.38))`, :634) has an offset and a soft blur. It is not a zero-offset halo, and craft-floor bans no hue.
- **Brief: conflict.** It is outside PRODUCT.md's fixed palette and DESIGN.md's Three Blues and Flat Planes rules. Under "the brief wins" a pinned palette must be honoured.
- **When it is allowed:** only if the owner adds it to the palette and it is documented as a derived token, for example `--blue-sheet: color-mix(in oklab, var(--blue-deep), var(--navy) 25%)` in global.css, not a hardcoded hex.
- **Detector:** flags it (design-system-color, Hero.astro:637).
- **Visibility:** it barely separates from the floor at 1440.
- **Mobile seam:** at 390 its bottom forms a hard horizontal seam against the blue-deep `.finerow` band.

## Priority issues

- **[P1] Tap beat broken.**
  - The problem: `.pc` is used on `.callbtn`, `.ring`, `.tdot` and `.dot`, but no rule defines it. Computed `transform-box: view-box; transform-origin: 0 0`.
  - The result: the ripple scales out of the clipped screen (at 1.62s the ring's box is at 2014,1747), so it is never seen. The Calling dots drift apart (tl-contact frame 3), and the press shifts the pill.
  - Fix: `.pc { transform-box: fill-box; transform-origin: center; }`.
- **[P1] Mobile first viewport shows no story.**
  - The problem: at 390x844 the screen shows the static website, cropped at "business law". IntersectionObserver threshold 0.4 on an approximately 795px stage (:1108) means playback starts only after about half a screen of scrolling.
  - Fix: threshold 0.15, or observe the screen rect. Trim `.art` margin-top (:1016) and `--pw` (:978) so Call now sits inside 844.
- **[P2] Dead lower-left quadrant at desktop.**
  - The problem: there is about 325px of empty floor between `.note` (bottom 534) and `.finerow` (top 859).
  - Fix: raise `.floor` top (:592) to just under `.acts`, or move `.slpos` (:972) so the slip lands near the CTA.
- **[P2] Headline tangency.**
  - The problem: `--h1r` estimates the headline end as `fs*9.25` (:491), so the claimed 4rem clearance is really about 28px.
  - Fix: overlap decisively, or use a factor of about 9.9 or a measured value.
- **[P2] Two crossing pale cut lines and the mobile sheet/finerow seam.**
  - Fix: keep one lip (drop `.sheet-lip` :75 or the floor polyline :47). At 62.5rem, clip the sheet to the floor or give `.finerow` the same ground (:1030-1035).
- **[P3] Polish.**
  - The end-state screen is blank between 0:14 and Call ended. Keep a resting line such as "Booked Thu 10:00 AM".
  - Mobile H1 breaks "first / minute" (:992). Fix with `text-wrap: balance` or a narrower max-width.
  - The phone sits off-centre at 390 (:979, -3vw).
  - Hide Replay until `[data-play]` is set.

## Detector

- **Hero.astro:** 8 advisories (7 font-size off-ramp, 1 colour, #143a8a). Exit 0.
- **Browser:** shape-assembled-illustration and clipped-overflow on `.hero` are both intentional, so they are false positives.

## Persona red flags

- **Casey (phone):** the story needs a scroll to start, and Replay is visible but inert before play.
- **Plumber owner:** the hero proof is law only ("lawyers close to home", "Consultation").
- **Jordan:** "Hear it answer a call" promises sound.
