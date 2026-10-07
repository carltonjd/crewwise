# Jobstead: direction

## Brief (self-authored from the project conversation)

- **What:** a marketing site for Jobstead, an AI front desk for US roofing companies (1 to 20 staff). Redesign of the existing site in this folder.
- **The one job:** in ten seconds a roofing owner who just got a cold call understands "this answers my calls and books inspections so I stop losing leads I paid for", trusts that it is a real business, and books a 15-minute demo.
- **Three words:** tough, straight-talking, useful.
- **References from outside the web:** a contractor's yard sign on a front lawn; a storm radar on the local TV news; a well-built roof.
- **What exists (locked by the client):** name Jobstead, logo (roof chevron and check), colours Stead navy #13233A, Ember #C4471B, Ember bright #F06A35, Timber #B98A5E, Canvas #F7F3EC, Booked green #2E8B57 (success only), Archivo for headings, Inter for body. Copy brief of Oct 1 (headline, sections, Storm Mode, report, pricing $499/month, FAQ). No photos, no customers, no testimonials (pre-launch).
- **Image generation:** not used (no consent asked; no paid credits spent).

## Current (the "before")

Shot in `shots/before/`. Look row: `site|media|paper|expanded|orange|data|scroll-story`.

- **Slop faces it wears:** The Paper Edition (warm paper ground, ink, one warm accent, pill buttons, floating product card, eyebrow label, `<details>` FAQ, a nine-card icon grid, a dark pricing card). 6+ shared features: rework.
- **Scan FAILs (9):** contrast failures in the call transcript and footer wave; "Book a 15-min demo" wraps; captions clipped on phones; footer waveform collapses at 390; placeholder form field flagged; Jobstead text clipped in the footer at 1280+.
- **Scan warns:** 25+ text sizes, 11 nested boxes, icon-card grid of nine, icons in tinted squares, timed demo text invisible on scroll.
- **What works and must survive (keep list):**
  - [ ] Name, logo, brand colours, Archivo and Inter
  - [ ] The live call demo idea (the product doing its job)
  - [ ] Sections from the Oct 1 brief: hero, where leads leak, what it does (9 items), Storm Mode, Lead Recovery Report (Example), how it works, pricing $499, FAQ (9), contact form, footer with legal links and company line
  - [ ] Trust strip: Not a lead-gen company / Not a robocaller / Not a call center
  - [ ] /privacy, /terms, /refunds, /roofers redirect, /photographers noindex
  - [ ] All placeholders kept and listed

## Category default refused

Top AI-receptionist sites (Smith.ai, Goodcall, Rosie, Sameday, Avoca) share: a white or pale ground, a blue or violet accent, Inter, a centred hero with a phone or chat mockup, a logo strip, three to six feature cards, a three-tier pricing table, testimonials. The category colour cliché is **trust blue / AI violet**. This brief naturally falls into **The Paper Edition** (the current site) and **The Launch Page** (dark navy, glow, feature cards).

## Concepts (three source families)

First ideas discarded: "a job ticket" (we already did it), "a front desk", "a departure board".

- **A. Nature / media: "Jobstead is the storm radar for your phone line."** Roofers live by hail maps and the TV weather radar. Dark navy ground, the hero is a radar over a service area drawn as a dot matrix: the sweep finds calls as ember blips and they turn into booked pins.
- **B. Printed object: "Jobstead is the yard sign in front of every job you win."** The corrugated sign roofers stake on a lawn. Ember colour-field ground, Archivo at its narrowest and heaviest, the sign's lines change like kinetic type.
- **C. Object: "Jobstead is a roof that doesn't leak."** A small 3D roof section built in CSS, shingles laying themselves course by course, on Canvas with Archivo expanded.

| | A Radar | B Yard sign | C Roof |
|---|---|---|---|
| ground | dark (navy) | colour-field (Ember) | paper (Canvas) |
| type | Archivo normal width (grotesque) | Archivo 62 width (condensed) | Archivo 125 width (expanded) |
| richness | data (radar, service area, calls) | shape (the sign object) | 3d-object |
| accent use | Ember bright blips on navy | navy and Canvas on Ember (the field is the accent) | Booked green: the leak is plugged |
| grammar | scroll-story | poster | scroll-story |
| motion | dot matrix / dither | kinetic type | 3D object |

Brand note: accent hue and font family are locked by the client, so the three differ on accent *use* and on Archivo's width axis rather than on hue family and typeface.

## Choice

**Winner: B, the yard sign, merged with A's radar for the Storm Mode section.**

- **B won** because it is the most *this product*: roofers already put this exact sign on every lawn they work on, so a roofer reads the page in their own visual language. It is also the only direction that clears the history rule against the current look (`site|printed|colour-field|condensed|orange|shape|scroll-story` differs on 5 of 6; accent is brand-locked and the section list is client-fixed).
- **A lost** as the hero: the radar is the strongest single image, but it keeps the same richness (live data) and grammar as the current site, so it is an evolution, not a redesign (3 of 6). It is kept as the Storm Mode visual, where a storm radar is literally the right picture.
- **C lost**: a small house on a pale ground drifts into 2018 SaaS illustration (imagery.md), it sits on the same paper ground and expanded type as today (2 of 6), and the left roof plane rendered edge-on.

### Problems to solve in the build (seen in the B render)

- Canvas body text on Ember measures 4.45:1 (fails AA by a hair). Body text on Ember must be white (4.9:1) or 24px+.
- The headline at 7.6rem ran six lines and pushed the sign below the fold: cap the display size so headline, action and sign share the first screen at 1440x900 and the action stays in the phone's first screen.
- The lawn strip caused sideways scroll (used -100vw); the stakes were off-screen at 1440.
- The client's headline is a two-beat line ("You paid for the lead. We make sure you don't lose it."), which copy.md flags. Kept because the client wrote it; noted as a decision.

## Revision after client feedback (Oct 6)

The client rejected A, B and C (too gimmicky, wrong colours and mood, not polished enough), then rejected an app-UI hero, and asked for a **type-led, minimal, polished-SaaS** page (the feel of Linear, Stripe, Vercel), with **no photos** and **no product UI**. The client then unlocked colours and fonts. Three palettes were rendered on the same type-led hero (`explore3/v1-galvanized`, `v2-slate`, `v3-editorial`); the client chose **v1, Galvanized**.

### Final direction: Galvanized

- **Concept:** "Jobstead is the quiet record of a call you never had to answer": one homeowner call, from first ring to booked inspection, laid out on a ruler.
- **Ground:** `#F2F3F4`, galvanized steel flashing, cool and light. Refuses warm paper and SaaS white.
- **Ink:** `#14181C`, asphalt shingle. Secondary `#47505A` (7.5:1), meta `#5F6973` (5.1:1).
- **Accent, one job:** copper `#B0522A`, the copper flashing on a roof: the call in motion (timeline, ring, the three "moment" labels). Text copper `#9C4722`.
- **State:** green `#23794A` only where something is booked.
- **One dark band:** `#14181C` for Storm Mode (the storm is the one time the page goes dark).
- **Type:** Schibsted Grotesk only, because it was drawn for a newspaper: sturdy, plain-spoken, made to be read fast, which is how a roofer reads. Display 700 at clamp(2.9rem…5.6rem), tracking -0.045em; h2 700; body 400 at 17px; meta 13px. No tabular figures: Schibsted's tabular colon and comma space out ("9 : 00"), and none of the numbers form columns that need them.
- **Layout:** type and hairlines, no cards, no icons. A ledger for the leaks, three time-based groups for features (On the call / Right after / Weeks later), a statement for the report, one form panel as the only box.
- **Signature:** the hero ruler. Trigger: the ruler enters view. Frames: copper ring pulses twice at the first event (1.6 s), the dot travels to Answered (1.3 s), Qualified (1.7 s), Booked (1.7 s), each label rising in as the dot arrives, the dot turns green and rests 9 s, then the call replays. Ease: cubic ease-out per leg. Reduced motion: the finished line, all four events shown, nothing moves. Phone and tablet: the same four events as a vertical list.
- **Voice:** a straight-talking contractor: short, specific, no hype.

History row (recorded at the end): `jobstead|site|printed|light|grotesque|orange|data|scroll-story`. Versus the old site it differs on ground and type only; the client fixed the grammar (section list), asked for no imagery (so richness stays the product's own data) and the copper accent sits in the orange family. Recorded with `--force`; the reason is the client's explicit direction.
