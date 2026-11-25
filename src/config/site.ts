// Single source of truth for anything that may change: links, contact details, legal text, prices.
// Values come from the legacy site.config.json. Two prices are shown on the site: PRICE_WEBSITE_PLAN (the main
// offer) and PRICE_FRONT_DESK (the add-on). No buyout price, no custom website price, no former or "% off" price.

export interface Site {
  brand: string;
  domain: string;
  CONTACT_EMAIL: string;
  CALENDLY_URL: string;
  FORM_ENDPOINT: string;
  /** The inspector demo line (answers as Keystone Home Inspections). Shown on /home-inspectors/ only; leave empty to hide. */
  DEMO_PHONE: string;
  OCTALOGIC_URL: string;
  company: string;
  companyAddress: string;
  governingLaw: string;
  legalLine: string;
  partnerLine: string;
  PRICE_FRONT_DESK: string;
  /** The main offer: the monthly website plan (terms v1.1, section 2). No setup fee, no free trial. */
  PRICE_WEBSITE_PLAN: string;
  /** Rename the plan here only. Always pair it with PLAN_LINE; never let the name stand alone as a promise. */
  PLAN_NAME: string;
  /** What the plan is, in one plain line. Never implies a result (rankings, calls, AI recommendations). */
  PLAN_LINE: string;
  /** What "AI Ready" means, for places that need a definition. */
  PLAN_DEFINITION: string;
  /** The name on receipts and PayPal. */
  PLAN_BILLING_NAME: string;
  /** Custom websites (Business, Signature) are hidden until the owner switches them back on. Code and copy stay. */
  SHOW_CUSTOM_WEBSITES: boolean;
  /** AI automation is shown only as a footer line. true brings back its home block and pricing row. */
  SHOW_AUTOMATION: boolean;
  /** Octalogic mentions (Built by section, footer partner line, copy) stay hidden until the partners agree. */
  SHOW_OCTALOGIC: boolean;
  /** Home hero headline, plus the backup to switch to only if Carlton asks. */
  HERO_HEADLINE: string;
  HERO_SUB: string;
  HERO_HEADLINE_BACKUP: string;
  /** Product described without a personal name on the site; each client can still name their own front desk. */
  FRONT_DESK_NAME: string;
  /** Empty means no analytics script is rendered. */
  ANALYTICS_TOKEN: string;
}

const company = 'Hallmark Data Systems Pvt Ltd';
/** The plan name: change it here and every page follows. */
const planName = 'AI Ready';
const companyAddress = '3rd Floor, Sunivas Building, St Inez, Panaji, Goa 403001, India';

export const SITE: Site = {
  brand: 'Crewwise',
  domain: 'https://crewwisehq.com',
  CONTACT_EMAIL: 'hello@crewwisehq.com',
  CALENDLY_URL: 'https://calendly.com/roswald-crewwisehq/crewwise-demo',
  FORM_ENDPOINT: 'https://formspree.io/f/xqpepyyw',
  DEMO_PHONE: '(813) 993-1087',
  OCTALOGIC_URL: 'https://octalogic.tech',
  company,
  companyAddress,
  governingLaw: 'the laws of India, and the courts of Goa, India have exclusive jurisdiction',
  legalLine: `Crewwise is a brand of ${company} · ${companyAddress}`,
  partnerLine:
    'Need a bigger build or an engineering team? Our engineering partner Octalogic does that.',
  PRICE_FRONT_DESK: 'From $299/month',
  PRICE_WEBSITE_PLAN: '$99/month',
  PLAN_NAME: planName,
  PLAN_LINE:
    'Your website, plus your listings on Google, Bing, Apple Maps and ChatGPT set up and kept up to date.',
  PLAN_DEFINITION:
    `${planName} means the places AI assistants and maps read about your business are set up and correct.`,
  PLAN_BILLING_NAME: `Crewwise ${planName}`,
  SHOW_CUSTOM_WEBSITES: false,
  SHOW_AUTOMATION: false,
  SHOW_OCTALOGIC: false,
  HERO_HEADLINE: 'Get AI Ready for $99 a month.',
  HERO_SUB: 'We build your web presence for the AI era, so ChatGPT, Google and Siri have more reasons to mention you.',
  HERO_HEADLINE_BACKUP: 'Win the first minute with every new client.',
  FRONT_DESK_NAME: 'AI front desk',
  ANALYTICS_TOKEN: '',
};

/** "AI Ready website plan": the name with the plain words beside it, for nav, form and titles. */
export const PLAN_LABEL = `${SITE.PLAN_NAME} plan`;

/**
 * Black Friday banner (owner decision 2026-11-25, review options A + C). The banner is rendered hidden and a script
 * reveals it only before PROMO.endsAt, so a static build never shows a deadline that has passed.
 * The displayed date is formatted from endsAt, so the weekday cannot disagree with the instant.
 */
export const PROMO = {
  /** End of the offer: 23:59:59 US Eastern (EST, UTC-5) on 2026-12-01. */
  endsAt: '2026-12-01T23:59:59-05:00',
  lockMonths: 24,
  href: '/pricing/#websites',
  linkText: 'See the plan',
};
export const PROMO_DEADLINE = new Date(PROMO.endsAt).toLocaleDateString('en-US', {
  weekday: 'long',
  month: 'long',
  day: 'numeric',
  timeZone: 'America/New_York',
});

export const PARTNER_LINK_TEXT = 'Octalogic';

/** Who builds the websites, worded to respect SHOW_OCTALOGIC. */
export const BUILDER = SITE.SHOW_OCTALOGIC ? 'Octalogic’s engineers' : 'our engineers';

/** Pages listed in llms.txt (path, title, one-line description). Phase 2 pages are added when they exist. */
export interface PageEntry {
  path: string;
  title: string;
  description: string;
}

export const PAGES: PageEntry[] = [
  {
    path: '/',
    title: 'Home',
    description: `The ${planName} plan: your website and your listings, and the AI front desk you can add when you miss calls.`,
  },
  {
    path: '/pricing/',
    title: 'Pricing',
    description: `What the ${planName} plan includes and costs, and the price of the AI front desk.`,
  },
  {
    path: '/free-audit/',
    title: 'Get started',
    description: `Ask for the ${planName} plan, or a free audit of your website and phone line.`,
  },
  {
    path: '/home-inspectors/',
    title: 'Home inspectors',
    description: 'The AI front desk for home inspectors, including busy season.',
  },
  { path: '/terms/', title: 'Client terms', description: 'The Crewwise client terms for the website plan, the AI front desk and websites.' },
  {
    path: '/privacy/',
    title: 'Privacy policy',
    description: 'What Crewwise collects and your choices.',
  },
  {
    path: '/refunds/',
    title: 'Refund and cancellation policy',
    description: 'How canceling and refunds work.',
  },
];

export const absoluteUrl = (path: string): string => new URL(path, SITE.domain).toString();
