import type { APIRoute } from 'astro';
import { SITE, PAGES, absoluteUrl, BUILDER } from '../config/site';

export const GET: APIRoute = () => {
  const body = `# ${SITE.brand}

> ${SITE.brand} helps small businesses stop losing customers in the first minute. It sells three services under one name: an AI front desk that answers every call; websites; and AI automation. ${SITE.legalLine}.

## Services

- AI front desk: answers every call 24/7, books appointments, captures the caller’s details, flags urgent calls to you and follows up. Texting switches on after carrier registration, usually 1 to 3 weeks. ${SITE.PRICE_FRONT_DESK}.
- Websites: modern, fast websites for small businesses, designed and built by ${BUILDER}.
- AI automation: a free 30-minute call, a paid automation review credited against any build, then fixed-price automations that take repetitive manual work off a team, for example matching purchase orders to invoices.

## Who it is for

- Home inspectors and home-service companies: home inspection, HVAC, plumbing, roofing, electrical and cleaning.
- Small professional firms: law, architecture and accounting firms.

## Who is behind it

${SITE.brand} is a brand of ${SITE.company}, based in Goa, India.${SITE.SHOW_OCTALOGIC ? ` Websites and automation work are built by Octalogic (${SITE.OCTALOGIC_URL}), a software engineering company and ${SITE.brand}’s engineering partner.` : ''}

## Pages

${PAGES.map((p) => `- [${p.title}](${absoluteUrl(p.path)}): ${p.description}`).join('\n')}

## Contact

- Email: ${SITE.CONTACT_EMAIL}
- Free audit: ${absoluteUrl('/free-audit/')}
`;
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
