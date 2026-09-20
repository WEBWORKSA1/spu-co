# SPU.co — Phase-wise Build Prompt

**Concept:** SPU = **Solar Power Unit**. SPU.co is a global, independent solar + home-battery decision platform: calculators → incentives → comparisons → guides → video → **installer quote lead generation**.

**Why this idea wins:** Solar/battery is one of the highest-value lead verticals (installers pay roughly $30–$250+ per qualified homeowner lead), AdSense CPCs in energy/home-improvement/finance are high, and calculator tools create repeat, linkable, high-dwell traffic. The same pages feed YouTube, affiliate (portable power stations, panels, EV chargers), sponsorships and donations. A 3-letter .co reads as a brand ("Solar Power Unit") and scales across countries.

Use the prompts below in order. Each phase is independently shippable.

---

## Phase 0 — Guardrails (paste first in every session)
> You are building SPU.co ("Solar Power Unit"), a static website hosted free on GitHub Pages (repo `webworksa1/spu-co`, branch `main`, root folder). Pure HTML/CSS/vanilla JS, no server, no framework, mobile-first, WCAG AA, Core Web Vitals green, light/dark theme.
> Every page must show a top bar: "Contact, if you are interested in this website/domain name" linking to https://web.works/contact.
> The ONLY contact email is the owner's inbox, and it must NEVER appear in any HTML, JS string, text or attribute. Store it encoded (char codes) and decode only at click/submit time. All forms post via FormSubmit AJAX to that inbox; the email button opens mailto via JS.
> Use relative links so the site works on `username.github.io/spu-co/` and on the custom domain.

## Phase 1 — Foundation & design system
> Create `assets/css/style.css` with CSS tokens (sun amber #f5a300, navy #0b1628, leaf green, sky blue), dark mode via `prefers-color-scheme` + `[data-theme]` toggle, Inter/Sora fonts, cards, buttons, forms, tabs, tables, FAQ accordions, ad slots, sticky mobile CTA, cookie banner, reveal animations respecting reduced motion.
> Create a Python generator (`build/layout.py`, `build/build.py`) that wraps every page in a shared head (SEO meta, OG, canonical, JSON-LD), domain bar, sticky header nav, footer (4 link columns + newsletter), cookie banner and scripts. Output static HTML to the repo root plus `sitemap.xml`, `robots.txt`, `ads.txt`, `manifest.json`, `.nojekyll`, `404.html`. Add a GitHub Action that rebuilds and commits the HTML on every push.

## Phase 2 — Core tools (traffic engines)
> Build `calculator.html` with two tabs:
> 1) **Solar savings**: region presets (US, CA, UK, AU, IN, EU, Other) for rate, sun hours, cost/W, incentive %; inputs: bill, rate, sun hours, cost/W, incentive %, offset %, shade. Outputs: kW, panels (430 W), kWh/yr, gross & net cost, year-1 savings, payback, 25-yr net savings (0.5%/yr degradation, 3%/yr rate rise), ROI, new bill, CO₂, roof area, SVG cumulative-savings chart, and a CTA that passes bill/region/kW to the quote funnel.
> 2) **Battery backup**: appliance checklist (watts × hours), days of backup, 90% DoD and efficiency → kWh needed, peak kW, recommended product class and panels to recharge.
> Build `compare.html` (sortable table of home batteries & portable power stations + panel technology table) and `incentives.html` (searchable/filterable country cards with "last reviewed" date and an alert signup form).

## Phase 3 — Lead generation (primary revenue)
> Build `get-quotes.html`: a 10-step, one-question-per-screen funnel with a progress bar and auto-advance: ZIP+country → homeowner → bill slider → interest → shade → credit band → timeline → address/city/property type → first/last/email → phone, contact preference, notes, unchecked TCPA-style consent, newsletter opt-in. Hidden fields: UTM, gclid, referrer, estimated kW. Compute a 0–100 lead score and include consent timestamp, page URL and user agent. Show a thank-you panel with next steps. Add a commercial-solar lead form and trust blocks (vetted, you control contact, no data broker sales). Prefill from `?zip=&bill=&region=&kw=&interest=`.
> Put ZIP boxes and "Get free quotes" CTAs on the homepage, calculators, guides and a sticky mobile button.

## Phase 4 — Content & SEO
> Build `guides/index.html` (searchable) and long-form guides with byline, updated date, TOC, tables, callouts, FAQ + Article/FAQ JSON-LD, in-article quote CTA and ad slots: solar panel cost, are solar panels worth it, how many panels, home battery guide, financing (cash/loan/lease/PPA), solar scams. Plan next: per-state/per-country pages, net metering, heat pump + solar, balcony solar, EV + solar, off-grid.

## Phase 5 — Monetization layer
> AdSense: `.ad-slot` placeholders on every major page; load `adsbygoogle.js` and inject `<ins>` only when `adsenseClient` is configured AND the visitor accepts cookies. GA4 the same way. Track events: funnel_step, generate_lead, form_submit, video_play, donate_click.
> `videos.html`: lite YouTube embeds (thumbnail → iframe on click) from `data-yt` IDs, channel subscribe CTA, topic cards, creator submission / sponsorship form.
> `advertise.html`: pay-per-lead, featured installer, sponsored guides, calculator sponsor, newsletter/video, contest sponsor + media-kit form.
> `installers.html`: vetting checklist, 10 questions to ask, installer partner application (service area, capacity, certifications).

## Phase 6 — Community, donations, talent
> `support.html`: amount picker ($5–$250 + custom), purpose selector (operations, promotions & marketing, hiring talent, contests & prizes), PayPal donate (address built at click time, or hosted button ID), monthly tiers, fund-allocation bars, pledge / in-kind form, share button.
> `contests.html`: current contest with live countdown, prize tiers, referral race, idea prize, student challenge, entry form with rules acceptance, official rules summary, sponsor-a-prize CTA.
> `careers.html`: remote roles (writer, video editor, energy advisor, partnerships, developer, community lead) + application / talent-network form.
> `about.html`, `contact.html` (form + hidden-email button + domain inquiry card), `privacy.html` (AdSense cookie language, GDPR/CCPA/DPDP rights), `terms.html` (#disclosure for ads/affiliates).

## Phase 7 — QA & launch
> Verify: no occurrence of the email in any file (`grep`), every page has the domain bar, no broken relative links, no JS errors, no horizontal scroll at 390 px, Lighthouse ≥ 90. Push to `main`, enable GitHub Pages (main / root), then add custom domain `spu.co` with GitHub's A records and enforce HTTPS. Submit sitemap to Google Search Console, apply for AdSense, activate FormSubmit via its first email.

## Phase 8 — Scale (post-launch)
> Programmatic state/city/utility pages from a JSON dataset; PVWatts API for exact production; installer directory with reviews; lead routing to buyers (webhook/CRM); A/B tests on funnel step order; newsletter automation; multilingual (Hindi, Spanish, French); YouTube Shorts from each guide; affiliate deal pages; annual "SPU Solar Price Index" report for backlinks and press.
