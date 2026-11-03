import { test, expect } from '@playwright/test';

async function sitemapPaths(
  request: import('@playwright/test').APIRequestContext,
): Promise<string[]> {
  const index = await (await request.get('/sitemap-index.xml')).text();
  const maps = [...index.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => new URL(m[1]).pathname);
  const paths: string[] = [];
  for (const map of maps) {
    const xml = await (await request.get(map)).text();
    for (const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) paths.push(new URL(m[1]).pathname);
  }
  return paths;
}

test('every page in the sitemap is sound', async ({ page, request }) => {
  const paths = await sitemapPaths(request);
  expect(paths.length).toBeGreaterThan(0);
  const titles = new Set<string>();
  for (const path of paths) {
    const res = await page.goto(path);
    expect(res?.status(), path).toBe(200);
    await expect(page.locator('h1'), `${path} h1 count`).toHaveCount(1);
    const title = await page.title();
    expect(title, `${path} title`).not.toBe('');
    expect(titles.has(title), `${path} duplicate title`).toBe(false);
    titles.add(title);
    await expect(page.locator('link[rel="canonical"]'), `${path} canonical`).toHaveCount(1);
    const desc = await page.locator('meta[name="description"]').getAttribute('content');
    expect(desc, `${path} description`).toBeTruthy();
  }
});

test('404 page is served for unknown paths', async ({ request }) => {
  const res = await request.get('/definitely-not-a-page/');
  expect(res.status()).toBe(404);
});
