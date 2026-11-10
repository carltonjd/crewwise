// Validation helpers for the free audit form. Pure functions, so they can be unit tested.
// Every message says what is wrong and how to fix it.

export const INTEREST_OPTIONS = ['Website and calls', 'AI automation', 'Both'] as const;
export const BUSINESS_TYPES = [
  'Home inspection',
  'HVAC',
  'Plumbing',
  'Roofing',
  'Electrical',
  'Cleaning',
  'Law firm',
  'Accounting firm',
  'Architecture firm',
  'Other',
] as const;

export type FieldName =
  | 'interest'
  | 'name'
  | 'company'
  | 'website'
  | 'phone'
  | 'email'
  | 'business_type';

export interface AuditValues {
  interest: string;
  name: string;
  company: string;
  website: string;
  noWebsite: boolean;
  phone: string;
  email: string;
  business_type: string;
}

export type AuditErrors = Partial<Record<FieldName, string>>;

/** Label shown in the error summary next to each message. */
export const FIELD_LABELS: Record<FieldName, string> = {
  interest: 'What would you like us to look at?',
  name: 'Your name',
  company: 'Business name',
  website: 'Website',
  phone: 'Business phone',
  email: 'Email',
  business_type: 'Type of business',
};

export const digitsOf = (value: string): string => value.replace(/\D/g, '');

export function validateInterest(value: string): string | null {
  return (INTEREST_OPTIONS as readonly string[]).includes(value)
    ? null
    : 'Choose what you would like us to look at: website and calls, AI automation, or both.';
}

export function validateName(value: string): string | null {
  const v = value.trim();
  if (!v) return 'Enter your name, so we know who to ask for.';
  if (v.length < 2) return 'Enter your full name. One letter is too short.';
  return null;
}

export function validateCompany(value: string): string | null {
  return value.trim() ? null : 'Enter your business name.';
}

export function validateEmail(value: string): string | null {
  const v = value.trim();
  if (!v) return 'Enter your email address, for example name@yourbusiness.com.';
  if (!v.includes('@')) return 'Your email is missing an @. Enter it like name@yourbusiness.com.';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) {
    return 'Check the part after the @. It should look like yourbusiness.com.';
  }
  return null;
}

export function validatePhone(value: string): string | null {
  const v = value.trim();
  if (!v) return 'Enter your business phone number, including the area code.';
  if (/[^\d\s()+\-.]/.test(v)) {
    return 'Use only numbers in your phone number. Spaces, dashes and brackets are fine.';
  }
  const d = digitsOf(v);
  if (d.length < 10) {
    return `That number has ${d.length} digit${d.length === 1 ? '' : 's'}. Enter at least 10, including the area code.`;
  }
  if (d.length > 15) return 'That number has too many digits. Enter 15 digits or fewer.';
  return null;
}

/** Adds https:// when a visitor types a bare domain. Returns '' for empty input. */
export function normalizeWebsite(value: string): string {
  const v = value.trim();
  if (!v) return '';
  return /^[a-z][a-z0-9+.-]*:\/\//i.test(v) ? v : `https://${v}`;
}

export function validateWebsite(value: string, noWebsite = false): string | null {
  if (noWebsite) return null;
  const v = value.trim();
  if (!v) return null; // optional
  if (/\s/.test(v)) return 'Remove the spaces from your website address.';
  try {
    const url = new URL(normalizeWebsite(v));
    if (!['http:', 'https:'].includes(url.protocol) || !url.hostname.includes('.')) {
      throw new Error('invalid');
    }
    return null;
  } catch {
    return 'Enter your website address like yourbusiness.com, or tick “I don’t have a website”.';
  }
}

export function validateBusinessType(value: string): string | null {
  return (BUSINESS_TYPES as readonly string[]).includes(value)
    ? null
    : 'Choose the type of business closest to yours. Pick “Other” if none fits.';
}

/** Formats a US style number (10 digits, or 1 plus 10) as (555) 123-4567. Anything else is left alone. */
export function formatPhone(value: string): string {
  const v = value.trim();
  if (v.startsWith('+') && !v.startsWith('+1')) return value;
  const d = digitsOf(v);
  const t = d.length === 11 && d[0] === '1' ? d.slice(1) : d;
  if (t.length !== 10) return value;
  return `(${t.slice(0, 3)}) ${t.slice(3, 6)}-${t.slice(6)}`;
}

export const firstName = (value: string): string => value.trim().split(/\s+/)[0] ?? '';

export function validateAudit(values: AuditValues): AuditErrors {
  const checks: [FieldName, string | null][] = [
    ['interest', validateInterest(values.interest)],
    ['name', validateName(values.name)],
    ['company', validateCompany(values.company)],
    ['website', validateWebsite(values.website, values.noWebsite)],
    ['phone', validatePhone(values.phone)],
    ['email', validateEmail(values.email)],
    ['business_type', validateBusinessType(values.business_type)],
  ];
  const errors: AuditErrors = {};
  for (const [field, msg] of checks) {
    if (msg) errors[field] = msg;
  }
  return errors;
}
