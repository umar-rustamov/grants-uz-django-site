/* Grants.uz — v2 interactions (no dependencies) */
(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover)').matches;

  /* ---------- Header, progress, back-to-top ---------- */
  var header = $('.site-header');
  var progress = $('.scroll-progress');
  var toTop = $('.to-top');
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, y / max) : 0;
    if (header) header.classList.toggle('is-scrolled', y > 24);
    if (progress) progress.style.setProperty('--p', p);
    if (toTop) { toTop.classList.toggle('is-visible', y > 600); toTop.style.setProperty('--p', p); }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });

  /* ---------- Mobile drawer ---------- */
  var burger = $('.burger');
  function closeNav() { document.body.classList.remove('nav-open'); if (burger) burger.setAttribute('aria-expanded', 'false'); }
  if (burger) burger.addEventListener('click', function () {
    var open = document.body.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  $$('.drawer a').forEach(function (a) { a.addEventListener('click', closeNav); });
  $$('.drawer-group > button').forEach(function (b) {
    b.addEventListener('click', function () { b.parentElement.classList.toggle('is-open'); });
  });

  /* ---------- Dropdowns (language, fab) ---------- */
  $$('[data-toggle-open]').forEach(function (wrap) {
    var btn = wrap.querySelector('button');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = wrap.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    $$('[data-toggle-open].is-open').forEach(function (w) { if (!w.contains(e.target)) w.classList.remove('is-open'); });
  });

  /* ---------- Reveal on scroll ---------- */
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }) : null;
  $$('[data-stagger]').forEach(function (group) {
    var step = parseInt(group.getAttribute('data-stagger'), 10) || 90;
    Array.prototype.forEach.call(group.children, function (child, i) {
      if (!child.hasAttribute('data-reveal')) child.setAttribute('data-reveal', '');
      child.style.setProperty('--d', (i % 8) * step + 'ms');
    });
  });
  $$('[data-reveal]').forEach(function (el) { if (io) io.observe(el); else el.classList.add('is-in'); });

  /* ---------- Counters ---------- */
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
  function runCount(el) {
    var to = parseInt(el.getAttribute('data-count'), 10) || 0;
    if (reduce) { el.textContent = fmt(to); return; }
    var dur = 2000, t0 = performance.now();
    (function step(now) {
      var k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 4);
      el.textContent = fmt(Math.round(to * e));
      if (k < 1) requestAnimationFrame(step);
    })(t0);
  }
  var cio = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { cio.unobserve(en.target); runCount(en.target); } });
  }, { threshold: 0.6 }) : null;
  $$('[data-count]').forEach(function (el) {
    if (!cio) { runCount(el); return; }
    if (!reduce) el.textContent = '0';
    cio.observe(el);
  });

  /* ---------- Spotlight & tilt ---------- */
  $$('.spot').forEach(function (el) {
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      el.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
  if (!reduce && canHover) {
    $$('[data-tilt]').forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = 'perspective(900px) rotateY(' + (x * 7) + 'deg) rotateX(' + (-y * 7) + 'deg) translateY(-6px)';
      });
      el.addEventListener('pointerleave', function () { el.style.transform = ''; });
    });
  }

  /* ---------- Hero slider ---------- */
  var hero = $('[data-hero]');
  if (hero) {
    var slides = $$('.hero-slide', hero), texts = $$('.hero-text', hero), dots = $$('.hero-dot', hero);
    var DUR = 7000, idx = 0, timer = null, touchX = null;
    hero.style.setProperty('--dur', DUR + 'ms');
    function loadBg(i) {
      var bg = slides[i] && slides[i].querySelector('.hero-bg[data-bg]');
      if (bg) { bg.style.backgroundImage = 'url("' + bg.getAttribute('data-bg') + '")'; bg.removeAttribute('data-bg'); }
    }
    function show(n) {
      if (!slides.length) return;
      [slides, texts, dots].forEach(function (list) { if (list[idx]) list[idx].classList.remove('is-active', 'is-running'); });
      idx = (n + slides.length) % slides.length;
      loadBg(idx); loadBg((idx + 1) % slides.length);
      [slides, texts, dots].forEach(function (list) { if (list[idx]) list[idx].classList.add('is-active'); });
      if (dots[idx]) { void dots[idx].offsetWidth; dots[idx].classList.add('is-running'); }
      clearTimeout(timer);
      if (slides.length > 1 && !reduce) timer = setTimeout(function () { show(idx + 1); }, DUR);
    }
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); }); });
    var prev = $('[data-hero-prev]', hero), next = $('[data-hero-next]', hero);
    if (prev) prev.addEventListener('click', function () { show(idx - 1); });
    if (next) next.addEventListener('click', function () { show(idx + 1); });
    hero.addEventListener('touchstart', function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (touchX === null) return;
      var dx = e.changedTouches[0].clientX - touchX; touchX = null;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    });
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) clearTimeout(timer); else show(idx);
    });
    show(0);
  }

  /* ---------- Card sliders (testimonials) ---------- */
  $$('[data-slider-root]').forEach(function (root) {
    var track = $('.slider-track', root);
    if (!track) return;
    var auto = null, hovered = false;
    function stepSize() { var c = track.children[0]; return c ? c.getBoundingClientRect().width + 22 : track.clientWidth; }
    function move(dir) {
      var max = track.scrollWidth - track.clientWidth - 2;
      if (dir > 0 && track.scrollLeft >= max) track.scrollTo({ left: 0, behavior: 'smooth' });
      else if (dir < 0 && track.scrollLeft <= 0) track.scrollTo({ left: max, behavior: 'smooth' });
      else track.scrollBy({ left: dir * stepSize(), behavior: 'smooth' });
    }
    var p = $('[data-slide-prev]', root), n = $('[data-slide-next]', root);
    if (p) p.addEventListener('click', function () { move(-1); restart(); });
    if (n) n.addEventListener('click', function () { move(1); restart(); });
    track.addEventListener('pointerenter', function () { hovered = true; });
    track.addEventListener('pointerleave', function () { hovered = false; });
    function restart() {
      clearInterval(auto);
      if (!reduce) auto = setInterval(function () { if (!hovered && !document.hidden) move(1); }, 5500);
    }
    restart();
  });

  /* ---------- Tabs ---------- */
  $$('[data-tabs]').forEach(function (root) {
    var btns = $$('[data-tab]', root), panels = $$('[data-panel]', root);
    function activate(id) {
      btns.forEach(function (b) { b.classList.toggle('is-active', b.getAttribute('data-tab') === id); b.setAttribute('aria-selected', b.getAttribute('data-tab') === id); });
      panels.forEach(function (p) { p.classList.toggle('is-active', p.getAttribute('data-panel') === id); });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { activate(b.getAttribute('data-tab')); }); });
    var first = btns.filter(function (b) { return b.classList.contains('is-active'); })[0] || btns[0];
    if (first) activate(first.getAttribute('data-tab'));
  });

  /* ---------- FAQ: one open at a time ---------- */
  var faqs = $$('.faq-item');
  faqs.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) faqs.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });

  /* ---------- Lightbox ---------- */
  var lbLinks = $$('[data-lightbox]');
  var lb = $('.lightbox'), lbImg = lb && $('img', lb), lbCount = lb && $('.lb-count', lb), lbIdx = 0;
  function lbShow(i) {
    lbIdx = (i + lbLinks.length) % lbLinks.length;
    lbImg.src = lbLinks[lbIdx].getAttribute('href');
    if (lbCount) lbCount.textContent = (lbIdx + 1) + ' / ' + lbLinks.length;
  }
  function lbClose() { if (lb) { lb.classList.remove('is-open'); document.body.classList.remove('lb-open'); } }
  if (lb && lbLinks.length) {
    lbLinks.forEach(function (a, i) {
      a.addEventListener('click', function (e) { e.preventDefault(); lbShow(i); lb.classList.add('is-open'); document.body.classList.add('lb-open'); });
    });
    $('.lb-close', lb).addEventListener('click', lbClose);
    $('.lb-prev', lb).addEventListener('click', function () { lbShow(lbIdx - 1); });
    $('.lb-next', lb).addEventListener('click', function () { lbShow(lbIdx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lbClose(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'ArrowLeft') lbShow(lbIdx - 1);
      if (e.key === 'ArrowRight') lbShow(lbIdx + 1);
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeNav(); lbClose(); $$('[data-toggle-open].is-open').forEach(function (w) { w.classList.remove('is-open'); }); }
  });

  /* ---------- University filter ---------- */
  var grid = $('[data-uni-grid]');
  if (grid) {
    var cards = $$('[data-uni]', grid), chips = $$('[data-filter-country]'), search = $('[data-uni-search]');
    var empty = $('[data-uni-empty]'), counter = $('[data-uni-count]'), country = 'all', q = '';
    function apply() {
      var shown = 0;
      cards.forEach(function (c) {
        var ok = (country === 'all' || c.getAttribute('data-country') === country) && (!q || c.getAttribute('data-name').indexOf(q) !== -1);
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (empty) empty.hidden = shown > 0;
      if (counter) counter.textContent = shown;
    }
    chips.forEach(function (ch) {
      ch.addEventListener('click', function () {
        chips.forEach(function (x) { x.classList.toggle('is-active', x === ch); });
        country = ch.getAttribute('data-filter-country');
        apply();
      });
    });
    if (search) search.addEventListener('input', function () { q = search.value.trim().toLowerCase(); apply(); });
    apply();
  }

  /* ---------- Lead form ---------- */
  var form = $('[data-lead-form]');
  if (form) {
    var status = $('[data-form-status]', form), submit = $('button[type="submit"]', form), card = form.closest('.form-card');
    var phone = $('input[type="tel"]', form);
    if (phone) {
      phone.addEventListener('focus', function () { if (!phone.value) phone.value = '+998 '; });
      phone.addEventListener('input', function () { phone.value = phone.value.replace(/[^\d+()\-\s]/g, ''); });
      phone.addEventListener('blur', function () { if (phone.value.trim() === '+998') phone.value = ''; });
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      form.classList.add('is-loading'); submit.disabled = true;
      status.className = 'form-status'; status.textContent = form.getAttribute('data-loading') || '';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'X-Requested-With': 'XMLHttpRequest' } })
        .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, data: d }; }, function () { return { ok: false, data: {} }; }); })
        .then(function (res) {
          if (res.ok && res.data.status === 'success') {
            form.reset(); status.textContent = '';
            if (card) { card.classList.add('is-sent'); card.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' }); }
          } else { throw new Error('failed'); }
        })
        .catch(function () { status.className = 'form-status is-error'; status.textContent = form.getAttribute('data-error') || 'Error'; })
        .then(function () { form.classList.remove('is-loading'); submit.disabled = false; });
    });
    var again = $('[data-form-again]');
    if (again && card) again.addEventListener('click', function () { card.classList.remove('is-sent'); });
  }

  /* ---------- Particle network ("tech" background) ---------- */
  $$('canvas[data-particles]').forEach(function (cv) {
    var ctx = cv.getContext('2d'); if (!ctx) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), w = 0, h = 0, pts = [], running = false, raf = 0;
    var mouse = { x: -9999, y: -9999 };
    function resize() {
      var r = cv.getBoundingClientRect(); w = r.width; h = r.height;
      cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.max(18, Math.min(70, Math.round(w * h / 16000)));
      pts = [];
      for (var i = 0; i < n; i++) pts.push({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35, r: Math.random() * 1.6 + .6 });
      draw();
    }
    function draw() {
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < pts.length; i++) {
        var a = pts[i];
        if (running) { a.x += a.vx; a.y += a.vy; if (a.x < 0 || a.x > w) a.vx *= -1; if (a.y < 0 || a.y > h) a.vy *= -1; }
        for (var j = i + 1; j < pts.length; j++) {
          var b = pts[j], dx = a.x - b.x, dy = a.y - b.y, d = dx * dx + dy * dy;
          if (d < 18000) { ctx.strokeStyle = 'rgba(120,190,255,' + (0.16 * (1 - d / 18000)) + ')'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
        }
        var mx = a.x - mouse.x, my = a.y - mouse.y, md = mx * mx + my * my;
        if (md < 26000) { ctx.strokeStyle = 'rgba(34,211,238,' + (0.35 * (1 - md / 26000)) + ')'; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke(); }
        ctx.fillStyle = 'rgba(160,215,255,.75)'; ctx.beginPath(); ctx.arc(a.x, a.y, a.r, 0, Math.PI * 2); ctx.fill();
      }
      if (running) raf = requestAnimationFrame(draw);
    }
    var host = cv.parentElement;
    host.addEventListener('pointermove', function (e) { var r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
    host.addEventListener('pointerleave', function () { mouse.x = mouse.y = -9999; });
    window.addEventListener('resize', function () { clearTimeout(cv._t); cv._t = setTimeout(resize, 150); });
    resize();
    if (reduce || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && !running) { running = true; raf = requestAnimationFrame(draw); }
        else if (!en.isIntersecting && running) { running = false; cancelAnimationFrame(raf); }
      });
    }).observe(cv);
  });

  /* ---------- Year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
