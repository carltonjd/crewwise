// Submits every URL in the built sitemap to IndexNow. Run manually after a deploy: pnpm indexnow
// Reads dist/sitemap-index.xml (and the sitemaps it lists). The key file lives in public/<key>.txt.
import { readFileSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
const host = 'crewwisehq.com';

const keyFile = readdirSync(join(root, 'public')).find((f) => /^[0-9a-f]{32}\.txt$/.test(f));
if (!keyFile) throw new Error('No IndexNow key file (<32 hex>.txt) found in public/');
const key = keyFile.replace('.txt', '');

const locs = (xml) => [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const read = (url) => readFileSync(join(dist, new URL(url).pathname), 'utf-8');

const urlList = locs(read(`https://${host}/sitemap-index.xml`)).flatMap((sm) => locs(read(sm)));
if (urlList.length === 0) throw new Error('No URLs found in dist sitemap. Run pnpm build first.');

const res = await fetch('https://api.indexnow.org/IndexNow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify({ host, key, keyLocation: `https://${host}/${key}.txt`, urlList }),
});
console.log(`IndexNow: submitted ${urlList.length} URLs, response ${res.status} ${res.statusText}`);
if (!res.ok && res.status !== 202) process.exit(1);
