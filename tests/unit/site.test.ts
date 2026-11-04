import { describe, expect, it } from 'vitest';
import { SITE, PAGES } from '../../src/config/site';

describe('SITE constants', () => {
  it('has the exact legal line', () => {
    expect(SITE.legalLine).toBe(
      'Crewwise is a brand of Hallmark Data Systems Pvt Ltd · 3rd Floor, Sunivas Building, St Inez, Panaji, Goa 403001, India',
    );
  });

  it('keeps the demo phone empty and points at Octalogic', () => {
    expect(SITE.DEMO_PHONE).toBe('');
    expect(SITE.OCTALOGIC_URL).toBe('https://octalogic.tech');
  });

  it('shows from $299 as the only price', () => {
    expect(SITE.PRICE_FRONT_DESK).toBe('From $299/month');
    const text = JSON.stringify({ ...SITE, PAGES });
    const prices = text.match(/\$\s?\d[\d,]*/g) ?? [];
    expect(new Set(prices)).toEqual(new Set(['$299']));
  });

  it('names Octalogic in the partner line', () => {
    expect(SITE.partnerLine).toContain('Octalogic');
  });
});
