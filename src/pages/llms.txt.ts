import type { APIRoute } from 'astro';
import { SITE, PAGES, absoluteUrl, PLAN_LABEL } from '../config/site';

export const GET: APIRoute = () => {
  const body = `# ${SITE.brand}

> ${SITE.brand} builds and runs websites for local service businesses in the US. Its main offer is the ${PLAN_LABEL}; an AI front desk that answers calls is a separate service. ${SITE.legalLine}.

## Services

- ${PLAN_LABEL}: ${SITE.PLAN_LINE} The website is built by ${SITE.brand} from its templates, hosted, with small text and photo updates; ready about 5 business days after the content arrives. ${SITE.PRICE_WEBSITE_PLAN}, no setup fee, no free trial, month to month with 30 days' notice to cancel. The website is licensed while the plan is active. Search engine optimization is not included, and no rankings or recommendations are promised. ${SITE.PLAN_DEFINITION}
- AI front desk: a separate service that answers every call 24/7, books appointments, captures the caller’s details, flags urgent calls to you and follows up. Texting switches on after carrier registration, usually 1 to 3 weeks. ${SITE.PRICE_FRONT_DESK}.
- AI automation: a free 30-minute call about automating repetitive manual work.

## Who it is for

- Local service businesses: auto detailing, pressure washing, pool cleaning, garage door and home inspection, and other home-service companies.

## Who is behind it

${SITE.brand} is a brand of ${SITE.company}, based in Goa, India.${SITE.SHOW_OCTALOGIC ? ` Websites and automation work are built by Octalogic (${SITE.OCTALOGIC_URL}), a software engineering company and ${SITE.brand}’s engineering partner.` : ''}

## Pages

${PAGES.map((p) => `- [${p.title}](${absoluteUrl(p.path)}): ${p.description}`).join('\n')}

## Contact

- Email: ${SITE.CONTACT_EMAIL}
- Get started (website plan or free audit): ${absoluteUrl('/free-audit/')}
`;
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
