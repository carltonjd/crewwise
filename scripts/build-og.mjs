// Builds the Open Graph share images (1200x630 JPEG) into public/ in the site's cut-paper style.
// Usage: pnpm og   (needs Playwright's chromium: pnpm exec playwright install chromium)
import { chromium } from '@playwright/test';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { readFileSync } from 'node:fs';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const fontUrl = 'data:font/woff2;base64,' + readFileSync(join(root, 'node_modules/@fontsource-variable/hanken-grotesk/files/hanken-grotesk-latin-wght-normal.woff2')).toString('base64');
// the real logo (outlined wordmark), inlined from the brand file
const logo = readFileSync(join(root, 'public/brand/crewwise-logo-on-blue.svg'), 'utf8')
  .replace(/<title>.*?<\/title>/, '')
  .replace(/width="190" height="44"/, 'width="167" height="39"');

const C = { blue: '#1E5BD8', deep: '#1749B0', sheet: '#163B88', navy: '#0F1B33' };

// hand-cut planes: slightly irregular edges, one nicked top-right corner each
const poly = (pts, fill) => `<polygon points="${pts}" fill="${fill}"/>`;

const pages = [
  {
    file: 'og.jpg',
    headline: 'Win the first minute with every new client.',
    sub: 'An AI front desk that answers every call, day or night, and a website clients choose.',
    size: 84,
    planes: [
      poly('560,631 640,402 905,318 1186,262 1201,276 1201,631', C.deep),
      poly('868,631 905,150 1176,118 1201,136 1201,631', C.sheet),
      poly('1010,631 1040,60 1186,-2 1201,-2 1201,631', C.navy),
    ],
    slip: { x: 780, y: 372, w: 340, title: 'Consultation booked', line: 'Thu 10:00 AM', rot: -3 },
  },
  {
    file: 'og-pricing.jpg',
    headline: 'Simple pricing, set up for you',
    sub: 'One monthly price for the AI front desk. Websites are scoped in your free audit.',
    size: 88,
    planes: [
      poly('-2,520 300,470 640,540 980,455 1201,500 1201,631 -2,631', C.deep),
      poly('760,-2 1201,-2 1201,380 1060,396 1002,300 786,210', C.sheet),
      poly('930,-2 1201,-2 1201,226 1172,196 1110,236 990,120', C.navy),
    ],
    slip: { x: 790, y: 300, w: 340, title: 'AI front desk', line: 'From $299/month', rot: 3 },
  },
  {
    file: 'og-free-audit.jpg',
    headline: 'Get a free audit',
    sub: 'Tell us a little about your business, and we’ll check it the way a new customer would.',
    size: 112,
    planes: [
      poly('700,631 760,330 1030,270 1201,300 1201,631', C.deep),
      poly('-2,600 -2,470 210,500 470,462 720,560 760,631 -2,631', C.sheet),
      poly('940,631 982,214 1170,176 1201,196 1201,631', C.navy),
    ],
    slip: { x: 760, y: 120, w: 340, title: 'Your free audit', line: 'In your inbox within two business days', rot: -2 },
  },
  {
    file: 'og-roofing.jpg',
    headline: 'Answers your phone while you’re on the roof.',
    sub: 'AI front desk for roofing companies',
    size: 80,
    planes: [
      poly('-2,631 -2,540 230,500 520,420 830,330 1130,170 1186,112 1201,128 1201,631', C.deep),
      poly('420,631 700,500 960,390 1201,300 1201,631', C.sheet),
      poly('780,631 1010,520 1201,452 1201,631', C.navy),
    ],
    slip: null,
  },
];

const html = (p) => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:'Hanken';src:url('${fontUrl}') format('woff2');font-weight:100 900}
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;background:${C.blue};font-family:'Hanken',sans-serif;position:relative;color:#fff}
svg.bg{position:absolute;inset:0}
.logo{position:absolute;left:64px;top:56px;line-height:0}
.logo svg{width:167px;height:39px}
.copy{position:absolute;left:64px;top:140px;width:${p.slip ? 700 : 900}px}
h1{font-size:${p.size}px;font-weight:850;line-height:.96;letter-spacing:-0.04em;text-wrap:balance}
.sub{margin-top:28px;font-size:28px;font-weight:550;line-height:1.3;color:rgba(255,255,255,.88);width:${p.slip ? 600 : 640}px}
.url{position:absolute;left:64px;bottom:48px;font-size:22px;font-weight:650;color:rgba(255,255,255,.86);letter-spacing:.01em}
.slip{position:absolute;left:${p.slip?.x}px;top:${p.slip?.y}px;width:${p.slip?.w}px;background:#fff;color:${C.navy};border-radius:12px;padding:24px 28px;
 transform:rotate(${p.slip?.rot}deg);box-shadow:0 1px 2px rgba(15,27,51,.16),0 18px 36px -10px rgba(15,27,51,.45)}
.slip b{display:block;font-size:30px;font-weight:800;letter-spacing:-0.02em}
.slip span{display:block;margin-top:6px;font-size:24px;font-weight:650;color:rgba(15,27,51,.8);line-height:1.25}
</style></head><body>
<svg class="bg" width="1200" height="630" viewBox="0 0 1200 630">${p.planes.join('')}</svg>
<div class="logo">${logo}</div>
<div class="copy"><h1>${p.headline}</h1><p class="sub">${p.sub}</p></div>
${p.slip ? `<div class="slip"><b>${p.slip.title}</b><span>${p.slip.line}</span></div>` : ''}
<div class="url">crewwisehq.com</div>
</body></html>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
for (const p of pages) {
  await page.setContent(html(p));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: join(root, 'public', p.file), type: 'jpeg', quality: 88, clip: { x: 0, y: 0, width: 1200, height: 630 } });
  console.log('wrote public/' + p.file);
}
await browser.close();
