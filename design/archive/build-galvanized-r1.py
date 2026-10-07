# Builds the Jobstead site (Galvanized direction) into the project root.
# Run: python design/build.py
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

NOTE = """<!--
  PLACEHOLDERS: find and replace before going live.
    [US PHONE]         Main business line. In href="tel:..." use digits only, e.g. +15551234567
    [CALENDLY LINK]    e.g. https://calendly.com/jobstead/15min
    [EMAIL]            e.g. hello@yourdomain.com
    [FORM ENDPOINT]    e.g. https://formspree.io/f/abcd1234
    [DOMAIN]           e.g. https://yourdomain.com  (canonical + Open Graph)
    [OG IMAGE URL]     1200x630 share image (design/og.html renders one)
    [COMPANY ADDRESS]  Registered address of Hallmark Data Systems Pvt Ltd
    [GOVERNING LAW]    Governing law and courts (Terms of Service)
  Design notes and tokens: design/DIRECTION.md. Styles: assets/style.css.
-->"""

MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="10" fill="#14181C"/>'
        '<polyline points="10,21 22,11 34,21" fill="none" stroke="#C0632F" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 44 44'%3E%3Crect width='44' height='44' rx='10' fill='%2314181C'/%3E"
           "%3Cpolyline points='10,21 22,11 34,21' fill='none' stroke='%23C0632F' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'/%3E"
           "%3Cpolyline points='15,26 20,31 30,21' fill='none' stroke='%23FFFFFF' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")

def head(title, desc, path, p, robots=''):
    return f"""<!doctype html>
<html lang="en">
<head>
{NOTE}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}<link rel="canonical" href="[DOMAIN]{path}">
<meta name="theme-color" content="#F2F3F4">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jobstead">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="[DOMAIN]{path}">
<meta property="og:image" content="[OG IMAGE URL]">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="[OG IMAGE URL]">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(p, nav=True):
    links = ('<nav class="nav" aria-label="Page sections"><a href="#what">What it does</a><a href="#storm">Storm Mode</a>'
             '<a href="#pricing">Pricing</a><a href="#faq">Questions</a><a href="#contact">Contact</a></nav>') if nav else ''
    return f"""<header class="site-header">
  <div class="wrap top">
    <a class="logo" href="{p or './'}" aria-label="Jobstead home">{MARK}Jobstead</a>
    {links}
    <a class="btn sm" href="[CALENDLY LINK]" target="_blank" rel="noopener">Book a demo</a>
  </div>
</header>
<main id="main">
"""

def footer(p):
    return f"""</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <p class="brandline">Every call answered. Every job booked.</p>
      <div class="foot-act"><a class="btn" href="[CALENDLY LINK]" target="_blank" rel="noopener">Book a 15-min demo</a><a class="link" href="tel:[US PHONE]">or call [US PHONE]</a></div>
    </div>
    <div class="foot-meta">
      <div>
        <p>Jobstead. AI front desk for roofing companies.</p>
        <p class="legalline">&copy; <span id="year">2026</span> Hallmark Data Systems Pvt Ltd. Jobstead is a brand of Hallmark Data Systems Pvt Ltd. [COMPANY ADDRESS]</p>
      </div>
      <nav class="foot-links" aria-label="Footer">
        <a href="mailto:[EMAIL]">[EMAIL]</a>
        <a href="{p}privacy/">Privacy Policy</a>
        <a href="{p}terms/">Terms of Service</a>
        <a href="{p}refunds/">Refund and Cancellation Policy</a>
      </nav>
    </div>
  </div>
</footer>
<script src="{p}assets/main.js"></script>
</body>
</html>
"""

# ---------------- Homepage ----------------
LEAKS = [
    ('Missed calls', 'On a roof, on the road, after hours.', 'Answered 24/7'),
    ('Slow response', 'Web and ad leads that wait hours for a callback.', 'Replied to within a minute'),
    ('Unqualified calls', 'Out-of-area or wrong-job calls eating your time.', 'Screened before they reach you'),
    ('Silent estimates', 'Quotes sent, never followed up.', 'Followed up automatically'),
    ('Old leads', 'Past inquiries sitting in your CRM, never contacted again.', 'Reached again'),
]
MOMENTS = [
    ('On the call', [
        ('Answers every call, 24/7', "In your company's name, nights, weekends and holidays included."),
        ('Qualifies every homeowner', 'Address, leak or damage, roof age, insurance claim, repair or replacement, residential or commercial.'),
        ('Checks your service area', 'Only books jobs inside the radius and towns you choose.'),
        ('Hands off when it matters', 'Active leaks, angry callers and complex insurance questions go straight to you.'),
    ]),
    ('Right after', [
        ('Books inspections into your calendar', 'With a text confirmation and reminders for the homeowner.'),
        ('Texts back missed calls and web leads', 'Anyone who hangs up, and every web lead, gets a reply within a minute.'),
    ]),
    ('Weeks later', [
        ('Follows up on unsold estimates', "Automatic check-ins on the quotes you've sent."),
        ('Reactivates old leads', 'Reaches back out to past inquiries you never closed, from a list you share with us.'),
        ('Asks for Google reviews', 'After the job, happy customers get a short review request with your link.'),
    ]),
]
QUEUE = [
    ('urgent', 'Urgent', 'Active leak, kitchen ceiling', '1418 Maple Ct, Round Rock. No claim yet.', 'Sent to you now'),
    ('', 'High', 'Hail damage, shingles missing', '88 Cedar Ridge Dr, Georgetown. Claim filed.', 'Mon 9:00 AM'),
    ('', 'Normal', 'Dented gutters and vents', '2205 Oak Bend, Pflugerville. Claim filed.', 'Mon 11:30 AM'),
    ('', 'Normal', 'Inspection before adjuster visit', '710 Pecan St, Hutto. Adjuster Thursday.', 'Tue 8:00 AM'),
]
REPORT = [('Calls answered', '180'), ('Missed calls recovered', '40'), ('Inspections booked', '24'),
          ('Estimates followed up', '30'), ('Old leads reactivated', '12')]
FAQ = [
    ('How much does it cost?', "$499 a month. Founding roofers pay no setup fee, and there's no contract. It's month to month, and you can cancel anytime."),
    ('Do I keep my number?', 'Yes. Your number stays the same. You forward missed and after-hours calls to a number we set up.'),
    ('What if a caller wants a real person?', 'It transfers the call to you or takes a message, based on your rules. Active leaks, angry callers and complex insurance questions go straight to you.'),
    ('What happens in storm season?', 'Storm Mode handles many calls at once, flags active leaks as urgent, captures the address, damage and insurance details, and books inspections in priority order. You see the full list and decide who to visit first.'),
    ('Will it book jobs outside my area?', 'No. It checks your service radius and towns first, and only books jobs inside the area you choose.'),
    ('Does it handle insurance questions?', 'It captures the claim details, like whether a claim is filed and when the adjuster is coming, and passes complex insurance questions to you.'),
    ('Do I need to change my CRM?', "No. It works alongside the tools you already use. There's no new CRM to learn."),
    ('Can I hear the calls?', 'Yes. Every call is recorded and transcribed, so you can listen to it or read it.'),
    ('Can I switch it off?', 'Anytime. Plans are month to month, so you can cancel whenever you like. Turn off call forwarding and your calls come straight back to you.'),
]
EVENTS = [('7:42 PM', '<b>Homeowner calls.</b> You\'re up on a roof.'),
          ('7:42 PM', '<b>Answered</b> on the first ring, in your company\'s name.'),
          ('7:43 PM', '<b>Qualified:</b> ceiling leak, roof about 15 years old, claim filed.'),
          ('7:44 PM', '<b>Booked Mon 9:00 AM</b><br>Added to your calendar.')]

def home():
    p = ''
    evs = ''.join(f'<div class="ev{" last" if i == 3 else ""}"><time>{t}</time>{d}</div>' for i, (t, d) in enumerate(EVENTS))
    vl = ''.join(f'<li><time>{t}</time>{d.replace("</b><br>", ".</b> ")}</li>' for t, d in EVENTS)
    leaks = ''.join(f'<div class="leak"><h3>{a}</h3><p>{b}</p><p class="fix">{c}</p></div>' for a, b, c in LEAKS)
    moments = ''.join(f'<div class="moment"><h3>{t}</h3><ul>' + ''.join(f'<li><h4>{h}</h4><p>{d}</p></li>' for h, d in items) + '</ul></div>' for t, items in MOMENTS)
    moments = moments.replace('<h3>Weeks later</h3><ul>', '<h3>Weeks later</h3><ul class="three">')
    queue = ''.join(f'<div class="q {c}"><span class="lvl">{l}</span><span><b>{h}</b><small>{d}</small></span><span class="slot">{s}</span></div>' for c, l, h, d, s in QUEUE)
    rep = ''.join(f'<div class="st-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in REPORT)
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return head('AI Receptionist for Roofers | Roofing Answering Service | Jobstead',
                'Jobstead answers your roofing calls 24/7, qualifies homeowners, books inspections and follows up on every estimate. Built for roofing companies.',
                '/', p) + header(p) + f"""
  <section class="wrap hero" aria-labelledby="hero-title">
    <h1 id="hero-title">You paid for the lead. We make sure you don't lose it.</h1>
    <div class="hero-row">
      <p class="sub">Jobstead is an AI front desk for roofing companies. It answers every call 24/7, qualifies the homeowner, books the inspection into your calendar, and follows up on every estimate.</p>
      <div class="act"><a class="btn" href="[CALENDLY LINK]" target="_blank" rel="noopener">Book a 15-min demo</a><a class="call" href="tel:[US PHONE]">or call <b>[US PHONE]</b></a></div>
    </div>
    <figure class="line" id="line" aria-label="Example: one Saturday evening call. At 7:42 PM a homeowner calls about a leak while you are up on a roof. It is answered on the first ring, qualified as a ceiling leak on a roof about 15 years old with a claim filed, and at 7:44 PM the inspection is booked for Monday at 9 AM." style="margin-inline:0">
      <div class="ruler" aria-hidden="true"><div class="trail"></div><span class="ring"></span><div class="dot done"></div></div>
      <div class="events" aria-hidden="true">{evs}</div>
      <ol class="vlist" aria-hidden="true">{vl}</ol>
      <figcaption class="cap"><span>One Saturday evening call. Example.</span><span>Every call is recorded and transcribed for you.</span></figcaption>
    </figure>
    <p class="not"><b>Not a lead-gen company.</b> <b>Not a robocaller.</b> <b>Not a call center.</b> <span>It answers the leads you already pay for.</span></p>
  </section>

  <section class="sec" id="leaks" aria-labelledby="leaks-title">
    <div class="wrap">
      <div class="intro"><h2 id="leaks-title">Where roofing leads leak</h2><p>You already pay for the leads. These are the five places they slip away.</p></div>
      <div class="ledger" role="table" aria-label="Where leads leak and what Jobstead does">
        <div class="ledger-head" aria-hidden="true"><span>The leak</span><span>Where it happens</span><span>With Jobstead</span></div>
        {leaks}
      </div>
      <p class="plug">Jobstead plugs every one of these.</p>
    </div>
  </section>

  <section class="sec" id="what" aria-labelledby="what-title">
    <div class="wrap">
      <div class="intro"><h2 id="what-title">What it does</h2><p>Your front desk while you're on the roof, from the first ring to the five-star review.</p></div>
      <div class="moments">{moments}</div>
    </div>
  </section>

  <section class="sec storm" id="storm" aria-labelledby="storm-title">
    <div class="wrap storm-grid">
      <div class="intro">
        <h2 id="storm-title">When the storm hits, every call gets answered.</h2>
        <p>After a storm, your phone explodes and the jobs go to whoever picks up first. Storm Mode handles many calls at once, flags active leaks as urgent, captures the address, damage and insurance details, and books inspections in priority order. You see the full list and decide who to visit first.</p>
      </div>
      <div>
        <div class="queue" role="table" aria-label="Example Storm Mode list, sorted by urgency">
          <div class="queue-head"><b>Storm Mode is on</b><span>Sorted by urgency</span></div>
          {queue}
        </div>
        <p class="note">Example. Addresses are made up.</p>
      </div>
    </div>
  </section>

  <section class="sec" id="report" aria-labelledby="report-title">
    <div class="wrap report-grid">
      <div class="intro"><h2 id="report-title">Your monthly Lead Recovery Report</h2><p>Every month you see exactly what happened to your leads. No guessing.</p></div>
      <figure class="statement" style="margin:0">
        <div class="st-head"><b>Lead Recovery Report, September</b><span>Example</span></div>
        <dl>{rep}<div class="st-row total"><dt>Estimated opportunity value</dt><dd>$72,000</dd></div></dl>
        <figcaption>Example report with illustrative numbers, not real results. Estimated opportunity value is based on booked inspections and your average job value. It is not revenue.</figcaption>
      </figure>
    </div>
  </section>

  <section class="sec" id="how" aria-labelledby="how-title">
    <div class="wrap">
      <div class="intro"><h2 id="how-title">How it works</h2></div>
      <ol class="steps">
        <li><span class="n">1</span><h3>30-minute setup call</h3><p>We learn your services, service area, hours, the questions you want asked and your booking rules.</p></li>
        <li><span class="n">2</span><h3>Forward your calls</h3><p>Missed and after-hours calls go to a number we set up. <strong>You keep your existing number.</strong></p></li>
        <li><span class="n">3</span><h3>Go live</h3><p>Hear every call, and get your monthly Lead Recovery Report.</p></li>
      </ol>
      <p class="works"><b>Works alongside the tools you already use.</b> No new CRM to learn.</p>
    </div>
  </section>

  <section class="sec" id="pricing" aria-labelledby="pricing-title">
    <div class="wrap price-grid">
      <div class="intro"><h2 id="pricing-title">One plan, one price</h2><p>Everything on this page, for one flat monthly price.</p></div>
      <div>
        <p class="plan-name">Jobstead for Roofers</p>
        <p class="amount tnum">$499<span>/month</span></p>
        <ul class="includes">
          <li>Everything in What it does</li><li>Storm Mode</li><li>Monthly Lead Recovery Report</li><li>Setup and tuning done for you</li><li>A real person to contact for support</li>
        </ul>
        <p class="founding"><b>Founding roofers:</b> setup fee waived, month-to-month, cancel anytime.</p>
        <div class="price-act"><a class="btn" href="[CALENDLY LINK]" target="_blank" rel="noopener">Book a 15-min demo</a></div>
        <p class="fine">Includes a generous monthly allowance of AI call minutes. We'll tell you upfront if you ever get close. Billed monthly in US dollars. See the <a href="refunds/">refund and cancellation policy</a>.</p>
      </div>
    </div>
  </section>

  <section class="sec" id="faq" aria-labelledby="faq-title">
    <div class="wrap faq-grid">
      <div class="intro"><h2 id="faq-title">Questions roofers ask us</h2><p>Something else on your mind? Ask us on the demo call.</p></div>
      <div class="faq-list">{faq}</div>
    </div>
  </section>

  <section class="sec" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact-grid">
      <div class="intro">
        <h2 id="contact-title">Rather we call you?</h2>
        <p>Leave your details and we'll call you at a time that works around your jobs.</p>
        <div class="reach">
          <a href="[CALENDLY LINK]" target="_blank" rel="noopener"><b>Book a 15-min demo</b><span>Pick a time</span></a>
          <a href="tel:[US PHONE]"><b>Call or text [US PHONE]</b><span>Talk to us today</span></a>
        </div>
      </div>
      <div class="form">
        <form class="lead-form" action="[FORM ENDPOINT]" method="POST" novalidate data-phone="[US PHONE]">
          <h3>We'll call you back</h3>
          <input type="hidden" name="page" value="home">
          <div class="fields">
            <div class="field"><label for="f-company">Roofing company</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
            <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
            <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
            <div class="field full"><label for="f-city">City and state</label><input id="f-city" name="city_state" type="text" autocomplete="address-level2" placeholder="Dallas, TX" required></div>
            <div class="field full"><label for="f-missed">Roughly how many calls do you miss a week? <span class="opt">(optional)</span></label><input id="f-missed" name="missed_calls_per_week" type="text" inputmode="numeric" placeholder="A rough guess is fine"></div>
            <div class="hp" aria-hidden="true"><label for="f-gotcha">Leave this field empty</label><input id="f-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
          </div>
          <div class="form-foot">
            <button class="btn" type="submit">Call me back</button>
            <p>We'll only use your details to contact you about Jobstead. We never sell your details.</p>
            <div class="form-error" role="alert" hidden></div>
          </div>
        </form>
        <div class="thanks" tabindex="-1" hidden>
          <h3>Thanks<span class="thanks-name"></span>. We'll call you soon.</h3>
          <p>If you'd rather pick a time yourself, book it now.</p>
          <a class="btn" href="[CALENDLY LINK]" target="_blank" rel="noopener">Book a 15-min demo</a>
        </div>
      </div>
    </div>
  </section>
""" + footer(p)

# ---------------- Legal pages: reuse the current wording ----------------
def legal(slug):
    cur = open(os.path.join(ROOT, slug, 'index.html'), encoding='utf-8').read()
    m = re.search(r'<article class="legal wrap">(.*?)</article>', cur, re.S)
    if not m:
        m = re.search(r'<article class="legal wrap">(.*?)</article>', open(os.path.join(ROOT, 'design', 'legal-src', slug + '.html'), encoding='utf-8').read(), re.S)
    body = m.group(1)
    title = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S).group(1).strip()
    body = re.sub(r'<h1[^>]*>', '<h1>', body)
    desc = re.search(r'<meta name="description" content="([^"]*)"', cur).group(1)
    os.makedirs(os.path.join(ROOT, 'design', 'legal-src'), exist_ok=True)
    open(os.path.join(ROOT, 'design', 'legal-src', slug + '.html'), 'w', encoding='utf-8').write(f'<article class="legal wrap">{body}</article>')
    return head(f'{html.unescape(title)} | Jobstead', html.unescape(desc), f'/{slug}/', '../') + header('../', nav=False) + f'  <article class="legal wrap">{body}</article>\n' + footer('../')

def write(rel, s):
    for bad in ('—', '–'):
        assert bad not in s, 'dash in ' + rel
    for w in ('hotograph', 'HVAC', 'lumbing', 'lectrical'):
        assert w not in s, w + ' in ' + rel
    path = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(s); print('wrote', rel)

if __name__ == '__main__':
    pages = {slug: legal(slug) for slug in ('privacy', 'terms', 'refunds')}
    write('index.html', home())
    for slug, s in pages.items():
        write(os.path.join(slug, 'index.html'), s)
