---
target: Crewwise H4 hero round 6 (premium pass)
total_score: 25
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 2
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
target_fingerprint: "sha256:538a9cf74c29699e2198552b2d7a72d6d1ef595e5dbc67046da6d0e5a5dba3f0"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
timestamp: 2026-11-03T15-43-40Z
slug: src-components-home-hero-astro
---
Method: dual-agent (A: isolated design-review sub-agent · B: isolated detector sub-agent), with parent captures: a 14-frame entrance timeline at 1440, 5 frames at 390, DPR 2 rest states, and reduced motion, no-JS, Firefox and WebKit.

# Hero critique (src/components/home/Hero.astro), round 6: H4 stacked stage after the premium pass

| # | Heuristic | Score | Key issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | The story starts at about 1.3s and shows its beats clearly: tap ripple, Calling, Answered 0:02, ended 0:14, slip. Replay appears afterwards. The sub-line and CTA are invisible for about the first 0.7 to 1.0s. |
| 2 | Match System / Real World | 4 | Website, tap, answered, booked: the real first minute. |
| 3 | User Control and Freedom | 3 | Replay works. The story is not interruptible, which is fine. |
| 4 | Consistency and Standards | 3 | A second Replay sits in Demo. The phone carries a 2D -5deg rotation (`.hs`) while the spec says "flat". |
| 5 | Error Prevention | 3 | n/a-ish; no inputs. |
| 6 | Recognition Rather Than Recall | 3 | Fine. |
| 7 | Flexibility | n/a | Persuade. |
| 8 | Aesthetic and Minimalist | 3 | Strong type and discipline. The lower-left floor (about y 390 to 900 css at 1440) holds only the 12px caption row. |
| 9 | Error Recovery | 3 | No error paths; the reduced-motion and no-JS final state is complete. |
| 10 | Help | n/a | Persuade. |
| **Total** | | **25/32 (78%)** | **Good** |

- **Clarity 8/10.** The headline, sub-line, orange CTA and note all sit above the fold at 1440 and 390.
- **Premium 8/10.** 92px/900 at -0.04em, crisp flat art, a 388px slip overlapping the phone's lower-left edge, and a themed focus ring.
- **Wow 6/10.**
  - The sequence is honest and clean, but once seen it is a quiet 0:14 call ending in a static slip.
  - Nothing travels beyond the hero.
  - The words stagger, the floor lays down and the phone arrives, but at networkidle a capture still shows the sub-line faded and no phone.

**Verdict:** this is the strongest hero the project has had, and it is near studio level on craft. It is held back by three things:
- the empty lower-left floor;
- copy that is hidden at t=0;
- a payoff that ends inside the hero instead of carrying into the page.

## Ban-list (hero)
- **Split hero:** BORDERLINE. The h1 ends at x=964 and the stage starts at x=949, so it reads as copy-left, product-right. The floor and the slip bridge soften it, and H4 is owner-fixed.
- **No 3D tilt:** PASS (2D rotate only).
- **No eyebrow:** PASS.
- **Orange only on the action:** PASS.
- **Already-visible default:** VIOLATION for the sub-line and CTA during the entrance.

## Priority issues
- **[P1] Sub-line and CTA hidden at load.** Fix: start them at rest, and stagger only the h1 words, the floor and the phone. Suggested command: /impeccable animate.
- **[P1] Lower-left dead zone at 1440.** Fix: move `.finerow` up under `.note`, or extend the slip left onto the floor, or cut the hero height so the floor ends under the slip. Suggested command: /impeccable layout.
- **[P2] The payoff ends in the hero.** Fix: let the booked slip become the first ledger row in SlipAway, or the close sheet. Suggested command: /impeccable animate.
- **[P3] Phone `rotate(-5deg)`.** Confirm with the owner, or set it to 0 to match "flat phone, no tilt".
