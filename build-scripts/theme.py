# -*- coding: utf-8 -*-
"""
theme.py -- the Fernhollow "look": deep forest green, marigold, soft leaf glow,
and the four-seasons hero. Lives apart from brand_config.py on purpose: this is
the designer's layer, so owner edits made through Client Style (which touch
brand_config.py) can't break it. Written into every page by
site_common.close_html() BEFORE CUSTOM_CSS.
"""

THEME_CSS = r"""
:root{--leaf:#9bd87a;--sun:#f0b33a;--paper:#f4efe0;--accent-text:#f0b33a}
h1,h2,h3{font-weight:700;letter-spacing:-.2px}
.nw{white-space:nowrap}
.maintain-credit a{color:var(--accent-text)}
body{background:radial-gradient(1000px 480px at 80% -10%,rgba(155,216,122,.10),transparent 62%),var(--bg-deep)}

/* ribbon + nav: leaf-green hairline, quiet shadow */
.demo-ribbon{background:var(--leaf);color:#0c1f12;text-align:center;font:700 11.5px/1.3 var(--font-body);letter-spacing:1.1px;padding:7px 14px;text-transform:uppercase}
@media(max-width:700px){.demo-ribbon{font-size:9.5px;letter-spacing:.4px;padding:5px 10px}}
.nav{border-bottom:1px solid rgba(155,216,122,.35);box-shadow:0 8px 26px rgba(0,0,0,.35)}
.nav .brand{color:var(--paper);font-family:var(--font-nav);letter-spacing:.2px}

/* buttons: soft-cornered, marigold solid / leaf outline */
.btn{border-radius:12px;font-weight:700;letter-spacing:.5px;transition:transform .2s,box-shadow .25s,background .2s,color .2s}
.btn-primary{background:var(--accent);color:var(--on-accent);box-shadow:0 6px 18px rgba(240,179,58,.28)}
.btn-primary:hover{background:#ffc552;box-shadow:0 8px 24px rgba(240,179,58,.45)}
.btn-ghost{border:2px solid var(--leaf);color:var(--leaf);background:transparent}
.btn-ghost:hover{background:var(--leaf);color:#0c1f12}

/* THE HERO: four seasons. One row of photo panels, the active one opens wide. */
.hero.hero-seasons{background:none;padding:0;position:relative;display:block;min-height:min(88vh,760px);overflow:hidden}
.hs-panels{position:absolute;inset:0;display:flex}
.hs-panel{position:relative;flex:1 1 0;min-width:0;border:0;padding:0;margin:0;cursor:pointer;background-size:cover;background-position:center;
  transition:flex-grow .9s cubic-bezier(.65,0,.25,1),filter .6s;filter:saturate(.85) brightness(.72);overflow:hidden;color:#fff;text-align:left;font:inherit}
.hs-panel+.hs-panel{border-left:2px solid rgba(11,19,14,.85)}
.hs-panel.is-active{flex-grow:6;filter:none}
.hs-panel:focus-visible{outline:3px solid var(--sun);outline-offset:-3px}
.hs-label{position:absolute;top:26px;left:22px;right:14px;display:flex;flex-direction:column;gap:3px;transition:opacity .5s}
.hs-label b{font:700 clamp(18px,2.2vw,26px)/1.1 var(--font-head);letter-spacing:.2px;text-shadow:0 2px 12px rgba(0,0,0,.7);white-space:nowrap}
.hs-label i{font:500 13.5px/1.35 var(--font-body);font-style:normal;color:var(--paper);text-shadow:0 2px 10px rgba(0,0,0,.8);max-width:260px;opacity:0;transform:translateY(6px);transition:opacity .6s .3s,transform .6s .3s}
.hs-panel.is-active .hs-label i{opacity:1;transform:none}
.hs-panel:not(.is-active) .hs-label b{writing-mode:vertical-rl;transform:rotate(180deg);font-size:18px;opacity:.9}
.hs-panel:not(.is-active) .hs-label{top:30px;left:50%;right:auto;transform:translateX(-50%)}
.hs-panel:not(.is-active) .hs-label b{text-shadow:0 0 10px rgba(0,0,0,.95),0 2px 14px rgba(0,0,0,.9);opacity:1;font-size:19px}
.hs-panel:not(.is-active):hover{filter:saturate(.95) brightness(.85)}
.hs-scrim{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(7,14,10,.18) 0%,rgba(7,14,10,.05) 30%,rgba(7,14,10,.55) 62%,rgba(7,14,10,.94) 100%)}
.hs-copy{position:absolute;left:0;right:0;bottom:0;max-width:1180px;margin:0 auto;padding:0 32px 54px;pointer-events:none}
.hs-copy .hero-btns,.hs-copy a{pointer-events:auto}
.hs-copy h1{font-size:clamp(34px,5.6vw,68px);line-height:1.04;color:#fff;max-width:760px;text-shadow:0 3px 24px rgba(0,0,0,.65);margin:12px 0}
.hs-copy .lead{font-size:clamp(16px,1.9vw,19px);color:var(--paper);max-width:560px;text-shadow:0 2px 12px rgba(0,0,0,.8)}
.hs-copy .hero-btns{margin-top:20px}
.badge-pill{background:var(--accent);color:var(--on-accent);letter-spacing:1.2px;text-transform:uppercase}
@media(max-width:760px){
  .hero.hero-seasons{min-height:0;background:var(--bg-deep)}
  .hs-panels{position:relative;inset:auto;height:330px;flex-direction:column}
  .hs-panel+.hs-panel{border-left:0;border-top:2px solid rgba(11,19,14,.85)}
  .hs-panel.is-active{flex-grow:5}
  .hs-label{top:12px;left:18px}
  .hs-panel:not(.is-active) .hs-label{top:50%;left:18px;transform:translateY(-50%)}
  .hs-panel:not(.is-active) .hs-label b{writing-mode:horizontal-tb;transform:none;font-size:17px}
  .hs-scrim{display:none}
  .hs-copy{position:static;padding:26px 22px 40px;pointer-events:auto}
  .hs-copy h1{text-shadow:none}
  .hs-copy .lead{text-shadow:none}
}

/* section labels + a soft leaf divider */
.sec-tag{color:var(--leaf);letter-spacing:3px}
.trust,.cta-band{position:relative}
.trust::before,.trust::after,.cta-band::before{content:"";position:absolute;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent,var(--leaf),var(--sun),var(--leaf),transparent);opacity:.7}
.trust::before,.cta-band::before{top:0}.trust::after{bottom:0}
.trust{padding:38px 0}
.trust-item .num{font-family:var(--font-head);font-size:19px;color:var(--paper)}

/* cards: soft, lifted, leaf edge on hover */
.card,.photo-card,.special-card{border-radius:18px;border:1px solid rgba(155,216,122,.16);transition:transform .28s,box-shadow .28s,border-color .28s}
.card:hover,.photo-card:hover,.special-card:hover{transform:translateY(-8px);border-color:rgba(155,216,122,.6);box-shadow:0 18px 40px rgba(0,0,0,.45)}
.card .img{height:230px;border-radius:12px;overflow:hidden;margin-bottom:16px}
.card .img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s}
.card:hover .img img{transform:scale(1.07)}
.photo-card .price,.special-card .tag{color:var(--accent-text)}
.story-img img{border-radius:18px;box-shadow:0 0 0 3px rgba(155,216,122,.2),0 22px 60px rgba(0,0,0,.5)}
.special{background:linear-gradient(135deg,#10301f,#1b4a31);border:2px solid var(--sun);border-radius:20px;box-shadow:0 0 34px rgba(240,179,58,.2),inset 0 0 40px rgba(0,0,0,.3)}
.menu-item .pr{color:var(--sun)}
"""

THEME_CSS += r"""
.js .lf-rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
.js .lf-rv.lf-in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){
  .hs-panel,.hs-label i{transition:none}
  .js .lf-rv{opacity:1;transform:none;transition:none}
  .card,.photo-card,.special-card,.btn{transition:none}
}
@media(max-width:700px){.trust{padding:30px 0}.card .img{height:200px}}
"""

THEME_JS = r"""
(function(){
  var d=document;d.documentElement.classList.add('js');
  /* seasons hero: hover / tap / keyboard picks a panel; otherwise it cycles by itself */
  var box=d.getElementById('hsPanels');
  if(box){
    var ps=[].slice.call(box.querySelectorAll('.hs-panel')),cur=0,timer=null;
    var still=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
    function show(i){cur=i;ps.forEach(function(p,k){var on=k===i;p.classList.toggle('is-active',on);p.setAttribute('aria-pressed',on?'true':'false');});}
    function play(){if(still)return;stop();timer=setInterval(function(){show((cur+1)%ps.length);},5000);}
    function stop(){if(timer){clearInterval(timer);timer=null;}}
    ps.forEach(function(p,k){
      p.addEventListener('mouseenter',function(){stop();show(k);});
      p.addEventListener('click',function(){stop();show(k);play();});
      p.addEventListener('focus',function(){stop();show(k);});
    });
    box.addEventListener('mouseleave',play);
    play();
  }
  if(!('IntersectionObserver' in window)){return;}
  var els=d.querySelectorAll('.sec-head,.cards .card,.photo-card,.special-card,.special,.story-flex,.split,.menu-section,.res-form,.res-hero');
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('lf-in');io.unobserve(e.target);}});},{threshold:.12});
  els.forEach(function(el,i){el.classList.add('lf-rv');el.style.transitionDelay=(i%3)*90+'ms';io.observe(el);});
})();
"""
