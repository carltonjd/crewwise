(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Header turns frosted once the page scrolls */
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Scroll reveals (also starts the 24-hour dial) */
  var targets = document.querySelectorAll('.reveal, .reveal-kids, .dial-wrap');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.18, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('in'); });
  }

  /* FAQ: smooth open and close */
  document.querySelectorAll('.faq-list details').forEach(function (d) {
    d.querySelector('summary').addEventListener('click', function (e) {
      e.preventDefault();
      if (d.open) {
        d.classList.remove('open');
        setTimeout(function () { d.open = false; }, reduce ? 0 : 400);
      } else {
        d.open = true;
        requestAnimationFrame(function () { requestAnimationFrame(function () { d.classList.add('open'); }); });
      }
    });
  });

  /* ---------- Call player ---------- */
  document.querySelectorAll('.player').forEach(function (root) {
    var data;
    try { data = JSON.parse(root.querySelector('.player-data').textContent); } catch (e) { return; }
    var calls = data.calls || [];
    if (!calls.length) return;

    var seg = root.querySelector('.seg');
    var pill = seg ? seg.querySelector('.pill') : null;
    var tabs = seg ? Array.prototype.slice.call(seg.querySelectorAll('button')) : [];
    var liveText = root.querySelector('.live-text');
    var clockEl = root.querySelector('.clock');
    var bizEl = root.querySelector('.biz b');
    var caps = root.querySelector('.captions');
    var sheetTitle = root.querySelector('.sheet-head b');
    var rowsEl = root.querySelector('.sheet dl');
    var sheetFoot = root.querySelector('.sheet-foot');
    var stamp = root.querySelector('.stamp');
    var note = root.querySelector('.player-foot > span');
    var replay = root.querySelector('.replay');
    var skipto = root.querySelector('.skipto');
    var canvas = root.querySelector('.wave');

    var current = 0, timers = [], tick = null, secs = 0, autoNext = calls.length > 1;
    var speaker = 'idle';

    function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
    function stop() { timers.forEach(clearTimeout); timers = []; clearInterval(tick); }
    function fmt(s) { return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); }

    /* Waveform: scrolling bars, colour and height follow who is speaking */
    var ctx = canvas.getContext('2d'), bars = [], W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2), visible = true, lastT = 0, level = 0.05;
    var GAP = 7, BW = 3;
    function sizeWave() {
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = W * dpr; canvas.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.ceil(W / GAP) + 1;
      while (bars.length < n) bars.unshift({ h: 0.04 + Math.random() * 0.03, who: 'idle' });
      if (bars.length > n) bars = bars.slice(bars.length - n);
      draw();
    }
    function colour(who) { return who === 'ai' ? '#F06A35' : who === 'them' ? 'rgba(247,243,236,.9)' : who === 'ring' ? 'rgba(240,106,53,.55)' : 'rgba(255,255,255,.16)'; }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      var mid = H / 2;
      for (var i = 0; i < bars.length; i++) {
        var b = bars[i], h = Math.max(2, b.h * (H - 8));
        ctx.fillStyle = colour(b.who);
        var x = i * GAP, y = mid - h / 2, r = BW / 2;
        ctx.beginPath();
        if (ctx.roundRect) ctx.roundRect(x, y, BW, h, r); else ctx.rect(x, y, BW, h);
        ctx.fill();
      }
    }
    function step(t) {
      if (!visible) return;
      if (t - lastT > 55) {
        lastT = t;
        var target;
        if (speaker === 'ai' || speaker === 'them') target = 0.22 + Math.random() * 0.72 * (0.6 + 0.4 * Math.sin(t / 180));
        else if (speaker === 'ring') target = (Math.floor(t / 400) % 3 === 2) ? 0.05 : 0.35 + Math.random() * 0.1;
        else target = 0.03 + Math.random() * 0.04;
        level += (target - level) * 0.55;
        bars.push({ h: Math.min(1, Math.max(0.03, level)), who: speaker });
        bars.shift();
        draw();
      }
      requestAnimationFrame(step);
    }
    sizeWave();
    window.addEventListener('resize', sizeWave);
    if (!reduce) {
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (e) {
          var v = e[0].isIntersecting;
          if (v && !visible) { visible = true; requestAnimationFrame(step); } else if (!v) visible = false;
        }).observe(root);
      }
      requestAnimationFrame(step);
    } else {
      bars.forEach(function (b, i) { b.h = 0.1 + 0.5 * Math.abs(Math.sin(i * 0.7)) * Math.random(); b.who = i % 9 < 5 ? 'ai' : 'them'; });
      draw();
    }

    /* Tabs */
    function movePill(i) {
      if (!pill || !tabs[i]) return;
      pill.style.width = tabs[i].offsetWidth + 'px';
      pill.style.transform = 'translateX(' + (tabs[i].offsetLeft - 4) + 'px)';
      tabs.forEach(function (t, j) { t.setAttribute('aria-selected', j === i ? 'true' : 'false'); t.tabIndex = j === i ? 0 : -1; });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { autoNext = false; if (reduce) showFinal(i); else play(i); });
    });
    window.addEventListener('resize', function () { movePill(current); });

    function capLine(line, full) {
      var li = document.createElement('li');
      li.className = line.f === 'ai' ? 'ai' : 'them';
      var s = document.createElement('small'); s.textContent = line.f === 'ai' ? 'Jobstead' : (line.who || 'Caller');
      var p = document.createElement('p');
      line.t.split(' ').forEach(function (w, k) {
        var span = document.createElement('span'); span.className = 'w' + (full ? ' on' : ''); span.textContent = (k ? ' ' : '') + w;
        p.appendChild(span);
      });
      li.appendChild(s); li.appendChild(p);
      return li;
    }
    function markPast() {
      var items = caps.children;
      for (var i = 0; i < items.length; i++) items[i].classList.toggle('past', i < items.length - 1);
      while (caps.children.length > 5) caps.removeChild(caps.firstChild);
    }
    function buildSheet(call) {
      sheetTitle.textContent = call.sheet.title;
      rowsEl.innerHTML = '';
      call.sheet.rows.forEach(function (k) {
        var r = document.createElement('div'); r.className = 'r';
        var dt = document.createElement('dt'); dt.textContent = k;
        var dd = document.createElement('dd'); dd.className = 'empty'; dd.setAttribute('data-k', k);
        r.appendChild(dt); r.appendChild(dd); rowsEl.appendChild(r);
      });
      sheetFoot.textContent = '';
      stamp.classList.remove('on');
      stamp.textContent = call.sheet.stamp || 'Booked';
    }
    function fill(obj, animate) {
      if (!obj) return;
      Object.keys(obj).forEach(function (k) {
        var dd = rowsEl.querySelector('dd[data-k="' + k + '"]');
        if (!dd) return;
        dd.textContent = obj[k]; dd.classList.remove('empty');
        if (animate) { dd.classList.remove('fill'); void dd.offsetWidth; dd.classList.add('fill'); }
      });
    }
    function setHead(call, i) {
      current = i; movePill(i);
      if (bizEl) bizEl.textContent = call.business;
      note.textContent = call.note;
    }
    function finish(call) {
      sheetTitle.textContent = call.sheet.doneTitle;
      sheetFoot.textContent = call.sheet.foot;
      stamp.classList.add('on');
      root.classList.remove('is-live'); root.classList.add('is-done');
      liveText.textContent = 'Call ended';
    }

    function showFinal(i) {
      stop(); var call = calls[i];
      setHead(call, i); buildSheet(call);
      caps.innerHTML = '';
      call.lines.forEach(function (l) { caps.appendChild(capLine(l, true)); fill(l.fill, false); });
      markPast();
      finish(call);
      skipto.hidden = true;
      clockEl.textContent = call.length || '';
      speaker = 'idle';
      replay.hidden = false;
    }

    function play(i) {
      stop(); var call = calls[i];
      setHead(call, i); buildSheet(call);
      caps.innerHTML = '';
      replay.hidden = true; skipto.hidden = false;
      root.classList.remove('is-done'); root.classList.add('is-live');
      liveText.textContent = 'Incoming call'; clockEl.textContent = '';
      speaker = 'ring';
      var sys = document.createElement('li');
      sys.className = 'sys ringing';
      sys.innerHTML = '<svg aria-hidden="true"><use href="#i-phone"/></svg><span></span>';
      sys.querySelector('span').textContent = 'Incoming call from ' + (call.from || 'a new caller');
      caps.appendChild(sys);

      var t = 900;
      later(function () {
        sys.classList.remove('ringing');
        sys.querySelector('span').textContent = 'Answered. Call from ' + (call.from || 'a new caller');
        liveText.textContent = 'On call'; secs = 0; clockEl.textContent = fmt(0);
        tick = setInterval(function () { secs++; clockEl.textContent = fmt(secs); }, 1000);
        speaker = 'idle';
      }, t);
      t += 200;

      call.lines.forEach(function (line) {
        var words = line.t.split(' ').length;
        var per = line.f === 'ai' ? 55 : 65;
        var li;
        later(function () {
          li = capLine(line, false); caps.appendChild(li); markPast();
          speaker = line.f === 'ai' ? 'ai' : 'them';
          var ws = li.querySelectorAll('.w');
          for (var k = 0; k < ws.length; k++) (function (w, k) { later(function () { w.classList.add('on'); }, k * per); })(ws[k], k);
        }, t);
        t += words * per + 120;
        later(function () { speaker = 'idle'; fill(line.fill, true); }, t);
        t += 320;
      });

      later(function () {
        clearInterval(tick);
        finish(call);
        skipto.hidden = true;
        later(function () {
          replay.hidden = false;
          if (autoNext) { autoNext = false; later(function () { play((current + 1) % calls.length); }, 4200); }
        }, 900);
      }, t + 200);
    }

    skipto.addEventListener('click', function () { autoNext = false; showFinal(current); });
    replay.addEventListener('click', function () { autoNext = false; if (reduce) showFinal(current); else play(current); });

    requestAnimationFrame(function () { showFinal(0); });
    if (!reduce && 'IntersectionObserver' in window) {
      var started = false;
      new IntersectionObserver(function (e, obs) {
        if (e[0].isIntersecting && !started) { started = true; obs.disconnect(); setTimeout(function () { play(0); }, 500); }
      }, { threshold: 0.35 }).observe(root);
    }
  });

  /* ---------- Lead forms ---------- */
  document.querySelectorAll('.lead-form').forEach(function (form) {
    var card = form.closest('.form-card');
    var btn = form.querySelector('button[type="submit"]');
    var btnLabel = btn.textContent;
    var err = form.querySelector('.form-error');
    var thanks = card.querySelector('.thanks');
    var phone = form.getAttribute('data-phone') || '';
    function showError(msg) { err.textContent = msg; err.hidden = false; }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      err.hidden = true;
      if (!form.checkValidity()) {
        var bad = form.querySelector(':invalid');
        var label = bad && bad.labels && bad.labels[0] ? bad.labels[0].childNodes[0].textContent.trim() : '';
        showError(label ? 'Fill in "' + label + '" to send your details.' : 'Fill in the required fields to send your details.');
        if (bad) bad.focus();
        return;
      }
      btn.disabled = true; btn.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (res) {
          if (!res.ok) throw new Error('Bad response');
          var first = (form.elements.name.value || '').trim().split(/\s+/)[0];
          var nameEl = thanks.querySelector('.thanks-name');
          if (nameEl) nameEl.textContent = first ? ', ' + first : '';
          form.hidden = true; thanks.hidden = false; thanks.focus();
        })
        .catch(function () {
          showError('Your details didn’t send. Check your connection and try again' + (phone ? ', or call us at ' + phone : '') + '.');
          btn.disabled = false; btn.textContent = btnLabel;
        });
    });
  });
})();

/* ---------- Roofer sections: leaks, Storm Mode, report ---------- */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function onView(el, fn) {
    if (!el) return;
    if (reduce || !('IntersectionObserver' in window)) { fn(true); return; }
    var io = new IntersectionObserver(function (e) {
      if (e[0].isIntersecting) { io.disconnect(); fn(false); }
    }, { threshold: 0.35 });
    io.observe(el);
  }
  function countUp(el, ms) {
    var to = +el.getAttribute('data-to'), pre = el.getAttribute('data-prefix') || '';
    var start = null;
    function frame(t) {
      if (start === null) start = t;
      var k = Math.min(1, (t - start) / ms), v = Math.round(to * (1 - Math.pow(1 - k, 3)));
      el.textContent = pre + v.toLocaleString('en-US');
      if (k < 1) requestAnimationFrame(frame);
    }
    el.textContent = pre + '0';
    requestAnimationFrame(frame);
  }

  /* Where leads leak: drips, then every step gets plugged */
  document.querySelectorAll('.pipe').forEach(function (pipe) {
    onView(pipe, function (instant) {
      pipe.classList.add('in');
      setTimeout(function () { pipe.classList.add('plugged'); }, instant ? 0 : 2600);
    });
  });

  /* Storm Mode: switch flips on, queue fills in priority order */
  document.querySelectorAll('.storm-card').forEach(function (card) {
    onView(card, function (instant) {
      card.classList.add('on');
      var c = card.querySelector('.sc-count');
      if (c && !instant) countUp(c, 1500);
    });
  });

  /* Lead Recovery Report: numbers count up once */
  document.querySelectorAll('.report').forEach(function (rep) {
    onView(rep, function (instant) {
      if (instant) return;
      rep.querySelectorAll('.num').forEach(function (n) { countUp(n, 1400); });
    });
  });
})();
