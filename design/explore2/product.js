// The hero app window: a call arrives, the transcript streams, details fill, the inspection lands in the calendar.
// The HTML holds the finished state, so the page is complete without JavaScript and for reduced motion.
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const app = document.querySelector('.app');
  if (!app) return;
  const $ = s => app.querySelector(s), $$ = s => [...app.querySelectorAll(s)];

  // Waveform: static shape, played portion follows the transcript
  const cv = $('.audio canvas'), ctx = cv.getContext('2d');
  const bars = Array.from({ length: 120 }, (_, i) => .25 + .75 * Math.abs(Math.sin(i * .37) * Math.cos(i * .11)));
  let played = 1;
  const css = getComputedStyle(app);
  function wave() {
    const w = cv.clientWidth, h = cv.clientHeight, d = Math.min(devicePixelRatio || 1, 2);
    if (!w) return;
    cv.width = w * d; cv.height = h * d; ctx.setTransform(d, 0, 0, d, 0, 0); ctx.clearRect(0, 0, w, h);
    const n = Math.floor(w / 4);
    for (let i = 0; i < n; i++) {
      const v = bars[Math.floor(i / n * bars.length)], bh = Math.max(2, v * h);
      ctx.fillStyle = i / n <= played ? css.getPropertyValue('--accent').trim() : css.getPropertyValue('--app-rule-strong').trim();
      ctx.fillRect(i * 4, (h - bh) / 2, 2, bh);
    }
  }
  wave(); addEventListener('resize', wave);
  if (reduce) return;

  const lines = $$('.tx .ln'), fields = $$('.kv dd'), ev = $('.ev.new'), newRow = $('.row.new'), status = $('.dh .st'), rowSt = newRow && newRow.querySelector('.st'), phoneSt = $('.phone-sum .st'), clock = $('.dh .dur');
  const finals = fields.map(f => f.textContent);
  let timers = [], tick = null;
  const later = (fn, ms) => timers.push(setTimeout(fn, ms));

  function reset() {
    timers.forEach(clearTimeout); timers = []; clearInterval(tick);
    lines.forEach(l => { l.hidden = true; l.classList.remove('in'); });
    fields.forEach(f => { f.textContent = '…'; f.classList.add('wait'); f.classList.remove('got'); });
    if (ev) ev.hidden = true;
    [status, rowSt, phoneSt].forEach(s => { if (s) { s.className = 'st hot'; s.textContent = 'On call'; } });
    played = 0; wave();
    if (newRow) { newRow.classList.remove('new'); void newRow.offsetWidth; newRow.classList.add('new'); }
  }
  function play() {
    reset();
    let t = 700, secs = 0;
    tick = setInterval(() => { secs++; if (clock) clock.textContent = '0:' + String(Math.min(59, secs * 6)).padStart(2, '0'); }, 1000);
    lines.forEach((l, i) => {
      later(() => {
        l.hidden = false; l.classList.add('in');
        played = (i + 1) / lines.length; wave();
        const k = l.getAttribute('data-fill');
        if (k) k.split(',').forEach(n => { const f = fields[+n]; if (f) { f.textContent = finals[+n]; f.classList.remove('wait'); f.classList.add('got'); } });
      }, t);
      t += 1200;
    });
    later(() => { clearInterval(tick); if (clock) clock.textContent = '1:48'; if (ev) { ev.hidden = false; ev.classList.remove('drop'); void ev.offsetWidth; ev.classList.add('drop'); } }, t);
    later(() => { [status, rowSt, phoneSt].forEach(s => { if (s) { s.className = 'st ok'; s.textContent = 'Booked Mon 9:00'; } }); }, t + 700);
    later(play, t + 7000);
  }
  let started = false;
  new IntersectionObserver(e => { if (e[0].isIntersecting && !started) { started = true; play(); } }, { threshold: .3 }).observe(app);
})();
