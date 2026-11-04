import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const legal = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/legal' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    updated: z.coerce.date(),
  }),
});

const industries = defineCollection({
  loader: glob({ pattern: '*.{md,mdx}', base: './src/content/industries' }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    heroLine: z.string(),
    deskHandles: z.string(),
    description: z.string(),
  }),
});

const faqs = defineCollection({
  loader: glob({ pattern: '*.{md,mdx}', base: './src/content/faqs' }),
  schema: z.object({
    question: z.string(),
    answer: z.string(),
    group: z.string().optional(),
    order: z.number().default(0),
  }),
});

const nameText = z.object({ title: z.string(), text: z.string() });
const speakerLine = z.object({ text: z.string(), speaker: z.enum(['ai', 'caller']) });

// Structured page copy (frontmatter only). Strings may contain the token {{PRICE_FRONT_DESK}}; resolve it from SITE.
const pages = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/pages' }),
  schema: z.object({
    slug: z.string(),
    path: z.string(),
    seo: z.object({
      title: z.string(),
      description: z.string(),
      ogTitle: z.string(),
      ogDescription: z.string(),
      ogImage: z.string(),
      ogAlt: z.string(),
      ogHeadline: z.string(),
      ogSub: z.string(),
    }),
    service: z.object({ name: z.string(), type: z.string() }),
    hero: z.object({ eyebrow: z.string(), h1: z.string(), sub: z.string() }),
    exampleCaption: z.string(),
    leaks: z.object({
      title: z.string(),
      intro: z.string(),
      items: z.array(z.object({ problem: z.string(), detail: z.string(), fix: z.string() })),
    }),
    whatHappens: z.object({
      title: z.string(),
      moments: z.array(z.object({ time: z.string(), label: z.string(), items: z.array(nameText) })),
    }),
    stormMode: z.object({
      id: z.string(),
      nav: z.string(),
      mode: z.string(),
      title: z.string(),
      copy: z.string(),
      note: z.string(),
      report: z.array(z.object({ label: z.string(), value: z.string() })),
      reportFootnote: z.string(),
      stripBooked: z.string(),
    }),
    plan: z.object({ name: z.string(), founding: z.string(), priceNote: z.string() }),
    faq: z.object({
      title: z.string(),
      items: z.array(z.object({ question: z.string(), answer: z.string() })),
    }),
    closing: z.string(),
    tagline: z.string(),
    example: z.object({
      business: z.string(),
      issue: z.string(),
      facts: z.array(z.string()),
      rules: z.array(z.object({ label: z.string(), value: z.string() })),
      ariaDescription: z.string(),
      callerCard: z.string(),
      jobCard: z.string(),
      call: z.array(speakerLine),
      chips: z.array(z.string()),
      calendar: z.object({ busy: z.string(), event: z.string(), where: z.string() }),
      sms: z.string(),
      urgentCall: z.array(speakerLine),
      urgentChips: z.array(z.string()),
      webLead: z.object({
        day: z.string(),
        busy: z.array(z.string()),
        event: z.array(z.string()),
        after: z.string(),
        sms: z.string(),
        reply: z.string(),
        note: z.string(),
      }),
      followups: z.array(z.object({ label: z.string(), text: z.string(), kind: z.string() })),
      queue: z.array(
        z.object({
          priority: z.string(),
          level: z.string(),
          title: z.string(),
          detail: z.string(),
          slot: z.string(),
          status: z.string(),
        }),
      ),
    }),
  }),
});

export const collections = { legal, industries, faqs, pages };
