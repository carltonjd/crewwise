// Single source of truth for anything that may change: links, contact details, legal text, prices.
// Values come from the legacy site.config.json. The ONLY price shown on the site is PRICE_FRONT_DESK.

export interface Site {
  brand: string;
  domain: string;
  CONTACT_EMAIL: string;
  CALENDLY_URL: string;
  FORM_ENDPOINT: string;
  /** Leave empty and hidden until a non-roofing demo line exists. */
  DEMO_PHONE: string;
  OCTALOGIC_URL: string;
  company: string;
  companyAddress: string;
  governingLaw: string;
  legalLine: string;
  partnerLine: string;
  PRICE_FRONT_DESK: string;
  /** Octalogic mentions (Built by section, footer partner line, copy) stay hidden until the partners agree. */
  SHOW_OCTALOGIC: boolean;
  /** Home hero headline, plus the backup to switch to only if Carlton asks. */
  HERO_HEADLINE: string;
  HERO_HEADLINE_BACKUP: string;
  /** Product described without a personal name on the site; each client can still name their own front desk. */
  FRONT_DESK_NAME: string;
  /** Empty means no analytics script is rendered. */
  ANALYTICS_TOKEN: string;
}

const company = 'Hallmark Data Systems Pvt Ltd';
const companyAddress = '3rd Floor, Sunivas Building, St Inez, Panaji, Goa 403001, India';

export const SITE: Site = {
  brand: 'Crewwise',
  domain: 'https://crewwisehq.com',
  CONTACT_EMAIL: 'hello@crewwisehq.com',
  CALENDLY_URL: 'https://calendly.com/roswald-crewwisehq/crewwise-demo',
  FORM_ENDPOINT: 'https://formspree.io/f/xqpepyyw',
  DEMO_PHONE: '',
  OCTALOGIC_URL: 'https://octalogic.tech',
  company,
  companyAddress,
  governingLaw: 'the laws of India, and the courts of Goa, India have exclusive jurisdiction',
  legalLine: `Crewwise is a brand of ${company} · ${companyAddress}`,
  partnerLine:
    'Need a bigger build or an engineering team? Our engineering partner Octalogic does that.',
  PRICE_FRONT_DESK: 'From $299/month',
  SHOW_OCTALOGIC: false,
  HERO_HEADLINE: 'Win the first minute with every new client.',
  HERO_HEADLINE_BACKUP: 'Make a great first impression, online and on the phone.',
  FRONT_DESK_NAME: 'AI front desk',
  ANALYTICS_TOKEN: '',
};

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
  { path: '/', title: 'Home', description: 'What Crewwise is and the three services.' },
  { path: '/pricing/', title: 'Pricing', description: 'What the AI front desk costs and how pricing works.' },
  {
    path: '/free-audit/',
    title: 'Free audit',
    description: 'Request a free audit of your website and phone line.',
  },
  {
    path: '/roofing/',
    title: 'Roofing',
    description: 'The AI front desk for roofing companies, including Storm Mode.',
  },
  { path: '/terms/', title: 'Terms of service', description: 'The terms for using Crewwise.' },
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
