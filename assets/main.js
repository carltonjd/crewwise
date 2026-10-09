(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Smooth scroll like the reference site; off for reduced motion and touch (native scroll is better there) */
  let lenis = null, wakeLenis = () => {};
  if (!reduce && window.Lenis && matchMedia('(pointer: fine)').matches) {
    lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
    /* Run Lenis's frame loop only while it is moving the page, so an idle page does no work */
    let looping = false, still = 0;
    const raf = t => { lenis.raf(t); still = lenis.isScrolling ? 0 : still + 1; if (still < 20) requestAnimationFrame(raf); else looping = false; };
    const wake = () => { still = 0; if (!looping) { looping = true; requestAnimationFrame(raf); } };
    wakeLenis = wake;
    ['wheel', 'keydown', 'pointerdown', 'scroll'].forEach(e => addEventListener(e, wake, { passive: true }));
    wake();
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      const el = id.length > 1 && document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      wake(); lenis.scrollTo(el, { offset: -88 });
      history.replaceState(null, '', id);
    }));
  }

  /* Header: flat at the top, a floating bar once scrolled; always visible so Book a demo is always one tap away */
  const header = document.querySelector('.site-header');
  const nav = document.getElementById('site-nav'), menu = document.querySelector('.menu');
  let lastY = scrollY, ticking = false;
  const onScroll = () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      const y = scrollY, open = nav && nav.classList.contains('open');
      header.classList.toggle('scrolled', y > 8);
      lastY = y; ticking = false;
    });
  };
  if (header) { addEventListener('scroll', onScroll, { passive: true }); onScroll(); }

  /* Mobile menu */
  if (menu && nav) {
    const setOpen = v => { nav.classList.toggle('open', v); menu.setAttribute('aria-expanded', v); };
    menu.addEventListener('click', () => setOpen(!nav.classList.contains('open')));
    nav.addEventListener('click', e => { if (e.target.closest('a')) setOpen(false); });
    addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('open')) { setOpen(false); menu.focus(); } });
  }

  /* Highlight the nav link for the section on screen */
  const spies = [...document.querySelectorAll('.nav a[data-spy]')];
  const targets = spies.map(a => document.getElementById(a.dataset.spy)).filter(Boolean);
  if (targets.length) {
    let queued = false;
    const pick = () => {
      queued = false;
      let best = null, top = -Infinity;
      targets.forEach(t => { const r = t.getBoundingClientRect(); if (r.top < innerHeight * .45 && r.top > top && r.bottom > 80) { top = r.top; best = t; } });
      spies.forEach(a => a.classList.toggle('active', !!best && a.dataset.spy === best.id));
    };
    addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(pick); } }, { passive: true });
    pick();
  }


  if (!reduce && 'IntersectionObserver' in window) {
    /* Scroll choreography: each .play container plays once when it comes into view */
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      e.target.querySelectorAll('[data-count]').forEach(countUp);
      io.unobserve(e.target);
    }), { threshold: .12, rootMargin: '0px 0px 8% 0px' });
    document.querySelectorAll('.play').forEach(el => io.observe(el));

  }

  /* Hero: the example call plays itself along the route once it's on screen (about 9s), pauses while the mouse
     rests on it (and says so), off screen or in a background tab, and rests on Booked with Replay. No scroll coupling, and every card
     keeps its final size from the start, so nothing on the page moves. Without motion the finished call shows. */
  if (!reduce && 'IntersectionObserver' in window) document.querySelectorAll('div.route').forEach(route => {
    const typeEl = route.querySelector('.r-type'), ghost = route.querySelector('.r-ghost'), full = ghost ? ghost.textContent : '';
    const replay = route.querySelector('.route-replay');
    const STEPS = [[0, 'at1'], [1400, 'at2'], [1600, 'at-typing'], [3300, 'at-caller'], [5100, 'at3'], [5300, 'at-tags'], [7300, 'at4'], [8000, 'at-sms'], [8700, 'at-done']];
    const CPS = 45, ALL = STEPS.map(s => s[1]);
    let t = 0, idx = 0, timer = 0, onScreen = false, held = false, last = 0;
    const set = (c, on) => route.classList.toggle(c, on);
    const tick = () => {
      const now = performance.now();
      if (onScreen && !held && !document.hidden) t += now - last;
      last = now;
      while (idx < STEPS.length && t >= STEPS[idx][0]) set(STEPS[idx++][1], true);
      if (route.classList.contains('at-typing')) {
        const c = Math.min(full.length, Math.max(0, Math.floor((t - 1600) / 1000 * CPS)));
        typeEl.textContent = full.slice(0, c);
        if (c >= full.length) set('at-typing', false);
      }
      if (idx >= STEPS.length) { clearInterval(timer); timer = 0; replay.hidden = false; }
    };
    const start = () => {
      ALL.forEach(c => set(c, false)); typeEl.textContent = ''; replay.hidden = true;
      t = 0; idx = 0; last = performance.now(); clearInterval(timer); timer = setInterval(tick, 50); tick();
    };
    route.classList.add('rplay');
    let started = false;
    new IntersectionObserver(es => {
      onScreen = es[0].isIntersecting;
      if (onScreen && !started) { started = true; start(); }
    }, { threshold: .3 }).observe(route);
    const hold = v => { held = v; set('r-held', v); };
    route.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') hold(true); });
    route.addEventListener('pointerleave', () => hold(false));
    replay.addEventListener('click', () => { hold(false); start(); });
  });

  /* Phones: a booking button in thumb reach, shown whenever the hero buttons are off screen,
     hidden again while the contact form or the closing band is on screen */
  const mcta = document.querySelector('.mcta'), heroAct = document.querySelector('.hero .act');
  if (mcta && heroAct && 'IntersectionObserver' in window) {
    mcta.hidden = false;
    const seen = new Map();
    const sync = () => {
      const on = seen.get(heroAct) === false && !seen.get('end');
      mcta.classList.toggle('on', on);
      document.documentElement.classList.toggle('mcta-on', on);  /* header button steps aside while the bottom one shows */
    };
    const ends = [document.querySelector('#pricing .btn'), document.getElementById('contact'), document.querySelector('.closing')].filter(Boolean);
    const endSeen = new Set();
    new IntersectionObserver(e => { e.forEach(x => seen.set(heroAct, x.isIntersecting)); sync(); }).observe(heroAct);
    const eo = new IntersectionObserver(e => { e.forEach(x => x.isIntersecting ? endSeen.add(x.target) : endSeen.delete(x.target)); seen.set('end', endSeen.size > 0); sync(); });
    ends.forEach(el => eo.observe(el));
  }

  if (!reduce && 'IntersectionObserver' in window) {
    const once = (el, fn, threshold = .35) => {
      const o = new IntersectionObserver(es => { if (es.some(x => x.isIntersecting)) { o.disconnect(); fn(); } }, { threshold });
      o.observe(el);
    };

    /* Busy-day list: calls show up in the order they came in, then sort themselves by urgency */
    const queue = document.querySelector('.queue');
    if (queue) {
      const rows = [...queue.querySelectorAll('.q')], state = queue.querySelector('.q-state');
      const arrival = [2, 0, 3, 1].filter(i => i < rows.length);
      if (rows.length === 4) {
        rows.forEach(r => { r.removeAttribute('data-a'); r.style.opacity = '0'; });
        if (state) state.textContent = 'Incoming calls';
        once(queue, () => {
          const tops = rows.map(r => r.getBoundingClientRect().top), hs = rows.map(r => r.offsetHeight);
          const gap = Math.max(0, tops[1] - tops[0] - hs[0]);
          let y = tops[0]; const slot = [];
          arrival.forEach(i => { slot[i] = y; y += hs[i] + gap; });
          rows.forEach((r, i) => { r.style.transition = 'none'; r.style.transform = `translateY(${slot[i] - tops[i]}px)`; });
          if (state) state.textContent = 'Incoming calls';
          /* If the rows change size mid-sequence (fonts, translation, rotation), stop and show the sorted list */
          const timers = []; let done = false;
          const finish = () => { if (done) return; done = true; timers.forEach(clearTimeout); ro.disconnect();
            rows.forEach(r => { r.style.transition = ''; r.style.transform = ''; r.style.opacity = ''; });
            if (state) state.textContent = 'Sorted by urgency'; queue.classList.add('sorted'); };
          const w0 = queue.offsetWidth, h0 = rows.map(r => r.offsetHeight).join();
          const ro = new ResizeObserver(() => { if (queue.offsetWidth !== w0 || rows.map(r => r.offsetHeight).join() !== h0) finish(); });
          ro.observe(queue); rows.forEach(r => ro.observe(r));
          arrival.forEach((i, k) => timers.push(setTimeout(() => { rows[i].style.transition = 'opacity .4s ease'; rows[i].style.opacity = '1'; }, 350 + k * 380)));
          timers.push(setTimeout(() => {
            if (state) state.textContent = 'Sorted by urgency';
            rows.forEach(r => { r.style.transition = 'transform .8s cubic-bezier(.22,1,.36,1), opacity .25s ease'; r.style.transform = ''; r.style.opacity = '.45'; });
            timers.push(setTimeout(() => rows.forEach(r => { r.style.opacity = '1'; }), 650));
            queue.classList.add('sorted');
            timers.push(setTimeout(() => { done = true; ro.disconnect(); }, 900));
          }, 350 + arrival.length * 380 + 700));
        });
      }
    }

    /* Live call: the recording timer runs while the transcript types in */
    document.querySelectorAll('.tmr').forEach(t => {
      const card = t.closest('.ui');
      once(card, () => {
        const end = 24, dur = 3600, t0 = performance.now();
        const tick = now => {
          const s = Math.min(end, Math.floor((now - t0) / dur * end));
          t.textContent = ` 0:${String(s).padStart(2, '0')}`;
          if (s < end) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    });
  }

  /* FAQ: the first six questions show; the rest open with "More questions". Without JS all of them show. */
  const more = document.querySelector('.faq-more'), extra = document.getElementById('faq-extra');
  if (more && extra) {
    more.hidden = false; extra.hidden = true; more.setAttribute('aria-expanded', 'false');
    more.addEventListener('click', () => { extra.hidden = false; more.setAttribute('aria-expanded', 'true'); more.hidden = true; const q = extra.querySelector('summary'); if (q) q.focus(); });
  }

  function countUp(el) {
    const to = +el.dataset.count, pre = el.dataset.prefix || '', dur = 1400, t0 = performance.now();
    const step = now => {
      const k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = pre + Math.round(to * e).toLocaleString('en-US');
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* Lead form */
  document.querySelectorAll('.lead-form').forEach(form => {
    const box = form.closest('.form'), btn = form.querySelector('button[type="submit"]'), label = btn.textContent;
    const err = form.querySelector('.form-error'), thanks = box.querySelector('.thanks'), phone = form.dataset.phone || '', email = form.dataset.email || '';
    const show = m => { err.textContent = m; err.hidden = false; };
    /* Field checks. Each returns an error message, or '' when the value is fine.
       Phone: a US number, 10 digits, or 11 starting with 1. */
    const digits = v => v.replace(/\D/g, '');
    const checks = {
      name: v => !v ? 'Enter your name.' : v.length < 2 || !/\p{L}/u.test(v) ? 'Enter your name so we know who to ask for.' : '',
      phone: v => {
        if (!v) return 'Enter a phone number we can call you back on.';
        if (/[^\d\s()+.\-]/.test(v)) return 'Use numbers only, like (512) 555-0134.';
        const d = digits(v);
        return d.length === 10 || (d.length === 11 && d[0] === '1') ? '' : 'Enter a 10-digit US phone number, like (512) 555-0134.';
      },
      company: v => v && v.length < 2 ? 'Enter your full company name, or leave it blank.' : '',
      trade: v => !v ? 'Tell us your trade, like painting or landscaping.' : '',
    };
    const touched = new Set();
    let pressing = false;
    btn.addEventListener('pointerdown', () => { pressing = true; setTimeout(() => { pressing = false; }, 700); });
    const check = input => {
      const msg = checks[input.name](input.value.trim()), slot = form.querySelector('#' + input.getAttribute('aria-describedby'));
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (slot) { slot.textContent = msg; slot.hidden = !msg; }
      return !msg;
    };
    Object.keys(checks).forEach(n => {
      const input = form.elements[n]; if (!input) return;
      input.addEventListener('blur', e => {
        if (n === 'phone') { const d = digits(input.value), t = d.length === 11 && d[0] === '1' ? d.slice(1) : d; if (t.length === 10) input.value = `(${t.slice(0, 3)}) ${t.slice(3, 6)}-${t.slice(6)}`; }
        /* Heading for the submit button: let submit validate, so an error message can't shift the button out from under the tap */
        if (e.relatedTarget === btn || pressing) return;
        if (input.value.trim()) touched.add(n);
        if (touched.has(n)) check(input);
      });
      input.addEventListener('input', () => { if (touched.has(n)) check(input); if (!err.hidden && form.querySelectorAll('[aria-invalid="true"]').length === 0) err.hidden = true; });
    });
    const edit = box.querySelector('.cb-edit');
    if (edit) edit.addEventListener('click', () => {
      thanks.hidden = true; form.hidden = false; btn.disabled = false; btn.textContent = 'Send again';
      form.elements.phone.focus(); form.elements.phone.select();
    });
    form.addEventListener('submit', e => {
      e.preventDefault(); err.hidden = true;
      if (btn.disabled) return;
      const bad = Object.keys(checks).map(n => form.elements[n]).filter(i => i && (touched.add(i.name), !check(i)));
      if (bad.length) { show(bad.length > 1 ? 'A few details need fixing before we can call you.' : 'One detail needs fixing before we can call you.'); bad[0].focus(); return; }
      if (form.elements._gotcha && form.elements._gotcha.value) return;
      btn.disabled = true; btn.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(r => { if (!r.ok) throw 0;
          const first = (form.elements.name.value || '').trim().split(/\s+/)[0];
          const n = thanks.querySelector('.thanks-name'); if (n) n.textContent = first ? ', ' + first : '';
          const cbP = thanks.querySelector('.cb-phone'), cbC = thanks.querySelector('.cb-company');
          if (cbP) cbP.textContent = form.elements.phone.value.trim();
          if (cbC) cbC.textContent = form.elements.company.value.trim() || form.elements.name.value.trim();
          form.hidden = true; thanks.hidden = false; thanks.classList.remove('in'); void thanks.offsetWidth; thanks.classList.add('in'); thanks.focus(); })
        .catch(() => { show(`Your details didn’t send. Check your connection and try again${phone ? ', or call us at ' + phone : email ? ', or email us at ' + email : ''}.`); btn.disabled = false; btn.textContent = label; });
    });
  });
  /* Other trades: "Join the list" opens the waitlist dialog (without JavaScript the link goes to the contact form) */
  const join = document.getElementById('join');
  if (join && join.showModal) {
    const close = () => join.close();
    document.addEventListener('click', e => {
      if (!e.target.closest('[data-join]')) return;
      e.preventDefault(); e.stopPropagation();
      join.showModal(); if (lenis) lenis.stop();
    }, true);
    join.querySelector('.dlg-x').addEventListener('click', close);
    join.addEventListener('click', e => { if (e.target === join) close(); });
    join.addEventListener('close', () => { if (lenis) { lenis.start(); wakeLenis(); } });
  }

  /* Report chart on phones: start the scroll at the storm, where the story is */
  const ms = document.querySelector('.month-scroll'), stormTag = ms && ms.querySelector('.storm-tag text'), msSvg = ms && ms.querySelector('svg');
  if (stormTag && msSvg) {
    const centre = () => { if (ms.scrollWidth > ms.clientWidth + 4) ms.scrollLeft = +stormTag.getAttribute('x') * msSvg.clientWidth / msSvg.viewBox.baseVal.width - ms.clientWidth / 2; };
    centre(); addEventListener('load', centre);
  }
})();
