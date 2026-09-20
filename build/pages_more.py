from layout import ad, hero, faq, faq_schema, cta_band
from pages_core import add
import json

HP = '<input class="hp" name="_honey" tabindex="-1" autocomplete="off"><div class="form-status"></div>'

# ------------------------------------------------------------------ INCENTIVES
INC = [
 ("US", "🇺🇸 United States", [
   ("Federal tax credit changes", "The 30% Residential Clean Energy Credit (Sec. 25D) ended for homeowner-owned systems paid for after Dec 31, 2025 under the 2025 federal budget law. Leased and PPA systems may still carry a commercial credit through the installer — ask each quote how it is priced in."),
   ("State & utility rebates", "Many states and utilities still offer cash rebates, performance payments (SRECs) and battery incentives, e.g. California SGIP for storage and Massachusetts SMART. Search your ZIP on DSIRE (dsireusa.org)."),
   ("Net metering / net billing", "Export credit rules vary by utility; California's NEM 3.0 pays far less for exports, which makes batteries more valuable."),
   ("Property & sales tax", "Many states exempt solar from property-tax reassessment and/or sales tax.")]),
 ("CA", "🇨🇦 Canada", [
   ("Provincial & utility programs", "Federal Greener Homes grants closed to new applicants; incentives are now mainly provincial and utility-led (e.g. BC Hydro solar + battery rebates, Nova Scotia programs). Check your province's energy-efficiency agency."),
   ("Net metering", "Most provinces offer net metering; credit rules and caps differ."),
   ("Green financing", "Several banks and municipalities (PACE-style programs) offer low-rate green home loans.")]),
 ("UK", "🇬🇧 United Kingdom", [
   ("0% VAT", "Solar panels and batteries installed in homes are zero-rated for VAT until 31 March 2027."),
   ("Smart Export Guarantee (SEG)", "Licensed suppliers must pay you for exported electricity; rates vary widely by supplier — shop around."),
   ("ECO4 & Warm Homes", "Low-income and eligible households may get free or subsidised solar via ECO4 and local Warm Homes schemes.")]),
 ("AU", "🇦🇺 Australia", [
   ("STCs (SRES)", "Small-scale Technology Certificates reduce the upfront price of systems up to 100 kW; the discount steps down each year until 2030."),
   ("Cheaper Home Batteries", "Since 1 July 2025 the federal program cuts eligible home battery costs by roughly 30% via STCs."),
   ("State schemes & FiTs", "Extra state rebates/loans (e.g. Victoria's Solar Homes) and retailer feed-in tariffs apply.")]),
 ("IN", "🇮🇳 India", [
   ("PM Surya Ghar: Muft Bijli Yojana", "Central Financial Assistance for residential rooftop solar: ₹30,000/kW for the first 2 kW, ₹18,000 for the 3rd kW, capped at ₹78,000. Apply on the national portal."),
   ("Collateral-free loans", "Public-sector banks offer low-interest rooftop solar loans under the scheme."),
   ("Net metering", "DISCOMs provide net metering; state rules and approval timelines vary.")]),
 ("EU", "🇪🇺 Europe", [
   ("Reduced VAT", "Germany applies 0% VAT to residential PV up to 30 kW; several other EU states apply reduced rates."),
   ("Feed-in & self-consumption", "Feed-in tariffs (e.g. Germany's EEG) are falling; self-consumption with a battery increasingly beats exporting."),
   ("Netherlands net metering", "The salderingsregeling ends on 1 January 2027 — batteries and smart usage become more important.")]),
]
inc_html = ""
for code, name, items in INC:
    inc_html += f'<div class="card" data-item data-cat="{code}" style="margin-bottom:18px"><h2 style="font-size:1.5rem">{name}</h2><div class="grid g2">' + \
        "".join(f'<div><h3 style="font-size:1.05rem">{t}</h3><p>{d}</p></div>' for t, d in items) + \
        f'</div><a class="btn btn-sun btn-sm" href="get-quotes.html?region={code}">Get quotes that include {name.split(" ",1)[1]} incentives →</a></div>'

add("incentives.html", "Solar & Battery Incentives, Rebates and Tax Rules by Country | SPU.co",
    "Solar and home battery incentives for the US, Canada, UK, Australia, India and Europe — rebates, subsidies, export tariffs and tax changes explained.",
    hero("Incentive finder", "Solar & battery incentives", "Incentives change often. This page summarises the main programs by country — always confirm eligibility with the official program or your installer before signing.",
         '<a href="index.html">Home</a> › Incentives') + f'''
<section style="padding-top:12px"><div class="container">
 <div class="card form" style="margin-bottom:22px">
  <div class="row"><div><label for="inc-q">Search programs</label><input id="inc-q" data-filter="#inc-list" data-filter-text placeholder="e.g. VAT, battery, net metering"></div>
  <div><label for="inc-c">Country</label><select id="inc-c" data-filter="#inc-list" data-filter-cat><option value="">All countries</option><option value="US">United States</option><option value="CA">Canada</option><option value="UK">United Kingdom</option><option value="AU">Australia</option><option value="IN">India</option><option value="EU">Europe</option></select></div></div>
 </div>
 <div id="inc-list">{inc_html}</div>
 <p class="form-note">Last reviewed: September 2026. Summaries only — not tax or legal advice. Found an outdated program? <a href="contact.html">Tell us</a>.</p>
</div></section>
{ad("inc-bottom")}
<section class="section-alt"><div class="container grid g2" style="align-items:center">
 <div><h2>Get incentive alerts for your area</h2><p>We email you when a rebate opens, changes or is about to close.</p></div>
 <form class="card form" data-spu-form="Incentive alert signup" data-success="Done! We'll alert you when incentives change in your area.">
  <div class="row"><div><label>Email</label><input type="email" name="email" required></div><div><label>ZIP / postal code</label><input name="zip" required></div></div>
  {HP}<button class="btn btn-sun" type="submit">Alert me</button></form>
</div></section>
{cta_band()}''', active="incentives.html", scripts=("calc.js",))

# ------------------------------------------------------------------ COMPARE
BATT = [
 ("Tesla Powerwall 3", "Home battery", 13.5, 11.5, "Integrated solar inverter", "10 yr", "$$$"),
 ("Enphase IQ Battery 5P", "Home battery", 5.0, 3.84, "Modular, stackable AC-coupled", "15 yr", "$$"),
 ("FranklinWH aPower 2", "Home battery", 15.0, 10.0, "Whole-home, generator-ready", "12 yr", "$$$"),
 ("LG RESU Prime 16H", "Home battery", 16.0, 7.0, "High-voltage DC", "10 yr", "$$$"),
 ("SolarEdge Home Battery", "Home battery", 9.7, 5.0, "DC-coupled with SolarEdge inverter", "10 yr", "$$"),
 ("EcoFlow DELTA Pro 3", "Portable / expandable", 4.1, 4.0, "Expandable to ~48 kWh", "5 yr", "$$"),
 ("Anker SOLIX F3800", "Portable / expandable", 3.84, 6.0, "120/240 V split-phase", "5 yr", "$$"),
 ("Jackery Explorer 2000 Plus", "Portable / expandable", 2.04, 3.0, "Expandable, LiFePO4", "5 yr", "$$"),
 ("Bluetti AC200L", "Portable", 2.05, 2.4, "LiFePO4, expandable", "5 yr", "$"),
 ("Goal Zero Yeti 1500X", "Portable", 1.52, 2.0, "Camping / light backup", "2 yr", "$$"),
 ("EcoFlow RIVER 3", "Portable", 0.25, 0.3, "Ultra-compact", "5 yr", "$"),
]
rows = "".join(f'<tr><td><b>{n}</b></td><td>{c}</td><td data-v="{k}">{k} kWh</td><td data-v="{p}">{p} kW</td><td>{f}</td><td data-v="{w[:-3]}">{w}</td><td>{pr}</td></tr>' for n, c, k, p, f, w, pr in BATT)
PANELS = [("Monocrystalline PERC", "19–21%", "Mainstream, best value"), ("TOPCon (N-type)", "21–23%", "Now the market default for new modules"),
          ("Heterojunction (HJT)", "21–23%", "Excellent heat performance"), ("Back-contact (IBC)", "22–24%+", "Premium look & efficiency"),
          ("Bifacial", "+5–15% yield", "Ground mounts, carports, light roofs")]
prow = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in PANELS)

add("compare.html", "Compare Home Batteries & Portable Power Stations (2026) | SPU.co",
    "Sortable comparison of popular home batteries and portable power stations — capacity, power, warranty and use case — plus solar panel technology explained.",
    hero("Compare", "Home batteries & power stations", "Click any column heading to sort. Specs are from manufacturer datasheets at time of review — confirm the current model before buying.",
         '<a href="index.html">Home</a> › Compare') + f'''
<section style="padding-top:12px"><div class="container">
 <div class="table-wrap"><table data-sort><thead><tr><th>Model ↕</th><th>Type ↕</th><th>Capacity ↕</th><th>Continuous power ↕</th><th>Notes</th><th>Warranty ↕</th><th>Price tier</th></tr></thead><tbody>{rows}</tbody></table></div>
 <p class="form-note">Some links on SPU.co may be affiliate links; we may earn a commission at no extra cost to you. Rankings are never sold.</p>
 <div class="grid g3 mt">
  <div class="card"><h3>Need whole-home backup?</h3><p>Look for ≥10 kWh and ≥7 kW continuous, with a transfer switch or gateway.</p></div>
  <div class="card"><h3>Renting or on a budget?</h3><p>A 1–4 kWh LiFePO4 power station covers fridge, Wi-Fi and lights for a day.</p></div>
  <div class="card"><h3>On time-of-use rates?</h3><p>A battery shifts cheap solar to expensive evening hours — often the best ROI case.</p></div>
 </div>
</div></section>
{ad("compare-mid")}
<section class="section-alt"><div class="container"><div class="section-head"><h2>Solar panel technologies</h2></div>
 <div class="table-wrap"><table><thead><tr><th>Technology</th><th>Typical module efficiency</th><th>Best for</th></tr></thead><tbody>{prow}</tbody></table></div>
 <div class="center mt"><a class="btn btn-sun" href="calculator.html#battery">Size my battery</a></div>
</div></section>{cta_band()}''', active="compare.html", scripts=("calc.js",))

# ------------------------------------------------------------------ VIDEOS
TOPICS = [("Solar basics", "how solar panels work for homes"), ("Home batteries", "home battery backup explained"),
          ("Installation day", "residential solar installation time lapse"), ("DIY & off-grid", "diy off grid solar system beginner"),
          ("Portable power", "portable power station review lifepo4"), ("Solar + EV", "charging ev with home solar")]
tcards = "".join(f'<a class="card" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query={q.replace(" ","+")}"><div class="ico">▶</div><h3>{t}</h3><p>Explore top videos on {t.lower()} →</p></a>' for t, q in TOPICS)
add("videos.html", "Solar & Battery Video Hub | SPU.co",
    "Watch explainers on solar sizing, home batteries, installation and off-grid power. Subscribe to the SPU.co YouTube channel.",
    hero("Video hub", "Learn solar by watching", "Our own explainers plus curated topics. New SPU videos every week.", '<a href="index.html">Home</a> › Videos') + f'''
<section style="padding-top:12px"><div class="container">
 <div class="section-head"><h2>Latest from SPU</h2><p>Add a YouTube video ID to any <code>data-yt</code> slot to publish it here (lazy-loaded for speed).</p></div>
 <div class="grid g3">
  <div><div class="video" data-yt=""><div class="video-ph">Episode 1 · How big should my Solar Power Unit be?</div></div><h3 style="margin-top:10px">Sizing your system in 5 minutes</h3></div>
  <div><div class="video" data-yt=""><div class="video-ph">Episode 2 · Battery or generator?</div></div><h3 style="margin-top:10px">Battery vs generator for outages</h3></div>
  <div><div class="video" data-yt=""><div class="video-ph">Episode 3 · Reading a solar quote</div></div><h3 style="margin-top:10px">How to read a solar quote</h3></div>
 </div>
 <div class="center mt"><a class="btn btn-sun btn-lg" data-yt-channel href="#" target="_blank" rel="noopener">▶ Subscribe on YouTube</a></div>
</div></section>
{ad("videos-mid")}
<section class="section-alt"><div class="container"><div class="section-head"><h2>Browse by topic</h2></div><div class="grid g3">{tcards}</div></div></section>
<section><div class="container grid g2">
 <div><span class="kicker">Creators</span><h2>Feature your solar video on SPU</h2><p>Installers, DIYers and reviewers: submit your video for our weekly roundup and newsletter. Sponsored placements available.</p></div>
 <form class="card form" data-spu-form="Video submission" data-success="Thanks! Our editors review submissions weekly.">
  <div class="row"><div><label>Your name / channel</label><input name="channel" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
  <div><label>Video URL</label><input type="url" name="video_url" required placeholder="https://youtube.com/watch?v=…"></div>
  <div><label>Interested in</label><select name="type"><option>Free roundup feature</option><option>Sponsored placement</option><option>Collaboration</option></select></div>
  {HP}<button class="btn btn-dark" type="submit">Submit video</button></form>
</div></section>''', active="videos.html")

# ------------------------------------------------------------------ INSTALLERS
add("installers.html", "Find Vetted Solar Installers & List Your Solar Company | SPU.co",
    "How SPU.co vets solar installers, what to ask before signing, and how installers can join the network to receive exclusive homeowner leads.",
    hero("Installer network", "Vetted installers — and how to join", "Homeowners: see how we vet. Installers: get exclusive, pre-qualified, consented leads in your service area.", '<a href="index.html">Home</a> › Installers') + f'''
<section style="padding-top:12px"><div class="container grid g2">
 <div class="card"><h2>Our vetting checklist</h2><ul>
  <li>Valid license & insurance where required</li><li>At least 2 years installing under the same name</li><li>Manufacturer certifications (panel, inverter, battery)</li>
  <li>Minimum 4.0★ public review average & complaint check</li><li>Written workmanship warranty (10 yrs+ preferred)</li><li>Transparent price-per-watt quotes, no pressure tactics</li></ul>
  <a class="btn btn-sun" href="get-quotes.html">Get matched with installers</a></div>
 <div class="card"><h2>10 questions to ask every installer</h2><ol>
  <li>What is the price per watt before and after incentives?</li><li>Which panel, inverter and battery models exactly?</li><li>Who does the install — employees or subcontractors?</li>
  <li>What workmanship and roof-penetration warranty do you give?</li><li>What production (kWh/yr) do you guarantee?</li><li>How are permits and utility interconnection handled?</li>
  <li>What happens if you go out of business?</li><li>Are there escalators in the loan/lease?</li><li>What monitoring is included?</li><li>Can I speak to three recent customers?</li></ol></div>
</div></section>
{ad("installers-mid")}
<section class="section-alt" id="join"><div class="container grid g2">
 <div><span class="kicker">For installers</span><h2>Grow with exclusive SPU leads</h2>
  <div class="grid g2">
   <div class="card"><h3>Exclusive or shared (max 3)</h3><p>Choose lead exclusivity by ZIP and product.</p></div>
   <div class="card"><h3>Pre-qualified</h3><p>Homeowner, bill, shade, credit band, timeline — scored 0–100.</p></div>
   <div class="card"><h3>Consent recorded</h3><p>Timestamp, page and consent text captured with every lead.</p></div>
   <div class="card"><h3>Featured listings</h3><p>Sponsored placement in guides, calculator results and the newsletter.</p></div>
  </div></div>
 <form class="card form" data-spu-form="Installer partner application" data-success="Thanks! Our partnerships team will contact you within 2 business days.">
  <h3>Apply to join the network</h3>
  <div class="row"><div><label>Company name</label><input name="company" required></div><div><label>Contact name</label><input name="name" required></div></div>
  <div class="row"><div><label>Email</label><input type="email" name="email" required></div><div><label>Phone</label><input type="tel" name="phone" required></div></div>
  <div class="row"><div><label>Website</label><input type="url" name="website" placeholder="https://"></div><div><label>Years in business</label><input type="number" name="years" min="0"></div></div>
  <div><label>Service areas (ZIPs, cities or states)</label><input name="service_area" required></div>
  <div class="row"><div><label>Products</label><select name="products"><option>Residential solar</option><option>Solar + storage</option><option>Batteries only</option><option>Commercial</option><option>All of the above</option></select></div>
  <div><label>Monthly lead capacity</label><select name="capacity"><option>1–10</option><option>11–50</option><option>51–200</option><option>200+</option></select></div></div>
  <div><label>Licenses / certifications</label><textarea name="certifications" style="min-height:80px"></textarea></div>
  {HP}<button class="btn btn-sun" type="submit">Apply now</button></form>
</div></section>''', active="installers.html")

# ------------------------------------------------------------------ CONTESTS
add("contests.html", "SPU Sun Challenge — Contests & Prizes | SPU.co",
    "Enter the SPU Sun Challenge to win portable power stations, solar gear and cash prizes. Photo, idea and referral contests every month.",
    hero("Contests & prizes", "The SPU Sun Challenge", "Share your solar story, idea or photo — or refer a friend — for a chance to win power stations and solar gear.", '<a href="index.html">Home</a> › Contests') + f'''
<section style="padding-top:12px"><div class="container grid g2" style="align-items:start">
 <div>
  <div class="card" style="margin-bottom:18px"><span class="tag sun">Current contest</span><h2 style="margin-top:10px">Best Solar Setup 2026</h2>
   <p>Show us your rooftop, balcony, RV or off-grid setup. Judged on creativity, usefulness and story.</p>
   <div class="countdown" data-countdown="2026-12-31T23:59:59"><div><b>00</b><small>days</small></div><div><b>00</b><small>hrs</small></div><div><b>00</b><small>min</small></div><div><b>00</b><small>sec</small></div></div></div>
  <div class="grid g3">
   <div class="card center"><div style="font-size:2rem">🥇</div><h3>Grand prize</h3><p>2 kWh portable power station</p></div>
   <div class="card center"><div style="font-size:2rem">🥈</div><h3>Runner-up</h3><p>200 W folding solar panel</p></div>
   <div class="card center"><div style="font-size:2rem">🥉</div><h3>10 winners</h3><p>SPU swag + gift cards</p></div>
  </div>
  <div class="card mt"><h3>Other ways to win</h3><ul><li><b>Referral race:</b> each friend who requests quotes = 1 extra entry.</li><li><b>Idea prize:</b> best idea to make solar cheaper wins a cash prize.</li><li><b>Student challenge:</b> school energy projects — winning class gets a solar kit.</li></ul></div>
  <div class="card mt"><h3>Sponsor a prize</h3><p>Brands can sponsor prizes and get featured to our audience. <a href="advertise.html">See sponsorship options →</a></p></div>
 </div>
 <form class="card form" data-spu-form="Contest entry" data-success="You're entered! Good luck — winners are announced on this page and by email.">
  <h3>Enter now — it's free</h3>
  <div class="row"><div><label>Full name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
  <div class="row"><div><label>Country</label><input name="country" required></div><div><label>Category</label><select name="category"><option>Best Solar Setup</option><option>Idea prize</option><option>Student challenge</option><option>Referral race</option></select></div></div>
  <div><label>Link to your photo/video (Drive, Instagram, YouTube…)</label><input type="url" name="entry_url" placeholder="https://"></div>
  <div><label>Tell your story (max 300 words)</label><textarea name="story" required maxlength="2000"></textarea></div>
  <div><label>Referred by (optional)</label><input name="referred_by"></div>
  <label class="check"><input type="checkbox" name="rules" value="accepted" required> I am 18+ (or have parental consent) and accept the <a href="#rules">official rules</a>.</label>
  {HP}<button class="btn btn-sun btn-lg" type="submit">Submit my entry</button></form>
</div></section>
<section class="section-alt" id="rules"><div class="container" style="max-width:860px"><h2>Official rules (summary)</h2>
 <p>No purchase necessary. Void where prohibited. Entries close at the countdown end date. Winners are selected by an SPU.co judging panel and notified by email within 14 days; unclaimed prizes after 30 days may be redrawn. Prize values are approximate; no cash alternative unless stated. By entering, you grant SPU.co a non-exclusive licence to display your entry with credit. Full rules are available on request via the <a href="contact.html">contact page</a>.</p></div></section>''', active="contests.html")

# ------------------------------------------------------------------ SUPPORT / DONATE
add("support.html", "Support SPU.co — Donate, Sponsor & Fund Free Solar Tools",
    "Help keep SPU.co independent. Donations fund free calculators, research, outreach, contests and new talent.",
    hero("Support SPU", "Keep solar advice free and independent", "Every contribution funds free tools, honest research, community contests, marketing that reaches more homeowners, and paid work for new talent.", '<a href="index.html">Home</a> › Support') + f'''
<section style="padding-top:12px"><div class="container grid g2" style="align-items:start">
 <div class="card" data-donate-box data-amount="25">
  <h2>Make a donation</h2>
  <label>Choose an amount (USD)</label>
  <div class="amounts"><button type="button" data-v="5">$5</button><button type="button" data-v="10">$10</button><button type="button" class="on" data-v="25">$25</button><button type="button" data-v="50">$50</button><button type="button" data-v="100">$100</button><button type="button" data-v="250">$250</button></div>
  <div class="form" style="margin-top:14px"><div class="row">
   <div><label for="d-custom">Custom amount</label><input id="d-custom" name="custom_amount" type="number" min="1" placeholder="Other"></div>
   <div><label for="d-purpose">Direct my support to</label><select id="d-purpose" name="purpose"><option>Where it's needed most</option><option>Operations & free tools</option><option>Promotions & marketing</option><option>Hiring talent</option><option>Contests & prizes</option></select></div>
  </div></div>
  <button class="btn btn-sun btn-lg" style="width:100%;margin-top:16px" data-donate="General">💛 Donate securely with PayPal</button>
  <p class="form-note" style="margin-top:10px">Opens PayPal in a new tab (cards accepted). SPU.co is not a registered charity; donations are not tax-deductible.</p>
 </div>
 <div>
  <div class="grid g2 tiers">
   <div class="card"><h3>☀ Sunbeam — $5/mo</h3><p>Name in our supporters list + monthly Sun Report.</p><button class="btn btn-ghost btn-sm mt" data-donate="Sunbeam monthly" data-amount="5">Support</button></div>
   <div class="card pick"><h3>⚡ Power Unit — $25/mo</h3><p>Early access to new tools and a vote on next guides.</p><button class="btn btn-sun btn-sm mt" data-donate="Power Unit monthly" data-amount="25">Support</button></div>
   <div class="card"><h3>🔋 Grid Hero — $100/mo</h3><p>Logo/name on the supporters wall + quarterly call.</p><button class="btn btn-ghost btn-sm mt" data-donate="Grid Hero monthly" data-amount="100">Support</button></div>
   <div class="card"><h3>🏢 Corporate patron</h3><p>Sponsor a tool, contest or scholarship.</p><a class="btn btn-ghost btn-sm mt" href="advertise.html">Talk to us</a></div>
  </div>
  <div class="card mt"><h3>Where the money goes</h3>
   <div style="display:grid;gap:8px">
    <div><small>Operations & free tools — 40%</small><div class="progress"><i style="width:40%"></i></div></div>
    <div><small>Promotions & marketing — 25%</small><div class="progress"><i style="width:25%"></i></div></div>
    <div><small>Hiring talent — 20%</small><div class="progress"><i style="width:20%"></i></div></div>
    <div><small>Contests & prizes — 15%</small><div class="progress"><i style="width:15%"></i></div></div>
   </div></div>
 </div>
</div></section>
<section class="section-alt"><div class="container grid g2">
 <div><h2>Other ways to help</h2><ul><li>Share SPU.co with a friend considering solar <button class="btn btn-ghost btn-sm" data-share>Share</button></li><li>Subscribe on <a data-yt-channel href="#" target="_blank" rel="noopener">YouTube</a></li><li>Volunteer: translate guides, test tools, suggest incentives</li><li>Donate gear for contest prizes</li></ul></div>
 <form class="card form" data-spu-form="Pledge / in-kind support" data-success="Thank you for your generosity! We'll be in touch.">
  <h3>Pledge, sponsor or give in-kind</h3>
  <div class="row"><div><label>Name / organisation</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
  <div><label>Type of support</label><select name="support_type"><option>Recurring pledge</option><option>Prize / gear donation</option><option>Volunteer time</option><option>Corporate sponsorship</option><option>Bank transfer / other method</option></select></div>
  <div><label>Message</label><textarea name="message"></textarea></div>
  {HP}<button class="btn btn-dark" type="submit">Send pledge</button></form>
</div></section>''', active="support.html")

# ------------------------------------------------------------------ CAREERS
JOBS = [("Solar content writer", "Remote · Freelance", "Write data-driven buyer guides and state/country incentive pages."),
        ("YouTube video editor", "Remote · Part-time", "Edit explainers, shorts and installer case studies."),
        ("Energy advisor", "Remote · Commission", "Help homeowners compare quotes over chat and phone."),
        ("Partnerships manager", "Remote · Full-time", "Recruit and manage installer partners and sponsors."),
        ("Front-end developer", "Remote · Contract", "Build calculators, maps and interactive tools."),
        ("Community & contest lead", "Remote · Part-time", "Run the Sun Challenge, social media and ambassador program.")]
jobs = "".join(f'<div class="card"><span class="tag">{l}</span><h3 style="margin-top:10px">{t}</h3><p>{d}</p></div>' for t, l, d in JOBS)
add("careers.html", "Careers & Talent Network — Work With SPU.co",
    "Join SPU.co: remote roles for solar writers, video editors, energy advisors, developers and partnership managers.",
    hero("Careers", "Help the world run on sunshine", "We hire remote talent worldwide — freelance, part-time and full-time. Join the talent network even if no role fits yet.", '<a href="index.html">Home</a> › Careers') + f'''
<section style="padding-top:12px"><div class="container"><div class="grid g3">{jobs}</div></div></section>
<section class="section-alt"><div class="container grid g2">
 <div><h2>Why SPU</h2><ul><li>100% remote, async-first</li><li>Paid per project or salaried</li><li>Mission-driven: cheaper clean energy for everyone</li><li>Ambassador & referral bonuses</li></ul></div>
 <form class="card form" data-spu-form="Job application" data-success="Application received! We review every application and reply within 7 days.">
  <h3>Apply / join the talent network</h3>
  <div class="row"><div><label>Full name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
  <div class="row"><div><label>Role</label><select name="role">{"".join(f"<option>{t}</option>" for t,_,_ in JOBS)}<option>Other / talent network</option></select></div><div><label>Country / time zone</label><input name="location" required></div></div>
  <div><label>Portfolio / LinkedIn / CV link</label><input type="url" name="portfolio" required placeholder="https://"></div>
  <div><label>Why you?</label><textarea name="pitch" required></textarea></div>
  {HP}<button class="btn btn-sun" type="submit">Submit application</button></form>
</div></section>''', active=None)

# ------------------------------------------------------------------ ADVERTISE
add("advertise.html", "Advertise, Sponsor & Promote on SPU.co",
    "Reach homeowners actively researching solar and batteries: sponsored guides, calculator placements, newsletter, video and contest sponsorships, pay-per-lead.",
    hero("Advertise", "Reach buyers at the moment they decide", "SPU.co audiences are homeowners researching system size, cost and financing — the highest-intent stage of the solar journey.", '<a href="index.html">Home</a> › Advertise') + f'''
<section style="padding-top:12px"><div class="container grid g3">
 <div class="card"><div class="ico">🎯</div><h3>Pay-per-lead</h3><p>Exclusive or shared consented leads by ZIP, product and score.</p></div>
 <div class="card"><div class="ico">📌</div><h3>Featured installer</h3><p>Top placement in results, guides and state pages.</p></div>
 <div class="card"><div class="ico">📰</div><h3>Sponsored guides</h3><p>Clearly labelled expert content and product reviews.</p></div>
 <div class="card"><div class="ico">🧮</div><h3>Calculator sponsor</h3><p>Branded placement on high-engagement tool pages.</p></div>
 <div class="card"><div class="ico">✉️</div><h3>Newsletter & video</h3><p>Sun Report sponsorships and YouTube integrations.</p></div>
 <div class="card"><div class="ico">🏆</div><h3>Contest sponsor</h3><p>Put your product in winners' hands and get UGC.</p></div>
</div></section>
<section class="section-alt"><div class="container grid g2">
 <div><h2>Request the media kit</h2><p>Audience data, rate card and available placements. Affiliate programs welcome (power stations, panels, EV chargers, smart home).</p></div>
 <form class="card form" data-spu-form="Advertising inquiry" data-success="Thanks! We'll send the media kit shortly.">
  <div class="row"><div><label>Company</label><input name="company" required></div><div><label>Name</label><input name="name" required></div></div>
  <div class="row"><div><label>Email</label><input type="email" name="email" required></div><div><label>Budget / month</label><select name="budget"><option>&lt; $1k</option><option>$1k–5k</option><option>$5k–20k</option><option>$20k+</option></select></div></div>
  <div><label>Interested in</label><select name="interest"><option>Pay-per-lead</option><option>Featured listing</option><option>Sponsored content</option><option>Newsletter / video</option><option>Contest sponsorship</option><option>Affiliate partnership</option></select></div>
  <div><label>Goals</label><textarea name="message"></textarea></div>
  {HP}<button class="btn btn-sun" type="submit">Get media kit</button></form>
</div></section>''', active=None)

# ------------------------------------------------------------------ ABOUT / CONTACT / LEGAL
add("about.html", "About SPU.co — Solar Power Unit",
    "SPU.co helps homeowners plan, price and buy solar panels and home batteries with free tools, honest guides and vetted installer matching.",
    hero("About", "About SPU.co", "SPU stands for Solar Power Unit — the panels, inverter and battery that make a home its own power plant.", '<a href="index.html">Home</a> › About') + '''
<section style="padding-top:12px"><div class="container article">
 <h2>Our mission</h2><p>Make going solar as simple as comparing phone plans: clear numbers, honest trade-offs and no pressure.</p>
 <h2>How we make money</h2><p>SPU.co is free for homeowners. We earn from display advertising (Google AdSense), referral fees from vetted installers when you request quotes, affiliate commissions on some product links, sponsorships and reader donations. None of these change calculator results or guide recommendations.</p>
 <h2>Editorial standards</h2><ul><li>Named assumptions on every calculator</li><li>Primary sources: NREL, EIA, national energy agencies and official program pages</li><li>Incentive pages reviewed regularly with a "last reviewed" date</li><li>Sponsored content always labelled</li></ul>
 <div class="callout">Spotted an error? <a href="contact.html">Tell us</a> — we correct fast and note significant updates.</div>
</div></section>''')

add("contact.html", "Contact SPU.co",
    "Contact SPU.co for questions, partnerships, press, corrections or support.",
    hero("Contact", "Get in touch", "Questions, partnerships, press or corrections — we reply within 1–2 business days.", '<a href="index.html">Home</a> › Contact') + f'''
<section style="padding-top:12px"><div class="container grid g2" style="align-items:start">
 <form class="card form" data-spu-form="Contact" data-success="Thanks for reaching out! We'll reply within 1–2 business days.">
  <div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
  <div><label>Topic</label><select name="topic"><option>General question</option><option>Help with a quote</option><option>Installer partnership</option><option>Advertising / sponsorship</option><option>Press</option><option>Correction</option><option>Domain / website acquisition</option></select></div>
  <div><label>Message</label><textarea name="message" required></textarea></div>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the privacy policy.</label>
  {HP}<button class="btn btn-sun" type="submit">Send message</button></form>
 <div>
  <div class="card"><h3>Prefer email?</h3><p>Click below to open your mail app — our address stays private to protect against spam.</p><a class="btn btn-dark" href="#" data-mail="Inquiry from SPU.co">✉ Email SPU.co</a></div>
  <div class="card mt"><h3>Interested in this domain or website?</h3><p>SPU.co may be available for acquisition or partnership.</p><a class="btn btn-ghost" href="https://web.works/contact" target="_blank" rel="noopener">Contact about the domain →</a></div>
 </div>
</div></section>''')

add("privacy.html", "Privacy Policy | SPU.co", "How SPU.co collects, uses and protects your information.",
    hero("Legal", "Privacy policy", "Last updated: September 2026", '<a href="index.html">Home</a> › Privacy') + '''
<section style="padding-top:12px"><div class="container article">
<h2>What we collect</h2><p>Information you submit in forms (such as name, email, phone, address, ZIP code and answers about your home), plus standard analytics data (pages visited, device, approximate location) when you accept cookies.</p>
<h2>How we use it</h2><ul><li>To answer your request and, if you ask for quotes, to share it with up to three matched installers</li><li>To send newsletters you opted into (unsubscribe anytime)</li><li>To improve our tools and measure performance</li><li>To show ads through Google AdSense</li></ul>
<h2>Advertising & cookies</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to this site and/or other sites. You may opt out of personalised advertising at Google Ads Settings (adssettings.google.com) or www.aboutads.info. You can decline non-essential cookies in our banner.</p>
<h2>Form processing</h2><p>Form submissions are delivered through a secure third-party form relay service. Donations are processed by PayPal; we never see your card details.</p>
<h2>Sharing</h2><p>We do not sell personal information to data brokers. We share lead information only with installers you are matched with, and with service providers who help us operate the site.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR, UK GDPR, CCPA/CPRA, PIPEDA, DPDP Act) you may request access, correction or deletion of your data, or withdraw consent, via our <a href="contact.html">contact page</a>.</p>
<h2>Retention & security</h2><p>We keep lead data only as long as needed for the purposes above and apply reasonable safeguards.</p>
<h2>Children</h2><p>SPU.co is not directed at children under 13.</p>
</div></section>''')

add("terms.html", "Terms of Use & Disclosures | SPU.co", "Terms of use, advertising and affiliate disclosure for SPU.co.",
    hero("Legal", "Terms of use & disclosures", "Last updated: September 2026", '<a href="index.html">Home</a> › Terms') + '''
<section style="padding-top:12px"><div class="container article">
<h2>Information only</h2><p>Calculators and guides provide estimates for general information. They are not financial, tax, legal or engineering advice. Confirm all figures with a qualified installer and official program sources.</p>
<h2 id="disclosure">Advertising & affiliate disclosure</h2><p>SPU.co is supported by advertising (including Google AdSense), installer referral fees, affiliate commissions and sponsorships. When you click some links or request quotes, we may be compensated. Compensation never affects calculator math. Sponsored content is labelled.</p>
<h2>Installer matching</h2><p>Installers are independent businesses. SPU.co is not a party to any contract between you and an installer and does not guarantee their work.</p>
<h2>Contests</h2><p>Contests are governed by the official rules published on the contests page.</p>
<h2>Donations</h2><p>Donations are voluntary, non-refundable and not tax-deductible unless stated otherwise.</p>
<h2>Content</h2><p>All site content © SPU.co. You may link to and quote brief excerpts with attribution.</p>
<h2>Contact</h2><p>Questions? Use our <a href="contact.html">contact page</a>.</p>
</div></section>''')

add("404.html", "Page not found | SPU.co", "This page could not be found.",
    '<section class="hero"><div class="container center"><h1>404 — this page is in the shade</h1><p class="lead-text" style="margin:0 auto 20px">The page you were looking for has moved or never existed.</p><a class="btn btn-sun" href="{R}index.html">Back to home</a> <a class="btn btn-ghost" href="{R}calculator.html">Try the calculator</a></div></section>',
    canonical="404.html")
