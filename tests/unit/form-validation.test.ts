import { describe, expect, it } from 'vitest';
import {
  firstName,
  formatPhone,
  normalizeWebsite,
  validateAudit,
  validateEmail,
  validateName,
  validatePhone,
  validateWebsite,
  type AuditValues,
} from '../../src/lib/form-validation';

const valid: AuditValues = {
  interest: 'Both',
  name: 'Dana Reyes',
  company: 'Reyes Plumbing',
  website: 'reyesplumbing.com',
  noWebsite: false,
  phone: '(555) 123-4567',
  email: 'dana@reyesplumbing.com',
  business_type: 'Plumbing',
};

describe('audit form validation', () => {
  it('accepts a complete form', () => {
    expect(validateAudit(valid)).toEqual({});
  });

  it('reports every missing required field', () => {
    const errors = validateAudit({
      ...valid,
      interest: '',
      name: '',
      company: '',
      phone: '',
      email: '',
      business_type: '',
    });
    expect(Object.keys(errors).sort()).toEqual(
      ['business_type', 'company', 'email', 'interest', 'name', 'phone'].sort(),
    );
  });

  it('treats the website as optional and skips it when the box is ticked', () => {
    expect(validateWebsite('')).toBeNull();
    expect(validateWebsite('not a site', true)).toBeNull();
    expect(validateWebsite('not a site')).toMatch(/spaces/);
    expect(validateWebsite('localhost')).toMatch(/yourbusiness\.com/);
    expect(validateWebsite('https://example.com/path')).toBeNull();
  });

  it('adds https to bare domains only', () => {
    expect(normalizeWebsite(' example.com ')).toBe('https://example.com');
    expect(normalizeWebsite('http://example.com')).toBe('http://example.com');
    expect(normalizeWebsite('')).toBe('');
  });

  it('explains email problems', () => {
    expect(validateEmail('')).toMatch(/Enter your email/);
    expect(validateEmail('dana.example.com')).toMatch(/missing an @/);
    expect(validateEmail('dana@example')).toMatch(/after the @/);
    expect(validateEmail('dana@example.com')).toBeNull();
  });

  it('checks phone digit counts', () => {
    expect(validatePhone('555 1234')).toMatch(/7 digits/);
    expect(validatePhone('call me')).toMatch(/only numbers/);
    expect(validatePhone('+91 98765 43210')).toBeNull();
    expect(validatePhone('1234567890123456')).toMatch(/too many/);
  });

  it('formats ten digit numbers', () => {
    expect(formatPhone('5551234567')).toBe('(555) 123-4567');
    expect(formatPhone('1-555-123-4567')).toBe('(555) 123-4567');
    expect(formatPhone('+91 98765 43210')).toBe('+91 98765 43210');
  });

  it('requires a real name and takes the first name', () => {
    expect(validateName(' ')).toMatch(/Enter your name/);
    expect(validateName('D')).toMatch(/too short/);
    expect(firstName('  Dana  Reyes')).toBe('Dana');
  });

  it('never uses an apology or a dash in a message', () => {
    const errors = validateAudit({ ...valid, name: '', phone: '1', email: 'x', website: 'a b' });
    for (const msg of Object.values(errors)) {
      expect(msg).not.toMatch(/sorry|oops|something went wrong|[–—]/i);
    }
  });
});
