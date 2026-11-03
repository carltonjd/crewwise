import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  reporter: process.env.CI ? 'github' : 'list',
  use: { baseURL: 'http://localhost:4329' },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
  // Builds the site, then serves dist on its own port, :4329, never reusing another project's server.
  webServer: {
    command: 'pnpm build && pnpm exec astro preview --port 4329',
    url: 'http://localhost:4329/',
    reuseExistingServer: false,
    timeout: 180_000,
  },
});
