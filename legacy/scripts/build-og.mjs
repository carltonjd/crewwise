// Renders og/og-template.html at 1200x630, once per page in content.py, into public/ and design/collateral/.
// Each page's og_image (e.g. og-roofing.jpg), og_headline and og_sub decide the file name and text.
// Usage: npm install, then npm run og
// Uses playwright-core with your installed Chrome or Edge; no browser download needed.
import { chromium } from 'playwright-core';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';
import { copyFileSync, statSync, mkdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const template = pathToFileURL(join(root, 'og', 'og-template.html')).href;
const pages = JSON.parse(execFileSync('python', ['-c',
  'import json, content; print(json.dumps([dict(file=p["og_image"].split("?")[0], h=p["og_headline"], s=p["og_sub"]) for p in content.PAGES]))'],
  { cwd: root, encoding: 'utf-8' }));

async function launch() {
  for (const channel of ['chrome', 'msedge']) {
    try { return await chromium.launch({ channel }); } catch {}
  }
  return chromium.launch(); // falls back to a Playwright-managed Chromium if one is installed
}

const browser = await launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
mkdirSync(join(root, 'public'), { recursive: true });
for (const { file, h, s } of pages) {
  const out = join(root, 'public', file);
  await page.goto(`${template}?h=${encodeURIComponent(h)}&s=${encodeURIComponent(s)}`);
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out, type: 'jpeg', quality: 85, clip: { x: 0, y: 0, width: 1200, height: 630 } });
  copyFileSync(out, join(root, 'design', 'collateral', file));
  console.log(`Saved public/${file} (${Math.round(statSync(out).size / 1024)} KB, 1200x630)`);
}
await browser.close();
