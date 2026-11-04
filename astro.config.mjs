// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import { unified } from '@astrojs/markdown-remark';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import remarkSiteTokens from './src/lib/remark-site-tokens.mjs';

// https://astro.build/config
export default defineConfig({
  site: 'https://crewwisehq.com',
  output: 'static',
  // URLs keep the existing style: /roofing/, /pricing/, ...
  trailingSlash: 'always',
  build: { format: 'directory' },
  markdown: { processor: unified({ remarkPlugins: [remarkSiteTokens] }) },
  integrations: [mdx(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
