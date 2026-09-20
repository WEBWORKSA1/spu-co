/* SPU.co — Solar savings + battery backup calculators */
(function () {
  'use strict';
  // Regional defaults (editable estimates; update yearly). Sources noted in guides.
  var R = {
    US: { cur: 'USD', sym: '$', rate: 0.18, sun: 4.5, cpw: 2.9, inc: 0, co2: 0.37, bill: 160, lbl: 'United States' },
    CA: { cur: 'CAD', sym: 'C$', rate: 0.17, sun: 3.8, cpw: 2.9, inc: 0, co2: 0.11, bill: 150, lbl: 'Canada' },
    UK: { cur: 'GBP', sym: '£', rate: 0.26, sun: 2.8, cpw: 1.6, inc: 0, co2: 0.2, bill: 110, lbl: 'United Kingdom' },
    AU: { cur: 'AUD', sym: 'A$', rate: 0.32, sun: 5.0, cpw: 1.1, inc: 25, co2: 0.6, bill: 180, lbl: 'Australia' },
    IN: { cur: 'INR', sym: '₹', rate: 8, sun: 5.2, cpw: 55, inc: 40, co2: 0.71, bill: 3000, lbl: 'India' },
    EU: { cur: 'EUR', sym: '€', rate: 0.28, sun: 3.4, cpw: 1.5, inc: 0, co2: 0.25, bill: 120, lbl: 'Europe' },
    XX: { cur: 'USD', sym: '$', rate: 0.15, sun: 4.5, cpw: 1.8, inc: 0, co2: 0.5, bill: 120, lbl: 'Other' }
  };
  var PANEL_W = 430, DERATE = 0.80, DEGRADE = 0.005, ESCALATE = 0.03, YEARS = 25;

  function $(s, c) { return (c || document).querySelector(s); }
  function num(el) { return parseFloat(el.value) || 0; }
  function fmt(n, sym) { return sym + Math.round(n).toLocaleString(); }

  /* ---------- Solar calculator ---------- */
  var sf = $('#solar-form');
  if (sf) {
    var region = $('#c-region');
    function applyRegion() {
      var r = R[region.value];
      $('#c-bill').value = r.bill; $('#c-rate').value = r.rate; $('#c-sun').value = r.sun;
      $('#c-cpw').value = r.cpw; $('#c-inc').value = r.inc;
      document.querySelectorAll('[data-sym]').forEach(function (s) { s.textContent = r.sym; });
      calc();
    }
    function calc() {
      var r = R[region.value];
      var bill = num($('#c-bill')), rate = Math.max(0.01, num($('#c-rate'))), sun = Math.max(0.5, num($('#c-sun')));
      var offset = num($('#c-offset')) / 100, cpw = num($('#c-cpw')), inc = num($('#c-inc')) / 100;
      var shade = parseFloat($('#c-shade').value);
      var monthlyKwh = bill / rate, annualKwh = monthlyKwh * 12;
      var kw = (annualKwh * offset) / (sun * 365 * DERATE * shade);
      var panels = Math.ceil(kw * 1000 / PANEL_W);
      kw = panels * PANEL_W / 1000;
      var prod = kw * sun * 365 * DERATE * shade;
      var gross = kw * 1000 * cpw, net = gross * (1 - inc);
      var savings1 = Math.min(prod, annualKwh) * rate;
      var cum = -net, payback = null, total = 0, series = [];
      for (var y = 1; y <= YEARS; y++) {
        var s = Math.min(prod * Math.pow(1 - DEGRADE, y - 1), annualKwh) * rate * Math.pow(1 + ESCALATE, y - 1);
        total += s; var prev = cum; cum += s; series.push(cum);
        if (payback === null && cum >= 0) payback = (y - 1) + (-prev / s);
      }
      var sym = r.sym;
      $('#r-size').textContent = kw.toFixed(1) + ' kW';
      $('#r-panels').textContent = panels;
      $('#r-prod').textContent = Math.round(prod).toLocaleString() + ' kWh';
      $('#r-gross').textContent = fmt(gross, sym);
      $('#r-net').textContent = fmt(net, sym);
      $('#r-save1').textContent = fmt(savings1, sym) + '/yr';
      $('#r-payback').textContent = payback === null ? '25+ yrs' : payback.toFixed(1) + ' yrs';
      $('#r-total').textContent = fmt(total - net, sym);
      $('#r-co2').textContent = (prod * r.co2 / 1000).toFixed(1) + ' t/yr';
      $('#r-roi').textContent = net > 0 ? Math.round(((total - net) / net) * 100) + '%' : '—';
      $('#r-area').textContent = Math.round(panels * 2.0) + ' m² / ' + Math.round(panels * 21.5) + ' ft²';
      $('#r-bill').textContent = fmt(Math.max(0, bill - savings1 / 12), sym) + '/mo';
      draw(series, sym);
      var q = $('#calc-to-quote');
      if (q) q.href = 'get-quotes.html?bill=' + Math.round(bill) + '&region=' + region.value + '&kw=' + kw.toFixed(1);
    }
    function draw(series, sym) {
      var svg = $('#payback-chart'); if (!svg) return;
      var W = 600, H = 220, P = 34, min = Math.min.apply(null, series.concat([0])), max = Math.max.apply(null, series.concat([0]));
      var sx = function (i) { return P + i * (W - P * 2) / (series.length - 1); };
      var sy = function (v) { return H - P - (v - min) * (H - P * 2) / ((max - min) || 1); };
      var d = series.map(function (v, i) { return (i ? 'L' : 'M') + sx(i).toFixed(1) + ' ' + sy(v).toFixed(1); }).join(' ');
      var area = d + ' L' + sx(series.length - 1) + ' ' + sy(min) + ' L' + sx(0) + ' ' + sy(min) + ' Z';
      svg.innerHTML =
        '<defs><linearGradient id="gA" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f5a300" stop-opacity=".35"/><stop offset="1" stop-color="#f5a300" stop-opacity="0"/></linearGradient></defs>' +
        '<line x1="' + P + '" x2="' + (W - P) + '" y1="' + sy(0) + '" y2="' + sy(0) + '" stroke="currentColor" stroke-opacity=".25" stroke-dasharray="4 4"/>' +
        '<path d="' + area + '" fill="url(#gA)"/><path d="' + d + '" fill="none" stroke="#f5a300" stroke-width="3" stroke-linejoin="round"/>' +
        '<text x="' + P + '" y="16" font-size="12" fill="currentColor" opacity=".7">Cumulative net savings (' + sym + ')</text>' +
        '<text x="' + P + '" y="' + (H - 8) + '" font-size="11" fill="currentColor" opacity=".6">Year 1</text>' +
        '<text x="' + (W - P) + '" y="' + (H - 8) + '" font-size="11" text-anchor="end" fill="currentColor" opacity=".6">Year 25</text>' +
        '<text x="' + (W - P) + '" y="' + (sy(series[series.length - 1]) - 8) + '" font-size="13" font-weight="700" text-anchor="end" fill="currentColor">' + sym + Math.round(series[series.length - 1]).toLocaleString() + '</text>';
    }
    region.addEventListener('change', applyRegion);
    sf.addEventListener('input', calc);
    var p = new URLSearchParams(location.search);
    if (p.get('region') && R[p.get('region')]) region.value = p.get('region');
    applyRegion();
    if (p.get('bill')) { $('#c-bill').value = p.get('bill'); calc(); }
  }

  /* ---------- Battery / backup sizing ---------- */
  var bf = $('#battery-form');
  if (bf) {
    function bcalc() {
      var dayWh = 0, peakW = 0;
      bf.querySelectorAll('.appl').forEach(function (row) {
        var on = row.querySelector('[type=checkbox]');
        if (!on || !on.checked) return;
        var w = parseFloat(row.querySelector('[name=w]').value) || 0, h = parseFloat(row.querySelector('[name=h]').value) || 0;
        dayWh += w * h; peakW += w;
      });
      var days = parseFloat($('#b-days').value) || 1, dod = 0.9, eff = 0.9;
      var need = dayWh * days / 1000 / dod / eff;
      $('#b-daily').textContent = (dayWh / 1000).toFixed(1) + ' kWh';
      $('#b-need').textContent = need.toFixed(1) + ' kWh';
      $('#b-peak').textContent = (peakW / 1000).toFixed(1) + ' kW';
      var rec;
      if (need <= 2.5) rec = 'Portable power station (1–3 kWh) — e.g. Jackery / EcoFlow / Anker SOLIX class';
      else if (need <= 6) rec = 'Large portable or expandable system (3–6 kWh) — e.g. EcoFlow DELTA Pro 3 / Anker SOLIX F3800 class';
      else if (need <= 15) rec = 'One whole-home battery (10–15 kWh) — e.g. Powerwall 3 / FranklinWH aPower 2 class';
      else rec = 'Two or more stacked home batteries (' + Math.ceil(need / 13.5) + '× ~13.5 kWh) + solar recharge';
      $('#b-rec').textContent = rec;
      $('#b-panels').textContent = Math.ceil((dayWh / 1000) / (4.5 * 0.8) * 1000 / 430) + ' panels (~' + ((dayWh / 1000) / (4.5 * 0.8)).toFixed(1) + ' kW) to recharge daily';
    }
    bf.addEventListener('input', bcalc); bf.addEventListener('change', bcalc); bcalc();
  }

  /* ---------- Tabs ---------- */
  document.querySelectorAll('.tabs').forEach(function (tabs) {
    tabs.addEventListener('click', function (e) {
      var b = e.target.closest('button[aria-controls]'); if (!b) return;
      tabs.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-selected', 'false'); });
      b.setAttribute('aria-selected', 'true');
      var host = tabs.parentElement;
      host.querySelectorAll(':scope > .tab-panel').forEach(function (p) { p.classList.toggle('active', p.id === b.getAttribute('aria-controls')); });
    });
  });

  /* ---------- Sortable / filterable tables ---------- */
  document.querySelectorAll('table[data-sort]').forEach(function (table) {
    table.querySelectorAll('th').forEach(function (th, i) {
      var asc = true;
      th.addEventListener('click', function () {
        var rows = Array.prototype.slice.call(table.tBodies[0].rows);
        rows.sort(function (a, b) {
          var x = a.cells[i].getAttribute('data-v') || a.cells[i].textContent, y = b.cells[i].getAttribute('data-v') || b.cells[i].textContent;
          var nx = parseFloat(x), ny = parseFloat(y);
          var r = (!isNaN(nx) && !isNaN(ny)) ? nx - ny : x.localeCompare(y);
          return asc ? r : -r;
        });
        asc = !asc; rows.forEach(function (r) { table.tBodies[0].appendChild(r); });
      });
    });
  });
  document.querySelectorAll('[data-filter]').forEach(function (inp) {
    var target = document.querySelector(inp.getAttribute('data-filter'));
    function run() {
      var q = (document.querySelector('[data-filter-text]') || {}).value || '';
      var cat = (document.querySelector('[data-filter-cat]') || {}).value || '';
      target.querySelectorAll('[data-item]').forEach(function (it) {
        var ok = it.textContent.toLowerCase().indexOf(q.toLowerCase()) > -1 && (!cat || it.getAttribute('data-cat') === cat);
        it.style.display = ok ? '' : 'none';
      });
    }
    inp.addEventListener('input', run); inp.addEventListener('change', run);
  });
})();
