import os
HERE = os.path.dirname(os.path.abspath(__file__))

MARK_DARK = '<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="10" fill="#13233A"/><polyline points="10,21 22,11 34,21" fill="none" stroke="#F06A35" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
MARK_LIGHT = '<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="10" fill="#F7F3EC"/><polyline points="10,21 22,11 34,21" fill="none" stroke="#C4471B" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><polyline points="15,26 20,31 30,21" fill="none" stroke="#13233A" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

THEMES = {
 'a': ('White', 'light', MARK_DARK, """
    --ground: #FFFFFF; --ink: #13233A; --ink-2: #4E5B6C; --rule-strong: #C9D1DB;
    --accent: #C4471B; --accent-ink: #B5401A; --cta: #C4471B; --cta-hover: #B23F17; --cta-edge: #A63A14;
    --app: #FFFFFF; --app-edge: #DDE3EA; --app-ink: #13233A; --app-ink-2: #5B6878; --app-rule: #EAEEF2; --app-rule-strong: #CDD5DE; --app-sel: #F3F5F8;
    --app-shadow: 0 1px 2px rgba(19,35,58,.06), 0 24px 60px -24px rgba(19,35,58,.28), 0 60px 120px -60px rgba(19,35,58,.25);
    --ok: #237A4B; --flash: rgba(196,71,27,.12); --ev: #F3F5F8; --ev-edge: #DDE3EA; --ev-new: #FBEDE7;
 """),
 'b': ('Navy', 'dark', MARK_LIGHT, """
    --ground: #0B1627; --ink: #EEF2F7; --ink-2: #A6B3C4; --rule-strong: #3A4C66;
    --accent: #F06A35; --accent-ink: #F58A5E; --cta: #C4471B; --cta-hover: #D0521F; --cta-edge: #E0602D;
    --app: #101E33; --app-edge: #22344F; --app-ink: #E6ECF3; --app-ink-2: #93A2B6; --app-rule: #1C2C44; --app-rule-strong: #34465F; --app-sel: #17283F;
    --app-shadow: 0 0 0 1px rgba(255,255,255,.02), 0 30px 80px -30px rgba(0,0,0,.7);
    --ok: #57C08A; --flash: rgba(240,106,53,.2); --ev: #162740; --ev-edge: #24385A; --ev-new: rgba(240,106,53,.16);
 """),
 'c': ('Canvas', 'light', MARK_DARK, """
    --ground: #F7F3EC; --ink: #13233A; --ink-2: #545B66; --rule-strong: #CFC6B6;
    --accent: #C4471B; --accent-ink: #A93C16; --cta: #13233A; --cta-hover: #1C3252; --cta-edge: #0B1627;
    --app: #FFFFFF; --app-edge: #E4DCCD; --app-ink: #13233A; --app-ink-2: #5E6672; --app-rule: #EFEAE1; --app-rule-strong: #D8D0C2; --app-sel: #F8F5EF;
    --app-shadow: 0 1px 2px rgba(19,35,58,.06), 0 30px 70px -30px rgba(70,50,20,.28);
    --ok: #237A4B; --flash: rgba(196,71,27,.12); --ev: #F7F3EC; --ev-edge: #E4DCCD; --ev-new: #FBEDE7;
 """),
}

BODY = """
<header class="wrap top">
  <a class="logo" href="#">{mark}Jobstead</a>
  <nav class="nav" aria-label="Page sections"><a href="#">What it does</a><a href="#">Storm Mode</a><a href="#">Pricing</a><a href="#">Questions</a></nav>
  <a class="btn sm" href="#">Book a demo</a>
</header>

<main>
  <section class="hero wrap">
    <div class="kicker">AI front desk for roofing companies</div>
    <div class="hero-grid">
      <h1>You paid for the lead. We make sure you don't lose it.</h1>
      <div>
        <p class="sub">Jobstead answers every call 24/7, qualifies the homeowner, books the inspection into your calendar, and follows up on every estimate.</p>
        <div class="actions"><a class="btn" href="#">Book a 15-min demo</a><a class="link" href="#">Or call <b>[US PHONE]</b></a></div>
      </div>
    </div>

    <div class="stage">
      <div class="app" role="img" aria-label="Example of the Jobstead app: a Saturday evening leak call from Round Rock, transcribed, qualified and booked for Monday at 9 AM.">
        <div class="bar">
          <span class="ws">{mark}Oak Ridge Roofing</span>
          <span class="tabs"><span class="on">Calls</span><span>Calendar</span><span>Estimates</span><span>Report</span></span>
          <span class="right"><span class="toggle"><i></i>Storm Mode</span><span class="tnum">Sat, Oct 4</span></span>
        </div>
        <div class="body">
          <div class="list">
            <h3>Today</h3>
            <div class="row sel new"><span class="who tnum">(512) 555-0199</span><span class="when tnum">7:42 PM</span><span class="what">Leak, kitchen ceiling</span><span class="st ok">Booked Mon 9:00</span></div>
            <div class="row"><span class="who tnum">(512) 555-0163</span><span class="when tnum">6:58 PM</span><span class="what">Hail damage, Georgetown</span><span class="st ok">Booked Mon 11:30</span></div>
            <div class="row"><span class="who tnum">(737) 555-0128</span><span class="when tnum">6:21 PM</span><span class="what">Active leak, attic</span><span class="st hot">Sent to you</span></div>
            <div class="row"><span class="who tnum">(512) 555-0187</span><span class="when tnum">5:47 PM</span><span class="what">Estimate follow-up</span><span class="st mute">Replied</span></div>
            <div class="row"><span class="who tnum">(254) 555-0141</span><span class="when tnum">4:12 PM</span><span class="what">Outside service area</span><span class="st mute">Declined</span></div>
            <div class="row"><span class="who tnum">(512) 555-0110</span><span class="when tnum">3:30 PM</span><span class="what">Missing shingles</span><span class="st ok">Booked Tue 8:00</span></div>
          </div>
          <div class="detail">
            <div class="dh"><b class="tnum">(512) 555-0199</b><span>Round Rock, TX</span><span class="tnum">7:42 PM, <span class="dur">1:48</span></span><span class="st ok">Booked Mon 9:00</span></div>
            <div class="audio"><span class="tnum">Recording</span><canvas aria-hidden="true"></canvas></div>
            <div class="cols">
              <div class="tx">
                <div class="ln ai"><span class="sp">Jobstead</span><span>Thanks for calling Oak Ridge Roofing. How can I help?</span></div>
                <div class="ln" data-fill="0"><span class="sp">Caller</span><span>Water's coming through my kitchen ceiling after last night's storm.</span></div>
                <div class="ln ai"><span class="sp">Jobstead</span><span>Sorry to hear that. What's the address?</span></div>
                <div class="ln" data-fill="1"><span class="sp">Caller</span><span>1418 Maple Court, Round Rock.</span></div>
                <div class="ln ai"><span class="sp">Jobstead</span><span>How old is the roof, and have you started an insurance claim?</span></div>
                <div class="ln" data-fill="2,3"><span class="sp">Caller</span><span>About fifteen years. We filed a claim this morning.</span></div>
                <div class="ln ai" data-fill="4"><span class="sp">Jobstead</span><span>I can have someone there Monday at 9 AM. Does that work?</span></div>
              </div>
              <div class="cap">
                <h4>Captured</h4>
                <dl>
                  <div class="kv"><dt>Problem</dt><dd>Leak, kitchen ceiling</dd></div>
                  <div class="kv"><dt>Address</dt><dd>1418 Maple Ct</dd></div>
                  <div class="kv"><dt>Roof age</dt><dd>About 15 years</dd></div>
                  <div class="kv"><dt>Insurance</dt><dd>Claim filed</dd></div>
                  <div class="kv"><dt>Inspection</dt><dd>Mon 9:00 AM</dd></div>
                </dl>
              </div>
            </div>
            <div class="phone-sum"><span><b>Inspection</b></span><span class="st ok">Booked Mon 9:00</span><span>1418 Maple Ct, Round Rock</span></div>
          </div>
          <div class="cal">
            <h3>Mon, Oct 6</h3>
            <div class="day">
              <div class="hr"><span>8 AM</span></div><div class="hr"><span>9 AM</span></div><div class="hr"><span>10 AM</span></div><div class="hr"><span>11 AM</span></div><div class="hr"><span>12 PM</span></div><div class="hr"><span>1 PM</span></div><div class="hr"><span>2 PM</span></div>
              <div class="ev" style="top:6px;height:42px"><b>Estimate</b>Cedar Park</div>
              <div class="ev new" style="top:60px;height:48px"><b>Inspection</b>1418 Maple Ct</div>
              <div class="ev" style="top:168px;height:48px"><b>Inspection</b>88 Cedar Ridge Dr</div>
              <div class="ev" style="top:276px;height:42px"><b>Crew: tear-off</b>Hutto</div>
            </div>
          </div>
        </div>
      </div>
      <p class="note">Example. The business, callers and addresses are made up.</p>
    </div>
  </section>

  <section class="next wrap">
    <h2>Where roofing leads leak</h2>
    <p>You already pay for the leads. These are the five places they slip away.</p>
  </section>
</main>
"""

for key, (name, scheme, mark, tokens) in THEMES.items():
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jobstead · {key.upper()} · Product hero, {name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500..700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {{
    color-scheme: {scheme};
    --display: "Archivo", "Helvetica Neue", Arial, sans-serif;
    --body: "Inter", system-ui, "Segoe UI", Roboto, Arial, sans-serif;{tokens}  }}
</style>
<link rel="stylesheet" href="product.css">
</head>
<body>{BODY.replace('{mark}', mark)}
<script src="product.js"></script>
</body>
</html>
"""
    open(os.path.join(HERE, f'{key}.html'), 'w', encoding='utf-8').write(html)
    print('wrote', key)
