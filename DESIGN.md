---
name: Crewwise
description: A flat cut-paper studio of overlapping blue, blue-deep, navy and sheet planes, with one orange action per screen.
colors:
  blue: "#1E5BD8"
  blue-ink: "#1A4FBD"
  blue-deep: "#1749B0"
  blue-sheet: "#163B88"
  navy: "#0F1B33"
  navy-raised: "#16264A"
  light-blue: "#8FB3FF"
  soft: "#F4F7FC"
  white: "#FFFFFF"
  orange: "#C94708"
  orange-press: "#A93B06"
  green: "#1F7547"
  slate-label: "#5B6B8C"
typography:
  display:
    fontFamily: "Hanken Grotesk Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(3rem, min(1.2rem + 6.6vw, 0.5rem + 11vh), 6rem)"
    fontWeight: 830
    lineHeight: 0.94
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Hanken Grotesk Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2.25rem, 1.4rem + 3.4vw, 4.25rem)"
    fontWeight: 820
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  title:
    fontFamily: "Hanken Grotesk Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem)"
    fontWeight: 750
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Hanken Grotesk Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.0625rem, 1rem + 0.2vw, 1.1875rem)"
    fontWeight: 420
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "Hanken Grotesk Variable, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 650
    lineHeight: 1.3
    letterSpacing: "0.01em"
rounded:
  card: "16px"
  slip: "12px"
  field: "10px"
  pill: "999px"
spacing:
  gutter: "clamp(1rem, 0.4rem + 2.6vw, 2.5rem)"
  band: "clamp(4.5rem, 3rem + 6vw, 8.5rem)"
  section-head: "clamp(2.5rem, 1.8rem + 3vw, 5rem)"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.85rem 1.6rem"
    height: "3.25rem"
  button-primary-hover:
    backgroundColor: "{colors.orange-press}"
    textColor: "{colors.white}"
  button-primary-sm:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.5rem 1.05rem"
    height: "2.75rem"
  card:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy}"
    rounded: "{rounded.card}"
  slip:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy}"
    rounded: "{rounded.slip}"
  band-blue:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.white}"
  band-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.white}"
  band-soft:
    backgroundColor: "{colors.soft}"
    textColor: "{colors.navy}"
  field:
    backgroundColor: "{colors.white}"
    textColor: "{colors.navy}"
    rounded: "{rounded.field}"
    height: "3.25rem"
    padding: "0.7rem 0.9rem"
  status-booked:
    backgroundColor: "{colors.green}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.5rem 0.75rem"
---

# Design System: Crewwise

## Overview

**Creative North Star: "The Cut-Paper Studio"**

Crewwise is built the way a paper model is built: flat sheets of colour laid over one another on a table, lit from the top left. Depth is never faked with volume. It comes from overlapping planes in four fixed tones (blue, blue-deep, navy and the derived blue-sheet), and from white slips and documents that sit on top and carry a soft paper shadow. Everything is a hand-cut polygon, with one nicked corner at the top right and a pale light facet at the top left shown in tone only.

The page is a stack of full-bleed bands, each one flat ground: blue, white, soft or navy. Type is Hanken Grotesk at heavy weights with tight tracking, so headlines read like cut lettering. The tone is calm and credible for a law firm and still friendly to a plumber; nothing is decorative that does not belong to the paper world. One orange pill per screen is the action, and nothing else is orange.

Motion is the second material. The masthead folds, the working day is scrubbed by scroll, and sheets lay, drop, settle and rise into place. Every movement is a decelerating ease-out to rest, never a bounce.

**Key Characteristics:**
- Flat overlapping planes in blue, blue-deep, navy and blue-sheet; no volume, no gradients.
- Light from the top left, told in tonal steps, never in shadow.
- Soft shadows only on white slips and documents, plus the hero's stage sheet.
- Heavy Hanken Grotesk, tracking -0.035em to -0.04em on headings.
- One orange pill per screen; green only when something is truly done.
- Fluid type scale and three motion durations, used everywhere.

## Colors

A blue studio: three blues and a derived darker sheet carry the planes, navy is the ink and the night, white and soft are the paper, orange is the single action.

### Primary
- **Crewwise Blue** (#1E5BD8): the main ground (hero, demo, day story, close), selection, focus ring on light grounds, and the lit facet of illustrations.
- **Blue Ink** (#1A4FBD): link hover on white and soft grounds only.
- **Shadow Blue** (#1749B0, `--blue-deep`): the second plane. The hero's hand-cut floor, the masthead's cut edge under the blue bar, the day story's far hills, and pressed or shaded facets in illustrations.
- **Sheet Blue** (#163B88, `--blue-sheet`, derived as 30% navy mixed into blue-deep in oklab): the third plane. The offset sheet behind the hero phone, the mid hills of the day story, the lowest shaded facet in illustrations. It must read against both blue and blue-deep.

### Secondary
- **Call Orange** (#C94708) with **Orange Press** (#A93B06): the primary action only. White text on it clears 4.5:1. Pressed goes one step deeper still.

### Tertiary
- **Booked Green** (#1F7547): real success states only: the booked slip, a booked event, a submitted form. Never decoration, never a category colour.

### Neutral
- **Night Navy** (#0F1B33, `--ink`): text on light grounds, the night ground of the day story, the footer, the mobile menu, the phone body.
- **Navy Raised** (#16264A): lit facets and lifted plates on navy.
- **After-Hours Blue** (#8FB3FF): times and quiet accents on navy, the lit windows, the lit facet on blue shapes.
- **Soft Paper** (#F4F7FC): the quiet band ground and disabled fields.
- **White** (#FFFFFF): the page ground, slips, cards and documents.
- **Slate Label** (#5B6B8C): secondary text inside the hero phone screen.
- Text tints from navy: 74% for secondary, 60% for tertiary; on blue, white at 86%; on navy, white at 78%. Rules are navy at 10% and 22%, light blue at 18% and 36% on navy, white at 28% on blue.

### Named Rules
**The One Orange Rule.** Orange is the primary action and nothing else. One orange pill per screen; a second one means one of them is wrong.
**The Real Success Rule.** Green means something actually happened (booked, sent). It is never used to say "good" or to decorate.
**The Four Planes Rule.** Depth is made by stacking blue, blue-deep, navy and blue-sheet. Do not add a fifth tone to fake a new layer.

## Typography

**Display Font:** Hanken Grotesk Variable (with ui-sans-serif, system-ui, sans-serif)
**Body Font:** Hanken Grotesk Variable (same family; one face carries the whole system)
**Label/Mono Font:** none. Times and counters use Hanken's tabular numerals.

**Character:** One heavy grotesque, set tight. Headlines are weight 800 to 900 and read like cut lettering; body is a light 420 so the contrast of weight carries hierarchy, not extra faces.

### Hierarchy
The fluid scale is `--step-*`: micro 0.75rem, label 0.8125rem, ui-small 0.9375rem, ui 1.0625rem, body clamp(1.0625rem to 1.1875rem), title-lead clamp(1.25rem to 1.5rem), subhead clamp(1.625rem to 2.25rem), headline clamp(2.25rem to 4.25rem), statement clamp(2.75rem to 5rem), display clamp(3rem to 6rem, height-aware).
- **Display** (830; the home hero h1 runs at 900; clamp(3rem, ..., 6rem); line-height 0.94, tracking -0.04em): hero, demo and story headings. Never above 6rem.
- **Headline** (820, clamp(2.25rem, 1.4rem + 3.4vw, 4.25rem), 0.98, -0.04em): band h2.
- **Title** (750, clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem), 1.15, -0.02em): card, step and FAQ titles. FAQ row questions are 750 at the same size.
- **Body** (420, clamp(1.0625rem, 1rem + 0.2vw, 1.1875rem), 1.6): running text, measure 62ch; `.lead` at 46ch.
- **Label** (650, 0.8125rem, +0.01em, tabular numerals): times, captions and plain tag text. Not uppercase.

### Named Rules
**The Tight Tracking Floor Rule.** Heading tracking runs from -0.02em to -0.04em and never tighter than -0.04em.
**The Weight Carries It Rule.** Hierarchy comes from weight and size steps in one family. No second face, no uppercase labels above headings.

## Layout

A single column of full-bleed bands inside a 84rem page (`--page-max`) with a fluid gutter of clamp(1rem, 0.4rem + 2.6vw, 2.5rem). Bands take vertical padding clamp(4.5rem, 3rem + 6vw, 8.5rem) and each is one flat ground; adjacent bands change ground (blue, white, soft, navy) to mark the seam. Order on home: hero (blue), demo (blue), pillars (white), the working day (blue to navy), setup route (white), who it is for, FAQ, close (blue), navy footer.

Rhythm is generous between sections and tight inside groups; section heads sit 2.5rem to 5rem above their content. Deliberate asymmetry is used instead of equal card grids: the pillars set a wide plate first and a tall one lower, the two audiences sit one lower than the other, the FAQ keeps a sticky 4/12 heading column beside 8/12 rows.

The two layout breakpoints that matter are 62.5rem (masthead collapses to a menu; the hero stacks) and 60rem (two-column section heads). The hero is a stacked stage: a full-width headline, then copy and the action, then one large flat phone right of centre standing on the blue-deep floor, with the sheet behind it and the booking slip overlapping its lower-left edge. At 100svh on desktop; stacked and auto height on phones, where the offset sheet is dropped so only the floor remains.

## Elevation & Depth

Depth is tonal and planar. Planes overlap: a blue ground, a blue-deep floor cut across it, a blue-sheet offset sheet, a navy phone, a white slip. Nothing is shaded to look round and no 3D is used on the hero phone or on any text.

### Shadow Vocabulary
- **Paper shadow** (`--shadow-paper`: `0 1px 2px rgb(15 27 51 / 0.16), 0 10px 24px -12px rgb(15 27 51 / 0.35)`): white cards, slips and documents on any ground.
- **Paper drop** (`--drop-paper`: `drop-shadow(0 1px 1.5px rgb(15 27 51 / 0.2)) drop-shadow(0 9px 9px rgb(15 27 51 / 0.2))`): the same shadow for SVG groups: the hero phone body (on its own sibling shape, never on the screen layers), the booking slip, `.illo .slip`.
- **Stage sheet** (`drop-shadow(0 10px 22px rgb(15 27 51 / 0.38))`): the hero's blue-sheet only.
- **Bar cut** (`drop-shadow(0 3px 5px rgb(15 27 51 / 0.28))`): follows the masthead's hand-cut edge.

### Named Rules
**The Flat Planes Rule.** Depth comes from overlapping flat planes in blue, blue-deep, navy and blue-sheet. Shadows are an accent, not the structure.
**The Soft Shadow Rule.** Every shadow has an offset and a blur. No zero-blur offset shadows anywhere. Only white slips and documents, plus the hero stage sheet (and the masthead cut that follows its edge), get soft shadows. Coloured or zero-offset halos are not part of the system.
**The Flat Phone Rule.** The hero phone and all text are 2D: no perspective, preserve-3d, translateZ or rotateX/Y, and no filters on the screen layers. The pointer tilt was removed because it blurred the screen. The phone may rotate in plane (-5deg) only.
**The Top-Left Light Rule.** Light comes from the top left and is told only in tone: lit facets step up (navy-raised on navy, light blue on blue) and the sheet steps down toward the bottom right (blue, blue-deep, blue-sheet).

## Shapes

Everything is hand-cut. Illustration pieces, the hero floor edge, the masthead edge and the nav tab are polygons with slightly uneven edges. Every illustrated piece carries exactly one nicked corner at the top right. The top-left light facet is a clipped triangle in a lighter tone. Illustrations have no strokes.

UI geometry is simple: pills (999px) for buttons, tabs and status chips; 16px for cards, 12px for slips and day pages, 10px for fields, 6px for focus rows. The phone is a 40-unit rounded rectangle. Links and controls take a pale 2px line, and text links use real underlines.

## Components

Paper in, paper out: crisp white surfaces on flat ground, drawn lines that move with ease-out.

### Buttons
- **Shape:** full pill (999px), min-height 3.25rem, weight 720, 1.0625rem, tracking -0.01em.
- **Primary:** Call Orange fill, white text, padding 0.85rem 1.6rem. Small variant 2.75rem. Hero action is 3.5rem.
- **Hover / Focus / Press:** hover goes to Orange Press and lifts 1px (translateY(-1px)); press scales to 0.98 and goes one step deeper (`--orange-deep`); transitions use `--dur-2` for transform and `--dur-1` for colour. Disabled and busy: 72% opacity and `cursor: progress`. Focus is a 3px ring offset 3px (blue on light, white on blue and navy).
- **Quiet link (secondary):** navy text (white on blue and navy) with a faint 2px underline; on hover or focus a 2px line draws across it from the left and retracts to the right (`.link-quiet`, `.link-draw` in running text). Always 44px tall.

### Masthead
- **At the top of home:** an oversized white wordmark over the blue hero with a hairline rule that wipes away as the page scrolls; the wordmark and links ride down and shrink into the compact bar on scroll (native scroll timelines, script fallback).
- **Compact bar:** brand blue with a hand-cut blue-deep edge beneath it and the bar-cut soft shadow. White links at 0.9375rem, weight 600; a 2px underline draws on hover. Hides while scrolling down and slides back on scroll up; stays put under reduced motion, within 240px of the top, and when keyboard focus is inside.
- **Current section:** one white cut-paper tab hangs under the links and slides between them as scroll-spy moves (transform only). Inner pages use the same bar, already compact.
- **Mobile (below 62.5rem):** a "Menu" pill with two drawn bars that turn into a cross; opens a full-screen navy panel of ruled 800-weight links with a drawn chevron, an orange action, and mail and booking links. Items stagger in at 55ms. The panel traps focus and Escape closes it.

### Cards / Containers
- **Corner Style:** 16px for cards, 12px for slips and day pages.
- **Background:** white, navy text, on blue, navy or soft grounds. No nested cards.
- **Shadow Strategy:** paper shadow only (see Elevation).
- **Border:** none; separation is by plane and shadow.
- **Internal Padding:** 1rem to 1.5rem, fluid.

### Inputs / Fields
- **Style:** white, 1.5px navy-32% border, 10px radius, min-height 3.25rem, caret blue.
- **Focus:** 3px blue-35% outline, border to blue; hover to navy.
- **Error / Disabled:** invalid becomes a 2px navy edge (inset ring, nothing moves) with a bold navy message; the brand has no red. Disabled goes soft with a faint rule.

### The Working Day (signature)
A scroll-scrubbed scene on a blue band: a cut-paper town (far blue-deep, mid blue-sheet, near navy hills), a hand-cut sun and moon, windows that light, and a pinned white day page. As each enquiry is read, the lost outcome is struck through and the kept outcome lands with the booking mark. The ground turns blue, then blue-deep, then navy using stacked flat layers whose opacity changes. Driven by named native view timelines, with a requestAnimationFrame fallback, and a static finished version (every lost and kept state shown) with no JS or reduced motion.

### The Hero Call (signature)
The phone screen plays the first minute: the firm's mobile site, a touch dot, Call now pressing and rippling, Calling, Answered by the AI front desk with a timer, then the booking slip landing and its check drawing. The story starts when the artwork scrolls into view (about 1.3s later), with a Replay control. The finished state is the default for no JS, reduced motion and crawlers.

### Cut-paper Illustrations
`.illo` SVG plates for the pillars, route markers and audiences. Flat fills only through the `.f-lb .f-b .f-bd .f-bs .f-n2 .f-n .f-w .f-g` classes; text on them through `.tx-*`; white slips take `.slip`.

### Audit Sheet and FAQ
The closing band sets the audit deliverable as a white cut-paper sheet, tilted slightly, whose three lines are ticked off with a drawn navy mark. FAQ rows are ruled, native `details`, with the plus turning to a minus and a measured open; no cards.

### Motion
Tokens: `--dur-1` 160ms (press, hover, focus), `--dur-2` 320ms (tabs, disclosure, underline), `--dur-3` 640ms (authored entrances); `--ease-out-quart` for control state, `--ease-out-expo` for entrances. Scroll-driven entrances use `[data-enter]`: **lay** (plates), **drop** (route markers), **draw** (rules and route lines), **settle** (FAQ rows, call log), **rise** (the demo phone), staggered with `--i`.
**The Ease-Out Only Rule.** Decelerating curves only. No bounce, no overshoot, no elastic.

## Do's and Don'ts

### Do:
- **Do** build depth from flat overlapping planes: blue, blue-deep, navy and `--blue-sheet`.
- **Do** give soft shadows only to white slips and documents and the hero stage sheet, with an offset and a blur.
- **Do** keep the hero phone and all text flat, 2D and sharp.
- **Do** use orange for the primary action only, one per screen, and green only for real success states.
- **Do** keep heading tracking between -0.02em and -0.04em, and use the `--step-*` scale.
- **Do** use `--dur-1/2/3` with `--ease-out-quart` or `--ease-out-expo`, and keep the finished state as the no-JS and reduced-motion default.
- **Do** call it the "AI front desk"; each client may name their own.
- **Do** show "from $299" as the only price.
- **Do** let the hero action go to /free-audit/. This is a recorded exception to "action in working form": the hero button links to the audit page instead of performing the action in place.
- **Do** cut every illustrated piece by hand with one nicked top-right corner and a top-left light facet in tone.

### Don't:
- **Don't** use zero-blur offset shadows anywhere.
- **Don't** apply 3D transforms to the hero phone or to text, or bring back the pointer tilt.
- **Don't** use bounce, overshoot or elastic easing.
- **Don't** put an eyebrow or kicker above a heading.
- **Don't** use unicode glyphs or emoji as icons; draw them as SVG or CSS shapes.
- **Don't** set tracking tighter than -0.04em.
- **Don't** use orange for anything but the primary action, or green for anything but success.
- **Don't** give the AI front desk a personal name.
- **Don't** show any price except "from $299".
- **Don't** use clinic or medical examples.
- **Don't** nest cards or build the page from equal icon-heading-text card grids.

### Defects the build carries (not canonized)
- Content using `[data-enter]` sits at opacity 0 until it scrolls into view, and the closing sheet and demo lines are also hidden by script before they play. This violates "content visible by default" and must not be copied to new surfaces; new entrances start from a visible default.
- Off-token values in the build: the pressed orange is hard-coded as #8c3105 in the masthead and close instead of `--orange-deep`; the booked check in the demo log uses #2f9a63 instead of Booked Green; the live-call status dot in the hero shows green before anything is booked.
- The hero doc comments still mention a pointer tilt and an overshoot on the slip; the code has neither.
