// Renders og/og-template.html at 1200x630 and saves public/og.jpg (and design/collateral/og.jpg).
// Usage: npm install, then npm run og
// Uses playwright-core with your installed Chrome or Edge; no browser download needed.
import { chromium } from 'playwright-core';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';
import { copyFileSync, statSync } from 'node:fs';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const template = pathToFileURL(join(root, 'og', 'og-template.html')).href;
const out = join(root, 'public', 'og.jpg');

async function launch() {
  for (const channel of ['chrome', 'msedge']) {
    try { return await chromium.launch({ channel }); } catch {}
  }
  return chromium.launch(); // falls back to a Playwright-managed Chromium if one is installed
}

const browser = await launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
await page.goto(template);
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: out, type: 'jpeg', quality: 85, clip: { x: 0, y: 0, width: 1200, height: 630 } });
await browser.close();

copyFileSync(out, join(root, 'design', 'collateral', 'og.jpg'));
console.log(`Saved public/og.jpg (${Math.round(statSync(out).size / 1024)} KB, 1200x630)`);
