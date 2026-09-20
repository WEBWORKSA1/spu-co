"""Shared layout for SPU.co static pages. Run `python3 build/build.py` to regenerate HTML."""

SITE = "https://spu.co"
BRAND = "SPU.co"

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffcf4a"/><stop offset="1" stop-color="#f5a300"/></linearGradient></defs>'
        '<rect x="2" y="2" width="36" height="36" rx="10" fill="#0b1628"/>'
        '<circle cx="20" cy="17" r="6.5" fill="url(#lg)"/>'
        '<g stroke="#ffcf4a" stroke-width="2" stroke-linecap="round"><path d="M20 5.5v2.5M9.5 17H7M33 17h-2.5M12.6 9.6l1.7 1.7M27.4 9.6l-1.7 1.7"/></g>'
        '<path d="M9 30h22l-2.5-5h-17z" fill="#1b64d8"/><path d="M15 25l-1 5M20 25v5M25 25l1 5M10.2 27.5h19.6" stroke="#0b1628" stroke-width="1"/></svg>')

NAV = [
    ("calculator.html", "Calculators"),
    ("get-quotes.html", "Get Quotes"),
    ("incentives.html", "Incentives"),
    ("compare.html", "Compare"),
    ("guides/index.html", "Guides"),
    ("videos.html", "Videos"),
    ("installers.html", "Installers"),
    ("contests.html", "Contests"),
    ("support.html", "Support Us"),
]

FOOTER_COLS = {
    "Tools": [("calculator.html", "Solar savings calculator"), ("calculator.html#battery", "Battery backup sizer"),
              ("incentives.html", "Incentive finder"), ("compare.html", "Battery & panel compare"), ("get-quotes.html", "Free installer quotes")],
    "Learn": [("guides/index.html", "All guides"), ("guides/solar-panel-cost.html", "Solar panel cost"),
              ("guides/home-battery-guide.html", "Home battery guide"), ("guides/solar-scams.html", "Avoid solar scams"), ("videos.html", "Video hub")],
    "Community": [("contests.html", "Contests & prizes"), ("support.html", "Donate / support"), ("careers.html", "Careers & talent"),
                  ("installers.html", "List your company"), ("advertise.html", "Advertise & sponsor")],
    "Company": [("about.html", "About SPU"), ("contact.html", "Contact"), ("privacy.html", "Privacy policy"),
                ("terms.html", "Terms & disclosures"), ("sitemap.xml", "Sitemap")],
}


# 404 can be served at any depth: set <base> to the site root (handles github.io/<repo>/ and custom domains)
CUR = ' aria-current="page"'
BASE404 = ("<script>(function(){var h=location.hostname,p=location.pathname.split('/')[1];"
           "var b=(h.slice(-10)==='github.io'&&p)?'/'+p+'/':'/';document.write('<base href=\"'+b+'\">')})();</script>")


def page(path, title, desc, body, active=None, scripts=(), schema=None, canonical=None):
    depth = path.count("/")
    r = "../" * depth  # relative root prefix so the site works on github.io sub-paths and custom domains
    url = SITE + "/" + (canonical if canonical is not None else ("" if path == "index.html" else path))
    nav = "".join(
        f'<li><a href="{r}{h}"{CUR if active == h else ""}>{t}</a></li>' for h, t in NAV)
    cols = "".join(
        f'<div><h4>{k}</h4><ul>' + "".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in v) + '</ul></div>'
        for k, v in FOOTER_COLS.items())
    js = "".join(f'<script src="{r}assets/js/{s}" defer></script>' for s in scripts)
    ld = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    body = body.replace("{R}", r)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{BASE404 if path == "404.html" else ""}
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b1628">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script>try{{var t=localStorage.getItem('spu-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="domain-bar"><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name</a></div>
<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="logo" href="{r}index.html" aria-label="SPU.co home">{LOGO}<b>SPU<span>.co</span></b></a>
    <ul class="nav-links">{nav}</ul>
    <div class="nav-actions">
      <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
      <a class="btn btn-sun btn-sm" href="{r}get-quotes.html">Free Quotes</a>
      <button class="icon-btn menu-btn" data-menu aria-label="Open menu" aria-expanded="false">☰</button>
    </div>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="{r}index.html" style="color:#fff">{LOGO}<b>SPU<span>.co</span></b></a>
        <p style="margin-top:12px">SPU — Solar Power Unit. Independent tools, guides and vetted installer matching to help every home run on sunshine.</p>
        <form class="news" data-spu-form="Newsletter" data-success="You're in! Watch your inbox for the SPU Sun Report.">
          <label class="sr" for="nl-{depth}">Email</label>
          <input id="nl-{depth}" type="email" name="email" placeholder="Your email" required>
          <input class="hp" name="_honey" tabindex="-1" autocomplete="off">
          <button class="btn btn-sun btn-sm" type="submit">Join</button>
          <div class="form-status"></div>
        </form>
      </div>
      {cols}
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> SPU.co · Estimates are for information only, not financial advice. Some links are affiliate or sponsored — see <a href="{r}terms.html#disclosure">disclosure</a>.</span>
      <span><a href="https://web.works/contact" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name</a></span>
    </div>
  </div>
</footer>
<div class="sticky-cta"><a class="btn btn-sun btn-lg" href="{r}get-quotes.html">☀ Compare free solar quotes</a></div>
<div class="cookie" role="dialog" aria-label="Cookie consent">
  <p style="margin:0 0 12px">We use cookies for analytics and ads (Google AdSense) to keep SPU.co free. <a href="{r}privacy.html">Privacy policy</a></p>
  <div style="display:flex;gap:8px"><button class="btn btn-sun btn-sm" data-consent="yes">Accept</button><button class="btn btn-ghost btn-sm" data-consent="no">Essential only</button></div>
</div>
<script src="{r}assets/js/main.js" defer></script>
{js}
</body>
</html>
"""


def ad(slot="auto", label="Advertisement"):
    return f'<div class="container"><div class="ad-slot" data-slot="{slot}"><span class="ad-label">{label}</span></div></div>'


def hero(kicker, h1, lead, crumbs=None):
    c = f'<div class="breadcrumbs">{crumbs}</div>' if crumbs else ""
    return f'<section class="page-hero"><div class="container">{c}<span class="kicker">{kicker}</span><h1>{h1}</h1><p class="lead-text">{lead}</p></div></section>'


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_schema(items):
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})


def cta_band(r="{R}"):
    return f'''<section><div class="container"><div class="cta-band">
<div><h2>See what solar would cost for your home</h2><p>Compare up to 3 quotes from vetted local installers. Free, no obligation, no spam.</p></div>
<a class="btn btn-sun btn-lg" href="{r}get-quotes.html">Get my free quotes →</a></div></div></section>'''
