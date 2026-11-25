import { describe, expect, it } from 'vitest';
import { SITE, PAGES, PROMO, PROMO_DEADLINE } from '../../src/config/site';

describe('SITE constants', () => {
  it('has the exact legal line', () => {
    expect(SITE.legalLine).toBe(
      'Crewwise is a brand of Hallmark Data Systems Pvt Ltd · 3rd Floor, Sunivas Building, St Inez, Panaji, Goa 403001, India',
    );
  });

  it('sets the inspector demo line and points at Octalogic', () => {
    expect(SITE.DEMO_PHONE).toBe('(813) 993-1087');
    expect(SITE.OCTALOGIC_URL).toBe('https://octalogic.tech');
  });

  it('shows only the website plan price and the AI front desk price', () => {
    expect(SITE.PRICE_WEBSITE_PLAN).toBe('$99/month');
    expect(SITE.PRICE_FRONT_DESK).toBe('From $299/month');
    const text = JSON.stringify({ ...SITE, PAGES });
    const prices = text.match(/\$\s?\d[\d,]*/g) ?? [];
    expect(new Set(prices)).toEqual(new Set(['$99', '$299']));
  });

  it('hides custom websites and sets the promo deadline', () => {
    expect(SITE.SHOW_CUSTOM_WEBSITES).toBe(false);
    expect(PROMO.endsAt).toBe('2026-12-01T23:59:59-05:00');
    expect(PROMO_DEADLINE).toContain('December 1');
  });

  it('names Octalogic in the partner line', () => {
    expect(SITE.partnerLine).toContain('Octalogic');
  });
});
