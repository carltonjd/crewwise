# Builds the static site into public/ from site.config.json.
# Usage: python build.py      Deploy: Cloudflare Pages, output directory "public".
import os, re, json, html, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'public')
C = json.load(open(os.path.join(ROOT, 'site.config.json'), encoding='utf-8'))
E = html.escape
B = C['brand']
def inline_logo(name):
    svg = open(os.path.join(ROOT, 'design', 'brand', 'crewwise-brand-assets', name), encoding='utf-8').read()
    svg = re.sub(r'<title>.*?</title>', '', svg)
    svg = re.sub(r'\s(width|height)="[^"]*"', '', svg, count=2)
    return svg.replace('<svg ', '<svg aria-hidden="true" focusable="false" shape-rendering="geometricPrecision" ', 1)
ICON = inline_logo('crewwise-icon.svg')
LOGO = f'<span class="logo-icon">{ICON}</span><span class="logo-text">{B.lower()}</span>'
LOGO_DARK = LOGO
PHONE = C.get('us_phone', '')
LOGIN = C.get('app_login', '')
def phone_link(text_before='', cls='call'):
    return f'<a class="{cls}" href="tel:{C["us_phone_tel"]}">{text_before}<b>{PHONE}</b></a>' if PHONE else ''

MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="10" fill="#0F1B33"/>'
        '<polyline points="10,21 22,11 34,21" fill="none" stroke="#F26A1B" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><rect width="44" height="44" rx="10" fill="#0F1B33"/>'
               '<polyline points="10,21 22,11 34,21" fill="none" stroke="#F26A1B" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
               '<polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def head(title, desc, path, p, extra='', comment='', og_title=None, og_desc=None, schema=''):
    url = C['domain'] + path
    ot, od = og_title or title, og_desc or desc
    img = C['og_image']
    return f"""<!doctype html>
<html lang="en">
<head>
{comment}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{extra}<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0E1A33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{B}">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(ot)}">
<meta property="og:description" content="{E(od)}">
<meta property="og:image" content="{img}">
<meta property="og:image:secure_url" content="{img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{B}: AI front desk for roofing companies. Every call answered, every job booked.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(ot)}">
<meta name="twitter:description" content="{E(od)}">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{B}: AI front desk for roofing companies.">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{p}favicon.ico" sizes="any">
<link rel="icon" href="{p}favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
<script>document.documentElement.classList.add('js')</script>
{schema}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(p, nav=True):
    items = [('#how-it-works', 'How it works'), ('#storm-mode', 'Storm Mode'), ('#pricing', 'Pricing'), ('#faq', 'FAQ')]
    href = lambda h: h if nav else f'{p}{h}'
    links = ''.join(f'<a href="{href(h)}" data-spy="{h[1:]}">{t}</a>' for h, t in items)
    login = f'<a class="login" href="{LOGIN}">Client login</a>' if LOGIN else ''
    return f"""<header class="site-header">
  <div class="wrap">
    <div class="bar">
      <a class="logo" href="{p or './'}" aria-label="{B} home">{LOGO}</a>
      <nav class="nav" id="site-nav" aria-label="Main">{links}{login}</nav>
      <div class="top-act">
        <a class="btn sm" href="{C['calendly']}" target="_blank" rel="noopener">Book a demo</a>
        <button class="menu" type="button" aria-expanded="false" aria-controls="site-nav"><span class="sr">Menu</span><i aria-hidden="true"></i></button>
      </div>
    </div>
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
    letters = ''.join(f'<span style="--i:{i}">{ch}</span>' for i, ch in enumerate(B.lower()))
    login = f'<a href="{LOGIN}">Client login</a>' if LOGIN else ''
    phone = f'<a href="tel:{C["us_phone_tel"]}">{PHONE}</a>' if PHONE else ''
    return f"""</main>

<footer class="closing">
  <div class="wrap inner">
    <div class="close-top">
      <h2>Next time you're on a roof, let Crewwise pick up.</h2>
      <div class="act"><a class="btn light" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>{phone_link('or call ')}</div>
    </div>
    <a class="foot-logo" href="{p or './'}" aria-label="{B} home">{LOGO_DARK}</a>
    <div class="foot">
      <nav aria-label="Product"><h3>Product</h3><a href="{a}#how-it-works">How it works</a><a href="{a}#storm-mode">Storm Mode</a><a href="{a}#pricing">Pricing</a><a href="{a}#faq">FAQ</a>{login}</nav>
      <nav aria-label="Legal"><h3>Legal</h3><a href="{p}privacy/">Privacy</a><a href="{p}terms/">Terms</a><a href="{p}refunds/">Refunds</a></nav>
      <div><h3>Contact</h3><a href="mailto:{C['email']}">{C['email']}</a>{phone}</div>
    </div>
    <div class="mark play" aria-hidden="true">
      <span class="sig-line"></span>
      <span class="word">{letters}</span>
    </div>
    <p class="legalline">&copy; <span id="year">2026</span> {B}. AI front desk for roofing companies.</p>
  </div>
</footer>
<script src="{p}assets/lenis.min.js"></script>
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
    ('Old leads', 'Past inquiries never contacted again.', 'Contacted again'),
]
MOMENTS = [
    ('0:00', 'On the call', [
        ('Answers every call, 24/7', "In your company's name, nights, weekends and holidays included."),
        ('Qualifies every homeowner', 'Address, leak or damage, roof age, insurance claim, repair or replacement, residential or commercial.'),
        ('Checks your service area', 'Only books jobs inside the radius and towns you choose.'),
        ('Hands off to you', 'Active leaks, upset callers and complex insurance questions go straight to you.'),
    ]),
    ('+1 min', 'Right after', [
        ('Books inspections into your calendar', 'With a text confirmation and reminders for the homeowner.'),
        ('Texts back missed calls and web leads', 'Anyone who hangs up, and every web lead, gets a reply within a minute.'),
    ]),
    ('+2 weeks', 'Weeks later', [
        ('Follows up on unsold estimates', "Automatic check-ins on the quotes you've sent."),
        ('Reactivates old leads', 'Gets back in touch with old inquiries that never turned into a job.'),
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
        out.append(f'<g class="bar" style="--d:{d * 45}">')
        for k in range(calls[d]):
            y = base - 6 - k * 5
            out.append(f'<rect x="{x - 7:.1f}" y="{y:.1f}" width="14" height="2.5" rx="1" fill="var(--line)"/>')
        if booked[d]:
            y = base - 6 - calls[d] * 5 - 8
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="var(--ok-dot)"/>')
        out.append('</g>')
        tall = d % 5 == 0
        out.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{base}" y2="{base + (10 if tall else 5)}" stroke="var(--ink-2)"/>')
        if tall or d == 29:
            anc = 'start' if d == 0 else 'end' if d == 29 else 'middle'
            tx = d * step + 1 if d == 0 else W - 1 if d == 29 else x
            out.append(f'<text x="{tx:.1f}" y="{base + 26}" text-anchor="{anc}">Sep {d + 1}</text>')
    out.insert(0, f'<line x1="0" x2="{W}" y1="{base}" y2="{base}" stroke="var(--ink-2)"/>')
    return (f'<figure class="month play"><div class="month-scroll"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Example: calls answered each day in September, 180 in total, with a spike mid-month after a storm, and the 24 days with a booked inspection marked.">{"".join(out)}</svg></div>'
            '<p class="swipe">Scroll for the full month</p><figcaption><span><i class="k-call"></i>One call answered</span><span><i class="k-book"></i>Inspection booked that day</span></figcaption></figure>')

def connector(label, x, kind='', ok=False):
    return '\n  <div class="connector play ' + kind + '" aria-hidden="true"><span class="dot"></span></div>\n'


def leakmap():
    W, H = 1160, 150
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for y in range(10, H, 22) for x in range(10, W, 22))
    xs = [190, 380, 570, 760, 950]
    route = f'M20 75 H{W - 20}'
    marks = ''.join(f'<g class="hit" style="--d:{900 + i * 260}"><path class="x" d="M{x - 9} 66 L{x + 9} 84 M{x + 9} 66 L{x - 9} 84"/>'
                    f'<path class="ck" d="M{x - 10} 75 L{x - 3} 82 L{x + 11} 67"/></g>' for i, x in enumerate(xs))
    return (f'<div class="leakmap play"><svg viewBox="0 0 {W} {H}" role="img" aria-label="The path from a homeowner\'s call to a booked job, broken in five places.">'
            f'<g class="dots">{dots}</g><path class="route" d="{route}"/>{marks}'
            f'<circle class="end" cx="20" cy="75" r="6"/><circle class="end" cx="{W - 20}" cy="75" r="6"/>'
            f'<text x="20" y="112">Homeowner calls</text><text x="{W - 20}" y="112" text-anchor="end">Booked job</text></svg></div>')


SCHEMA = '<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Organization", "@id": C['domain'] + "/#org", "name": B, "url": C['domain'] + "/",
         "logo": C['domain'] + "/icon-512.png", "email": C['email']},
        {"@type": "WebSite", "@id": C['domain'] + "/#site", "url": C['domain'] + "/", "name": B, "publisher": {"@id": C['domain'] + "/#org"}},
        {"@type": "Service", "name": f"{B} for Roofers", "serviceType": "AI receptionist and answering service for roofing companies",
         "provider": {"@id": C['domain'] + "/#org"}, "areaServed": "US",
         "offers": {"@type": "Offer", "price": C['price'].lstrip('$'), "priceCurrency": "USD"}},
    ]}) + '</script>\n'

def home():
    p = ''
    leaks = ''.join(f'<li data-a style="--d:{i * 90}"><h3>{a}</h3><p>{b}</p><p class="fix">{c}</p></li>' for i, (a, b, c) in enumerate(LEAKS))
    queue = ''.join(f'<div class="q {c}" data-a style="--d:{400 + i * 220}"><span class="lvl">{l}</span><span><b>{h}</b><small>{d}</small></span><span class="when {k}">{s}</span></div>' for i, (c, l, h, d, s, k) in enumerate(QUEUE))
    tiles = ''.join(f'<div class="tile" data-a style="--d:{i * 80}"><dt>{k}</dt><dd data-count="{v}">{v}</dd></div>' for i, (k, v) in enumerate(REPORT))
    det = [f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ]
    faq = f'<div class="faq-col">{"".join(det[:5])}</div><div class="faq-col">{"".join(det[5:])}</div>'
    def feats(items):
        return '<ul class="feats">' + ''.join(f'<li><h4>{h}</h4><p>{d}</p></li>' for h, d in items) + '</ul>'
    m0, m1, m2 = MOMENTS
    eb = C['example_business']
    return head(f'AI Receptionist for Roofers | Roofing Answering Service | {B}',
                f'{B} answers your roofing calls 24/7, qualifies homeowners, books inspections and follows up on every estimate. Built for roofing companies.',
                '/', p,
                og_title=f"{B} answers your phone while you're on the roof",
                og_desc="AI front desk for roofing companies. It picks up when you can't, gets the job details and books the inspection into your calendar. $499 a month.",
                schema=SCHEMA) + header(p) + f"""
  <section class="wrap hero" aria-labelledby="hero-title">
    <div class="hero-inner">
      <figure class="flow play" aria-label="Example: a Saturday evening call to {eb}, a made-up roofing company. The call is answered, qualified as a ceiling leak on a 15-year-old roof with a claim filed, and booked for Monday at 9 AM.">
        <svg class="path" viewBox="0 0 1000 290" preserveAspectRatio="none" aria-hidden="true">
          <path d="M0 46 H330 Q360 46 360 76 V140 Q360 170 390 170 H1000"/>
          <path class="live" d="M0 46 H330 Q360 46 360 76 V140 Q360 170 390 170 H870"/>
        </svg>
        <span class="signal" aria-hidden="true"></span>
        <span class="node pill" data-step="1" style="left:9%;top:46px"><i></i>Incoming call</span>
        <span class="node pill" data-step="2" style="left:45%;top:170px"><i></i>Answered</span>
        <span class="node pill" data-step="3" style="left:66%;top:170px"><i></i>Qualified</span>
        <span class="node pill ok" data-step="4" style="left:87%;top:170px"><i></i>Booked</span>
        <div class="fcard" data-step="1" style="left:1%;top:84px;width:23%"><div class="h"><span>Saturday, 7:42 PM</span><span>Example</span></div><b>Homeowner calling.</b> You're up on a roof.</div>
        <div class="fcard dk" data-step="2" style="left:29%;top:200px;width:22%"><div class="h"><span>0:03</span><span class="typing" aria-hidden="true"><i></i><i></i><i></i></span></div>"Thanks for calling {eb}. How can I help?"</div>
        <div class="fcard" data-step="3" style="left:53%;top:200px;width:19%"><div class="h"><span>1:05</span></div><b>Ceiling leak</b><div class="tags"><span>15-year roof</span><span>Claim filed</span><span>In your area</span></div></div>
        <div class="fcard booked" data-step="4" style="left:74.5%;top:200px;width:23%"><div class="h"><span>1:48</span></div><b>Booked Mon 9:00 AM</b><br>Added to your calendar. Text confirmation sent.</div>
      </figure>
      <div class="hero-copy">
        <div>
          <p class="eyebrow">AI front desk for roofing companies</p>
          <h1 id="hero-title">Crewwise answers your phone while you're on the roof.</h1>
        </div>
        <div>
          <p class="sub">It picks up day or night, gets the address, the damage and the insurance details, and books the inspection into your calendar. Then it follows up on your estimates, so the leads you pay for turn into jobs.</p>
          <div class="act"><a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a><a class="link" href="#how-it-works">See how it works</a></div>
        </div>
      </div>
      <p class="flow-cap">Example call. {eb} is a made-up company. Crewwise doesn't sell leads or make cold calls, and there's no call center behind it. It answers the calls your business already gets.</p>
    </div>
  </section>
""" + connector('Where leads go', '20%', 'to-dark') + f"""
  <section class="dark" id="leaks" aria-labelledby="leaks-title">
    <div class="wrap sec" style="padding-top:64px">
      <div class="split"><h2 id="leaks-title">Where roofing leads leak</h2><p>A homeowner who can't reach you calls the next roofer. Here's where paid leads usually go that way.</p></div>
      {leakmap()}
      <ul class="leaks play">{leaks}</ul>
      <p class="plug">{B} covers all five for one monthly price.</p>
    </div>
  </section>
""" + connector('What it does', '64%', 'from-dark') + f"""
  <section class="wrap" id="what-it-does" aria-labelledby="what-title" style="padding-top:56px;padding-bottom:40px">
    <div class="split"><h2 id="what-title">Your front desk while you're on the roof</h2><p>It answers in your company's name and handles each step, from the first ring to the review request.</p></div>
    <div class="rows">
      <div class="row">
        <div class="row-copy"><span class="pill"><i></i>On the call</span><h3>Every call answered and qualified</h3>{feats(m0[2])}</div>
        <div><div class="ui ondark play" aria-label="Example of a live call">
          <div class="ui-h">Live call<span class="rec">Recording</span></div>
          <div class="tx">
            <p class="ai" data-a style="--d:200"><b>{B}</b><span>Thanks for calling {eb}. How can I help?</span></p>
            <p data-a style="--d:900"><b>Caller</b><span>Water's coming through my kitchen ceiling after the storm.</span></p>
            <p class="ai" data-a style="--d:1700"><b>{B}</b><span>Let's get someone out. What's the address, and is there an insurance claim?</span></p>
            <p data-a style="--d:2500"><b>Caller</b><span>1418 Maple Court, Round Rock. We filed a claim this morning.</span></p>
          </div>
          <div class="chips"><span data-a="s" style="--d:3100">Leak, kitchen ceiling</span><span data-a="s" style="--d:3240">Residential</span><span data-a="s" style="--d:3380">Repair</span><span data-a="s" style="--d:3520">Claim filed</span><span data-a="s" style="--d:3660">In service area</span></div>
        </div><p class="ui-cap">Example. Names and addresses are made up.</p></div>
      </div>
      <div class="row flip">
        <div class="row-copy"><span class="pill ok"><i></i>Right after</span><h3>Booked on your calendar, confirmed by text</h3>{feats(m1[2])}</div>
        <div><div class="ui onlight play" aria-label="Example of a booked inspection and text confirmation">
          <div class="ui-h">Monday, October 12<span>Your calendar</span></div>
          <div class="slot"><time>8 AM</time><div><span class="busy">Estimate, Cedar Park</span></div></div>
          <div class="slot"><time>9 AM</time><div><span class="ev" data-a="drop" style="display:block;--d:500"><b>Inspection booked</b>1418 Maple Ct, Round Rock</span></div></div>
          <div class="slot"><time>10 AM</time><div></div></div>
          <div class="sms">
            <div class="bubble me" data-a style="--d:1400">You're booked with {eb} for Monday at 9:00 AM. Reply C to confirm.</div>
            <div class="bubble" data-a style="--d:2300">C. Thank you!</div>
            <small>Text confirmation, Saturday 7:44 PM</small>
          </div>
        </div><p class="ui-cap">Example. Names and addresses are made up.</p></div>
      </div>
      <div class="row">
        <div class="row-copy"><span class="pill"><i></i>Weeks later</span><h3>The follow-ups you never get to</h3>{feats(m2[2])}</div>
        <div><div class="ui ondark play" aria-label="Example of follow-up messages">
          <div class="ui-h">Follow-ups<span>This week</span></div>
          <div class="thread">
            <div class="msg" data-a style="--d:200"><small>Estimate follow-up, day 7</small>Hi Mike, just checking in on the roof estimate we sent last week. Any questions I can answer?</div>
            <div class="msg reply" data-a style="--d:1200"><small>Reply</small>Yes, can someone call me about the shingle options?</div>
            <div class="msg" data-a style="--d:2200"><small>Review request, after the job</small>Thanks for choosing {eb}. Would you leave us a quick Google review?</div>
          </div>
        </div><p class="ui-cap">Example. Names are made up.</p></div>
      </div>
    </div>
  </section>
""" + connector('Storm season', '30%', 'to-dark') + f"""
  <section class="dark storm" id="storm-mode" aria-labelledby="storm-title">
    <div class="wrap sec storm-grid" style="padding-top:64px">
      <div>
        <h2 id="storm-title">When the storm hits, every call gets answered.</h2>
        <p>After a storm, your phone explodes and the job goes to whoever picks up first. Storm Mode handles many calls at once, flags active leaks as urgent, captures the address, damage and insurance details, and books inspections in priority order. You see the full list and decide who to visit first.</p>
      </div>
      <div>
        <div class="queue play" aria-label="Example Storm Mode list, sorted by urgency">
          <div class="queue-head"><b><span class="switch" aria-hidden="true"></span>Storm Mode: On</b><span>Sorted by urgency</span></div>
          {queue}
        </div>
        <p class="note">Example. Addresses are made up.</p>
      </div>
    </div>
  </section>
""" + connector('Every month', '72%', 'from-dark') + f"""
  <section class="wrap" id="report" aria-labelledby="report-title" style="padding-top:56px;padding-bottom:104px">
    <div class="split"><h2 id="report-title">Your monthly Lead Recovery Report</h2><p>Once a month you get a plain count of what happened to every lead.</p></div>
    <dl class="tiles play">{tiles}<div class="tile total" data-a style="--d:420"><dt>Estimated opportunity value</dt><dd data-count="72000" data-prefix="$">$72,000</dd></div></dl>
    {month_strip()}
    <p class="report-foot">Example report with illustrative numbers, not real results. Estimated opportunity value is based on booked inspections and your average job value. It is not revenue.</p>
  </section>

  <section class="wrap" id="how-it-works" aria-labelledby="how-title" style="padding-bottom:120px">
    <div class="split"><h2 id="how-title">How it works</h2><p>It works with the tools you already use, so there's no new CRM to learn.</p></div>
    <ol class="steps play">
      <li data-a style="--d:200"><span class="pill"><i></i>Step 1</span><h3>30-minute setup call</h3><p>Your services, service area, hours, the questions to ask and your booking rules.</p></li>
      <li data-a style="--d:600"><span class="pill"><i></i>Step 2</span><h3>Forward your calls</h3><p>Missed and after-hours calls go to a number we set up. <strong>You keep your existing number.</strong></p></li>
      <li data-a style="--d:1000"><span class="pill"><i></i>Step 3</span><h3>Go live</h3><p>Crewwise starts answering. You can listen to any call, and the Lead Recovery Report arrives each month.</p></li>
    </ol>
  </section>

  <section class="wrap" id="pricing" aria-labelledby="pricing-title" style="padding-bottom:120px">
    <div class="split"><h2 id="pricing-title">One plan, one price</h2><p>{C['price']} a month covers everything on this page.</p></div>
    <div class="plan">
      <div>
        <p class="plan-name">{B} for Roofers</p>
        <p class="amount">{C['price']}<span>/month</span></p>
        <p class="founding"><b>Founding roofers:</b> setup fee waived, month-to-month, cancel anytime.</p>
        <a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>
      </div>
      <div>
        <ul class="includes"><li>Everything in What it does</li><li>Storm Mode</li><li>Monthly Lead Recovery Report</li><li>Setup and tuning done for you</li><li>A real person for support</li></ul>
        <p class="fine">Includes a generous monthly allowance of AI call minutes. We'll tell you upfront if you ever get close. Billed monthly in US dollars. See the <a href="refunds/">refund and cancellation policy</a>.</p>
      </div>
    </div>
  </section>

  <section class="wrap" id="faq" aria-labelledby="faq-title" style="padding-bottom:120px">
    <div class="split"><h2 id="faq-title">Questions roofers ask us</h2><p>Something else on your mind? Ask us on the demo call.</p></div>
    <div class="faq-list">{faq}</div>
  </section>

  <section class="wrap" id="contact" aria-labelledby="contact-title" style="padding-bottom:120px">
    <div class="contact-grid">
      <div>
        <h2 id="contact-title">Rather we call you?</h2>
        <p>Leave your details and we'll call you at a time that works around your jobs.</p>
        <div class="reach">
          <a href="{C['calendly']}" target="_blank" rel="noopener"><b>Book a 15-min demo</b><span>Pick a time</span></a>
          {f'<a href="tel:{C["us_phone_tel"]}"><b>Call or text {PHONE}</b><span>Talk to us today</span></a>' if PHONE else f'<a href="mailto:{C["email"]}"><b>Email {C["email"]}</b><span>Write to us anytime</span></a>'}
        </div>
        <p class="contact-note"><b>Founding roofers:</b> {C['price']} a month, no setup fee, no contract.</p>
      </div>
      <div class="form">
        <form class="lead-form" action="{C['form_endpoint']}" method="POST" novalidate data-phone="{PHONE}" data-email="{C['email']}">
          <h3>We'll call you back</h3>
          <p class="form-sub">We'll call you to set up a 15-minute demo.</p>
          <input type="hidden" name="page" value="home">
          <div class="fields">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
            <div class="field full"><label for="f-company">Company</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
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
    <p>Email: <a href="mailto:{C['email']}">{C['email']}</a>{f'<br>Phone: <a href="tel:{C["us_phone_tel"]}">{PHONE}</a>' if PHONE else ''}</p>"""
CONTACT_FULL = f"""
    <h2>Contact us</h2>
    <p>{C['company']}<br>{C['company_address']}<br>Email: <a href="mailto:{C['email']}">{C['email']}</a>{f'<br>Phone: <a href="tel:{C["us_phone_tel"]}">{PHONE}</a>' if PHONE else ''}</p>"""

PRIVACY = f"""
    <p>This policy explains, in plain English, what {B} ("we", "us") collects, how we use it and the choices you have.</p>
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
    {CONTACT_FULL}"""

REFUNDS = f"""
    <p>Billing for {B} is simple: one monthly price, no long contract, cancel anytime.</p>
    <h2>Pricing</h2>
    <p>{B} costs {C['price']} per month, billed monthly in advance in US dollars. For founding roofers, the setup fee is waived.</p>
    <h2>How to cancel</h2>
    <ul>
      <li>Email <a href="mailto:{C['email']}">{C['email']}</a> from the address on your account{f', or call <a href="tel:{C["us_phone_tel"]}">{PHONE}</a>' if PHONE else ''}.</li>
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
    for f in ('style.css', 'main.js', 'lenis.min.js'):
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
    ph = open(src, encoding='utf-8').read().replace('Jobstead', B).replace('[DOMAIN]', C['domain']).replace('[BUSINESS ADDRESS]', '').replace('tel:[US PHONE]', 'mailto:' + C['email']).replace('[US PHONE]', C['email']).replace('[EMAIL]', C['email']).replace('[GOVERNING LAW]', C['governing_law']).replace(C['company'], B).replace('[OG IMAGE URL]', C['og_image'])
    if 'name="robots"' not in ph:
        ph = ph.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)
    write(os.path.join('photographers', 'index.html'), ph)
    for f in ('site.css', 'site.js'):
        open(os.path.join(OUT, 'assets', f), 'w', encoding='utf-8').write(open(os.path.join(ROOT, 'design', 'archive', 'assets', f), encoding='utf-8').read().replace('Jobstead', B))
    os.makedirs(os.path.join(OUT, 'brand'), exist_ok=True)
    BA = os.path.join(ROOT, 'design', 'brand', 'crewwise-brand-assets')
    for f in ('crewwise-logo.svg', 'crewwise-logo-on-dark.svg', 'crewwise-icon.svg', 'crewwise-mark.svg'):
        shutil.copy(os.path.join(BA, f), os.path.join(OUT, 'brand', f))
    write('favicon.svg', open(os.path.join(ROOT, 'design', 'collateral', 'favicon.svg'), encoding='utf-8').read())
    write('site.webmanifest', json.dumps({"name": B, "short_name": B, "start_url": "/", "display": "browser",
        "background_color": "#F8F9FD", "theme_color": "#0E1A33",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}, {"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=2))
    for f in ('apple-touch-icon.png', 'icon-192.png', 'icon-512.png', 'favicon-16.png', 'favicon-32.png', 'favicon-48.png', 'favicon.ico', 'og.jpg'):
        s = os.path.join(ROOT, 'design', 'collateral', f)
        if os.path.exists(s):
            shutil.copy(s, os.path.join(OUT, f)); print('copied public/' + f)
    write('_redirects', '/roofers   /   301\n/roofers/  /   301\n')
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {C["domain"]}/sitemap.xml\n')
    urls = ''.join(f'  <url><loc>{C["domain"]}{u}</loc></url>\n' for u in ('/', '/privacy/', '/terms/', '/refunds/'))
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

if __name__ == '__main__':
    main()
