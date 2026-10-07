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
      /* Phones: the same one-clock logic on a vertical line */
      const cards = steps.map(g => g.find(el => el.classList.contains('fcard')));
      let mDots = [], mRaf = 0, mTimer = 0;
      const mLayout = () => {
        mDots = cards.map(c => c.offsetTop + 25);
        flow.style.setProperty('--t0', mDots[0] + 'px');
        flow.style.setProperty('--track', (mDots[3] - mDots[0]) + 'px');
      };
      const mStop = () => { cancelAnimationFrame(mRaf); clearTimeout(mTimer); flow.classList.remove('run'); flow.style.removeProperty('--fill'); cards.forEach(c => c.classList.add('hit')); };
      const mPlay = () => {
        cancelAnimationFrame(mRaf); clearTimeout(mTimer); mLayout();
        cards.forEach(c => c.classList.remove('hit')); flow.classList.add('run');
        const span = mDots[3] - mDots[0], T = 3600, start = performance.now() + 200; let n = 0;
        const f = now => {
          const k = Math.min(1, Math.max(0, (now - start) / T)), e = k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2, h = e * span;
          flow.style.setProperty('--fill', h + 'px');
          while (n < 4 && mDots[0] + h >= mDots[n] - 1) cards[n++].classList.add('hit');
          if (k < 1 && visible) mRaf = requestAnimationFrame(f);
          else if (k >= 1) mTimer = setTimeout(() => visible && !document.hidden && mPlay(), HOLD);
        };
        mRaf = requestAnimationFrame(f);
      };
      if (!wide.matches) mLayout();
      new ResizeObserver(() => { if (!wide.matches) mLayout(); }).observe(flow);

      new IntersectionObserver(e => {
        const was = visible; visible = e[0].isIntersecting;
        if (wide.matches) { if (visible && !was) play(); else if (!visible) stop(); }
        else { if (visible && !was) mPlay(); else if (!visible) mStop(); }
      }, { threshold: .25 }).observe(flow);
      wide.addEventListener('change', () => { stop(); mStop(); if (wide.matches) { layout(); visible && play(); } else { mLayout(); visible && mPlay(); } });
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
    form.addEventListener('submit', e => {
      e.preventDefault(); err.hidden = true;
      if (!form.checkValidity()) {
        const bad = form.querySelector(':invalid');
        const name = bad && bad.labels && bad.labels[0] ? bad.labels[0].childNodes[0].textContent.trim() : '';
        show(name ? `Fill in "${name}" to send your details.` : 'Fill in the required fields to send your details.');
        if (bad) bad.focus();
        return;
      }
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
