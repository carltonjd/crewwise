# Crewwise website

Astro 7 static site (Tailwind 4, MDX, sitemap). The previous Python generator and its output are in `legacy/` for reference. Nothing in `legacy/` is built or deployed.

## Develop
Needs Node 24 (`.nvmrc`) and pnpm 10.

    pnpm install
    pnpm dev          # http://localhost:4321
    pnpm build        # writes dist/
    pnpm preview
    pnpm check        # astro check (types)
    pnpm lint         # eslint
    pnpm format       # prettier
    pnpm test         # vitest (unit)
    pnpm test:e2e     # playwright smoke test: builds, previews, checks every sitemap page

Astro 7 refuses to run on Node older than 22.23.4, so use Node 24 locally too.
First time running the e2e test: `pnpm exec playwright install chromium`.

## Where things live
- `src/config/site.ts`: every constant that may change (brand, domain, email, Calendly, form endpoint, demo phone, Octalogic link, legal line, partner line, the one price `PRICE_FRONT_DESK`). The only price on the site is "From $299/month".
- `src/content/legal/*.md`: Terms, Privacy, Refunds (rendered by `src/pages/[legal].astro`). `{{PRICE_FRONT_DESK}}` in Markdown is replaced from `site.ts` at build time.
- `src/content/pages/roofing.md`: structured roofing copy (frontmatter) for the page to render.
- `src/content/industries`, `src/content/faqs`: empty collections ready for Phase 2.
- `src/components/Seo.astro`, `JsonLd.astro`, `src/lib/jsonld.ts`: meta tags and structured data helpers.
- `src/pages/robots.txt.ts`, `llms.txt.ts`: generated at build. Add new pages to `PAGES` in `site.ts` so they appear in `llms.txt`.
- `public/`: static files (logos, icons, OG images, `_redirects`, IndexNow key file).

## Deploy (Cloudflare Workers static assets)
`wrangler.jsonc` serves `./dist` with `not_found_handling: "404-page"` (uses `404.html`).

Dashboard build settings (Workers Builds) must change from the old Python setup:
- Build command: `pnpm build` (was `python build.py`)
- Deploy command: `npx wrangler deploy`
- Node version: 24 (set `NODE_VERSION=24` in build variables if the `.nvmrc` is not picked up)
- Output / assets directory: `dist` (set in `wrangler.jsonc`, was `public`)
- pnpm is detected from `packageManager` in `package.json`.

`public/_redirects` sends /roofers and /roofer (with and without trailing slash) to /roofing/ (301).

## IndexNow
After a deploy, notify search engines of the current URLs:

    pnpm build
    pnpm indexnow

It reads `dist/sitemap-index.xml` and POSTs the URLs to api.indexnow.org. The key file is `public/<key>.txt`; it must be live on the site before you run this.

## Social share images (legacy)
`pnpm og` runs the old generator in `legacy/scripts/build-og.mjs`. It still depends on the Python `content.py` and `site.config.json` layout from before the move, so it needs those paths fixed before it works again. Current images are `public/og.jpg` and `public/og-roofing.jpg`.

Legal pages are drafts to be reviewed by a lawyer.
