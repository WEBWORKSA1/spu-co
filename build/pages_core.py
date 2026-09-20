from layout import ad, hero, faq, faq_schema, cta_band
import json

PAGES = []


def add(path, title, desc, body, **kw):
    PAGES.append((path, title, desc, body, kw))


# ------------------------------------------------------------------ HOME
HOME_FAQ = [
    ("What does SPU stand for?", "SPU stands for Solar Power Unit — the panels, inverter and battery that turn a home into its own small power plant. SPU.co helps you size, price and buy that unit with confidence."),
    ("Is SPU.co free to use?", "Yes. All calculators, guides and quote matching are free. We earn from advertising, partner referrals and reader support, which never changes the numbers our calculators show."),
    ("Will I get spammed after requesting quotes?", "No. You choose how you want to be contacted, we share your request with at most three vetted installers, and you can opt out at any time."),
    ("Do I need to own my home?", "For rooftop solar, usually yes. Renters can still cut bills with portable power stations, balcony/plug-in solar where allowed, or community solar subscriptions — see our guides."),
    ("How accurate are the calculators?", "They use standard industry assumptions (80% system derate, 0.5%/yr degradation, 3%/yr utility price rise) plus your inputs. Treat results as a planning estimate; an on-site survey gives the final number."),
]

add("index.html", "SPU.co — Solar Power Unit: Calculators, Quotes & Home Battery Guides",
    "Size your solar power unit in 60 seconds. Free solar & battery calculators, incentive finder, honest guides and up to 3 vetted installer quotes.",
    f'''
<section class="hero">
 <div class="container hero-grid">
  <div>
   <span class="eyebrow"><span class="dot"></span> Independent · Free · No-pressure</span>
   <h1>Power your home with your own <em>Solar Power Unit</em></h1>
   <p class="lead-text">Find out how many panels you need, what a battery costs, which incentives apply — and compare quotes from vetted local installers. All in one place.</p>
   <form class="zip-box" data-zip action="get-quotes.html" role="search">
     <label class="sr" for="hz">ZIP / postal code</label>
     <input id="hz" inputmode="text" autocomplete="postal-code" placeholder="Enter your ZIP / postal code" maxlength="10">
     <button class="btn btn-sun" type="submit">See my savings →</button>
   </form>
   <div class="trust-row"><span>No obligation</span><span>Up to 3 vetted quotes</span><span>Takes 60 seconds</span></div>
  </div>
  <div class="hero-card reveal">
   <span class="tag sun">Quick estimate</span>
   <h3 style="margin-top:10px">Typical 7.3 kW home system</h3>
   <div class="results" style="grid-template-columns:repeat(2,1fr);margin-top:14px">
     <div class="result"><small>Panels</small><b>17</b></div>
     <div class="result"><small>Yearly output</small><b>~9,600 kWh</b></div>
     <div class="result"><small>Payback</small><b>7–11 yrs</b></div>
     <div class="result hi"><small>25-yr savings</small><b>$30k+</b></div>
   </div>
   <p class="form-note" style="margin-top:12px">Illustrative U.S. example at $0.18/kWh and 4.5 sun-hours. Your numbers will differ.</p>
   <a class="btn btn-dark" style="width:100%" href="calculator.html">Run my exact numbers</a>
  </div>
 </div>
</section>

<section style="padding-top:24px">
 <div class="container stats">
  <div class="stat"><b data-count="25" data-suffix="+">0</b><span>years of panel life</span></div>
  <div class="stat"><b data-count="60" data-suffix=" sec">0</b><span>to size your system</span></div>
  <div class="stat"><b data-count="3">0</b><span>vetted quotes max</span></div>
  <div class="stat"><b data-count="6">0</b><span>country incentive guides</span></div>
 </div>
</section>

{ad("home-top")}

<section>
 <div class="container">
  <div class="section-head center"><span class="kicker">Everything in one unit</span><h2>Plan, price and power up</h2><p>Built from what the best solar platforms do well — without the sales pressure.</p></div>
  <div class="grid g3">
   <a class="card reveal" href="calculator.html"><div class="ico">🧮</div><h3>Solar savings calculator</h3><p>System size, panels, cost, payback, 25-year savings and CO₂ offset — with a live chart.</p></a>
   <a class="card reveal" href="calculator.html#battery"><div class="ico">🔋</div><h3>Battery backup sizer</h3><p>Pick the appliances you want on during an outage and get the exact kWh you need.</p></a>
   <a class="card reveal" href="get-quotes.html"><div class="ico">🏷️</div><h3>Compare installer quotes</h3><p>Up to three pre-screened local installers. You pick who contacts you, and how.</p></a>
   <a class="card reveal" href="incentives.html"><div class="ico">💸</div><h3>Incentive finder</h3><p>Rebates, subsidies, export tariffs and tax rules for the US, Canada, UK, Australia, India and EU.</p></a>
   <a class="card reveal" href="compare.html"><div class="ico">⚖️</div><h3>Battery & power station compare</h3><p>Sortable specs for leading home batteries and portable power stations.</p></a>
   <a class="card reveal" href="guides/index.html"><div class="ico">📘</div><h3>Buyer guides</h3><p>Costs, financing, net metering, scams — written for homeowners, updated regularly.</p></a>
  </div>
 </div>
</section>

<section class="section-alt">
 <div class="container">
  <div class="section-head"><span class="kicker">How it works</span><h2>From bill to battery in 3 steps</h2></div>
  <div class="grid g3">
   <div class="card"><span class="tag sun">Step 1</span><h3 style="margin-top:10px">Tell us about your home</h3><p>ZIP code, monthly bill and roof. No account needed.</p></div>
   <div class="card"><span class="tag sun">Step 2</span><h3 style="margin-top:10px">See your SPU estimate</h3><p>Size, cost after incentives, payback and savings in seconds.</p></div>
   <div class="card"><span class="tag sun">Step 3</span><h3 style="margin-top:10px">Compare real quotes</h3><p>Vetted installers compete for your project. You decide — or walk away.</p></div>
  </div>
  <div class="center mt"><a class="btn btn-sun btn-lg" href="get-quotes.html">Start my free quote</a></div>
 </div>
</section>

<section>
 <div class="container">
  <div class="section-head"><span class="kicker">Popular guides</span><h2>Answers homeowners search for most</h2></div>
  <div class="grid g3">
   <a class="card" href="guides/solar-panel-cost.html"><span class="tag">Costs</span><h3 style="margin-top:10px">How much do solar panels cost?</h3><p>Price per watt, by system size and country, and what drives quotes up or down.</p></a>
   <a class="card" href="guides/are-solar-panels-worth-it.html"><span class="tag">ROI</span><h3 style="margin-top:10px">Are solar panels worth it?</h3><p>The five numbers that decide your payback period.</p></a>
   <a class="card" href="guides/how-many-solar-panels.html"><span class="tag">Sizing</span><h3 style="margin-top:10px">How many panels do I need?</h3><p>A simple formula plus worked examples.</p></a>
   <a class="card" href="guides/home-battery-guide.html"><span class="tag">Batteries</span><h3 style="margin-top:10px">Home battery buyer's guide</h3><p>kWh vs kW, backup vs self-consumption, and what to pay.</p></a>
   <a class="card" href="guides/solar-financing.html"><span class="tag">Financing</span><h3 style="margin-top:10px">Cash vs loan vs lease vs PPA</h3><p>Which one actually saves the most?</p></a>
   <a class="card" href="guides/solar-scams.html"><span class="tag">Protection</span><h3 style="margin-top:10px">Solar scams & red flags</h3><p>How to read a quote and spot pressure tactics.</p></a>
  </div>
 </div>
</section>

{ad("home-mid")}

<section class="section-alt">
 <div class="container grid g2" style="align-items:center">
  <div>
   <span class="kicker">SPU Video Hub</span><h2>Watch, learn, then decide</h2>
   <p>Short explainers on sizing, batteries, installs and real bills — new videos every week on our YouTube channel.</p>
   <div class="pill-list"><a class="btn btn-dark" href="videos.html">Browse videos</a><a class="btn btn-ghost" data-yt-channel href="#" target="_blank" rel="noopener">Subscribe on YouTube</a></div>
  </div>
  <div class="video-ph">▶ Solar Power Unit explained — in 5 minutes</div>
 </div>
</section>

<section>
 <div class="container grid g3">
  <a class="card" href="contests.html"><div class="ico">🏆</div><h3>Win a portable power station</h3><p>Enter the SPU Sun Challenge — monthly prizes for photos, ideas and referrals.</p></a>
  <a class="card" href="support.html"><div class="ico">💛</div><h3>Keep SPU independent</h3><p>Reader support funds free tools, research and outreach. Chip in from $5.</p></a>
  <a class="card" href="careers.html"><div class="ico">🤝</div><h3>Work with SPU</h3><p>Writers, video creators, energy advisors and developers — join the network.</p></a>
 </div>
</section>

<section class="section-alt">
 <div class="container" style="max-width:860px">
  <div class="section-head center"><span class="kicker">FAQ</span><h2>Common questions</h2></div>
  {faq(HOME_FAQ)}
 </div>
</section>
{cta_band()}
''', active=None, schema=json.dumps([
        {"@context": "https://schema.org", "@type": "Organization", "name": "SPU.co", "url": "https://spu.co",
         "logo": "https://spu.co/assets/img/favicon.svg", "description": "SPU — Solar Power Unit: solar & home battery calculators, guides and installer quotes."},
        {"@context": "https://schema.org", "@type": "WebSite", "name": "SPU.co", "url": "https://spu.co"},
        json.loads(faq_schema(HOME_FAQ))]))

# ------------------------------------------------------------------ CALCULATOR
APPLIANCES = [("Refrigerator", 150, 24, True), ("Wi-Fi router + modem", 20, 24, True), ("LED lights (10)", 100, 6, True),
              ("Phones & laptops", 80, 4, True), ("TV", 100, 4, False), ("Chest freezer", 60, 24, False),
              ("Well pump", 1000, 1, False), ("Sump pump", 800, 1, False), ("Furnace blower / fan", 600, 8, False),
              ("Window A/C", 900, 6, False), ("Central A/C (3-ton)", 3500, 6, False), ("Microwave", 1100, 0.3, False),
              ("Electric kettle / cooktop", 1500, 0.5, False), ("CPAP / medical device", 60, 8, False), ("EV charger (Level 2)", 7200, 2, False)]

appl_rows = "".join(
    f'<div class="appl"><label class="check" style="margin:0;color:var(--ink)"><input type="checkbox" {"checked" if on else ""}> {n}</label>'
    f'<input name="w" type="number" min="0" value="{w}" aria-label="{n} watts"><input name="h" type="number" min="0" step="0.1" max="24" value="{h}" aria-label="{n} hours per day"></div>'
    for n, w, h, on in APPLIANCES)

CALC_FAQ = [
    ("How is system size calculated?", "Annual usage (bill ÷ rate × 12) × target offset ÷ (peak sun hours × 365 × 0.80 derate × shade factor). We round up to whole 430 W panels."),
    ("What are peak sun hours?", "The number of hours per day at 1,000 W/m² equivalent irradiance. Most of the U.S. sees 3.5–6; the UK about 2.5–3; India and Australia 4.5–6. NREL PVWatts gives location-exact values."),
    ("Why does my installer quote a different size?", "Installers adjust for roof layout, orientation, local tariffs, net-metering rules and future loads such as an EV or heat pump."),
    ("How big a battery do I need?", "Add up the watt-hours of what you want running during an outage, multiply by the days of backup, then divide by usable depth-of-discharge (~90%) and round-trip efficiency (~90%)."),
]
add("calculator.html", "Solar Savings & Battery Backup Calculator | SPU.co",
    "Free solar calculator: system size, number of panels, cost after incentives, payback, 25-year savings and CO₂ — plus a battery backup sizer.",
    hero("Free tools", "Solar & battery calculators", "Adjust any input and results update instantly. Defaults are regional averages — replace them with numbers from your own bill for the best estimate.",
         '<a href="index.html">Home</a> › Calculators') + f'''
<section style="padding-top:12px">
 <div class="container">
  <div class="tabs" role="tablist">
   <button role="tab" aria-selected="true" aria-controls="solar">☀ Solar savings</button>
   <button role="tab" aria-selected="false" aria-controls="battery" id="battery-tab">🔋 Battery backup</button>
  </div>
  <div id="solar" class="tab-panel active">
   <div class="calc">
    <form id="solar-form" class="card form" onsubmit="return false">
     <div><label for="c-region">Where is the home?</label>
      <select id="c-region"><option value="US">United States</option><option value="CA">Canada</option><option value="UK">United Kingdom</option><option value="AU">Australia</option><option value="IN">India</option><option value="EU">Europe</option><option value="XX">Other</option></select></div>
     <div><label for="c-bill">Average monthly electric bill (<span data-sym>$</span>)</label><input id="c-bill" type="number" min="0" step="1"></div>
     <div class="row">
      <div><label for="c-rate">Rate per kWh</label><input id="c-rate" type="number" min="0" step="0.01"></div>
      <div><label for="c-sun">Peak sun hours</label><input id="c-sun" type="number" min="1" max="8" step="0.1"></div>
     </div>
     <div class="row">
      <div><label for="c-cpw">Installed cost per watt</label><input id="c-cpw" type="number" min="0" step="0.05"></div>
      <div><label for="c-inc">Incentives / rebates %</label><input id="c-inc" type="number" min="0" max="90" step="1"></div>
     </div>
     <div class="row">
      <div><label for="c-offset">Bill offset target %</label><input id="c-offset" type="number" min="10" max="150" value="100"></div>
      <div><label for="c-shade">Roof shade</label><select id="c-shade"><option value="1">No shade</option><option value="0.9">Some shade</option><option value="0.75">Heavy shade</option></select></div>
     </div>
     <p class="form-note mb0">Assumes 430 W panels, 80% system derate, 0.5%/yr degradation and 3%/yr electricity price rise.</p>
    </form>
    <div class="card">
     <div class="results">
      <div class="result hi"><small>System size</small><b id="r-size">–</b></div>
      <div class="result"><small>Panels (430 W)</small><b id="r-panels">–</b></div>
      <div class="result"><small>Yearly production</small><b id="r-prod">–</b></div>
      <div class="result"><small>Gross cost</small><b id="r-gross">–</b></div>
      <div class="result hi"><small>Net cost after incentives</small><b id="r-net">–</b></div>
      <div class="result"><small>Year-1 savings</small><b id="r-save1">–</b></div>
      <div class="result hi"><small>Payback</small><b id="r-payback">–</b></div>
      <div class="result hi"><small>25-yr net savings</small><b id="r-total">–</b></div>
      <div class="result"><small>25-yr ROI</small><b id="r-roi">–</b></div>
      <div class="result"><small>New bill (yr 1)</small><b id="r-bill">–</b></div>
      <div class="result"><small>CO₂ avoided</small><b id="r-co2">–</b></div>
      <div class="result"><small>Roof area</small><b id="r-area">–</b></div>
     </div>
     <svg id="payback-chart" class="chart" viewBox="0 0 600 220" role="img" aria-label="Cumulative savings chart"></svg>
     <div class="cta-band" style="padding:22px;margin-top:16px">
      <div><h3 style="color:#fff;margin:0">Turn this estimate into real prices</h3><p>Installers quote against your exact roof and utility tariff.</p></div>
      <a id="calc-to-quote" class="btn btn-sun" href="get-quotes.html">Get 3 free quotes →</a>
     </div>
    </div>
   </div>
  </div>
  <div id="battery" class="tab-panel">
   <div class="calc">
    <form id="battery-form" class="card" onsubmit="return false">
     <h3>What must stay on during an outage?</h3>
     <div class="appl" style="font-weight:700;border:0"><span>Appliance</span><span>Watts</span><span>Hrs/day</span></div>
     {appl_rows}
     <div style="margin-top:14px"><label for="b-days">Days of backup</label><select id="b-days"><option value="0.5">Half a day</option><option value="1" selected>1 day</option><option value="2">2 days</option><option value="3">3 days</option></select></div>
    </form>
    <div class="card">
     <div class="results" style="grid-template-columns:repeat(3,1fr)">
      <div class="result"><small>Daily energy</small><b id="b-daily">–</b></div>
      <div class="result hi"><small>Battery needed</small><b id="b-need">–</b></div>
      <div class="result"><small>Peak load</small><b id="b-peak">–</b></div>
     </div>
     <div class="callout"><b>Recommended:</b> <span id="b-rec"></span></div>
     <p class="muted">Solar to recharge: <b id="b-panels"></b>. Check that the battery's continuous kW rating covers your peak load and motor start-up surges (pumps, A/C).</p>
     <div class="pill-list"><a class="btn btn-sun" href="get-quotes.html?interest=battery">Get battery quotes</a><a class="btn btn-ghost" href="compare.html">Compare batteries</a></div>
    </div>
   </div>
  </div>
 </div>
</section>
{ad("calc-bottom")}
<section class="section-alt"><div class="container" style="max-width:860px"><div class="section-head"><h2>How the calculator works</h2></div>{faq(CALC_FAQ)}</div></section>
<script>if(location.hash==='#battery'){{document.addEventListener('DOMContentLoaded',function(){{document.getElementById('battery-tab').click()}})}}</script>
''', active="calculator.html", scripts=("calc.js",), schema=json.dumps([
        {"@context": "https://schema.org", "@type": "WebApplication", "name": "SPU Solar Savings Calculator", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0"}},
        json.loads(faq_schema(CALC_FAQ))]))

# ------------------------------------------------------------------ LEAD GEN
def choices(name, opts, required=True):
    return '<div class="choices">' + "".join(
        f'<label class="choice"><input type="radio" name="{name}" value="{v}" {"required" if required else ""}><span>{i} {v}</span></label>'
        for i, v in opts) + '</div>'


QUOTE_FAQ = [
    ("Is it really free?", "Yes. Installers in our network pay a referral fee when they receive a qualified request, so homeowners never pay SPU.co."),
    ("How many companies will contact me?", "No more than three, and only by the methods you allow. You can ask for email only."),
    ("How are installers vetted?", "We check licensing and insurance where applicable, years in business, manufacturer certifications, public reviews and complaint history."),
    ("Do you share my data with anyone else?", "No. We do not sell your data to data brokers. See our privacy policy for details."),
]
add("get-quotes.html", "Compare Free Solar & Battery Quotes From Vetted Installers | SPU.co",
    "Get up to 3 free, no-obligation quotes for solar panels and home batteries from pre-screened local installers. Takes 60 seconds.",
    f'''
<section class="hero" style="padding-bottom:40px">
 <div class="container">
  <div class="section-head center" style="max-width:760px">
   <span class="eyebrow"><span class="dot"></span> Free · No obligation · Max 3 installers</span>
   <h1>Compare solar quotes, <em>not sales pitches</em></h1>
   <p class="lead-text" style="margin:0 auto">Answer a few quick questions. We match you with up to three vetted installers who serve your area — you choose who contacts you.</p>
  </div>
  <form id="lead-funnel" class="funnel" novalidate>
   <div class="progress"><i></i></div>
   <div class="step-count"><span data-stepnum>Step 1</span><span>🔒 Secure & private</span></div>

   <div class="step"><h3>Where is the property?</h3>
    <div class="form"><div class="row">
     <div><label for="f-zip">ZIP / postal code</label><input id="f-zip" name="zip" required maxlength="10" autocomplete="postal-code" placeholder="e.g. 90210"></div>
     <div><label for="f-country">Country</label><select id="f-country" name="country"><option value="US">United States</option><option value="CA">Canada</option><option value="UK">United Kingdom</option><option value="AU">Australia</option><option value="IN">India</option><option value="EU">Europe</option><option value="XX">Other</option></select></div>
    </div></div>
    <div class="step-nav"><span></span><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Do you own this home?</h3>
    {choices("homeowner", [("🏠", "Yes"), ("🏢", "Landlord / investor"), ("🔑", "Renter"), ("🏗️", "Buying soon")])}
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Average monthly electric bill?</h3>
    <p class="callout" data-renter-note hidden>Renting? You can still save with portable power stations, plug-in balcony solar (where permitted) or community solar — we'll send options that fit renters.</p>
    <div class="range-out">$<span data-bill-out>150</span></div>
    <label class="sr" for="f-bill">Monthly bill</label>
    <input id="f-bill" type="range" name="bill" min="25" max="1000" step="5" value="150">
    <div style="display:flex;justify-content:space-between" class="form-note"><span>$25</span><span>$1,000+</span></div>
    <input type="hidden" name="est_kw">
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>What are you interested in?</h3>
    {choices("interest", [("☀", "Solar panels"), ("⚡", "Solar + battery"), ("🔋", "Battery only"), ("🎒", "Portable backup"), ("🚗", "EV charger + solar"), ("🏭", "Commercial solar")])}
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>How much shade does your roof get?</h3>
    {choices("shade", [("🌞", "No shade"), ("⛅", "Some shade"), ("🌳", "Heavy shade"), ("🤷", "Not sure")])}
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Estimated credit score?</h3>
    <p class="form-note">Helps installers show the right financing. No credit check is run.</p>
    {choices("credit", [("⭐", "Excellent 720+"), ("👍", "Good 680–719"), ("👌", "Fair 620–679"), ("🔄", "Below 620"), ("💵", "Paying cash")])}
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>When do you want to install?</h3>
    {choices("timeline", [("🚀", "ASAP"), ("📅", "1–3 months"), ("🗓️", "3–6 months"), ("🔎", "Just researching")])}
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Property details</h3>
    <div class="form">
     <div><label for="f-addr">Street address <span class="muted">(for a roof & sun check)</span></label><input id="f-addr" name="address" required autocomplete="street-address" placeholder="123 Sunny St"></div>
     <div class="row"><div><label for="f-city">City</label><input id="f-city" name="city" required autocomplete="address-level2"></div>
     <div><label for="f-ptype">Property type</label><select id="f-ptype" name="property_type"><option>Single-family</option><option>Townhouse</option><option>Multi-family</option><option>Farm / rural</option><option>Commercial</option></select></div></div>
    </div>
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Who should we send your quotes to?</h3>
    <div class="form">
     <div class="row"><div><label for="f-fn">First name</label><input id="f-fn" name="first_name" required autocomplete="given-name"></div>
     <div><label for="f-ln">Last name</label><input id="f-ln" name="last_name" required autocomplete="family-name"></div></div>
     <div><label for="f-em">Email</label><input id="f-em" type="email" name="email" required autocomplete="email"></div>
    </div>
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun" data-next>Continue →</button></div></div>

   <div class="step"><h3>Last step — how can installers reach you?</h3>
    <div class="form">
     <div><label for="f-ph">Phone</label><input id="f-ph" type="tel" name="phone" required autocomplete="tel" pattern="[0-9+()\\-\\s]{{7,}}" placeholder="(555) 123-4567"></div>
     <div><label for="f-pref">Preferred contact</label><select id="f-pref" name="contact_preference"><option>Email only</option><option>Phone call</option><option>Text message</option><option>Any</option></select></div>
     <div><label for="f-notes">Anything else? <span class="muted">(optional)</span></label><textarea id="f-notes" name="notes" style="min-height:80px" placeholder="Roof age, EV plans, outage concerns…"></textarea></div>
     <label class="check"><input type="checkbox" name="consent" value="yes" required> By clicking “Get my free quotes”, I agree to the <a href="terms.html">Terms</a> and <a href="privacy.html">Privacy Policy</a> and give SPU.co and up to three matched solar installers my express written consent to contact me about my request at the number and email provided, including by autodialed or prerecorded calls and texts. Consent is not a condition of purchase. Message/data rates may apply. Reply STOP to opt out.</label>
     <label class="check"><input type="checkbox" name="newsletter" value="yes"> Send me the free SPU Sun Report (monthly tips & deals).</label>
     <input class="hp" name="_honey" tabindex="-1" autocomplete="off">
     <input type="hidden" name="utm_source"><input type="hidden" name="utm_medium"><input type="hidden" name="utm_campaign"><input type="hidden" name="utm_term"><input type="hidden" name="utm_content"><input type="hidden" name="gclid"><input type="hidden" name="referrer">
     <div class="form-status"></div>
    </div>
    <div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-sun btn-lg" type="submit">Get my free quotes</button></div></div>
  </form>
  <div id="lead-thanks" class="funnel center" hidden>
   <div style="font-size:3rem">🎉</div><h2>You're all set, <span data-first></span>!</h2>
   <p>Your request is in. Expect your matched quotes within 1–2 business days. Meanwhile:</p>
   <div class="grid g3" style="text-align:left;margin-top:18px">
    <a class="card" href="guides/solar-scams.html"><h3>Read a quote like a pro</h3><p>Red flags to watch for.</p></a>
    <a class="card" href="incentives.html"><h3>Check incentives</h3><p>Know what you qualify for.</p></a>
    <a class="card" href="contests.html"><h3>Enter the Sun Challenge</h3><p>Win a power station.</p></a>
   </div>
  </div>
  <div class="trust-row" style="justify-content:center;margin-top:20px"><span>We never sell data to brokers</span><span>Max 3 installers</span><span>Opt out anytime</span><span>No credit check</span></div>
 </div>
</section>

<section class="section-alt">
 <div class="container grid g4">
  <div class="card"><div class="ico">🛡️</div><h3>Vetted installers</h3><p>Licensing, insurance, certifications and review history checked.</p></div>
  <div class="card"><div class="ico">🤫</div><h3>You control contact</h3><p>Email-only is one click away. No call-centre blitz.</p></div>
  <div class="card"><div class="ico">📊</div><h3>Apples-to-apples</h3><p>We help you compare price per watt, equipment and warranties.</p></div>
  <div class="card"><div class="ico">💬</div><h3>Independent help</h3><p>Questions about a quote? Our advisors answer free.</p></div>
 </div>
</section>

<section>
 <div class="container grid g2">
  <div><span class="kicker">For businesses</span><h2>Commercial, farm & multi-site solar</h2><p>Warehouses, farms, schools, places of worship and multi-family buildings qualify for different incentives and financing. Tell us about your site.</p>
   <form class="card form" data-spu-form="Commercial solar lead" data-success="Thanks — a commercial energy advisor will reach out within 1 business day.">
    <div class="row"><div><label>Company</label><input name="company" required></div><div><label>Your name</label><input name="name" required></div></div>
    <div class="row"><div><label>Work email</label><input type="email" name="email" required></div><div><label>Phone</label><input type="tel" name="phone"></div></div>
    <div class="row"><div><label>Monthly energy spend</label><select name="spend"><option>&lt; $1,000</option><option>$1,000–5,000</option><option>$5,000–20,000</option><option>$20,000+</option></select></div><div><label>Site location</label><input name="location" required></div></div>
    <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the privacy policy.</label>
    <input class="hp" name="_honey" tabindex="-1" autocomplete="off"><div class="form-status"></div>
    <button class="btn btn-dark" type="submit">Request commercial assessment</button>
   </form></div>
  <div><span class="kicker">FAQ</span><h2>Quote questions</h2>{faq(QUOTE_FAQ)}</div>
 </div>
</section>
''', active="get-quotes.html", scripts=("leadform.js",), schema=faq_schema(QUOTE_FAQ))
