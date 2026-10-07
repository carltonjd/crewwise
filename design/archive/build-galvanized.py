# Builds the static site into public/ from site.config.json.
# Usage: python build.py      Deploy: Cloudflare Pages, output directory "public".
import os, re, json, html, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'public')
C = json.load(open(os.path.join(ROOT, 'site.config.json'), encoding='utf-8'))
E = html.escape
B = C['brand']

MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="10" fill="#14181C"/>'
        '<polyline points="10,21 22,11 34,21" fill="none" stroke="#C0632F" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><rect width="44" height="44" rx="10" fill="#14181C"/>'
               '<polyline points="10,21 22,11 34,21" fill="none" stroke="#C0632F" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
               '<polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def head(title, desc, path, p, extra='', comment=''):
    url = C['domain'] + path
    return f"""<!doctype html>
<html lang="en">
<head>
{comment}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{extra}<link rel="canonical" href="{url}">
<meta name="theme-color" content="#F2F3F4">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{B}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{C['og_image']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{C['og_image']}">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(p, nav=True):
    links = ''
    if nav:
        links = ('<nav class="nav" aria-label="Page sections"><a href="#how-it-works">How it works</a><a href="#storm-mode">Storm Mode</a>'
                 '<a href="#pricing">Pricing</a><a href="#faq">FAQ</a></nav>')
    return f"""<header class="site-header">
  <div class="wrap top">
    <a class="logo" href="{p or './'}" aria-label="{B} home">{MARK}{B}</a>
    {links}
    <div class="top-act"><a class="login" href="{C['app_login']}">Client login</a><a class="btn sm" href="{C['calendly']}" target="_blank" rel="noopener">Book a demo</a></div>
  </div>
</header>
<main id="main">
"""

def analytics():
    t = C.get('analytics_token', '')
    if not t:
        return ''
    return f"""<!-- Web analytics (cookieless). Token lives in site.config.json. -->
<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "{t}"}}'></script>
"""

def footer(p, home=False):
    a = '' if home else p
    return f"""</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <p class="brandline">Every call answered. Every job booked.</p>
      <div class="foot-act"><a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a><a class="call" href="tel:{C['us_phone_tel']}">or call <b>{C['us_phone']}</b></a></div>
    </div>
    <div class="foot-meta">
      <nav class="foot-links" aria-label="Footer">
        <a href="{a}#how-it-works">How it works</a><a href="{a}#storm-mode">Storm Mode</a><a href="{a}#pricing">Pricing</a><a href="{a}#faq">FAQ</a>
        <a href="{p}privacy/">Privacy</a><a href="{p}terms/">Terms</a><a href="{p}refunds/">Refunds</a><a href="{C['app_login']}">Client login</a>
      </nav>
      <p class="foot-contact"><a href="tel:{C['us_phone_tel']}">{C['us_phone']}</a><a href="mailto:{C['email']}">{C['email']}</a></p>
      <p class="legalline">&copy; <span id="year">2026</span> {B}</p>
    </div>
  </div>
</footer>
<script src="{p}assets/main.js"></script>
{analytics()}</body>
</html>
"""

# ---------------- Homepage content ----------------
EVENTS = [(0, '0:00', "<b>Homeowner calls.</b> You're up on a roof."),
          (3, '0:03', "<b>Answered</b> on the first ring, in your company's name."),
          (65, '1:05', '<b>Qualified:</b> ceiling leak, roof about 15 years old, claim filed.'),
          (108, '1:48', '<b>Booked Mon 9:00 AM.</b> Added to your calendar.')]
LEAKS = [
    ('Missed calls', 'On a roof, on the road, after hours.', 'Answered 24/7'),
    ('Slow response', 'Web and ad leads waiting hours for a callback.', 'Replied to within a minute'),
    ('Wrong-fit calls', 'Out-of-area or wrong-job calls eating your time.', 'Screened before they reach you'),
    ('Silent estimates', 'Quotes sent, never followed up.', 'Followed up automatically'),
    ('Old leads', 'Past inquiries never contacted again.', 'Reached again'),
]
MOMENTS = [
    ('0:00', 'On the call', [
        ('Answers every call, 24/7', "In your company's name, nights, weekends and holidays included."),
        ('Qualifies every homeowner', 'Address, leak or damage, roof age, insurance claim, repair or replacement, residential or commercial.'),
        ('Checks your service area', 'Only books jobs inside the radius and towns you choose.'),
        ('Hands off to you', 'Active leaks, upset callers and complex insurance questions go straight to a person.'),
    ]),
    ('+1 min', 'Right after', [
        ('Books inspections into your calendar', 'With a text confirmation and reminders for the homeowner.'),
        ('Texts back missed calls and web leads', 'Anyone who hangs up, and every web lead, gets a reply within a minute.'),
    ]),
    ('+2 weeks', 'Weeks later', [
        ('Follows up on unsold estimates', "Automatic check-ins on the quotes you've sent."),
        ('Reactivates old leads', 'Reaches back out to past inquiries you never closed.'),
        ('Asks for Google reviews', 'After the job, happy customers get a short review request with your link.'),
    ]),
]
QUEUE = [
    ('urgent', 'Urgent', 'Active leak, kitchen ceiling', '1418 Maple Ct, Round Rock. No claim yet.', 'Sent to you now', ''),
    ('', 'High', 'Hail damage, shingles missing', '88 Cedar Ridge Dr, Georgetown. Claim filed.', 'Mon 9:00 AM', 'ok'),
    ('', 'Normal', 'Dented gutters and vents', '2205 Oak Bend, Pflugerville. Claim filed.', 'Mon 11:30 AM', 'ok'),
    ('', 'Normal', 'Inspection before adjuster visit', '710 Pecan St, Hutto. Adjuster Thursday.', 'Tue 8:00 AM', 'ok'),
]
REPORT = [('Calls answered', '180'), ('Missed calls recovered', '40'), ('Inspections booked', '24'),
          ('Estimates followed up', '30'), ('Old leads reactivated', '12')]
FAQ = [
    ('How much does it cost?', f"{C['price']} a month. The setup fee is waived for founding roofers, and there's no contract."),
    ('Do I keep my number?', 'Yes. Your number stays the same. You forward missed and after-hours calls to a number we set up.'),
    ('What if a caller wants a real person?', 'It transfers the call to you or takes a message, based on your rules.'),
    ('Can I hear the calls?', 'Yes. Every call is recorded and transcribed, so you can listen to it or read it.'),
    ('What happens in storm season?', 'Storm Mode takes many calls at once, flags active leaks as urgent, captures the address, damage and insurance details, and books inspections in priority order. You see the full list and decide who to visit first.'),
    ('Will it book jobs outside my area?', 'No. It checks your service radius and towns first, and only books jobs inside the area you choose.'),
    ('Does it handle insurance questions?', 'It captures the claim details, like whether a claim is filed and when the adjuster is coming, and passes complex insurance questions to you.'),
    ('Do I need to change my CRM?', "No. It works alongside the tools you already use. There's no new CRM to learn."),
    ('How long does setup take?', 'Usually 1 to 2 weeks. Most of that is waiting on US text-message registration, which carriers require before we can text your customers.'),
    ('Can I switch it off?', 'Anytime. Turn off call forwarding and your calls come straight back to you. Plans are month to month.'),
]

def month_strip():
    import random
    rnd = random.Random(11)
    w = [rnd.uniform(.6, 1.4) * (2.2 if d in (12, 13, 14) else 1) for d in range(30)]  # a storm mid-month
    tot = sum(w); calls = [max(1, round(x / tot * 180)) for x in w]
    calls[0] += 180 - sum(calls)
    booked = [0] * 30
    for i in sorted(range(30), key=lambda d: -calls[d])[:24]: booked[i] = 1
    W, H, base = 820, 176, 140
    step = W / 30
    out = []
    for d in range(30):
        x = d * step + step / 2
        for k in range(calls[d]):
            y = base - 6 - k * 5
            out.append(f'<rect x="{x - 7:.1f}" y="{y:.1f}" width="14" height="2.5" rx="1" fill="var(--accent)"/>')
        if booked[d]:
            y = base - 6 - calls[d] * 5 - 8
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="var(--ok)"/>')
        tall = d % 5 == 0
        out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{base}" y2="{base + (10 if tall else 5)}" stroke="var(--ink-2)"/>')
        if tall or d == 29:
            anc = 'start' if d == 0 else 'end' if d == 29 else 'middle'
            tx = d * step + 1 if d == 0 else W - 1 if d == 29 else x
            out.append(f'<text x="{tx:.1f}" y="{base + 26}" text-anchor="{anc}">Sep {d + 1}</text>')
    out.insert(0, f'<line x1="0" x2="{W}" y1="{base}" y2="{base}" stroke="var(--ink-2)"/>')
    return (f'<figure class="month"><div class="month-scroll"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Example: calls answered each day in September, 180 in total, with a spike mid-month after a storm, and the 24 days with a booked inspection marked.">{"".join(out)}</svg></div>'
            '<p class="swipe">Scroll for the full month</p><figcaption><span><i class="k-call"></i>One call answered</span><span><i class="k-book"></i>Inspection booked that day</span></figcaption></figure>')

def home():
    p = ''
    marks = ''.join(f'<span class="mark{" end" if i == 3 else ""} hit" data-t="{t}" style="left:{t / 120 * 100:.2f}%"></span>' for i, (t, _, _) in enumerate(EVENTS))
    evs = ''.join(f'<li data-t="{t}"{" class=\"last\"" if i == 3 else ""}><time>{c}</time>{d}</li>' for i, (t, c, d) in enumerate(EVENTS))
    leaks = ''.join(f'<div class="leak" role="row"><h3 role="rowheader">{a}</h3><p role="cell">{b}</p><p class="fix" role="cell">{c}</p></div>' for a, b, c in LEAKS)
    moments = ''.join(f'<div class="moment"><h3>{o}<span>{t}</span></h3><ul{" class=\"three\"" if len(items) == 3 else ""}>'
                      + ''.join(f'<li><h4>{h}</h4><p>{d}</p></li>' for h, d in items) + '</ul></div>' for o, t, items in MOMENTS)
    queue = ''.join(f'<div class="q {c}" role="row"><span class="lvl" role="cell">{l}</span><span role="cell"><b>{h}</b><small>{d}</small></span><span class="slot {k}" role="cell">{s}</span></div>' for c, l, h, d, s, k in QUEUE)
    rep = ''.join(f'<div class="st-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in REPORT)
    det = [f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ]
    faq = f'<div class="faq-col">{"".join(det[:5])}</div><div class="faq-col">{"".join(det[5:])}</div>'
    return head(f'AI Receptionist for Roofers | Roofing Answering Service | {B}',
                f'{B} answers your roofing calls 24/7, qualifies homeowners, books inspections and follows up on every estimate. Built for roofing companies.',
                '/', p) + header(p) + f"""
  <section class="wrap hero" aria-labelledby="hero-title">
    <p class="eyebrow">AI front desk for roofing companies</p>
    <h1 id="hero-title">You paid for the lead. We make sure you don't lose it.</h1>
    <div class="hero-row">
      <p class="sub">{B} answers every call 24/7, qualifies the homeowner, books the inspection into your calendar and follows up on every estimate, so the leads you already pay for turn into jobs.</p>
      <div class="act">
        <a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>
      </div>
    </div>
    <figure class="line" id="line" aria-label="Example: one Saturday evening call to {C['example_business']}, a made-up roofing company. At 0:00 a homeowner calls while you are up on a roof. At 0:03 it is answered on the first ring. At 1:05 it is qualified: a ceiling leak, a roof about 15 years old, a claim filed. At 1:48 the inspection is booked for Monday at 9 AM.">
      <div class="line-top"><span>Saturday, 7:42 PM.<span class="wide"> Answering for {C['example_business']}.</span></span><span class="clock" aria-hidden="true"><span>Call time</span><b id="clock">1<span class="c">:</span>48</b></span></div>
      <div class="ruler" aria-hidden="true"><div class="trail"></div><span class="ring"></span>{marks}</div>
      <svg class="leaders" aria-hidden="true"></svg>
      <ol class="events" aria-hidden="true">{evs}</ol>
      <figcaption class="cap">Example call. {C['example_business']} is a made-up company. Every real call is recorded and transcribed for you.</figcaption>
    </figure>
    <p class="not"><b>Not a lead-gen company.</b> <b>Not a robocaller.</b> <b>Not a call center.</b> <span>It answers the leads you already pay for.</span></p>
  </section>

  <section class="sec rest" id="leaks" aria-labelledby="leaks-title">
    <div class="wrap">
      <div class="intro"><h2 id="leaks-title">Where roofing leads leak</h2><p>You already pay for the leads. These are the five places they slip away.</p></div>
      <div class="ledger" role="table" aria-label="Where leads leak and what {B} does about it">
        <div class="ledger-head" role="row"><span role="columnheader">The leak</span><span role="columnheader">Where it happens</span><span role="columnheader">With {B}</span></div>
        {leaks}
      </div>
      <p class="plug">{B} plugs every one of these.</p>
    </div>
  </section>

  <section class="sec" id="what-it-does" aria-labelledby="what-title">
    <div class="wrap">
      <div class="intro"><h2 id="what-title">What it does</h2><p>Your front desk while you're on the roof, from the first ring to the review.</p></div>
      <div class="moments">{moments}</div>
    </div>
  </section>

  <section class="sec storm" id="storm-mode" aria-labelledby="storm-title">
    <div class="wrap storm-grid">
      <div class="intro">
        <h2 id="storm-title">When the storm hits, every call gets answered.</h2>
        <p>After a storm, your phone explodes and the job goes to whoever picks up first. Storm Mode handles many calls at once, flags active leaks as urgent, captures the address, damage and insurance details, and books inspections in priority order. You see the full list and decide who to visit first.</p>
      </div>
      <div>
        <div class="queue" role="table" aria-label="Example Storm Mode list, sorted by urgency">
          <div class="queue-head" role="row"><b role="columnheader"><i class="live" aria-hidden="true"></i>Storm Mode: On</b><span role="columnheader">Sorted by urgency</span></div>
          {queue}
        </div>
        <p class="note">Example. Addresses are made up.</p>
      </div>
    </div>
  </section>

  <section class="sec rest" id="report" aria-labelledby="report-title">
    <div class="wrap report-grid">
      <div class="intro"><h2 id="report-title">Your monthly Lead Recovery Report</h2><p>Every month you see exactly what happened to your leads.</p></div>
      <figure class="statement">
        <div class="st-head"><b>Lead Recovery Report, September</b><span>Example report</span></div>
        {month_strip()}
        <dl>{rep}<div class="st-row total"><dt>Estimated opportunity value</dt><dd>$72,000</dd></div></dl>
        <figcaption>Example report with illustrative numbers, not real results. Estimated opportunity value is based on booked inspections and your average job value. It is not revenue.</figcaption>
      </figure>
    </div>
  </section>

  <section class="sec" id="how-it-works" aria-labelledby="how-title">
    <div class="wrap">
      <div class="intro"><h2 id="how-title">How it works</h2></div>
      <ol class="steps">
        <li><span class="n">Step 1</span><h3>30-minute setup call</h3><p>Your services, service area, hours, the questions to ask and your booking rules.</p></li>
        <li><span class="n">Step 2</span><h3>Forward your calls</h3><p>Missed and after-hours calls go to a number we set up. <strong>You keep your existing number.</strong></p></li>
        <li><span class="n">Step 3</span><h3>Go live</h3><p>Hear every call and get your monthly Lead Recovery Report.</p></li>
      </ol>
      <p class="works"><b>Works alongside the tools you already use.</b> No new CRM to learn.</p>
    </div>
  </section>

  <section class="sec" id="pricing" aria-labelledby="pricing-title">
    <div class="wrap price-grid">
      <div class="intro"><h2 id="pricing-title">One plan, one price</h2><p>Everything on this page, for one flat monthly price.</p></div>
      <div>
        <div class="price-top"><div><p class="plan-name">{B} for Roofers</p>
        <p class="amount">{C['price']}<span>/month</span></p></div>
        <p class="founding"><b>Founding roofers:</b> setup fee waived, month-to-month, cancel anytime.</p></div>
        <ul class="includes">
          <li>Everything in What it does</li><li>Storm Mode</li><li>Monthly Lead Recovery Report</li><li>Setup and tuning done for you</li><li>A real person for support</li>
        </ul>
        <div class="price-act"><a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a></div>
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

  <section class="sec close" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact-grid">
      <div class="intro">
        <h2 id="contact-title">Rather we call you?</h2>
        <p>Leave your details and we'll call you at a time that works around your jobs.</p>
        <div class="reach">
          <a href="{C['calendly']}" target="_blank" rel="noopener"><b>Book a 15-min demo</b><span>Pick a time</span></a>
          <a href="tel:{C['us_phone_tel']}"><b>Call or text {C['us_phone']}</b><span>Talk to us today</span></a>
        </div>
        <p class="contact-note"><b>Founding roofers:</b> setup fee waived, month-to-month, cancel anytime. {C['price']} a month after that, with no contract.</p>
      </div>
      <div class="form">
        <form class="lead-form" action="{C['form_endpoint']}" method="POST" novalidate data-phone="{C['us_phone']}">
          <h3>We'll call you back</h3>
          <input type="hidden" name="page" value="home">
          <div class="fields">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
            <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
            <div class="field full"><label for="f-city">City and state</label><input id="f-city" name="city_state" type="text" autocomplete="address-level2" placeholder="Dallas, TX" required></div>
            <div class="field full"><label for="f-missed">Roughly how many calls do you miss a week? <span class="opt">(optional)</span></label><input id="f-missed" name="missed_calls_per_week" type="text" inputmode="numeric" placeholder="A rough guess is fine"></div>
            <div class="hp" aria-hidden="true"><label for="f-gotcha">Leave this field empty</label><input id="f-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
          </div>
          <div class="form-foot">
            <button class="btn" type="submit">Call me back</button>
            <p>We'll only use your details to contact you about {B}.</p>
            <div class="form-error" role="alert" hidden></div>
          </div>
        </form>
        <div class="thanks" tabindex="-1" hidden role="status">
          <h3>Thanks<span class="thanks-name"></span>. We'll call you soon.</h3>
          <p>If you'd rather pick a time yourself, book it now.</p>
          <a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>
        </div>
      </div>
    </div>
  </section>
""" + footer(p, home=True)

# ---------------- Legal pages ----------------
DRAFT = '<!-- Draft: to be reviewed by a lawyer. -->\n'
UPDATED = 'October 6, 2026'
CONTACT = f"""
    <h2>Contact us</h2>
    <p>{C['company']}<br>{C['company_address']}<br>Email: <a href="mailto:{C['email']}">{C['email']}</a><br>Phone: <a href="tel:{C['us_phone_tel']}">{C['us_phone']}</a></p>"""

PRIVACY = f"""
    <p>{B} is a brand of {C['company']} ("we", "us"). This policy explains, in plain English, what we collect, how we use it and the choices you have.</p>
    <h2>What we collect</h2>
    <h3>When you contact us</h3>
    <ul>
      <li>What you type into the form on our website: your name, company name, phone, email, city and state, and a rough number of missed calls if you give one.</li>
      <li>What you tell us on a demo call, by email or by phone.</li>
    </ul>
    <h3>When you become a client</h3>
    <ul>
      <li>Your business details: services, service area, hours, booking rules and how you want calls handled.</li>
      <li>Billing details. Payments are handled by our payment processor; we do not store your full card number.</li>
    </ul>
    <h3>Calls and messages we handle for clients</h3>
    <p>When {B} answers a call or sends or receives a text for a client, we keep the caller's phone number, a recording and transcript of the call or the messages, and the details the caller shares, such as their name, address, the job they need and the appointment they book. We hold this on behalf of the client. If a client asks us to follow up with past leads, we use the contact details the client gives us.</p>
    <h3>Website visits</h3>
    <p>Our host records basic technical information, such as your IP address and browser. We use cookieless analytics to count visits. Our fonts are loaded from a font service, which sees your IP address when it delivers them.</p>
    <h2>How we use it</h2>
    <ul>
      <li>To reply to you and set up a demo.</li>
      <li>To run the service for our clients: answering calls, booking inspections, sending confirmations and follow-ups, and producing recordings, transcripts and reports.</li>
      <li>To bill clients, keep the service secure and fix problems.</li>
      <li>To meet our legal obligations.</li>
    </ul>
    <h2>We don't sell your data</h2>
    <p>We do not sell personal information. We share it only with the client a caller was trying to reach, with the service providers who help us run {B} (hosting, telephone and text messaging, speech and AI processing, scheduling, form handling and payments), and with authorities when the law requires it. We do not share mobile numbers or text-message consent with anyone for their marketing.</p>
    <h2>How long we keep it</h2>
    <p>As long as we need it to provide the service and meet legal obligations. Clients can ask us to delete recordings and transcripts at any time.</p>
    <h2>Where it is processed</h2>
    <p>We and our service providers may store and process information in countries including India and the United States.</p>
    <h2>Your choices</h2>
    <p>You can ask us to see, correct or delete information we hold about you, or to stop contacting you. Email <a href="mailto:{C['email']}">{C['email']}</a>. If you called a business that uses {B}, contact that business first; we will help them respond.</p>
    <h2>Children</h2>
    <p>{B} is a service for businesses. We do not knowingly collect information from children under 13.</p>
    <h2>Changes</h2>
    <p>If we change this policy, we will post the new version here and update the date at the top.</p>
    {CONTACT}"""

TERMS = f"""
    <p>These terms are an agreement between you and {C['company']}, which provides the {B} service. By using {B}, you agree to them. If you sign up for a business, you confirm you can accept these terms for it.</p>
    <h2>1. The service</h2>
    <p>{B} is an AI front desk for roofing companies. Depending on your setup, it answers calls forwarded to it, qualifies callers, checks your service area, books inspections into your calendar, sends text confirmations and reminders, replies to missed calls and web leads, follows up on estimates and past leads, asks customers for reviews, transfers calls or takes messages, and gives you recordings, transcripts and a monthly report. We may improve or change features over time.</p>
    <h2>2. Your subscription</h2>
    <ul>
      <li>{B} costs {C['price']} per month, billed monthly in advance in US dollars, unless we agree a different price with you in writing.</li>
      <li>It is month-to-month. There is no long-term contract.</li>
      <li>A one-time setup fee may apply. For founding roofers, it is waived.</li>
      <li>Prices do not include taxes.</li>
      <li>If a payment fails, we may pause the service until the account is paid.</li>
      <li>We will give you at least 30 days' notice before changing your price.</li>
    </ul>
    <h2>3. Call minutes</h2>
    <p>Your plan includes a monthly allowance of AI call minutes. If you get close to it, we will tell you upfront. If you go over, we will contact you before any extra charge, explain the rate, and only charge it with your agreement.</p>
    <h2>4. Cancelling</h2>
    <p>You can cancel anytime. Cancellation takes effect at the end of your current billing month. See the <a href="../refunds/">Refund and Cancellation Policy</a>.</p>
    <h2>5. Acceptable use</h2>
    <ul>
      <li>Use {B} only for your own business and only for lawful purposes.</li>
      <li>You are responsible for following the laws that apply to your calls and texts, including giving callers any notice the law requires about call recording.</li>
      <li>You confirm you have the consent the law requires to contact the customers and past leads you ask us to call or text.</li>
      <li>Do not use {B} to make unsolicited calls or texts, or for anything harmful or misleading.</li>
    </ul>
    <h2>6. What an AI front desk can and can't do</h2>
    <p>{B} uses automated technology and can make mistakes, such as mishearing a caller or booking the wrong time. Please review your bookings and messages. It is not an emergency service. We do not guarantee any number of leads, jobs or bookings.</p>
    <h2>7. Your data</h2>
    <p>You own your business information and the recordings, transcripts and details from your calls. You let us use them to provide and improve the service for you. Our <a href="../privacy/">Privacy Policy</a> explains how we handle personal information.</p>
    <h2>8. Suspension</h2>
    <p>We may pause or end your account if you break these terms, do not pay, or use {B} in a way that could harm others. Where it is reasonable, we will tell you first and give you a chance to fix it.</p>
    <h2>9. Limitation of liability</h2>
    <p>To the extent the law allows, {B} is provided "as is", and we are not liable for indirect or consequential losses, or for lost profits, revenue, jobs or data. Our total liability for any claim is limited to the amount you paid us in the three months before the claim.</p>
    <h2>10. Changes to these terms</h2>
    <p>If we make an important change, we will tell you at least 30 days before it takes effect.</p>
    <h2>11. Who you are dealing with</h2>
    <p>These terms are with {C['company']}, {C['company_address']}. They are governed by {C['governing_law']}.</p>
    {CONTACT}"""

REFUNDS = f"""
    <p>{B} is a brand of {C['company']}. Billing is simple: one monthly price, no long contract, cancel anytime.</p>
    <h2>Pricing</h2>
    <p>{B} costs {C['price']} per month, billed monthly in advance in US dollars. For founding roofers, the setup fee is waived.</p>
    <h2>How to cancel</h2>
    <ul>
      <li>Email <a href="mailto:{C['email']}">{C['email']}</a> from the address on your account, or call <a href="tel:{C['us_phone_tel']}">{C['us_phone']}</a>.</li>
      <li>Your cancellation takes effect at the end of your current billing month. {B} keeps answering until then, and you will not be charged again.</li>
      <li>To send calls straight back to your own phone right away, turn off call forwarding at any time.</li>
      <li>We confirm every cancellation by email.</li>
    </ul>
    <h2>Refunds</h2>
    <ul>
      <li>Monthly fees are paid in advance and are not refunded for partial months, unless stated otherwise.</li>
      <li>If you were charged by mistake, charged twice, or charged after your cancellation took effect, we refund that charge in full.</li>
      <li>To ask for a refund, email us with your business name and the date of the charge. We aim to reply within 2 business days.</li>
      <li>Refunds go back to the original payment method. Your bank may take 5 to 10 business days to show them.</li>
    </ul>
    {CONTACT}"""

def legal(slug, title, desc, body):
    p = '../'
    return (head(f'{title} | {B}', desc, f'/{slug}/', p, comment=DRAFT) + header(p, nav=False)
            + f'  <article class="legal wrap">\n    <h1>{title}</h1>\n    <p class="updated">Last updated: {UPDATED}</p>{body}\n  </article>\n' + footer(p))

def notfound():
    p = '/'
    return head(f'Page not found | {B}', f'This page is not on the {B} website.', '/404', p, extra='<meta name="robots" content="noindex">\n') + header(p, nav=False) + f"""
  <section class="wrap legal">
    <h1>This page isn't here.</h1>
    <p class="updated">The link may be old, or the address may have a typo.</p>
    <p style="margin-top:32px"><a class="btn" href="/">Go to the homepage</a></p>
  </section>
""" + footer(p)

# ---------------- Write ----------------
def check(rel, s):
    for bad in ('—', '–', '·'):
        assert bad not in s, f'{repr(bad)} in {rel}'
    if not rel.startswith('photographers'):
        for w in ('hotograph', 'HVAC', 'lumbing', 'lectrical', 'Jobstead', 'GoHighLevel', 'Retell', 'Stripe'):
            assert w not in s, f'{w} in {rel}'

def write(rel, s):
    check(rel, s)
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(s)
    print('wrote', 'public/' + rel.replace('\\', '/'))

def main():
    os.makedirs(OUT, exist_ok=True)
    for n in os.listdir(OUT):
        q = os.path.join(OUT, n)
        shutil.rmtree(q) if os.path.isdir(q) else os.remove(q)
    os.makedirs(os.path.join(OUT, 'assets'))
    for f in ('style.css', 'main.js'):
        shutil.copy(os.path.join(ROOT, 'assets', f), os.path.join(OUT, 'assets', f))
    write('index.html', home())
    write(os.path.join('privacy', 'index.html'), legal('privacy', 'Privacy Policy', f'What {B} collects, how it is used, and your choices.', PRIVACY))
    write(os.path.join('terms', 'index.html'), legal('terms', 'Terms of Service', f'The terms for using {B}.', TERMS))
    write(os.path.join('refunds', 'index.html'), legal('refunds', 'Refund and Cancellation Policy', f'How cancelling and refunds work for {B}.', REFUNDS))
    write('404.html', notfound())
    write(os.path.join('roofers', 'index.html'), f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{B}</title>
<link rel="canonical" href="{C['domain']}/">
<meta http-equiv="refresh" content="0; url=/">
</head>
<body><p>This page has moved. <a href="/">Go to the {B} homepage</a>.</p></body>
</html>
""")
    # Paused page: kept, renamed, noindexed, unlinked. It uses the previous stylesheet.
    src = os.path.join(ROOT, 'design', 'archive', 'photographers', 'index.html')
    ph = open(src, encoding='utf-8').read().replace('Jobstead', B).replace('[DOMAIN]', C['domain']).replace('[BUSINESS ADDRESS]', C['company_address']).replace('[OG IMAGE URL]', C['og_image'])
    if 'name="robots"' not in ph:
        ph = ph.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    write(os.path.join('photographers', 'index.html'), ph)
    for f in ('site.css', 'site.js'):
        open(os.path.join(OUT, 'assets', f), 'w', encoding='utf-8').write(open(os.path.join(ROOT, 'design', 'archive', 'assets', f), encoding='utf-8').read().replace('Jobstead', B))
    write('favicon.svg', FAVICON_SVG)
    for f in ('apple-touch-icon.png', 'icon-512.png', 'og.png'):
        s = os.path.join(ROOT, 'design', 'collateral', f)
        if os.path.exists(s):
            shutil.copy(s, os.path.join(OUT, f)); print('copied public/' + f)
    write('_redirects', '/roofers   /   301\n/roofers/  /   301\n')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {C["domain"]}/sitemap.xml\n')
    urls = ''.join(f'  <url><loc>{C["domain"]}{u}</loc></url>\n' for u in ('/', '/privacy/', '/terms/', '/refunds/'))
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

if __name__ == '__main__':
    main()
