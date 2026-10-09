# -*- coding: utf-8 -*-
"""
build_reserve.py -- reservation page with a real-looking form: text/date fields,
radio groups (party size, seating) and checkboxes (special needs, newsletter).
DEMO ONLY: submitting shows a thank-you card in the browser and sends nothing.
Only builds when brand_config.RESERVE_ENABLED is True.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_config as C
import site_common as S
import es_translations as ES

RESERVE_CSS = """
.res-wrap{max-width:860px}
.res-hero{background:radial-gradient(ellipse at 70% 30%,var(--primary-bright) 0%,var(--primary) 60%,var(--primary-deep) 100%);border-radius:22px;padding:42px 28px;margin-bottom:30px;text-align:center;border:1px solid rgba(240,179,58,.35)}
.res-hero h2{font-size:clamp(30px,5vw,46px);margin:8px 0 12px;color:#fff;text-shadow:0 0 18px rgba(255,61,87,.7)}
.res-hero .lead{max-width:560px;margin:0 auto;color:var(--cream)}
.res-form{background:var(--panel);border:1px solid rgba(255,255,255,.12);border-radius:22px;padding:30px 28px;display:grid;gap:22px}
.res-row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.res-form label.fld{display:grid;gap:6px;font-size:13px;font-weight:700;letter-spacing:.6px;color:var(--cream-muted);text-transform:uppercase}
.res-form input[type=text],.res-form input[type=email],.res-form input[type=tel],.res-form input[type=date],.res-form select,.res-form textarea{width:100%;background:var(--bg-deep);color:var(--cream);border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:13px 14px;font:500 16px var(--font-body);text-transform:none;letter-spacing:0}
.res-form textarea{min-height:110px;resize:vertical}
.res-form input:focus,.res-form select:focus,.res-form textarea:focus{outline:2px solid var(--glow);outline-offset:1px}
.res-form fieldset{border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:16px 18px 14px;margin:0}
.res-form legend{padding:0 8px;font-size:13px;font-weight:800;letter-spacing:1.2px;color:var(--glow);text-transform:uppercase}
.res-opts{display:flex;flex-wrap:wrap;gap:10px 22px}
.res-opts label{display:flex;align-items:center;gap:9px;font-size:15px;color:var(--cream);cursor:pointer}
.res-submit{justify-self:start}
.res-note{font-size:13px;color:var(--cream-muted)}
.res-err{color:#ff8f9c;font-size:14px;min-height:20px}
.res-thanks{background:var(--panel);border:2px solid var(--glow);border-radius:22px;padding:34px 28px;text-align:center;box-shadow:0 0 34px rgba(155,216,122,.25)}
.res-thanks h3{font-size:30px;margin-bottom:10px}
.res-thanks dl{display:inline-grid;grid-template-columns:auto auto;gap:6px 18px;text-align:left;margin:16px 0}
.res-thanks dt{color:var(--cream-muted)}
@media(max-width:700px){.res-row{grid-template-columns:1fr}.res-form{padding:22px 16px}}
"""

PARTY = ["Small (under 5,000 sq ft)", "Medium (5,000 to 10,000 sq ft)", "Large (10,000 sq ft to 1 acre)", "Over 1 acre"]
SEATS = ["As soon as possible", "This month", "Within 3 months", "Just planning"]
NEEDS = ["Lawn care", "Gardens & planting", "Patio or stonework", "Trees & hedges", "Irrigation", "Snow or seasonal cleanup"]

def _radios(name, items, es, checked=0):
    return "".join(
        f'<label><input type="radio" name="{name}" value="{t}"{" checked" if i == checked else ""}> <span data-es="{es[i]}">{t}</span></label>'
        for i, t in enumerate(items))

def _checks(name, items, es):
    return "".join(f'<label><input type="checkbox" name="{name}" value="{t}"> <span data-es="{es[i]}">{t}</span></label>' for i, t in enumerate(items))

BODY = """__NAV__
<section class="sec wrap res-wrap" id="reserve" data-section="RESERVE">
  <div class="res-hero">
    <span class="sec-tag" __ES_tag__>FREE QUOTE</span><h2 __ES_title__>Let's walk your yard</h2>
    <p class="lead" __ES_lead__>Tell us what you have in mind. This is a demo form &mdash; nothing is sent anywhere.</p>
  </div>
  <form class="res-form" id="resForm" novalidate>
    <div class="res-row">
      <label class="fld"><span __ES_name__>Your name</span><input type="text" name="name" autocomplete="name" required></label>
      <label class="fld"><span __ES_email__>Email</span><input type="email" name="email" autocomplete="email"></label>
    </div>
    <div class="res-row">
      <label class="fld"><span __ES_date__>Preferred visit date</span><input type="date" name="date" id="resDate" required></label>
      <label class="fld"><span __ES_time__>Time</span><select name="time">
        <option>8:00 am</option><option>10:00 am</option><option selected>12:00 pm</option><option>2:00 pm</option><option>4:00 pm</option></select></label>
    </div>
    <fieldset><legend __ES_party__>Property size</legend><div class="res-opts">__PARTY__</div></fieldset>
    <fieldset><legend __ES_seat__>When would you like to start?</legend><div class="res-opts">__SEATS__</div></fieldset>
    <fieldset><legend __ES_need__>Which services are you interested in?</legend><div class="res-opts">__NEEDS__</div></fieldset>
    <fieldset><legend __ES_stay__>Stay in touch</legend><div class="res-opts">
      <label><input type="checkbox" name="news" value="yes"> <span __ES_news__>Email me seasonal tips and offers</span></label></div></fieldset>
    <label class="fld"><span __ES_notes__>Notes</span><textarea name="notes" placeholder="A dog in the yard, a gate code, an idea you saw online..." data-es-placeholder="__RAW_notes_ph__"></textarea></label>
    <div class="res-err" id="resErr" role="alert"></div>
    <button class="btn btn-primary res-submit" type="submit" __ES_submit__>REQUEST A QUOTE</button>
    <p class="res-note" __ES_note__>Demo only. Nothing you type here is stored or sent.</p>
  </form>
  <div class="res-thanks" id="resThanks" hidden>
    <h3 data-es="¡Recibimos tu solicitud!">We got your request!</h3>
    <p data-es="Esto es lo que habríamos programado:">Here's what we'd have scheduled:</p>
    <dl id="resSummary"></dl>
    <p class="res-note" data-es="Esto es una demostración, así que no se programó ninguna visita.">This is a demo, so no visit was actually booked.</p>
    <p style="margin-top:14px"><a class="btn btn-ghost" href="#" id="resAgain" data-es="ENVIAR OTRA">SEND ANOTHER</a></p>
  </div>
</section>
__FOOTER__"""

JS = """<script>(function(){
  var f=document.getElementById('resForm');if(!f)return;
  var d=document.getElementById('resDate'),err=document.getElementById('resErr');
  var t=new Date();d.min=t.toISOString().slice(0,10);
  f.addEventListener('submit',function(e){
    e.preventDefault();
    if(!f.name.value.trim()||!d.value){err.textContent='Please add your name and a date.';return;}
    err.textContent='';
    var fd=new FormData(f),dl=document.getElementById('resSummary');dl.textContent='';
    function row(k,v){var a=document.createElement('dt'),b=document.createElement('dd');a.textContent=k;b.textContent=v;dl.appendChild(a);dl.appendChild(b);}
    row('Name',fd.get('name'));row('Visit',fd.get('date')+' at '+fd.get('time'));
    row('Property',fd.get('party'));row('Start',fd.get('seat'));
    var needs=fd.getAll('need');row('Services',needs.length?needs.join(', '):'Not sure yet');
    row('Newsletter',fd.get('news')?'Yes please':'No thanks');
    f.hidden=true;document.getElementById('resThanks').hidden=false;
    document.getElementById('resThanks').scrollIntoView({behavior:'smooth',block:'center'});
  });
  document.getElementById('resAgain').addEventListener('click',function(e){
    e.preventDefault();f.reset();f.hidden=false;document.getElementById('resThanks').hidden=true;});
})();</script>"""

def build():
    if not getattr(C, "RESERVE_ENABLED", False):
        print("RESERVE_ENABLED is False -- skipping reserve page.")
        return
    title = f"Free quote - {C.BUSINESS_NAME}"
    desc = f"Request a free quote from {C.BUSINESS_NAME} (demo form)."
    body = (BODY.replace("__NAV__", S.nav("reserve")).replace("__FOOTER__", S.footer())
            .replace("__PARTY__", _radios("party", PARTY, ES.RES_ES["party_opts"]))
            .replace("__SEATS__", _radios("seat", SEATS, ES.RES_ES["seat_opts"]))
            .replace("__NEEDS__", _checks("need", NEEDS, ES.RES_ES["need_opts"])))
    for k in ("tag", "title", "lead", "name", "email", "date", "time", "notes", "party", "seat", "need", "stay", "news", "submit", "note"):
        body = body.replace(f"__ES_{k}__", f'data-es="{ES.RES_ES[k]}"')
    body = body.replace("__RAW_notes_ph__", ES.RES_ES["notes_ph"])
    html = (S.head(title, desc, getattr(C, "RESERVE_FILE", "reserve.html")) + "<style>" + RESERVE_CSS + "</style>" + S.age_gate()
            + body + JS + S.back_to_top() + S.close_html())
    S.write_two_copies("reserve", html)

if __name__ == "__main__":
    build()
