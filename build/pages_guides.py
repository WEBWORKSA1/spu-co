from layout import ad, faq, faq_schema
from pages_core import add
import json

AUTHOR = "SPU Editorial Team"
UPDATED = "September 2026"

GUIDES = []


def guide(slug, cat, title, desc, mins, body, faqs):
    GUIDES.append((slug, cat, title, desc))
    art = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
                      "author": {"@type": "Organization", "name": "SPU.co"}, "publisher": {"@type": "Organization", "name": "SPU.co"},
                      "dateModified": "2026-09-20", "mainEntityOfPage": f"https://spu.co/guides/{slug}.html"})
    html = f'''<section class="page-hero"><div class="container article">
<div class="breadcrumbs"><a href="../index.html">Home</a> › <a href="index.html">Guides</a> › {cat}</div>
<span class="kicker">{cat}</span><h1>{title}</h1>
<div class="byline"><span>By {AUTHOR}</span><span>Updated {UPDATED}</span><span>{mins} min read</span><button class="btn btn-ghost btn-sm" data-share>Share</button></div>
<p class="lead-text">{desc}</p></div></section>
<section style="padding-top:8px"><div class="container article">
{body}
<div class="cta-band" style="margin:32px 0"><div><h3 style="color:#fff;margin:0">Get real numbers for your roof</h3><p>Compare up to 3 vetted installer quotes — free.</p></div><a class="btn btn-sun" href="../get-quotes.html">Get quotes →</a></div>
<h2>FAQ</h2>{faq(faqs)}
</div></section>
{ad("guide-bottom")}'''
    add(f"guides/{slug}.html", f"{title} | SPU.co", desc, html, active="guides/index.html",
        schema=json.dumps([json.loads(art), json.loads(faq_schema(faqs))]))


guide("solar-panel-cost", "Costs", "How much do solar panels cost in 2026?",
      "Installed solar is priced per watt. Here is what a typical home system costs, what pushes the price up or down, and how to check a quote.", 7, '''
<div class="toc"><b>In this guide</b><ol><li><a href="#ppw">Price per watt</a></li><li><a href="#size">Cost by system size</a></li><li><a href="#drivers">What drives price</a></li><li><a href="#check">Checking a quote</a></li></ol></div>
<h2 id="ppw">Price per watt is the number that matters</h2>
<p>Compare quotes on <b>installed cost per watt (W)</b>: total price ÷ system size in watts. It normalises quotes of different sizes. Typical residential ranges (before incentives) at time of writing:</p>
<div class="table-wrap"><table><thead><tr><th>Market</th><th>Typical installed cost</th><th>Notes</th></tr></thead><tbody>
<tr><td>United States</td><td>$2.50 – $3.50 / W</td><td>Higher in the Northeast/California; soft costs are ~half of price</td></tr>
<tr><td>Canada</td><td>C$2.50 – C$3.30 / W</td><td>Varies by province and utility rules</td></tr>
<tr><td>United Kingdom</td><td>£1.40 – £1.90 / W</td><td>0% VAT on domestic installs</td></tr>
<tr><td>Australia</td><td>A$0.90 – A$1.30 / W</td><td>After STC discount; among the cheapest in the world</td></tr>
<tr><td>India</td><td>₹50,000 – ₹65,000 / kW</td><td>Before PM Surya Ghar subsidy</td></tr>
</tbody></table></div>
<h2 id="size">Cost by system size (U.S. example at $2.90/W)</h2>
<div class="table-wrap"><table><thead><tr><th>System</th><th>Panels (430 W)</th><th>Gross cost</th><th>Good for bills around</th></tr></thead><tbody>
<tr><td>4 kW</td><td>10</td><td>$11,600</td><td>$80–100/mo</td></tr><tr><td>6 kW</td><td>14</td><td>$17,400</td><td>$120–150/mo</td></tr>
<tr><td>8 kW</td><td>19</td><td>$23,200</td><td>$160–200/mo</td></tr><tr><td>10 kW</td><td>24</td><td>$29,000</td><td>$200–250/mo</td></tr>
<tr><td>12 kW</td><td>28</td><td>$34,800</td><td>$250–300/mo</td></tr></tbody></table></div>
<h2 id="drivers">What pushes price up or down</h2>
<ul><li><b>Equipment tier:</b> premium back-contact panels and microinverters cost more than standard modules with a string inverter.</li><li><b>Roof complexity:</b> multiple planes, tile/slate, steep pitch.</li><li><b>Electrical upgrades:</b> main panel upgrades can add $1,500–4,000.</li><li><b>Batteries:</b> typically adds $9,000–16,000 per ~13 kWh in the U.S.</li><li><b>Installer overhead:</b> national brands often cost more than local specialists.</li></ul>
<h2 id="check">How to sanity-check a quote</h2>
<ol><li>Divide price by watts — is it within your market range?</li><li>Check exact model numbers of panels, inverter, battery.</li><li>Confirm the production estimate (kWh/yr) against our <a href="../calculator.html">calculator</a>.</li><li>Get at least three quotes.</li></ol>
<div class="callout">Rule of thumb: a quote more than 25% above your market's typical price per watt needs a clear reason.</div>''',
      [("What is a good price per watt?", "In the U.S., roughly $2.50–3.50/W installed before incentives in 2026; lower is not always better if equipment or warranty are weaker."),
       ("Do batteries double the cost?", "Often close to it for small systems. A single ~13 kWh battery can cost as much as a 4–5 kW solar array.")])

guide("are-solar-panels-worth-it", "ROI", "Are solar panels worth it? The 5 numbers that decide",
      "Solar pays off when five numbers line up: your electricity rate, sunshine, system cost, incentives and export rules. Here is how to judge each.", 6, '''
<h2>1. Your electricity rate</h2><p>The higher your price per kWh, the faster solar pays back. Above roughly $0.15/kWh (or local equivalent) solar usually makes financial sense; above $0.25/kWh it is compelling.</p>
<h2>2. Peak sun hours</h2><p>Phoenix gets ~6, Seattle ~3.5, London ~2.8, Delhi ~5.5. Output scales directly with this number.</p>
<h2>3. Net installed cost</h2><p>Price per watt after incentives. See our <a href="solar-panel-cost.html">cost guide</a>.</p>
<h2>4. Export rules</h2><p>Full retail net metering is ideal. Where exports earn little (e.g. California NEM 3.0, Netherlands after 2026), sizing to self-consumption and adding a battery matters.</p>
<h2>5. How long you'll stay</h2><p>Payback is commonly 6–12 years; panels last 25–30+. Solar can also add resale value.</p>
<div class="callout"><b>Quick test:</b> plug your bill into the <a href="../calculator.html">SPU calculator</a>. A payback under 10 years is a strong case; over 15 years, look at efficiency upgrades, time-of-use strategies or community solar instead.</div>
<h2>When solar is NOT worth it</h2><ul><li>Heavily shaded roof</li><li>Roof needs replacing within 5 years (re-roof first)</li><li>Very low electricity rates</li><li>Moving within 3–4 years (unless resale value is strong)</li></ul>''',
      [("What is a typical payback period?", "Most grid-tied homes see 6–12 years, depending on rates, sun and incentives."),
       ("Do solar panels increase home value?", "Studies of owned (not leased) systems generally find a resale premium; leased systems can complicate a sale.")])

guide("how-many-solar-panels", "Sizing", "How many solar panels do I need?",
      "A simple formula, worked examples and the factors that change the answer.", 5, '''
<h2>The formula</h2><div class="callout"><b>System kW</b> = yearly kWh ÷ (peak sun hours × 365 × 0.8)<br><b>Panels</b> = system W ÷ panel W</div>
<h2>Worked example</h2><p>A home uses 900 kWh/month = 10,800 kWh/yr. With 4.5 sun hours: 10,800 ÷ (4.5 × 365 × 0.8) = <b>8.2 kW</b>. With 430 W panels: 8,200 ÷ 430 = <b>19 panels</b>, needing about 38 m² (410 ft²) of good roof.</p>
<div class="table-wrap"><table><thead><tr><th>Monthly use</th><th>3.5 sun hrs</th><th>4.5 sun hrs</th><th>5.5 sun hrs</th></tr></thead><tbody>
<tr><td>500 kWh</td><td>14 panels</td><td>11 panels</td><td>9 panels</td></tr><tr><td>900 kWh</td><td>25 panels</td><td>19 panels</td><td>16 panels</td></tr><tr><td>1,300 kWh</td><td>36 panels</td><td>28 panels</td><td>23 panels</td></tr></tbody></table></div>
<h2>Plan for the future</h2><p>An EV adds ~250–350 kWh/month; a heat pump can add 300–800 kWh/month in winter. Size now or leave roof space and inverter headroom.</p>''',
      [("What size panel should I assume?", "Most new residential modules are 400–450 W."), ("Can I have too many panels?", "Yes, if exports earn little. Size to your usage unless net metering pays retail rates.")])

guide("home-battery-guide", "Batteries", "Home battery buyer's guide: backup, savings & sizing",
      "What a home battery really does, how to size one, what it costs and when it pays off.", 8, '''
<h2>kWh vs kW — the two numbers</h2><p><b>Capacity (kWh)</b> is how long it lasts; <b>power (kW)</b> is how much it can run at once. A 13.5 kWh / 5 kW battery runs a 1 kW load for ~12 hours, but cannot start a 7 kW central A/C.</p>
<h2>Three reasons to buy</h2><ol><li><b>Backup</b> during outages (replaces or complements a generator)</li><li><b>Time-of-use savings</b> — store midday solar, use it at expensive evening rates</li><li><b>Poor export rates</b> — keep your solar instead of exporting it cheaply</li></ol>
<h2>Sizing</h2><p>Use the <a href="../calculator.html#battery">battery sizer</a>: essentials (fridge, Wi-Fi, lights, phones) are ~4–6 kWh/day; add A/C, well pump or electric heating and it can reach 20–40 kWh/day.</p>
<h2>Chemistry</h2><p>LiFePO4 (LFP) is now standard for homes: safer and typically rated for 6,000+ cycles.</p>
<h2>Cost</h2><p>U.S. installed prices commonly run ~$1,000–1,300 per usable kWh; Australia's Cheaper Home Batteries program and similar rebates can cut that substantially.</p>
<p><a class="btn btn-sun" href="../compare.html">Compare battery models →</a></p>''',
      [("Can a battery power my whole home?", "Yes with enough capacity and power — often two units for homes with central A/C or electric heat."),
       ("Battery or generator?", "Batteries are silent, need no fuel and pair with solar; generators run indefinitely with fuel. Many homes combine them.")])

guide("solar-financing", "Financing", "Cash vs loan vs lease vs PPA: which saves most?",
      "The four ways to pay for solar compared on lifetime savings, risk and flexibility.", 6, '''
<div class="table-wrap"><table><thead><tr><th>Option</th><th>Upfront</th><th>Who owns it</th><th>Lifetime savings</th><th>Watch out for</th></tr></thead><tbody>
<tr><td><b>Cash</b></td><td>Full price</td><td>You</td><td>Highest</td><td>Opportunity cost of cash</td></tr>
<tr><td><b>Solar loan</b></td><td>$0–low</td><td>You</td><td>High</td><td>Dealer fees hidden in "low APR" loans</td></tr>
<tr><td><b>Lease</b></td><td>$0</td><td>Installer</td><td>Low–medium</td><td>Escalators, home-sale transfer</td></tr>
<tr><td><b>PPA</b></td><td>$0</td><td>Installer</td><td>Low–medium</td><td>Per-kWh price escalators</td></tr></tbody></table></div>
<h2>The dealer-fee trap</h2><p>A "1.99% APR" solar loan often carries a 15–30% dealer fee baked into the system price. Always ask for the <b>cash price</b> and compare.</p>
<h2>When leases make sense</h2><p>Where tax-credit rules now favour third-party ownership, or if you cannot use incentives yourself, a lease/PPA with no or low escalator can still cut bills from day one.</p>''',
      [("Is a solar loan a good idea?", "It can be, if the APR and any dealer fee still leave monthly savings above the payment."), ("Can I sell my house with leased panels?", "Yes, but the buyer must qualify to take over the lease, or you may need to buy it out.")])

guide("solar-scams", "Protection", "Solar scams & red flags: how to read a quote",
      "Pressure tactics, fake 'free solar' offers and inflated quotes — and how to protect yourself.", 5, '''
<h2>Red flags</h2><ul><li>"Free solar" or "government program" door-knocking</li><li>Pressure to sign today for a "limited" price</li><li>No exact equipment model numbers</li><li>Savings claims that assume steep utility price rises</li><li>Promises of incentives you may not qualify for</li><li>Large deposits before permits</li></ul>
<h2>Your checklist</h2><ol><li>Get 3 quotes and compare price per watt</li><li>Verify license, insurance and reviews</li><li>Read the full contract, including loan dealer fees and lease escalators</li><li>Use the cooling-off period to review</li><li>Pay in stages tied to milestones</li></ol>
<div class="callout">Unsure about a quote? Send it to us via the <a href="../contact.html">contact page</a> and our advisors will give a free second opinion.</div>''',
      [("Is 'free solar' real?", "Usually it means a lease or PPA — you pay for the power, not the panels."), ("How long is the cooling-off period?", "It depends on your country/state; in many places it is at least 3 business days for door-to-door sales.")])

cards = "".join(f'<a class="card" data-item data-cat="{c}" href="{s}.html"><span class="tag">{c}</span><h3 style="margin-top:10px">{t}</h3><p>{d}</p></a>' for s, c, t, d in GUIDES)
cats = "".join(f'<option>{c}</option>' for c in dict.fromkeys(c for _, c, _, _ in GUIDES))
add("guides/index.html", "Solar & Home Battery Guides | SPU.co",
    "Independent, data-driven guides on solar panel cost, sizing, batteries, financing, incentives and avoiding scams.",
    f'''<section class="page-hero"><div class="container"><div class="breadcrumbs"><a href="../index.html">Home</a> › Guides</div>
<span class="kicker">Learn</span><h1>Solar & battery guides</h1><p class="lead-text">Clear answers, real numbers, named assumptions. Updated {UPDATED}.</p></div></section>
<section style="padding-top:12px"><div class="container">
<div class="card form" style="margin-bottom:22px"><div class="row"><div><label for="g-q">Search guides</label><input id="g-q" data-filter="#g-list" data-filter-text placeholder="battery, cost, loan…"></div>
<div><label for="g-c">Category</label><select id="g-c" data-filter="#g-list" data-filter-cat><option value="">All</option>{cats}</select></div></div></div>
<div id="g-list" class="grid g3">{cards}</div>
<div class="card mt"><h3>Coming next</h3><p>State & country pages, net metering explained, heat pumps + solar, balcony solar, EV charging with solar, off-grid cabins. <a href="../contact.html">Request a topic</a>.</p></div>
</div></section>{ad("guides-index")}''', active="guides/index.html", scripts=("calc.js",))
