# Builds the static site into public/ from site.config.json.
# Usage: python build.py      Deploy: Cloudflare Pages, output directory "public".
import os, re, json, html, shutil
from content import PAGES, HOME

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

def head(title, desc, path, p, extra='', comment='', og_title=None, og_desc=None, schema='', tw_desc=None, T=HOME):
    url = C['domain'] + path
    canon = '' if path == '/404' else f'<link rel="canonical" href="{url}">\n'
    ot, od = og_title or title, og_desc or desc
    td = tw_desc or od
    img = f"{C['domain']}/{T['og_image']}"
    alt = E(T['og_alt'])
    return f"""<!doctype html>
<html lang="en">
<head>
{comment}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{extra}{canon}<meta name="theme-color" content="#0E1A33">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{B}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{E(ot)}">
<meta property="og:description" content="{E(od)}">
<meta property="og:image" content="{img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(ot)}">
<meta name="twitter:description" content="{E(td)}">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{alt}">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{p}favicon.ico" sizes="any">
<link rel="icon" href="{p}favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600&family=Hanken+Grotesk:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
<script>document.documentElement.classList.add('js')</script>
{schema}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def nav_items(T):
    # Same order as the sections on the page, so each link moves further down; Roofing first on the general pages
    trades = [('roofing/', 'Roofing')] if T['slug'] == 'home' else []
    return trades + [('#' + T['busy_id'], T['busy_nav']), ('#how-it-works', 'How it works'), ('#pricing', 'Pricing'), ('#faq', 'FAQ')]

def header(p, nav=True, T=HOME):
    items = nav_items(T)
    href = lambda h: h if nav else f'{p}{h}'
    links = ''.join(f'<a href="{href(h)}" data-spy="{h[1:]}">{t}</a>' if h.startswith('#') else f'<a href="{p}{h}">{t}</a>' for h, t in items)
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

def footer(p, home=False, T=HOME):
    a = '' if home else p
    product = ''.join(f'<a href="{a}{h}">{t}</a>' for h, t in nav_items(T))
    letters = ''.join(f'<span style="--i:{i}">{ch}</span>' for i, ch in enumerate(B.lower()))
    login = f'<a href="{LOGIN}">Client login</a>' if LOGIN else ''
    phone = f'<a href="tel:{C["us_phone_tel"]}">{PHONE}</a>' if PHONE else ''
    return f"""</main>

<footer class="closing">
  <div class="wrap inner">
    <div class="close-top">
      <div><h2>{T['closing']}</h2>
      <div class="act"><a class="btn light" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>{phone_link('or call ')}</div></div>
      <div class="close-card play" aria-hidden="true"><div class="fcard booked" data-a="s" style="--d:300"><div class="h"><span>1:48</span><span>Example</span></div><b>Booked Mon 9:00 AM</b><br>Added to your calendar. Text confirmation sent.</div></div>
    </div>
    <a class="foot-logo" href="{p or './'}" aria-label="{B} home">{LOGO_DARK}</a>
    <div class="foot">
      <nav aria-label="Product"><h3>Product</h3>{product}{login}</nav>
      <nav aria-label="Legal"><h3>Legal</h3><a href="{p}privacy/">Privacy</a><a href="{p}terms/">Terms</a><a href="{p}refunds/">Refunds</a></nav>
      <div><h3>Contact</h3><a href="mailto:{C['email']}">{C['email']}</a>{phone}</div>
    </div>
    <div class="mark play" aria-hidden="true">
      <span class="sig-line"></span>
      <span class="word">{letters}</span>
    </div>
    <p class="legalline">&copy; <span id="year">2026</span> {B}. {T['tagline']}</p>
    <p class="legalline brandline">{B} is a brand of {C['company']} &middot; {C['company_address']}</p>
  </div>
</footer>
<script src="{p}assets/lenis.min.js"></script>
<script src="{p}assets/main.js"></script>
{analytics()}</body>
</html>
"""


# ---------------- Trade page template ----------------
# Page text lives in content.py, one block per page.

def month_strip(booked_label):
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
    peak = max(range(30), key=lambda d: calls[d]); px = peak * step + step / 2; py = base - 6 - calls[peak] * 5 - 22
    out.append(f'<g class="storm-tag" style="--d:{30 * 45 + 300}"><text x="{px:.1f}" y="{py:.1f}" text-anchor="middle">Storm</text></g>')
    out.insert(0, f'<line x1="0" x2="{W}" y1="{base}" y2="{base}" stroke="var(--ink-2)"/>')
    return (f'<figure class="month play"><div class="month-scroll"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Example: calls answered each day in September, 180 in total, with a spike mid-month after a storm, and the 24 days with a booking marked.">{"".join(out)}</svg></div>'
            '<p class="swipe">Scroll for the full month</p><figcaption><span><i class="k-call"></i>One call answered</span><span><i class="k-book"></i>' + booked_label + '</span></figcaption></figure>')

def connector(label, x, kind='', ok=False):
    return '\n  <div class="connector play ' + kind + '" aria-hidden="true"><span class="dot"></span></div>\n'


def leakmap(start):
    W, H = 1160, 150
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for y in range(10, H, 22) for x in range(10, W, 22))
    xs = [190, 380, 570, 760, 950]
    route = f'M20 75 H{W - 20}'
    marks = ''.join(f'<g class="hit" style="--d:{900 + i * 260}"><path class="x" d="M{x - 9} 66 L{x + 9} 84 M{x + 9} 66 L{x - 9} 84"/>'
                    f'<path class="ck" d="M{x - 10} 75 L{x - 3} 82 L{x + 11} 67"/></g>' for i, x in enumerate(xs))
    return (f'<div class="leakmap play"><svg viewBox="0 0 {W} {H}" role="img" aria-label="The path from a customer\'s call to a booked job, broken in five places.">'
            f'<g class="dots">{dots}</g><path class="route" d="{route}"/>{marks}'
            f'<circle class="end" cx="20" cy="75" r="6"/><circle class="end" cx="{W - 20}" cy="75" r="6"/>'
            f'<text x="20" y="112">{start}</text><text x="{W - 20}" y="112" text-anchor="end">Booked job</text></svg></div>')


def schema(T):
    url = C['domain'] + T['path']
    return '<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": C['domain'] + "/#org", "name": B, "url": C['domain'] + "/",
             "logo": C['domain'] + "/icon-512.png", "email": C['email']},
            {"@type": "WebSite", "@id": C['domain'] + "/#site", "url": C['domain'] + "/", "name": B, "publisher": {"@id": C['domain'] + "/#org"}},
            {"@type": "Service", "name": T['service_name'], "serviceType": T['service_type'], "url": url,
             "provider": {"@id": C['domain'] + "/#org"}, "areaServed": "US",
             "offers": {"@type": "Offer", "price": C['price'].lstrip('$'), "priceCurrency": "USD"}},
        ]}) + '</script>\n'

def trade_page(T):
    p, X = T['p'], T['example']
    eb = X['business']
    leaks = ''.join(f'<li data-a style="--d:{i * 90}"><h3>{a}</h3><p>{b}</p><p class="fix">{c}</p></li>' for i, (a, b, c) in enumerate(T['leaks']))
    queue = ''.join(f'<div class="q {c}" data-a style="--d:{400 + i * 220}"><span class="lvl">{l}</span><span><b>{h}</b><small>{d}</small></span><span class="when {k}">{s}</span></div>' for i, (c, l, h, d, s, k) in enumerate(X['queue']))
    ledger = ''.join(f'<div data-a style="--d:{200 + i * 110}"><dt>{k}</dt><dd data-count="{v}">{v}</dd></div>' for i, (k, v) in enumerate(T['report']))
    first = ('How much', 'What does it sound', 'What if a caller', 'What if it gets', 'Do I keep', 'Can I switch')
    qa = sorted(T['faq'], key=lambda x: next((i for i, f in enumerate(first) if x[0].startswith(f)), 99))
    det = [f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qa]
    top, rest = det[:6], det[6:]
    half = (len(rest) + 1) // 2
    faq = (f'<div class="faq-col">{"".join(top[:3])}</div><div class="faq-col">{"".join(top[3:])}</div>'
           f'<div class="faq-extra" id="faq-extra"><div class="faq-col">{"".join(rest[:half])}</div><div class="faq-col">{"".join(rest[half:])}</div></div>'
           f'<button class="faq-more" type="button" aria-controls="faq-extra" aria-expanded="true" hidden>More questions ({len(rest)})</button>')
    call = ''
    for i, (line, who) in enumerate(X['w_call']):
        cls, name = (' class="ai"', B) if who == 'ai' else ('', 'Caller')
        call += f'<p{cls} data-a style="--d:{200 + i * 750}"><b>{name}</b><span>{line}</span></p>'
    chips = ''.join(f'<span data-a="s" style="--d:{3100 + i * 140}">{c}</span>' for i, c in enumerate(X['w_chips']))
    thread = ''.join(f'<div class="msg{" " + k if k else ""}" data-a style="--d:{200 + i * 1000}"><small>{h}</small>{m}</div>' for i, (h, m, k) in enumerate(X['followups']))
    def feats(items):
        return '<ul class="feats">' + ''.join(f'<li><h4>{h}</h4><p>{d}</p></li>' for h, d in items) + '</ul>'
    m0, m1, m2 = T['moments']
    rules = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in X['rules'])
    trade_row = f'<p class="trade-row">{T["trade_row"]}</p>' if T['trade_row'] else ''
    return head(T['title'], T['desc'], T['path'], p, og_title=T['og_title'], og_desc=T['og_desc'], tw_desc=T['tw_desc'],
                schema=schema(T), T=T) + header(p, T=T) + f"""
  <section class="wrap hero" aria-labelledby="hero-title">
    <div class="hero-inner">
      <figure class="flow play" aria-label="{X['flow_aria']}">
        <svg class="path" viewBox="0 0 1000 290" preserveAspectRatio="none" aria-hidden="true">
          <path d="M0 46 H330 Q360 46 360 76 V120 Q360 150 390 150 H1000"/>
          <path class="live" d="M0 46 H330 Q360 46 360 76 V120 Q360 150 390 150 H870"/>
        </svg>
        <span class="signal" aria-hidden="true"></span>
        <span class="mtip" aria-hidden="true"></span>
        <span class="node pill" data-step="1" style="left:9%;top:46px"><i></i>Incoming call</span>
        <span class="node pill" data-step="2" style="left:45%;top:150px"><i></i>Answered</span>
        <span class="node pill" data-step="3" style="left:66%;top:150px"><i></i>Qualified</span>
        <span class="node pill ok" data-step="4" style="left:87%;top:150px"><i></i>Booked</span>
        <div class="fcard" data-step="1" style="left:1%;top:80px;width:23%"><div class="h"><span>Saturday, 7:42 PM</span><span>Example</span></div><div class="fb">{X['flow_card1']}</div></div>
        <div class="fcard dk" data-step="2" style="left:29%;top:178px;width:22%"><div class="h"><span>0:03</span><span class="typing" aria-hidden="true"><i></i><i></i><i></i></span></div><span class="say">"{X['call'][0][0]}"</span></div>
        <div class="fcard" data-step="3" style="left:53%;top:178px;width:19%"><div class="h"><span>1:05</span></div><div class="fb">{X['flow_card3']}</div></div>
        <div class="fcard booked" data-step="4" style="left:74.5%;top:178px;width:23%"><div class="h"><span>1:48</span></div><div class="fb"><b>Booked Mon 9:00 AM</b><br>Added to your calendar. Text confirmation sent.</div></div>
      </figure>
      <div class="hero-copy">
        <div>
          {T['back_link']}<p class="eyebrow">{T['eyebrow']}</p>
          <h1 id="hero-title">{T['h1']}</h1>
        </div>
        <div>
          <p class="sub">{T['sub']}</p>
          <div class="act"><a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a><a class="link" href="#how-it-works">See how it works</a></div>
          <p class="cta-note">15-minute demo, you'll hear it answer a call. {C['price']} a month, no contract.</p>
          {trade_row}
        </div>
      </div>
      <div class="scene">
        <div class="scene-pin">
          <ol class="rail" aria-label="Steps of the example call"><li><button type="button" data-beat="0" aria-label="Show the incoming call step"><i></i><b>Incoming call</b><span>0:00</span></button></li><li><button type="button" data-beat="1" aria-label="Show the answered step"><i></i><b>Answered</b><span>0:03</span></button></li><li><button type="button" data-beat="2" aria-label="Show the qualified step"><i></i><b>Qualified</b><span>1:05</span></button></li><li class="ok"><button type="button" data-beat="3" aria-label="Show the booked step"><i></i><b>Booked</b><span>1:48</span></button></li><li class="rail-fill" aria-hidden="true"></li></ol>
          <div class="stage" role="img" aria-label="{X['flow_aria']}">
            <div class="beat b1"><div class="ring"><span></span><span></span></div>
              <div class="fcard big"><div class="h"><span>Saturday, 7:42 PM</span><span>Example</span></div>{X['flow_card1']}<p class="ringing">Ringing</p></div><p class="scroll-cue">Scroll to follow the call</p></div>
            <div class="beat b2"><p class="said ai"><small>{B}</small><span class="type" data-text="{E(X['call'][0][0])}"></span></p><p class="said caller"><small>Caller</small><span>{X['call'][1][0]}</span></p></div>
            <div class="beat b3"><div class="fcard big detail"><div class="h"><span>1:05</span><span>Qualified</span></div><b>{X['issue']}</b><div class="tags">{"".join(f'<span style="--k:{i}">{f}</span>' for i, f in enumerate(X['facts']))}</div></div></div>
            <div class="beat b4"><div class="cal"><div class="cal-h">Monday, October 12<span>Your calendar</span></div><div class="slot"><time>8 AM</time><div><span class="busy">{X['cal_busy']}</span></div></div><div class="slot"><time>9 AM</time><div class="drop"><span class="ev"><b>Booked Mon 9:00 AM</b>{X['cal_where']}</span></div></div><div class="slot"><time>10 AM</time><div></div></div></div>
              <div class="bubble me sms-pop">{X['sms']}</div></div>
          </div>
          <a class="skip-call" href="#leaks">Skip the call</a>
        </div>
      </div>
      <p class="flow-cap">{T['flow_cap']}</p>
    </div>
  </section>
""" + connector('Where leads go', '20%', 'to-dark') + f"""
  <section class="dark" id="leaks" aria-labelledby="leaks-title">
    <div class="wrap sec" style="padding-top:64px">
      <div class="split"><h2 id="leaks-title">{T['leaks_title']}</h2><p>{T['leaks_intro']}</p></div>
      {leakmap(T['leakmap_start'])}
      <ul class="leaks play">{leaks}</ul>
      <p class="plug">{B} covers all five for one monthly price.</p>
    </div>
  </section>
""" + connector('What it does', '64%', 'from-dark') + f"""
  <section class="wrap" id="what-it-does" aria-labelledby="what-title" style="padding-top:56px;padding-bottom:40px">
    <div class="split"><h2 id="what-title">{T['what_title']}</h2><p>It answers in your company's name and handles each step, from the first ring to the review request.</p></div>
    <div class="rows">
      <div class="row">
        <div class="row-copy"><span class="pill"><i></i>On the call</span><h3>Every call answered and qualified</h3>{feats(m0[2])}</div>
        <div><div class="ui ondark play" aria-label="Example of an urgent call transferred to the owner">
          <div class="ui-h">Live call<span class="rec">Recording<span class="tmr" aria-hidden="true"></span></span></div>
          <div class="tx">{call}</div>
          <div class="chips">{chips}</div>
        </div><p class="ui-cap">Example. Names and addresses are made up.</p></div>
      </div>
      <div class="row flip">
        <div class="row-copy"><span class="pill ok"><i></i>Right after</span><h3>Booked on your calendar, confirmed by text</h3>{feats(m1[2])}</div>
        <div><div class="ui onlight play" aria-label="Example of a web lead texted back and booked">
          <div class="ui-h">{X['w_day']}<span>Your calendar</span></div>
          <div class="slot"><time>{X['w_busy'][0]}</time><div><span class="busy">{X['w_busy'][1]}</span></div></div>
          <div class="slot"><time>{X['w_ev'][0]}</time><div><span class="ev" data-a="drop" style="display:block;--d:500"><b>{X['w_ev'][1]}</b>{X['w_ev'][2]}</span></div></div>
          <div class="slot"><time>{X['w_after']}</time><div></div></div>
          <div class="sms">
            <div class="bubble me" data-a style="--d:1400">{X['w_sms']}</div>
            <div class="bubble" data-a style="--d:2300">{X['w_reply']}</div>
            <small>{X['w_note']}</small>
          </div>
        </div><p class="ui-cap">Example. Names and addresses are made up.</p></div>
      </div>
      <div class="row">
        <div class="row-copy"><span class="pill"><i></i>Weeks later</span><h3>The follow-ups you never get to</h3>{feats(m2[2])}</div>
        <div><div class="ui ondark play" aria-label="Example of follow-up messages">
          <div class="ui-h">Follow-ups<span>This week</span></div>
          <div class="thread">{thread}</div>
        </div><p class="ui-cap">Example. Names are made up.</p></div>
      </div>
    </div>
  </section>
""" + connector('Busy days', '30%', 'to-dark') + f"""
  <section class="dark storm" id="{T['busy_id']}" aria-labelledby="storm-title">
    <div class="wrap sec storm-grid" style="padding-top:64px">
      <div>
        <h2 id="storm-title">{T['busy_title']}</h2>
        <p>{T['busy_copy']}</p>
      </div>
      <div>
        <div class="queue play" aria-label="Example {T['busy_mode']} list, sorted by urgency">
          <div class="queue-head"><b><span class="switch" aria-hidden="true"></span>{T['busy_mode']}: On</b><span class="q-state">Sorted by urgency</span></div>
          {queue}
        </div>
        <p class="note">{T['busy_note']}</p>
      </div>
    </div>
  </section>
""" + connector('Every month', '72%', 'from-dark') + f"""
  <section class="wrap" id="report" aria-labelledby="report-title" style="padding-top:56px;padding-bottom:104px">
    <div class="split"><h2 id="report-title">Your monthly Lead Recovery Report</h2><p>Once a month you get a plain count of what happened to every lead.</p></div>
    <article class="sheet play" aria-label="Example Lead Recovery Report">
      <header class="sheet-h"><div><b>Lead Recovery Report</b><span>{eb}, September</span></div><span class="ex">Example report</span></header>
      {month_strip(T['strip_booked'])}
      <dl class="ledger">{ledger}</dl>
      <p class="report-foot">{T['report_foot']}</p>
    </article>
  </section>

  <section class="wrap" id="how-it-works" aria-labelledby="how-title" style="padding-bottom:120px">
    <div class="split"><h2 id="how-title">How it works</h2><p>It works with the tools you already use, so there's no new CRM to learn.</p></div>
    <ol class="journey play">
      <li data-a style="--d:200"><span class="pill"><i></i>Step 1</span><h3>30-minute setup call</h3><p>Your services, service area, hours, the questions to ask and your booking rules.</p>
        <div class="fcard jc"><div class="h"><span>Your rules</span><span>Example</span></div><dl class="rules">{rules}</dl></div></li>
      <li data-a style="--d:700"><span class="pill"><i></i>Step 2</span><h3>Forward your calls</h3><p>Missed and after-hours calls go to a number we set up. <strong>You keep your existing number.</strong></p>
        <div class="fcard dk jc"><div class="h"><span>Call forwarding</span><span class="fwd"><span class="switch" aria-hidden="true"></span>On</span></div><b>Missed and after-hours calls</b> now ring through to {B}. Your number stays the same.</div></li>
      <li data-a style="--d:1200"><span class="pill ok"><i></i>Step 3</span><h3>Go live</h3><p>{B} starts answering. You can listen to any call, and the Lead Recovery Report arrives each month.</p>
        <div class="fcard booked jc"><div class="h"><span>Live</span><span>Usually 1 to 2 weeks</span></div><b>Answering your calls</b><br>Every call recorded, every booking in your calendar.</div></li>
    </ol>
  </section>

  <section class="wrap" id="pricing" aria-labelledby="pricing-title" style="padding-bottom:120px">
    <div class="split"><h2 id="pricing-title">One plan, one price</h2><p>{C['price']} a month covers everything on this page.</p></div>
    <div class="price">
      <div class="price-main">
        <p class="plan-name">{T['plan_name']}</p>
        <p class="amount">{C['price']}<span>a month</span></p>
        <ul class="terms"><li>No contract</li><li>Keep your number</li><li>Cancel anytime</li></ul>
        <p class="founding"><b>{T['founding']}:</b> setup fee waived.</p>
        <a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>
      </div>
      <div class="price-side">
        <p class="side-h">Everything included</p>
        <ul class="includes"><li>Calls answered, qualified and booked, 24/7</li><li>Follow-ups, old leads and review requests</li><li>{T['busy_mode']}</li><li>Monthly Lead Recovery Report</li><li>Setup and tuning done for you</li><li>A real person for support</li></ul>
        <p class="fine">Includes a generous monthly allowance of AI call minutes. We'll tell you upfront if you ever get close. Billed monthly in US dollars. See the <a href="{p}refunds/">refund and cancellation policy</a>.</p>
      </div>
    </div>
  </section>

  <section class="wrap" id="faq" aria-labelledby="faq-title" style="padding-bottom:120px">
    <div class="split"><h2 id="faq-title">{T['faq_title']}</h2><p>Something else on your mind? Ask us on the demo call.</p></div>
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
        <p class="contact-note"><b>{T['founding']}:</b> {C['price']} a month, no setup fee, no contract.</p>
      </div>
      <div class="form">
        <form class="lead-form" action="{C['form_endpoint']}" method="POST" novalidate data-phone="{PHONE}" data-email="{C['email']}">
          <h3>We'll call you back</h3>
          <p class="form-sub">We'll call you to set up a 15-minute demo.</p>
          <input type="hidden" name="page" value="{T['slug']}">
          <div class="fields">
            <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required minlength="2" maxlength="80" aria-describedby="e-name"><p class="field-err" id="e-name" hidden></p></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required maxlength="20" placeholder="(512) 555-0134" aria-describedby="e-phone"><p class="field-err" id="e-phone" hidden></p></div>
            <div class="field full"><label for="f-company">Company</label><input id="f-company" name="company" type="text" autocomplete="organization" required minlength="2" maxlength="120" aria-describedby="e-company"><p class="field-err" id="e-company" hidden></p></div>
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
          <div class="cb-card"><div class="h"><span>Call-back requested</span><span>Just now</span></div><b class="cb-company"></b><p>We'll call <b class="cb-phone"></b>. <button type="button" class="cb-edit">Wrong number? Change it</button></p></div>
          <p>If you'd rather pick a time yourself, book it now.</p>
          <a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a>
        </div>
      </div>
    </div>
  </section>
  <div class="mcta" hidden><a class="btn" href="{C['calendly']}" target="_blank" rel="noopener">Book a 15-min demo</a></div>
""" + footer(p, home=True, T=T)

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
      <li>To run the service for our clients: answering calls, booking appointments, sending confirmations and follow-ups, and producing recordings, transcripts and reports.</li>
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
    <p>{B} is an AI front desk for home-service businesses. Depending on your setup, it answers calls forwarded to it, qualifies callers, checks your service area, books visits and inspections into your calendar, sends text confirmations and reminders, replies to missed calls and web leads, follows up on quotes, estimates and past leads, asks customers for reviews, transfers calls or takes messages, and gives you recordings, transcripts and a monthly report. We may improve or change features over time.</p>
    <h2>2. Your subscription</h2>
    <ul>
      <li>{B} costs {C['price']} per month, billed monthly in advance in US dollars, unless we agree a different price with you in writing.</li>
      <li>It is month-to-month. There is no long-term contract.</li>
      <li>A one-time setup fee may apply. For founding customers, it is waived.</li>
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
    <p>{B} costs {C['price']} per month, billed monthly in advance in US dollars. For founding customers, the setup fee is waived.</p>
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
def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)       # comments
    css = re.sub(r'\s+', ' ', css)                          # whitespace runs
    css = re.sub(r'\s*([{};,>])\s*', lambda m: m.group(1), css)   # around punctuation (never around ':' or '+'/'-': selectors and calc() need them)
    return css.replace(';}', '}').strip()

def check(rel, s):
    for bad in ('—', '–', '·'):
        assert bad not in s, f'{repr(bad)} in {rel}'
    if rel == '_redirects':   # routing only, never shown: may name retired paths
        return
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
    for f in ('main.js', 'lenis.min.js'):
        shutil.copy(os.path.join(ROOT, 'assets', f), os.path.join(OUT, 'assets', f))
    # The stylesheet ships minified; assets/style.css stays the readable source
    open(os.path.join(OUT, 'assets', 'style.css'), 'w', encoding='utf-8').write(minify_css(open(os.path.join(ROOT, 'assets', 'style.css'), encoding='utf-8').read()))
    for T in PAGES:
        write(os.path.join(T['path'].strip('/'), 'index.html'), trade_page(T))
    write(os.path.join('privacy', 'index.html'), legal('privacy', 'Privacy Policy', f'What {B} collects, how it is used, and your choices.', PRIVACY))
    write(os.path.join('terms', 'index.html'), legal('terms', 'Terms of Service', f'The terms for using {B}.', TERMS))
    write(os.path.join('refunds', 'index.html'), legal('refunds', 'Refund and Cancellation Policy', f'How cancelling and refunds work for {B}.', REFUNDS))
    write('404.html', notfound())
    os.makedirs(os.path.join(OUT, 'brand'), exist_ok=True)
    BA = os.path.join(ROOT, 'design', 'brand', 'crewwise-brand-assets')
    for f in ('crewwise-logo.svg', 'crewwise-logo-on-dark.svg', 'crewwise-icon.svg', 'crewwise-mark.svg'):
        shutil.copy(os.path.join(BA, f), os.path.join(OUT, 'brand', f))
    write('favicon.svg', open(os.path.join(ROOT, 'design', 'collateral', 'favicon.svg'), encoding='utf-8').read())
    write('site.webmanifest', json.dumps({"name": B, "short_name": B, "start_url": "/", "display": "browser",
        "background_color": "#F8F9FD", "theme_color": "#0E1A33",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}, {"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=2))
    for f in ('apple-touch-icon.png', 'icon-192.png', 'icon-512.png', 'favicon-16.png', 'favicon-32.png', 'favicon-48.png', 'favicon.ico') + tuple(T['og_image'].split('?')[0] for T in PAGES):
        s = os.path.join(ROOT, 'design', 'collateral', f)
        if os.path.exists(s):
            shutil.copy(s, os.path.join(OUT, f)); print('copied public/' + f)
    write('_redirects', ''.join(f'{u:<10} /roofing/  301\n' for u in ('/roofers', '/roofers/', '/roofer', '/roofer/'))
          + '/photographers   /  301\n/photographers/  /  301\n')   # the retired photographers page goes to the homepage
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {C["domain"]}/sitemap.xml\n')
    urls = ''.join(f'  <url><loc>{C["domain"]}{u}</loc></url>\n' for u in [T['path'] for T in PAGES] + ['/privacy/', '/terms/', '/refunds/'])
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

if __name__ == '__main__':
    main()
