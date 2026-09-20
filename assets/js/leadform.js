/* SPU.co — multi-step lead funnel (quotes) */
(function () {
  'use strict';
  var form = document.getElementById('lead-funnel');
  if (!form) return;
  var steps = Array.prototype.slice.call(form.querySelectorAll('.step'));
  var bar = form.querySelector('.progress i');
  var countEl = form.querySelector('[data-stepnum]');
  var i = 0;
  var p = new URLSearchParams(location.search);

  // Prefill from URL / calculator hand-off
  if (p.get('zip')) form.zip.value = p.get('zip');
  if (p.get('region') && form.country) form.country.value = p.get('region');
  if (p.get('bill')) { form.bill.value = Math.min(1000, +p.get('bill')); }
  if (p.get('kw')) form.est_kw.value = p.get('kw');
  if (p.get('interest') === 'battery') { var bi = form.querySelector('input[name=interest][value="Battery only"]'); if (bi) bi.checked = true; }
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid'].forEach(function (k) {
    if (p.get(k) && form[k]) form[k].value = p.get(k);
  });
  if (form.referrer) form.referrer.value = document.referrer || 'direct';

  var billOut = form.querySelector('[data-bill-out]');
  function billLbl() { billOut.textContent = (form.bill.value >= 1000 ? '1,000+' : Number(form.bill.value).toLocaleString()); }
  form.bill.addEventListener('input', billLbl); billLbl();

  function show(n) {
    steps.forEach(function (s, k) { s.classList.toggle('active', k === n); });
    i = n;
    bar.style.width = Math.round(((n + 1) / steps.length) * 100) + '%';
    countEl.textContent = 'Step ' + (n + 1) + ' of ' + steps.length;
    var f = steps[n].querySelector('input:not([type=hidden]):not([type=radio]),select');
    if (f && window.innerWidth > 700) setTimeout(function () { f.focus(); }, 50);
    if (window.SPU && SPU.track) SPU.track('funnel_step', { step: n + 1 });
  }
  function valid(n) {
    var ok = true;
    steps[n].querySelectorAll('input,select,textarea').forEach(function (el) {
      if (ok && !el.checkValidity()) { el.reportValidity(); ok = false; }
    });
    var radios = steps[n].querySelectorAll('input[type=radio][required]');
    if (ok && radios.length && !steps[n].querySelector('input[type=radio]:checked')) {
      radios[0].reportValidity(); ok = false;
    }
    return ok;
  }

  // Auto-advance on radio pick for speed (top converters do this)
  form.addEventListener('change', function (e) {
    if (e.target.type === 'radio' && steps[i].querySelectorAll('input[type=radio]').length &&
        !steps[i].querySelector('input:not([type=radio]):not([type=hidden]),select')) {
      setTimeout(function () { if (i < steps.length - 1) show(i + 1); }, 220);
    }
    // Renters route to portable power / community solar
    if (e.target.name === 'homeowner' && e.target.value === 'Renter') {
      var n = form.querySelector('[data-renter-note]'); if (n) n.hidden = false;
    }
  });
  form.addEventListener('click', function (e) {
    if (e.target.closest('[data-next]')) { e.preventDefault(); if (valid(i)) show(i + 1); }
    if (e.target.closest('[data-prev]')) { e.preventDefault(); if (i > 0) show(i - 1); }
  });

  function score(d) {
    var s = 0;
    if (d.homeowner === 'Yes') s += 30;
    s += Math.min(25, (+d.bill || 0) / 12);
    if (d.shade === 'No shade') s += 10; else if (d.shade === 'Some shade') s += 5;
    if (/Excellent|Good/.test(d.credit || '')) s += 15;
    if (/ASAP|1–3/.test(d.timeline || '')) s += 20;
    return Math.round(Math.min(100, s));
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!valid(i)) return;
    if (form._honey && form._honey.value) return;
    var d = {};
    new FormData(form).forEach(function (v, k) { if (k !== '_honey') d[k] = v; });
    d.lead_score = score(d);
    d._subject = 'SPU.co — NEW SOLAR LEAD (score ' + d.lead_score + ') ' + (d.zip || '');
    d._template = 'table'; d._captcha = 'false';
    d.consent_timestamp = new Date().toISOString();
    d.consent_page = location.href;
    d.user_agent = navigator.userAgent;
    var btn = form.querySelector('[type=submit]'); btn.disabled = true; btn.textContent = 'Matching you…';
    SPU.send(d).then(function () {
      form.hidden = true;
      var ty = document.getElementById('lead-thanks'); ty.hidden = false;
      ty.querySelector('[data-first]').textContent = d.first_name || 'there';
      ty.scrollIntoView({ behavior: 'smooth', block: 'start' });
      SPU.track('generate_lead', { value: d.lead_score, currency: 'USD' });
    }).catch(function () {
      btn.disabled = false; btn.textContent = 'Get my free quotes';
      var st = form.querySelector('.form-status'); st.className = 'form-status err';
      st.textContent = 'We could not submit right now. Please try again in a minute.';
    });
  });
  show(0);
})();
