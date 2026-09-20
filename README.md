# SPU.co — Solar Power Unit

Static, dependency-free website: solar & battery calculators, multi-step lead funnel, incentives, comparisons, guides, video hub, installer network, contests, donations, careers and advertising — monetized via Google AdSense, YouTube, lead sales, affiliates, sponsorships and donations.

Hosted free on **GitHub Pages** (plain HTML/CSS/JS). HTML is generated from `build/*.py`; the GitHub Action in `.github/workflows/build.yml` rebuilds and commits the HTML automatically on every push.

## Go-live checklist
1. **AdSense** – after approval, set `adsenseClient` in `assets/js/main.js` and replace the pub ID in `ads.txt`. Ad slots load only after cookie consent.
2. **GA4** – set `ga4Id` in `assets/js/main.js`.
3. **YouTube** – set `youtubeChannel`; paste video IDs into `data-yt=""` slots (`build/pages_more.py` → videos).
4. **Forms** – all forms post to the protected inbox via FormSubmit. The **first submission triggers a one-time activation email** — click it. Then set `formsubmitAlias` to the random string FormSubmit gives you.
5. **Donations** – works immediately through PayPal; optionally create a PayPal hosted donate button and set `paypalHostedButtonId`.
6. **Custom domain** – in repo *Settings → Pages* add `spu.co`, then at the registrar: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and `www` CNAME → `webworksa1.github.io`. Enable *Enforce HTTPS*.

The contact email never appears in any file: it is stored encoded in `main.js` and decoded only when a form is submitted or the email button is clicked.

## Editing
Pages are generated from `build/*.py` (shared header, domain bar, footer). Edit there, then run:
```
python3 build/build.py
```
(or just push — the Action rebuilds). Add a guide: copy a `guide(...)` block in `build/pages_guides.py`.

See `PROMPT.md` (phase-wise build prompt) and `RESEARCH.md` (competitor analysis).
