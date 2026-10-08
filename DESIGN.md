---
name: Crewwise
description: AI front desk for roofing and home-service companies. A crisp site plan in logo blue, with one sun-yellow action.
colors:
  logo-blue: "#1E5BD8"
  logo-blue-raised: "#2C68E4"
  logo-blue-rule: "#5A8BEE"
  deep-navy: "#0B1530"
  sun-yellow: "#FFC233"
  sun-yellow-pressed: "#FFB300"
  pale-sun: "#FFE08A"
  page-white: "#FFFFFF"
  surface-white: "#FFFFFF"
  plan-tint: "#F4F7FE"
  slate-text: "#3A4766"
  muted-slate: "#55617D"
  hairline: "#DDE4F2"
  rule-steel: "#BFCBE3"
  on-blue: "#FFFFFF"
  on-blue-soft: "#DCE6FF"
  booked-green: "#1F7547"
  booked-dot: "#2E8B57"
  booked-mint: "#B9F5CF"
  error-red: "#B42318"
typography:
  display:
    fontFamily: "Archivo, Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(4rem, 0.5rem + 6vw, 6rem)"
    fontWeight: 600
    lineHeight: 0.96
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Archivo, Hanken Grotesk, system-ui, sans-serif"
    fontSize: "clamp(2.1rem, 1.3rem + 2.8vw, 3.75rem)"
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Archivo, Hanken Grotesk, system-ui, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "Hanken Grotesk, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Hanken Grotesk, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  small:
    fontFamily: "Hanken Grotesk, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Hanken Grotesk, system-ui, Segoe UI, Roboto, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.5
  wordmark:
    fontFamily: "Hanken Grotesk"
    fontWeight: 650
    letterSpacing: "-0.019em"
rounded:
  tag: "6px"
  control: "10px"
  card: "14px"
  panel: "18px"
  sheet: "22px"
  pill: "999px"
spacing:
  gutter: "20px"
  tight: "12px"
  group: "24px"
  block: "40px"
  split: "64px"
  section: "120px"
components:
  button-primary:
    backgroundColor: "{colors.sun-yellow}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.control}"
    padding: "12px 22px"
    height: "48px"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.sun-yellow-pressed}"
    textColor: "{colors.deep-navy}"
  step-pill:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.pill}"
    padding: "6px 12px 6px 7px"
    typography: "{typography.label}"
  tag:
    backgroundColor: "{colors.plan-tint}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.tag}"
    padding: "3px 8px"
  input:
    backgroundColor: "{colors.plan-tint}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.control}"
    padding: "12px 14px"
    height: "50px"
  card:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.deep-navy}"
    rounded: "{rounded.card}"
    padding: "14px 16px"
  card-dark:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.panel}"
    padding: "20px"
  nav-link:
    textColor: "{colors.slate-text}"
    rounded: "{rounded.control}"
    padding: "9px 14px"
  nav-link-active:
    backgroundColor: "#E8EFFC"
    textColor: "{colors.logo-blue}"
---

# Design System: Crewwise

## Overview

**Creative North Star: "The Site Plan"**

Crewwise looks like a contractor's plan sheet that works: a crisp white page, a fine logo-blue grid where the sheet begins, and bold marks that show a job moving from first ring to booked. Every visual device is a working part of the plan. The blue line is the route of a call, the dots are checkpoints, the cards are the documents a roofer actually receives (a call transcript, a calendar slot, a text, a monthly report), and the grid is the paper they are drawn on.

The mood is bold, sharp and modern. Headlines are big and tight, the logo blue owns whole sections, and one sun-yellow action sits on every screen. The parts you touch are friendly and soft: generously rounded corners, light borders and short lifts, so the boldness reads as confident rather than hard. Density is generous on the page and compact inside the cards, the way a plan has open margins and dense annotations.

Motion is narrative, never decorative. The page plays the product: the call happens as you scroll, the busy-day list sorts itself, the line draws to the next step. Everything is complete and readable without motion.

**Key Characteristics:**
- Crisp white sheet with a faint logo-blue plan grid fading from the top right of the first screen.
- Logo blue (#1E5BD8) as the brand's field colour: whole sections, the call line, checkpoints.
- Sun yellow only on things you click; green only for booked.
- Archivo headlines set tight; Hanken Grotesk for reading and for the logo.
- Product artifacts (call, calendar, text, queue, report) instead of illustrations or photos, always labelled as examples.

## Colors

A two-colour brand on white: logo blue carries identity and structure, sun yellow carries action, deep navy carries the words.

### Primary
- **Logo Blue** (logo-blue): the fixed brand colour. Full-bleed bold sections (leaks, busy days), the call line and progress rail, checkpoint dots, active nav, links, focus rings, the plan grid. Never altered or swapped.
- **Raised Blue** (logo-blue-raised) and **Blue Rule** (logo-blue-rule): secondary surfaces and dividers inside logo-blue sections only.

### Secondary
- **Sun Yellow** (sun-yellow): every primary action (Book a demo, Call me back, the phone booking bar), with deep navy text. Pressed state is **Pressed Sun** (sun-yellow-pressed).
- **Pale Sun** (pale-sun): small marks on blue sections (the leak crosses, urgent labels).

### Tertiary
- **Booked Green** (booked-green, booked-dot, booked-mint): only for a booked or successful state: the Booked card, calendar bookings, "fixed" ticks, the call-back confirmation.

### Neutral
- **Deep Navy** (deep-navy): body and headline text on white; the closing band; dark cards (live call, follow-ups, busy-day list, call forwarding).
- **Page White** (page-white) and **Surface White** (surface-white): the page and every light card.
- **Plan Tint** (plan-tint): tinted fills inside white surfaces: inputs, tags, busy calendar slots, incoming text bubbles.
- **Slate Text** (slate-text) and **Muted Slate** (muted-slate): secondary copy and captions.
- **Hairline** (hairline) and **Rule Steel** (rule-steel): card borders, list dividers, inactive rail track.
- **On Blue** (on-blue) and **On Blue Soft** (on-blue-soft): headings and body copy on logo-blue sections.
- **Error Red** (error-red): form field errors only.

### Named Rules
**The Fixed Blue Rule.** The logo blue and the logo (icon plus the Hanken Grotesk 650 wordmark) never change. Everything else may evolve around them.

**The One Yellow Rule.** Sun yellow means "click this". It never decorates, never fills a section, and never appears on something that is not an action.

**The Booked Green Rule.** Green appears only when something is booked or succeeded. A decorative green is a lie about state.

## Typography

**Display Font:** Archivo (with Hanken Grotesk, system-ui fallback)
**Body Font:** Hanken Grotesk (with system-ui, Segoe UI, Roboto fallback)
**Wordmark:** Hanken Grotesk 650, fixed by the logo spec

**Character:** Archivo gives the headlines a sturdy, engineered weight at a calm normal width; Hanken Grotesk keeps reading friendly and matches the logo, so the brand voice stays one family in spirit.

### Hierarchy
- **Display** (600, clamp to 6rem on desktop, 0.96): the hero headline only. Two to three lines, tight tracking.
- **Headline** (600, up to 3.75rem, 1.02): section headings, paired with a lead paragraph in a left/right split on desktop.
- **Title** (600, 1.375rem, 1.2): every card and step title: feature titles, leak titles, journey steps, report header. One size for one job.
- **Lead** (400, 1.1875rem, 1.6): section intros and the hero description.
- **Body** (400, 1.0625rem, 1.6): running text; keep to 65 to 75 characters a line.
- **Small** (400, 0.9375rem): card text, list details, form help.
- **Label** (600, 0.875rem): pills, buttons, timestamps, captions, example tags.

### Named Rules
**The One Title Rule.** Every card-level title uses the single Title role. If a new card needs a different size, the card is wrong, not the scale.

**The Display Ceiling Rule.** Nothing exceeds the hero's 6rem. Prices and big figures stay at or below it.

## Layout

A centred sheet: content sits in a 1240px container with a 20px gutter on phones, and logo-blue or navy bands run full bleed behind it. Sections open with a split header (headline left, lead paragraph right) on desktop and stack on phones. Sections are separated by generous space (88 to 120px) and joined by a thin vertical connector line with a dot, the plan's route from one area to the next.

Breakpoints follow the content: 560, 640, 760, 900, 980, 1000 and 1100px. Below 1000px the hero reorders to headline, explanation and buttons, then the call scene. Phones get a sun-yellow booking bar in thumb reach once the hero buttons scroll away; it hides near the form and the closing band, and the header button steps aside while it shows.

The plan grid (56px squares, logo blue at 9% opacity) exists only behind the top of the first screen, fading out from the top right. It never runs behind body content.

## Elevation & Depth

Depth is mostly flat: borders define surfaces and a short, offset lift raises them slightly off the sheet. Coloured bands, not shadows, create the big changes in depth.

### Shadow Vocabulary
- **Card lift** (`box-shadow: 0 1px 2px rgba(11,21,48,.06), 0 4px 8px -4px rgba(11,21,48,.16)`): every card, panel, form and the report sheet.
- **Booked halo** (`box-shadow: 0 0 0 3px rgba(46,139,87,.14), 0 4px 8px -4px rgba(11,21,48,.16)`): the Booked card and the call-back confirmation only.
- **Floating header** (`box-shadow: 0 1px 2px rgba(11,21,48,.05), 0 6px 12px -8px rgba(11,21,48,.22)`): the header bar once the page scrolls.
- **Checkpoint ring** (`box-shadow: 0 0 0 4–5px` of the dot colour at about 20%): dots on the call line, rail and connectors.

### Named Rules
**The Short Lift Rule.** Shadows are offset and short (8px blur or less). A border plus a wide soft blur is not used anywhere.

**The No Glow Rule.** No blurred colour glows. Rings around checkpoints are crisp and mean "this is a point on the route".

## Shapes

Friendly, soft corners on a sharp grid. Small parts use 6px (tags), controls 10px (buttons, inputs, nav items), cards 14px, dark panels 18px and the report sheet 22px. Pills and checkpoint dots are fully round. Lines are thin and straight (1.5 to 2px), with rounded caps on the call line. Marks such as ticks, crosses and plus signs are drawn in CSS or SVG, never typed characters.

## Components

### Buttons
Friendly, solid and unmistakable.
- **Shape:** gently rounded (10px), at least 48px tall.
- **Primary:** sun yellow with deep navy label at 700 weight (padding 12px 22px).
- **Hover / Focus:** pressed sun on hover, a slight press scale on click, a 2px logo-blue focus ring (white on blue sections).
- **Text link (secondary):** underlined navy text beside the primary ("See how it works"). There is no outlined or ghost button.

### Step Pills
- **Style:** white pill with a hairline border and a logo-blue dot (green when the step is booked or live). Used for "On the call", "Step 1", and the progress labels.

### Tags
- **Style:** plan-tint fill, 6px corners, label size. Used for qualified details on call cards ("15-year roof", "Claim filed").

### Cards / Containers
- **Corner Style:** 14px for cards, 18px for dark panels, 22px for the report sheet and form.
- **Background:** surface white on the page; deep navy for transcripts, follow-ups and the busy-day list.
- **Shadow Strategy:** card lift (see Elevation).
- **Border:** hairline on white cards; none on navy.
- **Internal Padding:** 14 to 20px; sheet 44 to 48px on desktop.
- **Labelling:** every card showing example data carries an "Example" label in its header or caption.

### Inputs / Fields
- **Style:** plan-tint fill, rule-steel 1px border, 10px corners, 50px tall, 16px text.
- **Focus:** white fill, logo-blue border and a soft 3px blue ring.
- **Error:** error-red border and a plain-language message under the field; a summary under the button.

### Navigation
- **Style:** small label-size links in slate text, 10px rounded hit areas; the active section gets a logo-blue tint and blue text.
- **Header:** flat on the white page at the top, becoming a floating white bar with the floating-header shadow on scroll. Book a demo always sits at the right.
- **Mobile:** a menu button opens the same links as large rows; the phone booking bar takes over the action while you read.

### The Call Line (signature)
The brand's route mark: a logo-blue line with checkpoint dots that carries a call from ring to booked. It appears as the hero's progress rail, the journey through How it works, the connectors between sections, and the phone hero track. Checkpoints fill blue as they are reached and turn green at Booked.

### The Call Scene (signature)
The hero's pinned scene plays one example call in four beats (ringing, answered, qualified, booked) as you scroll, with a scroll cue, autoplay after a pause, clickable rail steps and a skip link. Without motion it shows the four cards as a static diagram.

### The Report Sheet (signature)
The monthly report drawn as the document itself: a header with the business and month, the storm chart, then a ledger of counts with dotted leaders. Counts only; no money figures.

## Do's and Don'ts

### Do:
- **Do** keep the logo blue (#1E5BD8) and the logo exactly as specified.
- **Do** use sun yellow (#FFC233) with deep navy text for every primary action, and nothing else.
- **Do** show the product itself (calls, calendar slots, texts, the queue, the report) and label it as an example.
- **Do** use the Title role (1.375rem Archivo 600) for every card and step title.
- **Do** use the card lift shadow and hairline border for raised surfaces.
- **Do** keep the plan grid faint (9% logo blue) and only behind the top of the first screen.
- **Do** draw icons and marks in CSS or SVG with one stroke weight.
- **Do** make every animated element readable with motion off.

### Don't:
- **Don't** change, recolour or re-letter the logo, or use the logo blue at a different value.
- **Don't** use yellow for decoration, backgrounds or non-clickable highlights.
- **Don't** use green for anything that is not booked or successful.
- **Don't** bring back orange, a warm off-white page, or the pale blue-grey page ground.
- **Don't** use wide soft shadows, blurred colour glows or gradient text.
- **Don't** use thick coloured side bars on cards or list items.
- **Don't** use typed characters (×, +, ✓, emoji) as icons.
- **Don't** exceed 6rem for any text.
