(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Smooth scroll like the reference site; off for reduced motion and touch (native scroll is better there) */
  let lenis = null;
  if (!reduce && window.Lenis && matchMedia('(pointer: fine)').matches) {
    lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
    const raf = t => { lenis.raf(t); requestAnimationFrame(raf); };
    requestAnimationFrame(raf);
    document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      const el = id.length > 1 && document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      lenis.scrollTo(el, { offset: -88 });
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
    }), { threshold: .3, rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.play').forEach(el => io.observe(el));

    /* Hero: one clock drives the line, the signal and every checkpoint, so they can never drift apart.
       The path is rebuilt in real pixels (no stretched SVG), so its length and the fill are exact. */
    const flow = document.querySelector('.flow');
    const wide = matchMedia('(min-width: 1000px)');
    if (flow) {
      const svg = flow.querySelector('svg.path'), base = svg.querySelector('path:not(.live)'), live = svg.querySelector('path.live');
      const sig = flow.querySelector('.signal');
      const steps = [1, 2, 3, 4].map(n => [...flow.querySelectorAll(`[data-step="${n}"]`)]);
      const nodeX = [.09, .45, .66, .87];
      const TRAVEL = 4200, HOLD = 6500;
      let W = 0, LEN = 0, stops = [], t0 = 0, raf = 0, timer = 0, visible = false, hit = 0;

      const layout = () => {
        W = flow.clientWidth; const H = flow.clientHeight; if (!W) return;
        const VW = document.documentElement.clientWidth, OFF = flow.getBoundingClientRect().left;
        svg.style.left = -OFF + 'px'; svg.style.width = VW + 'px'; svg.style.right = 'auto';
        svg.setAttribute('viewBox', `${-OFF} 0 ${VW} ${H}`); svg.setAttribute('preserveAspectRatio', 'none');
        const bx = .36 * W, r = 30, y1 = 46, y2 = 170;
        const d = end => `M${-OFF} ${y1} H${bx - r} Q${bx} ${y1} ${bx} ${y1 + r} V${y2 - r} Q${bx} ${y2} ${bx + r} ${y2} H${end}`;
        base.setAttribute('d', d(VW - OFF)); live.setAttribute('d', d(nodeX[3] * W));
        base.removeAttribute('pathLength'); live.removeAttribute('pathLength');
        LEN = live.getTotalLength();
        // length along the path at which each node sits
        stops = nodeX.map((nx, i) => {
          const tx = nx * W, ty = i === 0 ? y1 : y2;
          let best = 0, bd = 1e9;
          for (let l = 0; l <= LEN; l += 2) { const p = live.getPointAtLength(l); const dd = Math.hypot(p.x - tx, p.y - ty); if (dd < bd) { bd = dd; best = l; } }
          return best;
        });
        stops[3] = LEN;
        live.style.strokeDasharray = `${LEN} ${LEN}`;
      };

      const ease = k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      const reach = n => {
        hit = n; steps[n - 1].forEach(el => el.classList.add('hit'));
        flow.classList.remove('s1', 's2', 's3', 's4'); flow.classList.add('s' + n);
      };
      const frame = now => {
        const k = Math.min(1, Math.max(0, (now - t0) / TRAVEL)), l = ease(k) * LEN;
        live.style.strokeDashoffset = LEN - l;
        const p = live.getPointAtLength(l);
        sig.style.transform = `translate(${p.x}px, ${p.y}px)`;
        sig.style.opacity = k >= 1 ? '0' : '';
        while (hit < 4 && l >= stops[hit] - 1) reach(hit + 1);
        if (k < 1 && visible) raf = requestAnimationFrame(frame);
        else if (k >= 1) timer = setTimeout(() => visible && !document.hidden && play(), HOLD);
      };
      const play = () => {
        cancelAnimationFrame(raf); clearTimeout(timer);
        steps.flat().forEach(el => el.classList.remove('hit')); hit = 0;
        flow.classList.remove('run', 's1', 's2', 's3', 's4'); void flow.offsetWidth; flow.classList.add('run');
        live.style.strokeDashoffset = LEN;
        t0 = performance.now() + 250; raf = requestAnimationFrame(frame);
      };
      const stop = () => {
        cancelAnimationFrame(raf); clearTimeout(timer);
        flow.classList.remove('run'); steps.flat().forEach(el => el.classList.add('hit'));
        live.style.strokeDashoffset = 0;
      };
      if (wide.matches) layout();
      new ResizeObserver(() => { if (wide.matches) { layout(); if (!flow.classList.contains('run')) live.style.strokeDashoffset = 0; } }).observe(flow);
      /* Phones: the line is driven by scroll, not a clock, so the reader always sees it happen.
         It fills toward a point 62% down the screen, never retracts, and each card wakes when the line reaches its dot. */
      const cards = steps.map(g => g.find(el => el.classList.contains('fcard')));
      let mDots = [], track = 0, fill = 0, target = 0, mRaf = 0;
      const mLayout = () => {
        mDots = cards.map(c => c.offsetTop + 25); track = mDots[3] - mDots[0];
        flow.style.setProperty('--t0', mDots[0] + 'px');
        flow.style.setProperty('--track', track + 'px');
      };
      const wake = (c, i) => {
        c.classList.add('hit');
        if (i === 1) setTimeout(() => c.classList.add('said'), 800);
        if (i === 3) flow.classList.add('mdone');
      };
      const mTick = () => {
        mRaf = 0;
        const gap = target - fill;
        fill += Math.sign(gap) * Math.min(Math.abs(gap), Math.max(1.5, Math.min(9, Math.abs(gap) * .12)));
        flow.style.setProperty('--fill', fill + 'px');
        cards.forEach((c, i) => { if (!c.classList.contains('hit') && fill >= mDots[i] - mDots[0] - 1) wake(c, i); });
        if (fill !== target) mRaf = requestAnimationFrame(mTick);
      };
      const mScroll = () => {
        if (wide.matches || flow.classList.contains('mdone')) return;
        const at = innerHeight * .62 - (flow.getBoundingClientRect().top + mDots[0]);
        if (at < 0 || at <= target) return;
        target = Math.min(track, at);
        if (!mRaf) mRaf = requestAnimationFrame(mTick);
      };
      const mStart = () => {
        mLayout(); fill = target = 0; flow.classList.remove('mdone', 'run');
        cards.forEach(c => c.classList.remove('hit', 'said'));
        flow.style.setProperty('--fill', '0px'); flow.classList.add('mrun'); mScroll();
      };
      const mOff = () => { cancelAnimationFrame(mRaf); mRaf = 0; flow.classList.remove('mrun'); flow.style.removeProperty('--fill'); };
      if (!wide.matches) mStart();
      addEventListener('scroll', mScroll, { passive: true });
      new ResizeObserver(() => { if (!wide.matches) { mLayout(); if (fill > track) { fill = target = track; flow.style.setProperty('--fill', fill + 'px'); } mScroll(); } }).observe(flow);

      new IntersectionObserver(e => {
        const was = visible; visible = e[0].isIntersecting;
        if (wide.matches) { if (visible && !was) play(); else if (!visible) stop(); }
      }, { threshold: .25 }).observe(flow);
      wide.addEventListener('change', () => { stop(); if (wide.matches) { mOff(); layout(); visible && play(); } else { mStart(); } });
    }
  }

  /* Phone hero line always ends on the Booked dot, with or without motion */
  const pf = document.querySelector('.flow');
  if (pf) {
    const pc = [1, 2, 3, 4].map(n => pf.querySelector(`.fcard[data-step="${n}"]`));
    const size = () => {
      if (innerWidth >= 1000 || !pc[0]) return;
      const a = pc[0].offsetTop + 25, z = pc[3].offsetTop + 25;
      pf.style.setProperty('--t0', a + 'px'); pf.style.setProperty('--track', (z - a) + 'px');
    };
    size(); addEventListener('resize', size); addEventListener('load', size);
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
      company: v => !v ? 'Enter your company name.' : v.length < 2 ? 'Enter your full company name.' : '',
    };
    const touched = new Set();
    const check = input => {
      const msg = checks[input.name](input.value.trim()), slot = form.querySelector('#e-' + input.name);
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (slot) { slot.textContent = msg; slot.hidden = !msg; }
      return !msg;
    };
    Object.keys(checks).forEach(n => {
      const input = form.elements[n]; if (!input) return;
      input.addEventListener('blur', () => {
        if (n === 'phone') { const d = digits(input.value), t = d.length === 11 && d[0] === '1' ? d.slice(1) : d; if (t.length === 10) input.value = `(${t.slice(0, 3)}) ${t.slice(3, 6)}-${t.slice(6)}`; }
        if (input.value.trim()) touched.add(n);
        if (touched.has(n)) check(input);
      });
      input.addEventListener('input', () => { if (touched.has(n)) check(input); if (!err.hidden && form.querySelectorAll('[aria-invalid="true"]').length === 0) err.hidden = true; });
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
          form.hidden = true; thanks.hidden = false; thanks.focus(); })
        .catch(() => { show(`Your details didn’t send. Check your connection and try again${phone ? ', or call us at ' + phone : email ? ', or email us at ' + email : ''}.`); btn.disabled = false; btn.textContent = label; });
    });
  });
})();
