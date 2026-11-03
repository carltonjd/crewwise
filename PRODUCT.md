# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two audiences, one site (the AI front desk is described without a personal name; each client can choose a name for their own):

- **Home-service companies:** HVAC, plumbing, roofing, electrical and cleaning businesses, usually owner-operators with small crews. The owner is on a job when the next customer calls; calls go to voicemail, web enquiries get answered that evening, quotes go unchased, and the customer books someone else.
- **Small professional firms:** law firms, architects and accounting firms. No medical practices or clinic examples anywhere for now (patient calls bring US health privacy rules not yet set up). A new client enquiry deserves a reply in minutes; partners are in meetings or with clients, so enquiries wait and go cold.

Both read the site on a phone, between jobs or meetings, short on time and wary of hype. The hero must feel calm and credible to a lawyer and still friendly to a plumber.

Core idea (owner brief, 2026-11-02): new clients decide in their first minute of contact, a glance at the website and then a call. Crewwise covers that whole minute: a website that makes the business easy to choose and an AI front desk that answers every call. Hero headline: "Win the first minute with every new client." (backup in constants).

## Product Purpose

Crewwise is the tech crew a small business never had to hire: a done-for-you tech partner that sells three services under its own name.

- **The AI front desk:** answers every call 24/7, books appointments, captures the caller's details, flags urgent calls and follows up.
- **Websites:** modern, fast, phone-friendly websites with clear call and booking buttons, designed and built by Octalogic's engineers.
- **AI automation:** a free 30-minute AI audit call, then automations that take repetitive manual work off a team (for example, matching purchase orders to invoices).

The website's single job is to push every visitor towards one action: the free audit (`/free-audit`, Formspree form). Booking a call (Calendly) is the secondary route.

## Positioning

- **Your crew:** "Crew" means the people and tools working on the owner's behalf. Done for you: we set it up, we tune it, we report back monthly.
- **Jobs are lost in the first few minutes,** long before anyone compares quotes: slow mobile site, missed call, late reply, no follow-up. Crewwise covers those minutes.
- **Built by real engineers:** Octalogic (founded 2017, Goa; 40+ engineers; clients in more than 10 countries; longest client relationship 8 years). ON HOLD: every Octalogic mention is hidden behind `SHOW_OCTALOGIC` (off) until Carlton confirms the partners agree.
- **Pricing on the site:** only "from $299/month" for the AI front desk. No other prices are shown anywhere (owner decision 2026-11-01). Website and automation work is scoped after the free audit.

Octalogic's extended engineering teams and product builds are not sold here; they get one footer line linking to https://octalogic.tech.

## Operating Context

- The AI front desk works with the business's existing website and number: calls forward to it when unanswered or after hours, the owner chooses. It says it is an AI assistant if a caller asks. On law-firm calls it never gives legal advice.
- Setup: about a week for the AI front desk, about 10 days for a new website, two rounds of changes included. Texting switches on once the number is registered with carriers, usually 1 to 3 weeks.
- Free audit: we review the website and Google profile, call the line like a customer would, and send what we found (within two business days, pending confirmation).
- Monthly check-in: a short report on what came in and what was followed up.

## Capabilities and Constraints

- Site: Astro 7, static output, Tailwind 4, MDX content, TypeScript; deployed on Cloudflare Workers static assets from `dist/`. All prices, links, phone numbers and emails live in `src/config/site.ts`.
- Phase 1 pages: `/`, `/pricing`, `/free-audit`, `/roofing` (existing copy incl. Storm Mode), `/terms`, `/privacy`, `/refunds`. Phase 2: `/ai-front-desk`, `/websites`, `/ai-automation`, `/hvac`, `/plumbing`, `/law-firms`, `/accounting-firms`, `/about`. Never link to a page that doesn't exist yet; no "coming soon".
- Company: Crewwise is a brand of Hallmark Data Systems Pvt Ltd, Panaji, Goa, India. Never say or imply US-based. Footer legal line is fixed text.
- No demo phone number until a non-roofing demo line exists. No recorded sample call yet: the example call on the page is a read-along transcript until a recorded sample exists.
- Must be SEO and AI-search ready: unique titles/descriptions, canonical, OG, sitemap, JSON-LD, llms.txt, all crawlers allowed.
- Accessibility: one H1 per page, AA contrast, visible focus, reduced motion respected. Fast: no heavy libraries for simple effects.
- Never push to GitHub without the user's explicit approval for that push.

## Brand Commitments

- Name: Crewwise (capital C in text; the lowercase wordmark is logo-only). Domain crewwisehq.com, email hello@crewwisehq.com.
- No personal name for the AI front desk on the site (owner decision 2026-11-02): it is described as the AI front desk to avoid confusion.
- Owner decision (2026-11-03): the hero action stays a button linking to `/free-audit/`. This is an exception to mode-persuade's "action in working form"; the form page is the dedicated surface for the audit request.
- Logo: existing files in `design/brand/crewwise-brand-assets/`, unchanged unless the owner confirms the refined version.
- Fixed palette (brief, 2026-11-01): navy `#0F1B33` (text, dark sections), Crewwise blue `#1E5BD8` (brand, links, accents), light blue `#8FB3FF` (accents on navy only), soft background `#F4F7FC`, white `#FFFFFF`, action orange `#C94708` (primary buttons only), success green `#1F7547` (success states only). Derived tints for cut-paper planes: blue-deep `#1749B0` (hero floor, pressed states) and `--blue-sheet` = `color-mix(in oklab, blue-deep, navy 30%)` (the hero's offset sheet; documented in `src/styles/global.css`). Every text/background pair meets WCAG AA.
- Fixed type: Hanken Grotesk throughout; bold to extra-bold headlines with tight tracking, never tighter than -0.04em; regular to medium body; body measure under about 75 characters.
- Standing preference (owner, 2026-11-01, after three direction rounds): a clean, premium product site, the category standard executed at top craft, executed in a cut-paper world (owner confirmed 2026-11-03): flat Crewwise blue fields, navy and white shapes with slightly irregular hand-cut edges, depth from overlapping flat planes and one soft paper shadow, no photographs or screenshots. Bar: Goodcall (labelled example call that plays), Avoca (timestamped call timeline), Dialzara (plain receptionist headline); the price lands with the AI front desk details in the services section. Lead with the AI front desk, an AI receptionist for any business; websites and AI automation shown as part of the same offer.
- Everything else (layout, composition, texture, motion, imagery approach) is open; the owner wants a bold, incredible showpiece with brilliant motion, while boldness is spent mostly on the hero call moment.
- Avoid: identical rounded cards in endless grids, gradient washes, stock photos, fake product screenshots, a single highlighted word in a headline, all-caps labels, eyebrow labels above headings (banned outright).
- Voice: plain, direct, practical, for a busy owner on a phone. Short sentences, specific over clever, confident never hypey. Sentence case for headings and buttons. Buttons say exactly what happens ("Get my free audit", "Book a call"). No "it's not X, it's Y", no "the difference between X and Y", no tidy triads in running copy, no clipped two-word closers, no buzzwords (leverage, unlock, supercharge, seamless, cutting-edge, game-changer, revolutionise), no meta strings joined by middle dots (the one exception is the fixed legal line in the footer), no "→" on buttons, no em or en dashes in copy.

## Evidence on Hand

No customers, testimonials, ratings, call recordings, case studies, results or client logos yet. Safe facts: Octalogic founded 2017, Goa; 40+ engineers; clients in more than 10 countries (never list them); longest client relationship 8 years. Never name clients (including TKO or UFC). Never promise rankings, leads, revenue or percentage savings. Example screens and transcripts are synthetic and labelled as examples.

## Product Principles

1. Honest before impressive: every example labelled, every claim something we do today.
2. One action: every page leads to the free audit.
3. Speak the customer's day: on a job, mid-install, burst pipe at 9 PM, tax season; never generic AI talk.
4. The first few minutes: frame everything around the moment a customer reaches out.
5. Done for you: low effort, keep your number, keep your site, we set it up.
