# -*- coding: utf-8 -*-
"""
site_common.py -- shared layout pieces for every page (head, nav, footer,
age gate, back-to-top, base CSS). All page builders import from here so the
whole site stays consistent. Values come from brand_config.py -- edit facts
and colors THERE, not in this file.
"""
import os, sys, re, base64, mimetypes, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_config as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the client folder

def slug():
    s = re.sub(r"[^a-z0-9]+", "_", C.BUSINESS_NAME.lower()).strip("_")
    return s or "site"

def _hex_to_rgb(h):
    """'#e8ab52' -> '232,171,82', for building rgba(var(--x-rgb),alpha) glows.
    Mirrors the helper in SITE/build-scripts/site_common.py (the mS marketing
    site's own build) -- kept in sync so both sites can use the same
    radial-gradient glow pattern (see .logo-divider below)."""
    h = h.lstrip("#")
    return f"{int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)}"

def css_root():
    k = C.COLORS
    return f""":root{{
  --primary:{k['primary']}; --primary-bright:{k['primary_bright']}; --glow:{k['glow']};
  --accent:{k['accent']}; --accent-deep:{k['accent_deep']}; --cream:{k['cream']};
  --cream-muted:{k['cream_muted']}; --bg-deep:{k['bg_deep']}; --panel:{k['panel']};
  --ink:{k['ink']}; --on-accent:{k.get('on_accent', k['bg_deep'])};
  --primary-deep:{k.get('primary_deep', k['bg_deep'])};
  --glow-rgb:{_hex_to_rgb(k['glow'])};
  --footer-glow-rgb:{_hex_to_rgb(k.get(getattr(C, "FOOTER_GLOW_COLOR", "glow"), k['glow']))};
  --footer-glow-strength:{getattr(C, "FOOTER_GLOW_STRENGTH", 0.38)};
  --font-head:'{C.FONT_HEADING}',Georgia,serif;
  --font-body:'{C.FONT_BODY}',system-ui,Arial,sans-serif;
  --font-nav:'{getattr(C, "NAV_WORDMARK_FONT", "") or C.FONT_HEADING}',Georgia,serif;
  --font-nav-weight:{700 if getattr(C, "NAV_WORDMARK_BOLD", True) else 400};
  --story-mobile-pos:{getattr(C, "STORY_IMG_MOBILE_POSITION", "center")};
}}"""


def base_css():
    return css_root() + """
*{box-sizing:border-box;margin:0;padding:0}
/* Minimalist scrollbars -- matches the thin, borderless-thumb treatment
   applied to the Client Style portal's own UI (2026-09-13). Without this,
   every client site rendered its browser's default scrollbar, which is what
   showed up as the "missed" scrollbar inside the portal's Content & Preview
   live-preview iframe -- that iframe shows THIS site's own CSS, not the
   portal's, so the portal-side fix alone never reached it. */
*{scrollbar-width:thin;scrollbar-color:var(--cream-muted) transparent}
*::-webkit-scrollbar{width:8px;height:8px}
*::-webkit-scrollbar-track{background:transparent}
*::-webkit-scrollbar-thumb{background:var(--cream-muted);border-radius:8px;border:none}
*::-webkit-scrollbar-thumb:hover{background:var(--cream)}
html{scroll-behavior:smooth}
section[id]{scroll-margin-top:92px}
body{font-family:var(--font-body);color:var(--cream);background:var(--bg-deep);line-height:1.6}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
h1,h2,h3{font-family:var(--font-head);line-height:1.12;font-weight:600}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
.accent{color:var(--accent)}
.grad{background:linear-gradient(90deg,var(--primary-bright),var(--glow));-webkit-background-clip:text;background-clip:text;color:transparent}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:7px;font-weight:700;font-family:var(--font-body);cursor:pointer;border:0;transition:background .25s ease,color .25s ease,border-color .25s ease,transform .2s ease,box-shadow .25s ease;font-size:15px}
.btn-primary{background:var(--accent);color:var(--on-accent)}
.btn-primary:hover{background:var(--accent-deep);color:var(--on-accent);transform:translateY(-2px);box-shadow:0 10px 24px rgba(0,0,0,.45)}
.btn-ghost{background:transparent;border:1.5px solid var(--cream-muted);color:var(--cream)}
.btn-ghost:hover{background:rgba(255,255,255,.12);border-color:var(--cream);color:var(--cream);transform:translateY(-2px)}
.nav-cta .btn{padding:10px 20px;font-size:13px;border-radius:7px;letter-spacing:.5px}
/* nav */
.nav{position:sticky;top:0;z-index:50;background:rgba(11,11,12,.92);backdrop-filter:blur(8px);border-bottom:1px solid rgba(255,255,255,.08);padding:18px 0}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:18px}
.brand{font-family:var(--font-head);font-weight:700;font-size:22px;color:var(--cream);display:flex;align-items:center;gap:10px}
.brand img{height:56px;width:auto}
/* Add-on: nav wordmark can use its own font (NAV_WORDMARK_FONT in
   brand_config.py) to match a client's actual logo lettering, distinct from
   the site's --font-head used everywhere else. Falls back to --font-head
   (i.e. no visual change) when unset. NAV_WORDMARK_BOLD (default True, so
   every other client is unaffected) lets a client drop the default bold too. */
.brand span{font-family:var(--font-nav);font-weight:var(--font-nav-weight)}
.nav-links{display:flex;gap:32px;align-items:center}
.nav-links a{font-weight:500;font-size:14px;letter-spacing:.5px;color:var(--cream-muted)}
.nav-links a:hover{color:var(--cream)}
.nav-cta{display:flex;gap:10px;align-items:center}
.hamb{display:none;margin-left:auto;background:none;border:0;color:var(--cream);font-size:26px;cursor:pointer}
.mobile-menu{display:none;flex-direction:column;align-items:center;text-align:center;background:var(--panel);padding:16px 22px;gap:14px}
.mobile-menu.open{display:flex}
.mobile-menu a{text-transform:uppercase;letter-spacing:.5px}
.mobile-order-btn{background:var(--accent)!important;color:var(--on-accent)!important;font-weight:700;text-align:center;padding:12px;border-radius:7px;width:100%}
.mobile-call-btn{background:transparent!important;color:var(--cream)!important;font-weight:700;text-align:center;border:1px solid rgba(255,255,255,.25);padding:12px;border-radius:7px;width:100%}
/* sections */
/* longhand on purpose: when a page combines class="sec wrap" on one element
   (story/find-us/catering), a shorthand `padding:70px 0` here would win the
   whole padding property over .wrap's `padding:0 32px` (same specificity,
   later in source) and silently zero out the side padding. Longhand only
   touches top/bottom, so .wrap's left/right survives untouched either way. */
.sec{padding-top:70px;padding-bottom:70px}
.sec-tag{color:var(--accent);font-weight:700;letter-spacing:.14em;font-size:13px;text-transform:uppercase}
.sec h2{font-size:32px;margin:8px 0 14px}
.split h2{font-size:30px}
.sec-head{text-align:center}
.sec-head .sec-tag{display:block;margin-bottom:10px}
.sec-head h2{margin-bottom:44px}
.lead{color:var(--cream-muted);font-size:17px;max-width:640px}
.badge-pill{display:inline-block;background:var(--accent);color:var(--on-accent);font-size:12px;font-weight:700;padding:6px 14px;border-radius:999px;letter-spacing:.5px;margin-bottom:22px}
/* hero (Fat Tony's frame: photo left flex .9, text right flex 1.1, gap 56) */
.hero{background:radial-gradient(ellipse at 70% 30%,var(--primary) 0%,var(--primary-bright) 55%,var(--primary-deep) 100%);padding:80px 0 70px}
.hero .wrap{display:flex;align-items:center;gap:56px}
.hero-text{flex:1.1}
.hero-photo{flex:0.9;display:flex;justify-content:center}
.hero-photo-inner{position:relative;display:inline-block}
.hero-frame{position:relative;width:340px;max-width:calc(100vw - 64px);border-radius:18px;overflow:hidden;box-shadow:0 24px 50px rgba(0,0,0,.55);border:3px solid rgba(255,255,255,.18);aspect-ratio:1/1}
.hero-frame img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0;opacity:0;animation:heroFade var(--fadedur,0s) infinite}
.hero-frame img.single{opacity:1;position:relative;animation:none}
.hero-frame img.contain{object-fit:contain;background:var(--bg-deep)}
.hero-logo{position:absolute;bottom:-33px;right:-33px;width:96px;height:auto;z-index:2;filter:drop-shadow(0 8px 16px rgba(0,0,0,.5))}
/* heroFade keyframe is injected per slide-count by build_homepage.py */
.hero h1{font-size:clamp(30px,5vw,48px);line-height:1.2;margin-bottom:18px}
.hero .lead{max-width:440px;margin-bottom:30px}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap}
/* trust (Fat Tony's two-line stat blocks, spread evenly) */
.trust{background:var(--bg-deep);padding:26px 0;border-top:1px solid rgba(255,255,255,.06);border-bottom:1px solid rgba(255,255,255,.06)}
#favorites{background:var(--panel)}
.trust .wrap{display:flex;justify-content:space-around;text-align:center;flex-wrap:wrap;gap:20px}
.trust-item .num{font-size:15px;font-weight:700;color:var(--cream)}
.trust-item .lbl{font-size:12px;color:var(--cream-muted);margin-top:2px}
/* cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:var(--panel);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:18px}
.card .ic{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--primary-bright),var(--glow));color:var(--bg-deep);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;font-family:var(--font-head);margin-bottom:14px}
/* Add-on: optional photo on a FEATURES card (favorites() fallback branch) --
   opt-in per feature via a 4th tuple element; replaces the .ic letter box
   with a real photo when set, every other client's plain icon cards unaffected. */
.card .img{aspect-ratio:1/1;width:100%;border-radius:8px;overflow:hidden;margin-bottom:14px}
.card .img img{width:100%;height:100%;object-fit:cover;display:block}
.card h3{font-size:20px;margin-bottom:8px}
.card p{color:var(--cream-muted);font-size:15px}
/* photo cards (Fat Tony's favorites: 4-up photo grid) */
.photo-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.photo-card{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:18px}
.photo-card .img{height:130px;border-radius:8px;margin-bottom:14px;overflow:hidden}
.photo-card .img img{width:100%;height:100%;object-fit:cover;display:block}
.photo-card h3{font-size:16px;margin-bottom:6px}
.photo-card p{color:var(--cream-muted);font-size:13px;line-height:1.5}
.photo-card .price{color:var(--accent);font-weight:700}
.sec-note{text-align:center;font-size:13px;color:var(--cream-muted);margin-top:28px;max-width:560px;margin-left:auto;margin-right:auto;line-height:1.6}
.sec-note .hl{font-family:var(--font-head);font-weight:700;color:var(--cream)}
/* specials */
.special{background:linear-gradient(135deg,var(--primary),var(--bg-deep));border:1px solid var(--glow);border-radius:12px;padding:34px;text-align:center;max-width:720px;margin:0 auto}
.special .tag{display:inline-block;background:var(--accent);color:var(--on-accent);font-weight:700;font-size:12px;letter-spacing:.1em;padding:5px 12px;border-radius:20px;margin-bottom:12px}
.special h3{font-size:28px;margin-bottom:10px}
.special p{color:var(--cream);opacity:.9;margin-bottom:18px}
/* specials grid (Fat Tony's multi-special: up to 3 cards) */
.specials-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.special-card{background:var(--panel);border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.1)}
.special-card .img{height:280px;overflow:hidden;background:var(--bg-deep);display:flex;align-items:flex-start;justify-content:center;padding-top:12px}
.special-card .img img{max-width:92%;max-height:96%;width:auto;height:auto;object-fit:contain;display:block}
.special-card .body{padding:22px 22px 26px;text-align:center}
.special-card .tag{font-size:12px;color:var(--accent);font-weight:700;letter-spacing:1px;margin-bottom:10px}
.special-card h3{font-size:20px;margin-bottom:10px}
.special-card p{font-size:13px;color:var(--cream-muted);line-height:1.6}
/* story + find us */
.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.split.find{gap:40px}
.map{border-radius:12px;overflow:hidden;height:320px;border:1px solid rgba(255,255,255,.1)}
.map iframe{width:100%;height:100%;border:0;display:block}
/* story with photo (Fat Tony's pattern) */
.story-flex{display:flex;align-items:center;gap:56px}
.story-flex .story-text{flex:1}
.story-img{flex:1;height:300px;border-radius:12px;overflow:hidden}
.story-img img{width:100%;height:100%;object-fit:cover;display:block}
/* cta band */
.cta-band{background:linear-gradient(135deg,var(--primary),var(--primary-bright));text-align:center;padding:60px 32px}
.cta-band h2{font-size:clamp(24px,4vw,38px);color:var(--cream);margin-bottom:10px}
.cta-band p{color:var(--cream);opacity:.9;margin-bottom:22px}
.cta-band .wrap{display:flex;align-items:center;justify-content:center;gap:36px}
.cta-plaque{flex:0 0 auto}
.cta-plaque img{width:120px;filter:drop-shadow(0 12px 22px rgba(0,0,0,.5))}
.cta-band .center{flex:0 1 560px}
.cta-buttons{display:flex;gap:16px;flex-wrap:wrap;justify-content:center}
/* footer (Fat Tony's pattern: big logo divider, then simple social footer).
   Background updated 2026-08-19 to match the radial-glow-behind-the-logo
   treatment used on maintain.style itself (its own .logo-divider/.hero use
   the identical rgba(var(--x-rgb),.38) ellipse-glow-on-dark pattern) -- a
   soft light source from above/behind the logo instead of a flat panel
   color. Uses --glow (the per-client "highlights/subtle glow" token) rather
   than --primary so the wash stays subtle regardless of how saturated a
   given client's primary color is. */
.logo-divider{background:radial-gradient(ellipse 1100px 380px at 50% -40px,rgba(var(--footer-glow-rgb),var(--footer-glow-strength)) 0%,rgba(var(--footer-glow-rgb),0) 75%) var(--bg-deep);padding:50px 0 60px;text-align:center;border-top:1px solid rgba(255,255,255,.06)}
.logo-divider img{width:300px;max-width:60vw;height:auto;margin:0 auto}
/* 2026-09-27: the glow is a STANDARD part of every footer (George). With no
   logo image yet, the divider still renders -- the business name stands in
   as a wordmark so the glow is never skipped. */
.logo-divider-name{font-family:var(--font-head);font-weight:700;font-size:clamp(30px,5vw,48px);letter-spacing:.04em;color:var(--cream);text-transform:uppercase;line-height:1.1;text-shadow:0 2px 18px rgba(var(--footer-glow-rgb),.35)}
.logo-divider img + .logo-divider-name{font-size:22px;margin-top:18px;text-shadow:none}
/* 2026-10-04: with no logo image the divider is only as tall as the wordmark (~160px), but the glow is a
   380px-tall ellipse that fades out by ~245px -- so it was cut off with a hard edge instead of fading into
   the footer. Give the wordmark divider the same height a logo gives it so the spotlight fades out fully. */
.logo-divider-wordmark{min-height:290px;display:flex;align-items:center;justify-content:center;box-sizing:border-box}
.foot{background:var(--bg-deep);padding:44px 0 30px;text-align:center}
.foot h4{font-family:var(--font-head);font-size:17px;letter-spacing:.5px;margin-bottom:18px;color:var(--cream);text-transform:uppercase}
.foot-social{display:flex;justify-content:center;gap:24px;margin-bottom:16px}
.social-icon{display:flex;align-items:center;justify-content:center;width:64px;height:64px;color:var(--cream-muted);transition:color .2s ease,transform .2s ease}
.social-icon:hover{color:var(--cream);transform:translateY(-2px)}
.social-icon svg{width:40px;height:40px}
.foot a{color:var(--cream-muted);font-size:15px;display:block;margin-bottom:8px}
.foot a:hover{color:var(--glow)}
.foot-handle{color:var(--accent);font-weight:700;font-size:14px}
.compliance{margin:26px auto 0;max-width:600px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)}
.compliance p{font-size:12px;opacity:.55;line-height:1.5}
.copyright{margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.08);font-size:12px;color:var(--cream-muted);opacity:.7;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.copyright .maintain-credit a{display:inline;margin-bottom:0;color:var(--accent);font-weight:600;opacity:1}
/* back to top (Fat Tony's pattern: bare brand icon, no circle) */
.totop{position:fixed;bottom:28px;right:28px;width:54px;height:54px;background:none;border:0;cursor:pointer;padding:0;opacity:0;pointer-events:none;transform:translateY(16px) rotate(-15deg);transition:opacity .3s ease,transform .3s ease;z-index:999;filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}
.totop img{width:100%;height:100%;object-fit:contain}
.totop.show{opacity:1;pointer-events:auto;transform:translateY(0) rotate(0deg)}
.totop.show:hover{transform:translateY(-3px) rotate(12deg) scale(1.12);filter:drop-shadow(0 8px 16px rgba(0,0,0,.6))}
.totop.noicon{width:48px;height:48px;border-radius:50%;background:var(--accent);color:var(--on-accent);font-size:22px;transform:translateY(16px);filter:none;box-shadow:0 6px 18px rgba(0,0,0,.35)}
.totop.noicon.show{transform:translateY(0)}
.totop.noicon.show:hover{transform:translateY(-3px) scale(1.1)}
/* age gate */
.agegate{position:fixed;inset:0;z-index:9999;background:rgba(11,11,12,.97);display:flex;align-items:center;justify-content:center;padding:22px}
.agegate.hide{display:none}
.agebox{background:var(--panel);border:1px solid var(--glow);border-radius:18px;max-width:420px;text-align:center;padding:38px 30px}
.agebox h2{font-size:26px;margin-bottom:12px}
.agebox p{color:var(--cream-muted);margin-bottom:22px;font-size:15px}
.agebox .btn{margin:0 6px}
/* responsive */
@media(max-width:900px){
 .hero .wrap{flex-direction:column;gap:36px;text-align:center}
 .hero-text{flex:none;width:100%}
 .hero .lead{margin-left:auto;margin-right:auto}
 .hero-btns{justify-content:center}
 .hero-photo{flex:none;width:100%;order:-1}
 .hero h1{font-size:34px}
 .sec h2,.split h2{font-size:26px}
 .cards{grid-template-columns:1fr}.split{grid-template-columns:1fr}
 .photo-cards{grid-template-columns:repeat(2,1fr)}
 .specials-grid{grid-template-columns:1fr;max-width:440px;margin:0 auto}
 .story-flex{flex-direction:column}.story-img{flex:none;width:100%;height:310px}
 .story-img img{object-position:var(--story-mobile-pos)}
 .cta-band .wrap{flex-direction:column;gap:24px}
 .cta-plaque img{width:90px}
 .cta-band .center{flex:none;width:100%}
 .foot-grid{grid-template-columns:1fr}.nav-links,.nav-cta{display:none}.hamb{display:block}
 .hero-logo{width:76px;bottom:-22px;right:-8px}
}
@media(max-width:560px){
 .photo-cards{grid-template-columns:1fr}
}
/* lang toggle -- keep top:100px (unchanged at both breakpoints) and
   right:20px/16px-mobile in sync across every site (mS, FT, Simon's, and
   any future client) so the button lands in the same spot everywhere.
   Do not tune this per client. */
.lang-toggle{position:fixed;top:100px;right:20px;background:rgba(11,11,12,.8);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.2);color:var(--cream);font-size:11px;font-weight:700;letter-spacing:.06em;padding:5px 12px;border-radius:999px;cursor:pointer;font-family:var(--font-body);z-index:60;box-shadow:0 4px 12px rgba(0,0,0,.35);transition:background .2s ease}
.lang-toggle:hover{background:rgba(11,11,12,.95)}
@media(max-width:900px){.lang-toggle{top:100px;right:16px}}
/* Add-on: Hero 4 - stacked photo collage (opt-in via HERO_STYLE="collage" in
   brand_config.py; approved by George 2026-08-03 for Desert Inn, ported from
   Template-Scaffold/demos/hero_scroll_demos.html #hero-4). Sits inside the
   existing .hero-photo/.hero-photo-inner wrapper so hero layout/logo-overhang
   plumbing is reused as-is -- classic single-frame hero is still the default
   for every other client. */
.hero-collage{display:flex;justify-content:center;gap:0}
.hero-collage .cimg{width:180px;height:180px;border:6px solid var(--cream);border-radius:9px;overflow:hidden;box-shadow:0 14px 30px rgba(0,0,0,.5);cursor:pointer;transition:transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .35s,border-radius .35s}
.hero-collage .cimg img{width:100%;height:100%;object-fit:cover;display:block}
/* Each photo keeps its own static tilt/offset at rest; the :hover rule below
   re-states that same rotate/translate and appends scale(1.2) so the whole
   FRAME grows on mouse hover (border, shadow and all -- not just the photo
   content inside a fixed-size box). z-index bumps on hover so the enlarged
   card pops above its overlapping neighbors instead of hiding under them. */
.hero-collage .cimg:nth-child(1){transform:rotate(-6deg) translateX(20px) scale(1);z-index:1}
.hero-collage .cimg:nth-child(2){transform:translateY(-10px) scale(1);z-index:2}
.hero-collage .cimg:nth-child(3){transform:rotate(6deg) translateX(-20px) scale(1);z-index:1}
.hero-collage .cimg:hover{z-index:5;border-radius:14px;box-shadow:0 22px 44px rgba(0,0,0,.65)}
.hero-collage .cimg:nth-child(1):hover{transform:rotate(-6deg) translateX(20px) scale(1.2)}
.hero-collage .cimg:nth-child(2):hover{transform:translateY(-10px) scale(1.2)}
.hero-collage .cimg:nth-child(3):hover{transform:rotate(6deg) translateX(-20px) scale(1.2)}
@media(max-width:900px){.hero-collage .cimg{width:120px;height:120px}}
/* Add-on: Hero 2 - full-bleed background photo, centered overlay copy (opt-in
   via HERO_STYLE="fullbleed" in a client's config.py; ported from
   Template-Scaffold/demos/hero_scroll_demos.html #hero-2, 2026-09-13). Every
   other client's classic/collage/diagonal/parallax hero is unaffected. */
.hero.hero-fullbleed{background:none;padding:0;min-height:560px;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;overflow:hidden}
.hero-fb-bg{position:absolute;inset:0;background-size:cover;background-position:center}
.hero-fb-scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,14,19,.35),rgba(10,14,19,.85))}
.hero-fb-copy{position:relative;z-index:2;max-width:640px;margin:0 auto;padding:70px 32px}
.hero-fullbleed .hero-logo{position:static;filter:drop-shadow(0 8px 16px rgba(0,0,0,.5));width:88px;margin:0 auto 18px;display:block}
.hero-fullbleed .lead{margin-left:auto;margin-right:auto}
.hero-fullbleed .hero-btns{justify-content:center}
@media(max-width:900px){.hero-fullbleed{min-height:460px}.hero-fb-copy{padding:50px 24px}}
/* Add-on: Hero 3 - diagonal color-block split, angled clip-path panel instead
   of the classic straight column (opt-in via HERO_STYLE="diagonal"; ported
   from Template-Scaffold/demos/hero_scroll_demos.html #hero-3, 2026-09-13). */
.hero.hero-diagonal{padding:0;min-height:520px;display:flex;align-items:stretch;background:var(--bg-deep)}
.hero-diag-panel{width:56%;background:var(--primary-deep);display:flex;align-items:center;padding:70px 6% 70px 48px;clip-path:polygon(0 0,100% 0,86% 100%,0 100%)}
.hero-diag-inner{max-width:460px}
.hero-diag-photo{flex:1;position:relative;background-size:cover;background-position:center;display:flex;align-items:flex-end;justify-content:flex-end;padding:20px}
.hero-diagonal .hero-logo{position:static;filter:drop-shadow(0 8px 16px rgba(0,0,0,.5));width:80px}
.hero-diagonal .lead{max-width:380px}
@media(max-width:900px){.hero.hero-diagonal{flex-direction:column;min-height:0}.hero-diag-panel{width:100%;clip-path:none;padding:44px 24px 36px;text-align:center}.hero-diag-inner{max-width:none;margin:0 auto}.hero-diag-photo{height:240px}}
/* Add-on: Hero 5 - layered parallax background, drifts slower than the page
   on scroll (opt-in via HERO_STYLE="parallax"; ported from
   Template-Scaffold/demos/hero_scroll_demos.html #hero-5, 2026-09-13).
   Includes its own scroll listener in build_homepage.py, scoped to
   #heroParallax -- no effect on any other client's hero. */
.hero.hero-parallax{background:none;padding:0;min-height:560px;position:relative;overflow:hidden;display:flex;align-items:flex-end}
.hero-px-back{position:absolute;inset:-20% 0;background:linear-gradient(160deg,var(--primary-deep),var(--primary));will-change:transform}
.hero-px-mid{position:absolute;inset:10% -5% -5% -5%;opacity:.5;will-change:transform;background-size:cover;background-position:center}
.hero-px-scrim{position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,14,19,.92),transparent 60%)}
.hero-px-copy{position:relative;z-index:3;padding:60px 32px 50px;max-width:640px}
.hero-parallax .hero-logo{position:static;filter:drop-shadow(0 8px 16px rgba(0,0,0,.5));width:80px;margin-bottom:14px}
@media(max-width:900px){.hero.hero-parallax{min-height:460px}}
/* Add-on: Scroll 4 - horizontal scroll-snap gallery (opt-in via EVENTS_SNAP
   list in brand_config.py; ported from #scroll-4 in the same demo file).
   Good for weekly specials/recurring events -- a sports bar's game nights,
   trivia, taco night, etc. */
/* Full-bleed: breaks out of .wrap's 1180px cap so the row runs edge-to-edge on
   desktop (a horizontal-scroll gallery reads as intentional/roomy that way,
   not squeezed into the same column as the rest of the page). Left/right
   padding is calculated to match .wrap's own responsive inset, so the first
   card still lines up under the section heading above it. Markup: the
   .snap-row div must be a sibling of (not nested inside) .wrap for this to
   work -- see events_snap() in build_homepage.py. */
.snap-row{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 max(32px,calc((100vw - 1180px)/2 + 32px)) 10px;-webkit-overflow-scrolling:touch;width:100vw;position:relative;left:50%;margin-left:-50vw}
.snap-row .card{scroll-snap-align:start;flex:1 1 220px;min-width:220px;background:var(--panel);border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08)}
.snap-row .card .ph{height:150px;overflow:hidden;background:var(--bg-deep)}
.snap-row .card .ph img{width:100%;height:100%;object-fit:cover;display:block}
.snap-row .card .body{padding:16px}
.snap-row .card h4{font-family:var(--font-head);font-size:16px;color:var(--cream);margin-bottom:4px}
.snap-row .card p{color:var(--cream-muted);font-size:13px}
/* Mobile: cancel the full-bleed breakout entirely and stack single-column,
   matching how every other card grid on the site (.cards/.photo-cards/
   .specials-grid) collapses at this breakpoint -- no horizontal scroll on
   phones. This MUST be declared after the base .snap-row rule above (not in
   the shared responsive block near the top of this file) so it wins the
   cascade at equal specificity -- media-scoping does not add specificity,
   only source order does, so an override placed earlier in the file loses to
   an unconditional rule declared later, even when its condition is true. */
@media(max-width:900px){.snap-row{display:grid;grid-template-columns:1fr;max-width:440px;margin:0 auto;overflow-x:visible;scroll-snap-type:none;width:auto;position:static;left:auto;padding:0 32px}}
/* Add-on: "coming soon" placeholder for an EVENTS_SNAP card with no photo yet
   (img=None in brand_config.py) -- styled like an actual promo/ad graphic for
   the special (corner ribbon + big price badge + oversized watermark icon),
   in the client's own palette, not a bare "missing image" box. Swap in a real
   photo later by setting img normally -- this only shows until then. */
.snap-row .card .ph.ph-placeholder{background:linear-gradient(135deg,var(--primary) 0%,var(--primary-bright) 100%);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.snap-row .card .ph-icon-bg{position:absolute;font-size:120px;line-height:1;opacity:.16;transform:rotate(-12deg);right:-14px;bottom:-24px;pointer-events:none}
.snap-row .card .ph-ribbon{position:absolute;top:16px;left:-38px;background:var(--glow);color:var(--bg-deep);font-size:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:4px 44px;transform:rotate(-45deg);box-shadow:0 4px 10px rgba(0,0,0,.35);z-index:1}
.snap-row .card .ph-badge{position:relative;z-index:1;background:var(--accent);color:var(--on-accent);width:96px;height:96px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-6deg);box-shadow:0 12px 26px rgba(0,0,0,.5);border:3px solid var(--cream);text-align:center;padding:4px}
.snap-row .card .ph-badge .amt{font-family:var(--font-head);font-size:19px;font-weight:700;line-height:1.05}
.snap-row .card .ph-badge .lbl{font-size:8px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;margin-top:3px;opacity:.9}
.snap-row .card .ph-tag{position:absolute;bottom:8px;right:10px;background:rgba(0,0,0,.5);color:var(--cream);font-size:9px;font-weight:600;letter-spacing:.03em;padding:3px 9px;border-radius:999px;z-index:1}
"""


import base64, mimetypes

def embed_img(value, inline=False):
    """Return a usable img src. http(s)/data URLs pass through unchanged.
    Local files are COPIED into the deployable site/assets/ folder and
    returned as a relative "assets/<name>" URL (2026-09-27, ported from Fat
    Tony's): every page shares one cached copy of each image instead of
    re-embedding it as base64 -- base64 pages balloon to several MB (Bend
    Grub's homepage was 8 MB) and can't be edited safely by Client Style.
    inline=True keeps the old self-contained data: URI for the rare page
    that needs it (e.g. an email template). A missing file falls back to its
    raw string so a typo is obvious instead of silently swallowed."""
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://") or value.startswith("data:"):
        return value
    path = value if os.path.isabs(value) else os.path.join(ROOT, value)
    if not os.path.exists(path):
        return value  # not found yet -- leave the path so it's obvious to fix
    if inline:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f"data:{mime};base64,{b64}"
    basename = os.path.basename(path)
    site_assets_dir = os.path.join(ROOT, "site", "assets")
    os.makedirs(site_assets_dir, exist_ok=True)
    dest = os.path.join(site_assets_dir, basename)
    if not os.path.exists(dest) or os.path.getsize(dest) != os.path.getsize(path):
        shutil.copyfile(path, dest)
    # The root working copy sits next to the source assets/ folder, so the
    # same relative URL works there too as long as images live in assets/.
    return f"assets/{basename}"

def site_url():
    """The real public address (SITE_URL), falling back to LIVE_URL."""
    return (getattr(C, "SITE_URL", "") or getattr(C, "LIVE_URL", "") or "").rstrip("/")

def structured_data():
    """JSON-LD (schema.org) for the homepage: business identity, contact,
    address, hours, socials and an OrderAction for the ordering link -- what
    Google uses for the business panel and rich results. Ported from Fat
    Tony's 2026-09-27 and made generic: @type comes from SCHEMA_TYPE (or
    SITE_TYPE: restaurant -> Restaurant, else LocalBusiness)."""
    import json
    addr = getattr(C, "ADDRESS_FULL", "")
    street = city = region = postal = ""
    m = re.match(r"^(.*),\s*([^,]+?),\s*([A-Za-z]{2})\s+(\d{5}(?:-\d{4})?)\s*$", addr)
    if m:
        street, city, region, postal = (g.strip() for g in m.groups())
    kind = getattr(C, "SCHEMA_TYPE", "") or ("Restaurant" if getattr(C, "SITE_TYPE", "") == "restaurant" else "LocalBusiness")
    data = {"@context": "https://schema.org", "@type": kind, "name": C.BUSINESS_NAME}
    if site_url():
        data["url"] = site_url()
    for key, attr in (("telephone", "PHONE_DISPLAY"), ("email", "EMAIL"),
                      ("servesCuisine", "CUISINE"), ("priceRange", "PRICE_RANGE")):
        val = getattr(C, attr, "")
        if val:
            data[key] = val
    if street:
        data["address"] = {"@type": "PostalAddress", "streetAddress": street, "addressLocality": city,
                           "addressRegion": region, "postalCode": postal, "addressCountry": "US"}
    opens, closes = getattr(C, "HOURS_OPENS", ""), getattr(C, "HOURS_CLOSES", "")
    if opens and closes:
        data["openingHoursSpecification"] = {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": opens, "closes": closes}
    same_as = [u for u in (getattr(C, "INSTAGRAM_URL", ""), getattr(C, "FACEBOOK_URL", "")) if u]
    if same_as:
        data["sameAs"] = same_as
    order_url = getattr(C, "ORDER_URL", "")
    if order_url and "example.com" not in order_url:
        data["potentialAction"] = [{"@type": "OrderAction", "target": {
            "@type": "EntryPoint", "urlTemplate": order_url,
            "actionPlatform": ["https://schema.org/DesktopWebPlatform", "https://schema.org/MobileWebPlatform"]}}]
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'

def head(title, description, canonical_path=""):
    """<head> for every page. canonical_path = the page's address inside the
    site ("" for the homepage, "menu.html", ...). 2026-09-27: adds the SEO
    tags Fat Tony's already had -- canonical + og:url pointing at the real
    domain (SITE_URL), robots, share image, apple-touch icon, and the JSON-LD
    business info on the homepage only (one entity per site)."""
    # Favicon: prefer an explicit FAVICON_IMAGE override, else the round/divider
    # logo (Fat Tony's V1 used its round logo as the favicon), else the main logo.
    favicon = getattr(C, "FAVICON_IMAGE", "") or getattr(C, "DIVIDER_LOGO", "") or C.LOGO_IMAGE
    favicon_src = embed_img(favicon) if favicon else ""
    favicon_tag = f'<link rel="icon" type="image/png" href="{favicon_src}">' if favicon else ""
    apple_touch_tag = f'<link rel="apple-touch-icon" href="{favicon_src}">' if favicon else ""
    base = site_url()
    canonical_url = (base + "/" + canonical_path.lstrip("/")) if base else ""
    canonical_tags = (f'<link rel="canonical" href="{canonical_url}">\n'
                      f'<meta property="og:url" content="{canonical_url}">') if canonical_url else ""
    share_img = getattr(C, "OG_IMAGE", "") or getattr(C, "HERO_IMAGE", "") or favicon
    share_src = embed_img(share_img) if share_img else ""
    if share_src and base and not share_src.startswith(("http", "data:")):
        share_src = base + "/" + share_src
    og_image_tag = f'<meta property="og:image" content="{share_src}">' if share_src.startswith("http") else ""
    ld_json = structured_data() if canonical_path == "" else ""
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{_robots_meta()}">
{canonical_tags}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
{og_image_tag}
{favicon_tag}
{apple_touch_tag}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{C.GOOGLE_FONTS_HREF}" rel="stylesheet">
{ld_json}
<style>{base_css()}</style></head><body>"""


def _robots_meta():
    return "noindex, nofollow" if getattr(C, "NOINDEX", False) else "index, follow"

def demo_banner():
    """Thin ribbon above the nav on every page when DEMO_BANNER is set."""
    t = getattr(C, "DEMO_BANNER", "")
    es = getattr(C, "DEMO_BANNER_ES", "")
    attr = f' data-es="{es}"' if es else ""
    return f'<div class="demo-ribbon"{attr}>{t}</div>' if t else ""

def brand_short():
    """Short display name for nav/footer ('Fat Tony's' vs the fuller
    BUSINESS_NAME used in <title>/metadata). Falls back to BUSINESS_NAME."""
    return getattr(C, "BRAND_SHORT", "") or C.BUSINESS_NAME

def brand_mark():
    """Nav wordmark. Fat Tony's pattern: icon + business-name text together
    (not image-only) -- set NAV_SHOW_TEXT=False on a client to go icon-only."""
    show_text = getattr(C, "NAV_SHOW_TEXT", True)
    img = f'<img src="{embed_img(C.LOGO_IMAGE)}" alt="{C.BUSINESS_NAME} logo">' if C.LOGO_IMAGE else ""
    if img and show_text:
        return img + f'<span>{brand_short()}</span>'
    if img:
        return img
    return C.BUSINESS_NAME

def nav(active=""):
    """Sticky nav. Cross-page links use __HOME__ / __MENU__ / __CATERING__ tokens
    filled per copy. Fat Tony's pattern: MENU / SPECIALS / FIND US / CATERING."""
    import es_translations as ES
    def _es(label):
        es = ES.NAV_ES.get(label)
        return f' data-es="{es}"' if es else ""
    show_menu = C.MENU_MODE != "none"
    show_specials_page = bool(getattr(C, "SPECIALS_LIST", None))
    show_specials_anchor = (not show_specials_page) and bool(
        getattr(C, "SPECIALS_ENABLED", False) or getattr(C, "SPECIALS", None))
    show_catering = bool(getattr(C, "CATERING_ENABLED", False))
    location_id = getattr(C, "LOCATION_SECTION_ID", "find")
    links = []
    mob_links = []
    if show_menu:
        _ml = getattr(C, "NAV_MENU_LABEL", "MENU")
        links.append(f'<a href="__MENU__"{_es(_ml)}>{_ml}</a>')
        mob_links.append(f'<a href="__MENU__"{_es(_ml)}>{_ml}</a>')
    if show_specials_page:
        # Full dedicated specials page (SPECIALS_LIST set) -- takes priority
        # over the old on-page-anchor grid below when both would apply.
        links.append(f'<a href="__SPECIALS__"{_es("SPECIALS")}>SPECIALS</a>')
        mob_links.append(f'<a href="__SPECIALS__"{_es("Specials")}>Specials</a>')
    elif show_specials_anchor:
        links.append(f'<a href="__HOME__#specials"{_es("SPECIALS")}>SPECIALS</a>')
        mob_links.append(f'<a href="__HOME__#specials"{_es("Specials")}>Specials</a>')
    show_calendar = bool(getattr(C, "CALENDAR_EVENTS", None))
    if show_calendar:
        links.append(f'<a href="__CALENDAR__"{_es("CALENDAR")}>CALENDAR</a>')
        mob_links.append(f'<a href="__CALENDAR__"{_es("Calendar")}>Calendar</a>')
    links.append(f'<a href="__HOME__#{location_id}"{_es("FIND US")}>FIND US</a>')
    mob_links.append(f'<a href="__HOME__#{location_id}"{_es("Find Us")}>Find Us</a>')
    if show_catering:
        links.append(f'<a href="__CATERING__"{_es("CATERING")}>CATERING</a>')
        mob_links.append(f'<a href="__CATERING__"{_es("Catering")}>Catering</a>')
    if getattr(C, "RESERVE_ENABLED", False):
        _rl = getattr(C, "NAV_RESERVE_LABEL", "RESERVE")
        links.append(f'<a href="__RESERVE__"{_es(_rl)}>{_rl}</a>')
        mob_links.append(f'<a href="__RESERVE__"{_es(_rl.title())}>{_rl.title()}</a>')
    return f"""{demo_banner()}<nav class="nav" data-section="NAV"><div class="wrap">
  <a class="brand" href="__HOME__">{brand_mark()}</a>
  <div class="nav-links">
    {''.join(links)}
  </div>
  <div class="nav-cta">
    <a class="btn btn-ghost" href="tel:{C.PHONE_TEL}" data-es="{ES.CALL_LABEL_ES} {C.PHONE_DISPLAY}">CALL {C.PHONE_DISPLAY}</a>
    <a class="btn btn-primary" href="{C.ORDER_URL}" target="_blank" rel="noopener" data-es="{ES.ORDER_LABEL_ES}">{C.ORDER_LABEL}</a>
  </div>
  <button class="hamb" onclick="document.getElementById('mm').classList.toggle('open')">&#9776;</button>
</div>
<div class="mobile-menu" id="mm">
  {''.join(mob_links)}
  <a class="mobile-order-btn" href="{C.ORDER_URL}" target="_blank" rel="noopener" data-es="{ES.ORDER_LABEL_ES}">{C.ORDER_LABEL}</a>
  <a class="mobile-call-btn" href="tel:{C.PHONE_TEL}" data-es="{ES.CALL_LABEL_ES} {C.PHONE_DISPLAY}">CALL {C.PHONE_DISPLAY}</a>
</div></nav>
<button class="lang-toggle" id="langToggle" type="button" aria-label="Switch language">ESP</button>"""


_SVG_IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/>'
           '<circle cx="12" cy="12" r="4.2"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg>')
_SVG_FB = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="M15 8.5h-2c-.8 0-1.5.7-1.5 1.5v2H15'
           'l-.4 2.5h-2.1V21h-2.5v-6.5H8V12h2V9.8C10 7.7 11.5 6 13.6 6H15v2.5z"/></svg>')
_SVG_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/>'
             '<path d="M3 7l9 6 9-6"/></svg>')

def social_icons():
    out = []
    if C.INSTAGRAM_URL:
        out.append(f'<a href="{C.INSTAGRAM_URL}" class="social-icon" aria-label="Instagram" '
                   f'target="_blank" rel="noopener">{_SVG_IG}</a>')
    if C.FACEBOOK_URL:
        out.append(f'<a href="{C.FACEBOOK_URL}" class="social-icon" aria-label="Facebook" '
                   f'target="_blank" rel="noopener">{_SVG_FB}</a>')
    if C.EMAIL:
        out.append(f'<a href="mailto:{C.EMAIL}" class="social-icon" aria-label="Email">{_SVG_MAIL}</a>')
    return '<div class="foot-social">' + "".join(out) + "</div>" if out else ""

def footer():
    # Fat Tony's footer pattern: a big centered logo divider, then a simple
    # footer -- FOLLOW + social icons + email + compliance (if any) + copyright.
    # Address/hours/phone live in the Find Us section and trust strip; they are
    # deliberately NOT repeated here.
    # The glow divider ALWAYS renders (standard footer, 2026-09-27): the logo
    # if there is one, otherwise the business name as a wordmark.
    divider_logo = getattr(C, "DIVIDER_LOGO", "") or C.LOGO_IMAGE
    divider_inner = (f'<img src="{embed_img(divider_logo)}" alt="{C.BUSINESS_NAME} logo">'
                     if divider_logo else f'<div class="logo-divider-name">{brand_short()}</div>')
    if divider_logo and getattr(C, "DIVIDER_SHOW_NAME", False):
        divider_inner += f'<div class="logo-divider-name">{brand_short()}</div>'
    divider_cls = "logo-divider" if divider_logo else "logo-divider logo-divider-wordmark"
    divider = f'<section class="{divider_cls}">{divider_inner}</section>'
    compliance = ""
    if C.COMPLIANCE_LINES:
        compliance = '<div class="compliance">' + "".join(
            f"<p>{ln}</p>" for ln in C.COMPLIANCE_LINES) + "</div>"
    import datetime
    yr = datetime.date.today().year
    # Icon-only by default (social_icons() already links EMAIL as a mailto icon).
    # Only show the email as a separate visible text line if a client explicitly
    # wants it -- set SHOW_FOOTER_EMAIL_TEXT = True in brand_config.py.
    email_line = (f'<a href="mailto:{C.EMAIL}">{C.EMAIL}</a>'
                  if C.EMAIL and getattr(C, "SHOW_FOOTER_EMAIL_TEXT", False) else "")
    handle_line = (f'<a href="{C.INSTAGRAM_URL}" class="foot-handle" target="_blank" '
                   f'rel="noopener">{C.INSTAGRAM_HANDLE}</a>') if (C.INSTAGRAM_URL and C.INSTAGRAM_HANDLE) else ""
    import es_translations as ES
    return f"""{divider}<footer class="foot" id="contact" data-section="FOOTER"><div class="wrap">
  <h4 data-es="{ES.FOLLOW_ES} {brand_short()}">Follow {brand_short()}</h4>
  {social_icons()}
  {handle_line}
  {email_line}
  {compliance}
  <div class="copyright"><span data-es="&copy; {yr} {C.BUSINESS_NAME}. Todos los derechos reservados.">&copy; {yr} {C.BUSINESS_NAME}. All rights reserved.</span><span class="maintain-credit" data-es-html='Sitio construido y mantenido con <a href="https://maintain.style" target="_blank" rel="noopener">mAIntAIn Style</a>'>Site built &amp; maintained with <a href="https://maintain.style" target="_blank" rel="noopener">mAIntAIn Style</a></span></div>
</div></footer>"""


def back_to_top():
    # Brand icon back-to-top (Fat Tony's pizza-slice pattern): the bare icon,
    # no circle/background behind it. Every client site should set TOTOP_ICON
    # to an svg/png that reflects the business (pizza slice, leaf, chili...).
    # Falls back to a plain accent-circle arrow only if no icon is set yet.
    icon = getattr(C, "TOTOP_ICON", "") or getattr(C, "BACKTOTOP_ICON", "")
    rot = getattr(C, "TOTOP_ICON_ROTATE", getattr(C, "BACKTOTOP_ICON_ROTATE", 0))
    if icon:
        style = f' style="transform:rotate({rot}deg)"' if rot else ""
        inner = f'<img src="{embed_img(icon)}" alt=""{style}>'
        cls = "totop"
    else:
        inner = "&#8593;"
        cls = "totop noicon"
    return (f'<button class="{cls}" id="totop" aria-label="Back to top"\n'
            " onclick=\"window.scrollTo({top:0,behavior:'smooth'})\">" + inner + "</button>\n"
            "<script>window.addEventListener('scroll',function(){\n"
            " document.getElementById('totop').classList.toggle('show',window.scrollY>320);},{passive:true});</script>")

def age_gate():
    if not C.AGE_GATE_ENABLED:
        return ""
    key = "age_verified_until"
    ms = C.AGE_GATE_DAYS * 86400000
    return f"""<div class="agegate" id="agegate">
  <div class="agebox">
    <h2>{C.AGE_GATE_TITLE}</h2>
    <p>You must be {C.AGE_GATE_MIN} or older to enter this site.</p>
    <button class="btn btn-primary" onclick="ageYes()">{C.AGE_GATE_YES}</button>
    <button class="btn btn-ghost" onclick="location.href='{C.AGE_GATE_BOUNCE}'">{C.AGE_GATE_NO}</button>
  </div></div>
<script>
(function(){{try{{var u=localStorage.getItem('{key}');
 if(u&&Date.now()<parseInt(u)){{document.getElementById('agegate').classList.add('hide');document.body.style.overflow='';}}
 else{{document.body.style.overflow='hidden';}}}}catch(e){{}}}})();
function ageYes(){{try{{localStorage.setItem('{key}',String(Date.now()+{ms}));}}catch(e){{}}
 document.getElementById('agegate').classList.add('hide');document.body.style.overflow='';}}
</script>"""

def lang_script():
    return """<script>(function(){
  var LANG_KEY='site_lang';
  function getLang(){try{return localStorage.getItem(LANG_KEY)||'en';}catch(e){return 'en';}}
  function setLang(l){try{localStorage.setItem(LANG_KEY,l);}catch(e){}}
  function apply(lang){
    document.querySelectorAll('[data-es]').forEach(function(el){
      if(el.dataset.enOrig===undefined) el.dataset.enOrig=el.textContent;
      el.textContent = lang==='es' ? el.dataset.es : el.dataset.enOrig;
    });
    document.querySelectorAll('[data-es-html]').forEach(function(el){
      if(el.dataset.enOrigHtml===undefined) el.dataset.enOrigHtml=el.innerHTML;
      el.innerHTML = lang==='es' ? el.dataset.esHtml : el.dataset.enOrigHtml;
    });
    document.querySelectorAll('[data-es-placeholder]').forEach(function(el){
      if(el.dataset.enOrigPlaceholder===undefined) el.dataset.enOrigPlaceholder=el.getAttribute('placeholder')||'';
      el.setAttribute('placeholder', lang==='es' ? el.dataset.esPlaceholder : el.dataset.enOrigPlaceholder);
    });
    document.documentElement.setAttribute('lang', lang);
    var btn=document.getElementById('langToggle');
    if(btn) btn.textContent = lang==='es' ? 'ENG' : 'ESP';
  }
  document.addEventListener('DOMContentLoaded', function(){
    apply(getLang());
    var btn=document.getElementById('langToggle');
    if(btn) btn.addEventListener('click', function(){
      var next = getLang()==='es' ? 'en' : 'es';
      setLang(next);
      apply(next);
    });
  });
})();</script>"""

def close_html():
    # THEME_CSS/JS come from theme.py (the look); CUSTOM_CSS/JS come from
    # brand_config.py (what the owner adds through Client Style) and go last.
    import theme
    css = (getattr(C, "CUSTOM_CSS", "") or "").strip().replace("</style", "<\\/style")
    js = (getattr(C, "CUSTOM_JS", "") or "").strip().replace("</script", "<\\/script")
    extra = '<style id="theme-css">' + theme.THEME_CSS + "</style>"
    extra += '<script id="theme-js">' + theme.THEME_JS + "</script>"
    if css:
        extra += '<style id="custom-css">' + css + "</style>"
    if js:
        extra += '<script id="custom-js">' + js + "</script>"
    return lang_script() + extra + "</body></html>"

def out_names():
    """(root_working_file, site_file) name pairs, keyed by page."""
    s = slug()
    return {
        "home": (f"{s}_homepage.html", "index.html"),
        "menu": (f"{s}_menu.html", "menu.html"),
        "catering": (f"{s}_catering.html", "catering.html"),
        "specials": (f"{s}_specials.html", "specials.html"),
        "calendar": (f"{s}_calendar.html", "calendar.html"),
        "reserve": (f"{s}_reserve.html", getattr(C, "RESERVE_FILE", "reserve.html")),
    }


def write_two_copies(page_key, html):
    """Write the root working copy and the deployable site/ copy of a page,
    filling the __HOME__ / __MENU__ / __CATERING__ / __SPECIALS__ cross-links
    for each."""
    names = out_names()
    root_home, site_home = names["home"]
    root_menu, site_menu = names["menu"]
    root_cat,  site_cat  = names["catering"]
    root_spec, site_spec = names["specials"]
    root_cal,  site_cal  = names["calendar"]
    root_res,  site_res  = names["reserve"]

    def fill(h, home, menu, cat, spec, cal, res, self_menu_anchor=False, self_home_anchor=False):
        # On the home page itself, __HOME__#section should jump to the on-page
        # anchor instead of re-navigating to index.html#section (which forces
        # a full page reload even though it's the same document). A bare
        # __HOME__ (the logo link) still resolves normally.
        if self_home_anchor:
            h = h.replace("__HOME__#", "#")
        h = h.replace("__HOME__", home)
        # On the menu page itself, MENU should jump to the on-page anchor
        h = h.replace("__MENU__", "#menu" if self_menu_anchor else menu)
        h = h.replace("__CATERING__", cat)
        h = h.replace("__SPECIALS__", spec)
        h = h.replace("__CALENDAR__", cal)
        h = h.replace("__RESERVE__", res)
        # same-site links never need a new tab
        h = re.sub(r'(href="[^"]*\.html(?:#[^"]*)?") target="_blank" rel="noopener"', r"\1", h)
        return h

    self_menu_anchor = (page_key == "menu")
    self_home_anchor = (page_key == "home")
    root_html = fill(html, root_home, root_menu, root_cat, root_spec, root_cal, root_res, self_menu_anchor, self_home_anchor)
    site_html = fill(html, site_home, site_menu, site_cat, site_spec, site_cal, site_res, self_menu_anchor, self_home_anchor)

    root_name, site_name = names[page_key]
    root_path = os.path.join(ROOT, root_name)
    site_dir  = os.path.join(ROOT, "site")
    os.makedirs(site_dir, exist_ok=True)
    site_path = os.path.join(site_dir, site_name)
    for p, h in [(root_path, root_html), (site_path, site_html)]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(h)
        print(f"written {len(h.encode('utf-8'))} -> {p}")


def write_seo_files(pages):
    """Write robots.txt and sitemap.xml into the deployable site/ folder
    (2026-09-27, ported from Fat Tony's -- every site build now ships them
    instead of it being a manual checklist item). `pages` = the site-relative
    paths built this run, e.g. ["", "menu.html"] ("" = the homepage).
    The named AI-crawler blocks are redundant with the wildcard Allow but are
    listed because SEO / AI-visibility checkers look for them by name."""
    site_dir = os.path.join(ROOT, "site")
    os.makedirs(site_dir, exist_ok=True)
    if getattr(C, "NOINDEX", False):
        with open(os.path.join(site_dir, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write("User-agent: *\nDisallow: /\n")
        print("written robots.txt (NOINDEX: whole site hidden from search)")
        return
    base = site_url()
    ai_bots = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-Web", "anthropic-ai",
               "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot",
               "Bytespider", "Meta-ExternalAgent"]
    robots = "".join(f"User-agent: {bot}\nAllow: /\n\n" for bot in ai_bots) + "User-agent: *\nAllow: /\n"
    if base:
        robots += f"\nSitemap: {base}/sitemap.xml\n"
    with open(os.path.join(site_dir, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(robots)
    print("written robots.txt")
    if not base:
        print("sitemap.xml skipped -- set SITE_URL (or LIVE_URL) in brand_config.py")
        return
    import datetime
    today = datetime.date.today().isoformat()
    urls = "".join(f"  <url><loc>{base}/{p.lstrip('/')}</loc><lastmod>{today}</lastmod></url>\n" for p in pages)
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    with open(os.path.join(site_dir, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(sitemap)
    print("written sitemap.xml")
