# Crewwise website

Static site. Everything brand-specific (name, domain, phones, email, links, price, company, address, analytics token) lives in `site.config.json`.

## Build
    python build.py
Writes the site to `public/`.

## Deploy (Cloudflare Pages)
Build command: `python build.py`. Output directory: `public`. `_redirects` sends /roofers, /roofers/, /roofer and /roofer/ to /roofing/ (301). `404.html`, `robots.txt` and `sitemap.xml` are generated.

## Files
- `assets/style.css`, `assets/main.js`: the design (tokens at the top of style.css)
- `content.py`: the text of every trade page, one block per page (`HOME`, `ROOFING`)
- `build.py`: the shared trade page template, legal pages, sitemap, redirects
- `design/`: direction, critique log, screenshots, social card source (`design/collateral/og.html`), archive of earlier versions

Legal pages are drafts to be reviewed by a lawyer.

## Pages
- `/` (`HOME` in content.py): the general home-service page. Its hero links to the live trade pages.
- `/roofing/` (`ROOFING`): the roofer page. Today we only sell to roofers, so this is the only trade page.

Both are rendered by `trade_page()` in build.py, so layout changes apply to every page at once.

## Adding a trade page (for example /plumbing/)
Only do this once you actually sell to that trade.

1. In `content.py`, copy the `ROOFING` block and rename it `PLUMBING`.
2. Change `slug='plumbing'`, `path='/plumbing/'`, `og_image='og-plumbing.jpg?v=1'`, and every text field: title, description, og and twitter text, eyebrow, h1, sub, leaks, moments, the busy-day section (`busy_id`, `busy_nav`, `busy_mode`, title, copy), report labels, plan name, FAQ, closing line, tagline, `og_headline` and `og_sub`.
3. Give it its own example screens: copy `ROOF_EXAMPLE` to `PLUMB_EXAMPLE` with a made-up plumbing business, call, calendar, texts and queue, and set `example=PLUMB_EXAMPLE`.
4. Add it to `PAGES = [HOME, ROOFING, PLUMBING]`. The sitemap, canonical URL and share-image copy pick it up from there.
5. On the homepage (`HOME`), add a link to `trade_row` and update the hero note and meta description so they no longer say roofing is the only live trade.
6. `build.py` refuses pages that contain trade words we don't sell to yet (`check()`, e.g. 'lumbing'). Remove that word from the list when the page goes live.
7. Run `npm run og` (renders `og-plumbing.jpg`), then `python build.py`.

## Social share images
One per page, rendered from `og/og-template.html` with each page's `og_headline` and `og_sub`. Run `npm install` (once) and `npm run og`; it writes `public/og.jpg`, `public/og-roofing.jpg` and so on, plus copies in `design/collateral/`. When an image changes, bump `?v=` on that page's `og_image` in content.py so WhatsApp fetches the new one.
