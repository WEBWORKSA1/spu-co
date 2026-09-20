/* SPU.co — core site script (no dependencies) */
(function () {
  'use strict';

  /* ================= CONFIG — edit these to go live ================= */
  var SPU = window.SPU = window.SPU || {};
  SPU.config = {
    adsenseClient: '',            // e.g. 'ca-pub-1234567890123456' — ads load only when set + consent given
    ga4Id: '',                    // e.g. 'G-XXXXXXX'
    youtubeChannel: 'https://www.youtube.com/@spuco', // your channel URL
    paypalHostedButtonId: '',     // optional: PayPal hosted donate button id (preferred once created)
    formsubmitAlias: '',          // optional: FormSubmit random alias string (after activation) — hides address even in network calls
    currency: 'USD'
  };

  /* ================= Protected contact channel =================
     The single contact address is never written in HTML/JS as text.
     It is decoded only at the moment of use (click / form submit). */
  var _k = [116, 118, 106, 53, 115, 112, 104, 116, 110, 71, 56, 104, 122, 114, 121, 118, 126, 105, 108, 126];
  function addr() { return _k.slice().reverse().map(function (c) { return String.fromCharCode(c - 7); }).join(''); }

  SPU.endpoint = function () {
    var id = SPU.config.formsubmitAlias || addr();
    return 'https://formsubmit.co/ajax/' + id;
  };

  // Any element with [data-mail] opens the mail client without revealing the address in the page
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-mail]');
    if (!el) return;
    e.preventDefault();
    var subj = el.getAttribute('data-mail') || 'Inquiry from SPU.co';
    window.location.href = 'mai' + 'lto:' + addr() + '?subject=' + encodeURIComponent(subj);
  });

  /* ================= Theme ================= */
  var root = document.documentElement;
  try { var t = localStorage.getItem('spu-theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  document.addEventListener('click', function (e) {
    if (!e.target.closest('[data-theme-toggle]')) return;
    var dark = root.getAttribute('data-theme') === 'dark' ||
      (!root.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('spu-theme', next); } catch (e) {}
  });

  /* ================= Mobile nav ================= */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-menu]');
    if (!b) return;
    var nl = document.querySelector('.nav-links');
    var open = nl.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* ================= Forms (all go to the protected inbox) ================= */
  SPU.send = function (data) {
    return fetch(SPU.endpoint(), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) { if (!r.ok) throw new Error('Network'); return r.json(); });
  };

  function formToObj(form) {
    var o = {};
    new FormData(form).forEach(function (v, k) {
      if (k === '_honey') return;
      o[k] = o[k] ? o[k] + ', ' + v : v;
    });
    return o;
  }

  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form.matches('form[data-spu-form]')) return;
    e.preventDefault();
    var status = form.querySelector('.form-status');
    var hp = form.querySelector('[name=_honey]');
    if (hp && hp.value) return; // bot
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var btn = form.querySelector('[type=submit]');
    var data = formToObj(form);
    data._subject = 'SPU.co — ' + (form.getAttribute('data-spu-form') || 'Form') + ' submission';
    data._template = 'table';
    data._captcha = 'false';
    data.page = location.href;
    data.submitted_at = new Date().toISOString();
    if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending…'; }
    SPU.send(data).then(function () {
      if (status) { status.className = 'form-status ok'; status.textContent = form.getAttribute('data-success') || 'Thank you! We received your submission and will be in touch shortly.'; }
      form.reset();
      SPU.track('form_submit', { form: form.getAttribute('data-spu-form') });
    }).catch(function () {
      if (status) { status.className = 'form-status err'; status.textContent = 'Something went wrong. Please try again in a moment.'; }
    }).finally(function () {
      if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
    });
  });

  /* ================= Analytics + AdSense (consent-gated) ================= */
  SPU.track = function (name, params) { if (window.gtag) window.gtag('event', name, params || {}); };

  function loadScript(src, attrs) {
    var s = document.createElement('script'); s.async = true; s.src = src;
    if (attrs) Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); });
    document.head.appendChild(s);
  }
  function startTracking() {
    var c = SPU.config;
    if (c.ga4Id) {
      loadScript('https://www.googletagmanager.com/gtag/js?id=' + c.ga4Id);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag('js', new Date()); window.gtag('config', c.ga4Id);
    }
    if (c.adsenseClient) {
      loadScript('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + c.adsenseClient, { crossorigin: 'anonymous' });
      document.querySelectorAll('.ad-slot').forEach(function (slot) {
        slot.classList.add('live'); slot.innerHTML = '';
        var ins = document.createElement('ins');
        ins.className = 'adsbygoogle'; ins.style.display = 'block';
        ins.setAttribute('data-ad-client', c.adsenseClient);
        ins.setAttribute('data-ad-slot', slot.getAttribute('data-slot') || '');
        ins.setAttribute('data-ad-format', 'auto');
        ins.setAttribute('data-full-width-responsive', 'true');
        slot.appendChild(ins);
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      });
    }
  }
  function consent() { try { return localStorage.getItem('spu-consent'); } catch (e) { return null; } }
  function initCookie() {
    var bar = document.querySelector('.cookie');
    var c = consent();
    if (c === 'yes') startTracking();
    if (!bar || c) return;
    bar.classList.add('show');
    bar.addEventListener('click', function (e) {
      var v = e.target.getAttribute('data-consent');
      if (!v) return;
      try { localStorage.setItem('spu-consent', v); } catch (err) {}
      bar.classList.remove('show');
      if (v === 'yes') startTracking();
    });
  }

  /* ================= YouTube lite embeds ================= */
  function initVideos() {
    document.querySelectorAll('[data-yt]').forEach(function (v) {
      var id = v.getAttribute('data-yt');
      if (!id) return;
      v.innerHTML = '<img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><i>▶</i></div>';
      v.addEventListener('click', function () {
        v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Video"></iframe>';
        SPU.track('video_play', { id: id });
      }, { once: true });
    });
    document.querySelectorAll('[data-yt-channel]').forEach(function (a) { a.href = SPU.config.youtubeChannel; });
  }

  /* ================= Reveal + counters ================= */
  function initReveal() {
    var els = document.querySelectorAll('.reveal, [data-count]');
    if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target; el.classList.add('in'); io.unobserve(el);
        if (el.hasAttribute('data-count')) {
          var end = parseFloat(el.getAttribute('data-count')), suf = el.getAttribute('data-suffix') || '', pre = el.getAttribute('data-prefix') || '';
          var t0 = performance.now();
          (function tick(now) {
            var p = Math.min(1, (now - t0) / 1400), val = end * (1 - Math.pow(1 - p, 3));
            el.textContent = pre + (end % 1 ? val.toFixed(1) : Math.round(val).toLocaleString()) + suf;
            if (p < 1) requestAnimationFrame(tick);
          })(t0);
        }
      });
    }, { threshold: .15 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ================= ZIP hand-off to lead funnel ================= */
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f.matches('form[data-zip]')) return;
    e.preventDefault();
    var z = (f.querySelector('input').value || '').trim();
    location.href = (f.getAttribute('action') || 'get-quotes.html') + (z ? '?zip=' + encodeURIComponent(z) : '');
  });

  /* ================= Sticky mobile CTA ================= */
  function initSticky() {
    var s = document.querySelector('.sticky-cta'); if (!s) return;
    window.addEventListener('scroll', function () { s.classList.toggle('show', window.scrollY > 600); }, { passive: true });
  }

  /* ================= Donations ================= */
  SPU.donate = function (amount, purpose) {
    var c = SPU.config, url;
    if (c.paypalHostedButtonId) {
      url = 'https://www.paypal.com/donate/?hosted_button_id=' + encodeURIComponent(c.paypalHostedButtonId);
    } else {
      url = 'https://www.paypal.com/donate/?business=' + encodeURIComponent(addr()) +
        '&currency_code=' + c.currency + '&item_name=' + encodeURIComponent('SPU.co support — ' + (purpose || 'General')) +
        (amount ? '&amount=' + encodeURIComponent(amount) : '');
    }
    SPU.track('donate_click', { amount: amount, purpose: purpose });
    window.open(url, '_blank', 'noopener');
  };
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-donate]');
    if (!b) return;
    e.preventDefault();
    var box = b.closest('[data-donate-box]');
    var amt = b.getAttribute('data-amount') || (box && box.dataset.amount) || '';
    var custom = box && box.querySelector('[name=custom_amount]');
    if (custom && custom.value) amt = custom.value;
    var purpose = (box && box.querySelector('[name=purpose]') && box.querySelector('[name=purpose]').value) || b.getAttribute('data-donate') || 'General';
    SPU.donate(amt, purpose);
  });
  document.addEventListener('click', function (e) {
    var a = e.target.closest('.amounts button');
    if (!a) return;
    var box = a.closest('[data-donate-box]');
    box.querySelectorAll('.amounts button').forEach(function (x) { x.classList.remove('on'); });
    a.classList.add('on'); box.dataset.amount = a.getAttribute('data-v');
    var c = box.querySelector('[name=custom_amount]'); if (c) c.value = '';
  });

  /* ================= Share ================= */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-share]');
    if (!b) return;
    e.preventDefault();
    var data = { title: document.title, url: location.href };
    if (navigator.share) navigator.share(data).catch(function () {});
    else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { b.textContent = 'Link copied ✓'; });
  });

  /* ================= Year ================= */
  document.querySelectorAll('[data-year]').forEach(function (y) { y.textContent = new Date().getFullYear(); });

  /* ================= Countdown ================= */
  document.querySelectorAll('[data-countdown]').forEach(function (el) {
    var end = new Date(el.getAttribute('data-countdown')).getTime();
    function upd() {
      var d = Math.max(0, end - Date.now());
      var v = [Math.floor(d / 864e5), Math.floor(d / 36e5) % 24, Math.floor(d / 6e4) % 60, Math.floor(d / 1e3) % 60];
      el.querySelectorAll('b').forEach(function (b, i) { b.textContent = String(v[i]).padStart(2, '0'); });
    }
    upd(); setInterval(upd, 1000);
  });

  initCookie(); initVideos(); initReveal(); initSticky();
})();
