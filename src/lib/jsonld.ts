import { SITE, absoluteUrl, PLAN_LABEL } from '../config/site';

export type JsonLdObject = Record<string, unknown>;

export const organizationJsonLd = (): JsonLdObject => ({
  '@context': 'https://schema.org',
  '@type': 'Organization',
  '@id': `${SITE.domain}/#organization`,
  name: SITE.brand,
  url: SITE.domain,
  logo: absoluteUrl('/icon-512.png'),
  email: SITE.CONTACT_EMAIL,
  contactPoint: { '@type': 'ContactPoint', email: SITE.CONTACT_EMAIL, contactType: 'sales' },
  description: `${SITE.brand} is a brand of ${SITE.company}. It sells the ${PLAN_LABEL} and an AI front desk to local service businesses.`,
  parentOrganization: {
    '@type': 'Organization',
    name: SITE.company,
    address: {
      '@type': 'PostalAddress',
      streetAddress: '3rd Floor, Sunivas Building, St Inez',
      addressLocality: 'Panaji',
      addressRegion: 'Goa',
      postalCode: '403001',
      addressCountry: 'IN',
    },
  },
});

export const websiteJsonLd = (): JsonLdObject => ({
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  '@id': `${SITE.domain}/#website`,
  name: SITE.brand,
  url: SITE.domain,
  publisher: { '@id': `${SITE.domain}/#organization` },
  inLanguage: 'en-US',
});

export interface ServiceInput {
  name: string;
  serviceType: string;
  description: string;
  path: string;
  /** Fragment id, giving the Service a stable @id such as https://crewwisehq.com/#websites. */
  id?: string;
  areaServed?: string;
}

/** No numeric Offer is emitted: prices (SITE.PRICE_WEBSITE_PLAN, SITE.PRICE_FRONT_DESK) are shown as text only. */
export const serviceJsonLd = (s: ServiceInput): JsonLdObject => ({
  '@context': 'https://schema.org',
  '@type': 'Service',
  ...(s.id ? { '@id': `${SITE.domain}/#${s.id}` } : {}),
  name: s.name,
  serviceType: s.serviceType,
  description: s.description,
  url: absoluteUrl(s.path),
  provider: { '@id': `${SITE.domain}/#organization` },
  ...(s.areaServed ? { areaServed: s.areaServed } : {}),
});

export interface FaqItem {
  question: string;
  answer: string;
}

const stripHtml = (s: string): string => s.replace(/<[^>]*>/g, '');

export const faqJsonLd = (items: FaqItem[]): JsonLdObject => ({
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: items.map((i) => ({
    '@type': 'Question',
    name: i.question,
    acceptedAnswer: {
      '@type': 'Answer',
      text: stripHtml(i.answer).replaceAll('{{PRICE_FRONT_DESK}}', SITE.PRICE_FRONT_DESK),
    },
  })),
});
