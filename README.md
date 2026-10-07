# Crewwise website

Static site. Everything brand-specific (name, domain, phones, email, links, price, company, address, analytics token) lives in `site.config.json`.

## Build
    python build.py
Writes the site to `public/`.

## Deploy (Cloudflare Pages)
Build command: `python build.py` · Output directory: `public`. `_redirects` sends /roofers to /. `404.html`, `robots.txt` and `sitemap.xml` are generated.

## Files
- `assets/style.css`, `assets/main.js`: the design (tokens at the top of style.css)
- `build.py`: page content and templates
- `design/`: direction, critique log, screenshots, social card source (`design/collateral/og.html`), archive of earlier versions

Legal pages are drafts to be reviewed by a lawyer.

## Social share image
Edit `og/og-template.html`, then run `npm install` (once) and `npm run og` to regenerate `public/og.jpg`. Bump `?v=` on `og_image` in `site.config.json` each time so WhatsApp fetches the new image.
