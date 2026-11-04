---
target: Crewwise home hero (Tap to call) v7
total_score: 20
max_score: 24
na_heuristics: 5,7,9,10
p0_count: 0
p1_count: 1
target_identity: "file:D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
target_fingerprint: "sha256:bd6138daba9f50a90c839b06030f02b48066e25b57a64d195ada13a0749b6479"
target_path: "D:\\Work\\Projects\\tradeapp\\src\\components\\home\\Hero.astro"
timestamp: 2026-11-03T07-03-36Z
slug: src-components-home-hero-astro
---
Method: dual-agent (A: critique agent, isolated from detector until done; B: detector sub-agent). v7, build fresh (dist 21:51 > Hero.astro 21:49).

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | The story reads in order. The tap dot and ripple are too faint to read as a tap. |
| 2 | Match system / real world | 4 | Real call-screen grammar, a law-firm site, a plain slip. |
| 3 | User control and freedom | 4 | Replay is there, the sequence plays once, reduced motion is static. |
| 4 | Consistency and standards | 3 | The final screen shows 0:14 twice and a dead waveform. |
| 5 | Error prevention | n/a | Persuade hero |
| 6 | Recognition rather than recall | 3 | The slip carries the outcome. The phone's final focal point is a duration. |
| 7 | Flexibility | n/a | Persuade hero |
| 8 | Aesthetic and minimalist | 3 | The phone text is soft at DPR 2 or higher. Empty lower-left on desktop. A translucent slip passes over screen text. |
| 9 | Error recovery | n/a | Persuade hero |
| 10 | Help | n/a | Persuade hero |
| **Total** | | **20/24** | **Good (83%)** |

Clarity 9, premium 7.5, wow 7.5. Ship-ready: not yet (one P1).

Previous run: resolved = green Answered pill under Call ended (now "Handled by AI front desk", grey dot), waveform animating at rest (stops at scaleY .4 by ~5.2s). Still open = soft screen text (escalated to P1, root cause found), slip crossing screen text mid-slide (now cuts "Call ended 0:14" at 5.12-5.3s), empty blue gap under the note on desktop (about 185px at 1440).

Detector: CLI 16 advisories in Hero.astro (15 off-ramp font sizes vs the outdated DESIGN.md, 1 undocumented colour #2a3a5c at line 901). index.astro is clean. Overlay: 16-18 at 1440, 17 at 390. The 13 text-occlusion hits are stacked SVG phone states (false positives). 3 tight-leading are probably the 0.96 headline. CLS 0, no overflow at 360/390, all hero text AA (5.93:1, button 4.79:1).

## Priority issues
- [P1] Phone-screen and slip text rasterised soft at DPR 2 or higher, including the reduced-motion static state. Cause: .dio preserve-3d + .lyr translateZ (lines 626-637) composite at 1x. On touch, the continuous sway (lines 1316-1325, 1342) keeps rAF alive, so apply(true) never snaps. Fix: at rest (settle timeout, reduced motion, no JS), flatten to 2D (transform-style: flat, no translateZ, the .dio rotation replaced by a 2D matrix or dropped, keeping .hs rotate(-9deg)). Stop the touch sway after one cycle so the snap runs.
- [P2] Slip crosses screen text mid-slide: @keyframes slide (989-1001) starts at translate(-90px,-70px) with 0 to 20% opacity, so a translucent and then opaque slip covers the timer and "Call ended 0:14" from 5.1 to 5.4s. Fix: enter from the lower right, e.g. translate(48px, 36px), so it never sweeps over the screen, and reach opacity 1 by 10%.
- [P2] Final phone screen is redundant: the 44px 0:14 + "Call ended 0:14" (t-ce, 378-388) + a static waveform at .35 opacity (360-366, wvfade 945-951). Fix: wvfade to 0 (and the default .wv opacity 0 at rest). Change t-ce to "Call ended", or drop the duration.
- [P2] Desktop lower-left void: .main align-items:start (516) leaves ~185px of empty blue between .note and .finerow at 1440 (~110px at 1280). Fix: at min-width 62.5rem, .copy { align-self: center } (or end), so the copy block sits against the phone's middle.
- [P3] The tap barely reads: .tdot r 7 and the .ring stroke #1E5BD8 at 1.75 on the navy pill (193-221) are nearly invisible at real size. Fix: white ring stroke over the pill, r 10, stroke-width 2.5.
- [P3] flipA (972-980) fades opacity together with scaleX, so the calling screen ghosts grey at ~3.48s. Fix: drop the opacity from flipA.
- [P3] Undocumented #2a3a5c in @keyframes lift (901): use the --blue-deep token or a documented navy press tint.

## Personas
Casey (mobile): the soft text on the phone is the first thing that looks cheap on a retina phone. The two identical orange buttons in the first 300px are fine. Jordan: the flow reads. The tap is missed, so the "website to call" link is implied, not seen. Riley: Replay before first play is guarded. The timer resets correctly.
