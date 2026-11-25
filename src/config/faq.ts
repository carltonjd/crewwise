// FAQ answers shared by the home and pricing pages, so the two never disagree.
// Facts come from the client terms v1.1 (sections 2, 4, 5 and 8). No buyout price, no result promises.
import { SITE, PLAN_LABEL } from './site';

export interface FaqItem {
  question: string;
  answer: string;
}

const [planAmt] = SITE.PRICE_WEBSITE_PLAN.split('/');

export const planFaq: FaqItem[] = [
  {
    question: `What does ${planAmt} a month include?`,
    answer: `Your website, built by Crewwise from our templates, its hosting, small text and photo updates, and setting up and updating your business profiles on Google, Bing, Apple Maps and ChatGPT, where those services allow it. There is no setup fee. Search engine optimization is not included.`,
  },
  {
    question: `What does “${SITE.PLAN_NAME}” mean?`,
    answer: `${SITE.PLAN_DEFINITION} It is the name of our website plan. Those services decide what they show, so we can’t promise rankings, calls or recommendations.`,
  },
  {
    question: 'Do I own the website?',
    answer:
      'While your plan is active, the website is licensed to you. If the plan ends, we take the website offline. You keep your domain, your logo, your photos and the text you gave us.',
  },
  {
    question: 'How do I cancel?',
    answer:
      'Email us. The plan is month to month, and either of us can cancel with 30 days’ written notice. Fees already paid are not refunded, except where the law requires it.',
  },
  {
    question: 'When do I pay?',
    answer: `The first payment is taken when you sign up, before we start building. After that, it is the same date each month. There is no free trial. Your receipt says “${SITE.PLAN_BILLING_NAME}”.`,
  },
  {
    question: 'How long does it take?',
    answer:
      'About 5 business days after we have your logo, photos and details. Two rounds of changes are included before launch.',
  },
  {
    question: 'Who is Crewwise?',
    answer: `Crewwise builds and runs websites and AI phone answering for local service businesses in the US. It is a brand of ${SITE.company}, a company in Panaji, Goa, India. You can reach us at ${SITE.CONTACT_EMAIL}.`,
  },
];

export const deskFaq: FaqItem[] = [
  {
    question: 'Is the AI front desk part of the website plan?',
    answer: `No. The AI front desk is a separate service, ${SITE.PRICE_FRONT_DESK.toLowerCase()}. Add it when you miss calls. It works with the ${PLAN_LABEL} or with the website you already have.`,
  },
  {
    question: 'Can I keep my phone number?',
    answer: 'Yes. Calls forward to the AI front desk when you don’t pick up, or after hours. You choose.',
  },
  {
    question: 'Will callers know they’re talking to an AI?',
    answer: 'It answers naturally and always says it’s an AI assistant if a caller asks.',
  },
  {
    question: 'How long does the AI front desk take to set up?',
    answer:
      'About a week. Texting switches on once your business number is registered with the phone carriers, usually 1 to 3 weeks.',
  },
];
