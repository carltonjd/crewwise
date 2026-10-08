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
        const bx = .36 * W, r = 30, y1 = 46, y2 = 150;
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

  /* Overdrive: the hero call as a pinned, scroll-driven scene. Without motion or sticky support,
     the regular hero flow stays in place, so nothing is lost. */
  const scene = document.querySelector('.scene');
  if (scene && !reduce && window.CSS && CSS.supports('position', 'sticky')) {
    document.documentElement.classList.add('od');
    /* One hero note in the page: move it into the scene rather than showing a second copy */
    const note = document.querySelector('.hero-inner .flow-cap');
    if (note) { note.classList.add('scene-cap'); scene.querySelector('.scene-pin').appendChild(note); }
    const type = scene.querySelector('.type'), full = type ? type.dataset.text : '';
    const fill = scene.querySelector('.rail-fill'), nodes = [...scene.querySelectorAll('.rail li')];
    const B = [0, .2, .46, .7];
    const clamp = v => Math.min(1, Math.max(0, v));
    let raf = 0, lastP = -1;
    const set = (c, on) => scene.classList.toggle(c, on);
    const update = () => {
      raf = 0;
      const r = scene.getBoundingClientRect(), span = Math.max(1, scene.offsetHeight - innerHeight);
      const p = clamp(-r.top / span);
      if (p === lastP) return;
      lastP = p;
      const beat = p >= B[3] ? 4 : p >= B[2] ? 3 : p >= B[1] ? 2 : 1;
      for (let i = 1; i <= 4; i++) set('s' + i, beat === i);
      nodes.forEach((n, i) => n.classList.toggle('hit', p >= B[i]));
      if (fill) fill.style.transform = `scaleX(${clamp(p / B[3])})`;
      const l2 = clamp((p - B[1]) / (B[2] - B[1]));
      if (type) type.textContent = full.slice(0, Math.round(full.length * clamp(l2 * 1.7)));
      set('typing', l2 > 0 && l2 < .59);
      set('caller', l2 > .62 || beat > 2);
      set('tags', clamp((p - B[2]) / (B[3] - B[2])) > .12 || beat > 3);
      const l4 = clamp((p - B[3]) / (1 - B[3]));
      set('drop', l4 > .12);
      set('green', l4 > .38);
      set('sms', l4 > .55);
    };
    const kick = () => { if (!raf) raf = requestAnimationFrame(update); };
    addEventListener('scroll', kick, { passive: true });
    addEventListener('resize', () => { lastP = -1; kick(); });
    update();
  }

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
    const ends = [document.getElementById('contact'), document.querySelector('.closing')].filter(Boolean);
    const endSeen = new Set();
    new IntersectionObserver(e => { e.forEach(x => seen.set(heroAct, x.isIntersecting)); sync(); }).observe(heroAct);
    const eo = new IntersectionObserver(e => { e.forEach(x => x.isIntersecting ? endSeen.add(x.target) : endSeen.delete(x.target)); seen.set('end', endSeen.size > 0); sync(); });
    ends.forEach(el => eo.observe(el));
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
          if (cbC) cbC.textContent = form.elements.company.value.trim();
          form.hidden = true; thanks.hidden = false; thanks.classList.remove('in'); void thanks.offsetWidth; thanks.classList.add('in'); thanks.focus(); })
        .catch(() => { show(`Your details didn’t send. Check your connection and try again${phone ? ', or call us at ' + phone : email ? ', or email us at ' + email : ''}.`); btn.disabled = false; btn.textContent = label; });
    });
  });
})();
