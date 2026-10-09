# -*- coding: utf-8 -*-
"""
build_calendar_page.py -- a full month-grid Calendar page. Days that have one
or more events show small icons (by event "type"); clicking a day with events
opens a card popup listing that day's events (icon, title, time, description).
Opt-in: only builds anything if CALENDAR_EVENTS in brand_config.py is
non-empty -- same convention as build_specials_page.py's SPECIALS_LIST.
Run:
    python build-scripts/build_calendar_page.py

brand_config.py inputs (see section 18 for the full TODO block):
    CALENDAR_PAGE_TAG, CALENDAR_PAGE_TITLE, CALENDAR_PAGE_INTRO -- header copy
    CALENDAR_EVENT_TYPES = {key: (icon, label), ...} -- controls the icon
        shown on a day cell and the legend row under the calendar. Only types
        that actually appear in CALENDAR_EVENTS are shown in the legend.
    CALENDAR_EVENTS = [{"date": "YYYY-MM-DD", "type": "<key>", "title": "...",
        "time": "" , "desc": "", "title_es": "", "desc_es": ""}, ...]
        time/desc/title_es/desc_es are all optional.

Everything else (month grid, prev/next navigation, "today" ring, the click
popup, and the ESP/ENG toggle re-rendering month/weekday names) is rendered
client-side in vanilla JS from the event data embedded in the page -- no
backend, consistent with every other page in this template.
"""
import os, sys, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_config as C
import site_common as S
import es_translations as ES

# Reuses the same radial-gradient "hero" recipe as the Menu/Specials/Catering
# pages (each page owns its own copy rather than importing another page's CSS,
# same pattern as CATERING_CSS) so Calendar reads as part of the same site.
CALENDAR_CSS = """
.cal-wrap{max-width:900px;margin:0 auto;padding:40px 22px}
.cal-hero{background:radial-gradient(ellipse at 70% 30%,var(--primary) 0%,var(--primary-bright) 55%,var(--primary-deep) 100%);border-radius:16px;padding:36px 28px;margin-bottom:30px;text-align:center}
.cal-hero h2{font-size:34px;text-transform:uppercase;margin:8px 0 10px;color:var(--cream)}
.cal-hero .lead{max-width:560px;margin:0 auto;color:var(--cream)}
.cal-nav-row{display:flex;align-items:center;justify-content:center;gap:22px;margin-bottom:18px}
.cal-nav-btn{background:var(--panel);border:1px solid rgba(255,255,255,.14);color:var(--cream);width:38px;height:38px;border-radius:7px;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s ease,transform .2s ease}
.cal-nav-btn:hover{background:rgba(255,255,255,.12);transform:translateY(-2px)}
.cal-month-label{font-family:var(--font-head);font-size:22px;min-width:220px;text-align:center;color:var(--cream)}
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}
.cal-weekday{text-align:center;font-size:11px;font-weight:700;letter-spacing:.08em;color:var(--cream-muted);text-transform:uppercase;padding-bottom:6px}
.cal-day{position:relative;aspect-ratio:1/1;background:var(--panel);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:8px 6px;display:flex;flex-direction:column;gap:4px}
.cal-day.outside{opacity:.32;border-color:rgba(255,255,255,.04)}
.cal-day.today{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.cal-day.has-events{cursor:pointer;transition:transform .2s ease,border-color .2s ease,background .2s ease}
.cal-day.has-events:hover{transform:translateY(-2px);border-color:var(--glow);background:rgba(255,255,255,.06)}
.cal-day-num{font-size:13px;font-weight:600;color:var(--cream)}
.cal-day.outside .cal-day-num{color:var(--cream-muted)}
.cal-day-icons{display:flex;gap:3px;flex-wrap:wrap;align-items:center;margin-top:auto}
.cal-day-icons .ic{font-size:15px;line-height:1}
.cal-day-icons .more{font-size:10px;font-weight:700;color:var(--cream-muted);background:rgba(255,255,255,.08);border-radius:999px;padding:1px 5px}
.cal-legend{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:26px}
.cal-legend-chip{display:inline-flex;align-items:center;gap:6px;background:var(--panel);border:1px solid rgba(255,255,255,.1);border-radius:999px;padding:6px 14px;font-size:12px;color:var(--cream-muted)}
.cal-legend-chip .ic{font-size:15px}
/* popup */
.cal-modal-overlay{position:fixed;inset:0;z-index:500;background:rgba(11,11,12,.82);display:none;align-items:center;justify-content:center;padding:22px}
.cal-modal-overlay.show{display:flex}
.cal-modal{background:var(--panel);border:1px solid var(--glow);border-radius:16px;max-width:420px;width:100%;max-height:80vh;overflow-y:auto;padding:28px 26px;position:relative}
.cal-modal-close{position:absolute;top:14px;right:14px;background:rgba(255,255,255,.08);border:0;color:var(--cream);width:30px;height:30px;border-radius:50%;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s ease}
.cal-modal-close:hover{background:rgba(255,255,255,.18)}
.cal-modal h3{font-size:20px;margin:0 26px 18px 0}
.cal-event-row{display:flex;gap:12px;padding:12px 0;border-bottom:1px dashed rgba(255,255,255,.1)}
.cal-event-row:last-child{border-bottom:0}
.cal-event-row .ic{font-size:22px;line-height:1.3}
.cal-event-row .body{flex:1}
.cal-event-row .ttl{font-weight:700;color:var(--cream);font-size:15px}
.cal-event-row .tm{color:var(--accent);font-size:12px;font-weight:700;margin-top:2px}
.cal-event-row .ds{color:var(--cream-muted);font-size:13px;margin-top:4px;line-height:1.5}
@media(max-width:560px){
 .cal-day{padding:6px 4px}
 .cal-day-num{font-size:12px}
 .cal-day-icons .ic{font-size:12px}
 .cal-month-label{font-size:18px;min-width:160px}
}
"""

# Plain (non-f) template -- the JS below is full of { } so it's built with
# __TOKEN__ placeholders and filled with .replace() afterward instead of an
# f-string, same reasoning as the __HOME__/__MENU__ cross-page link tokens.
CALENDAR_JS = """
<script>
(function(){
  var EVENTS = __EVENTS_JSON__;
  var TYPES = __TYPES_JSON__;
  var MONTHS = {en:["January","February","March","April","May","June","July",
    "August","September","October","November","December"],
    es:["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto",
    "Septiembre","Octubre","Noviembre","Diciembre"]};
  var WD = {en:["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
    es:["Dom","Lun","Mar","Mié","Jue","Vie","Sáb"]};
  var WD_FULL = {en:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    es:["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]};

  function lang(){ try{ return localStorage.getItem('site_lang')||'en'; }catch(e){ return 'en'; } }

  var today = new Date();
  var viewYear = today.getFullYear(), viewMonth = today.getMonth();

  var grid = document.getElementById('calGrid');
  var wdRow = document.getElementById('calWeekdays');
  var label = document.getElementById('calMonthLabel');
  var overlay = document.getElementById('calModalOverlay');
  var modalBody = document.getElementById('calModalBody');

  function pad(n){ return n < 10 ? '0' + n : '' + n; }
  function key(y, m, d){ return y + '-' + pad(m + 1) + '-' + pad(d); }

  function renderWeekdays(){
    var l = lang();
    wdRow.innerHTML = WD[l].map(function(w){ return '<div class="cal-weekday">' + w + '</div>'; }).join('');
  }

  function dayCellHTML(y, m, d, outside){
    var k = key(y, m, d);
    var evs = EVENTS[k] || [];
    var isToday = (y === today.getFullYear() && m === today.getMonth() && d === today.getDate() && !outside);
    var cls = 'cal-day' + (outside ? ' outside' : '') + (isToday ? ' today' : '') + (evs.length && !outside ? ' has-events' : '');
    var icons = '';
    if (evs.length && !outside) {
      var shown = evs.slice(0, 2);
      icons = '<div class="cal-day-icons">' + shown.map(function(e){
        var t = TYPES[e.type] || ['\\u2022', e.type];
        return '<span class="ic">' + t[0] + '</span>';
      }).join('') + (evs.length > 2 ? '<span class="more">+' + (evs.length - 2) + '</span>' : '') + '</div>';
    }
    return '<div class="' + cls + '" data-date="' + (outside ? '' : k) + '"><span class="cal-day-num">' + d + '</span>' + icons + '</div>';
  }

  function render(){
    renderWeekdays();
    var l = lang();
    label.textContent = MONTHS[l][viewMonth] + ' ' + viewYear;
    var firstDow = new Date(viewYear, viewMonth, 1).getDay();
    var daysInMonth = new Date(viewYear, viewMonth + 1, 0).getDate();
    var prevDays = new Date(viewYear, viewMonth, 0).getDate();
    var cells = [];
    for (var i = firstDow - 1; i >= 0; i--) {
      cells.push(dayCellHTML(viewYear, viewMonth - 1, prevDays - i, true));
    }
    for (var d = 1; d <= daysInMonth; d++) {
      cells.push(dayCellHTML(viewYear, viewMonth, d, false));
    }
    while (cells.length % 7 !== 0) {
      var nextD = cells.length - (firstDow + daysInMonth) + 1;
      cells.push(dayCellHTML(viewYear, viewMonth + 1, nextD, true));
    }
    grid.innerHTML = cells.join('');
    grid.querySelectorAll('.cal-day.has-events').forEach(function(cell){
      cell.addEventListener('click', function(){ openModal(cell.dataset.date); });
    });
  }

  function openModal(k){
    var evs = EVENTS[k] || [];
    if (!evs.length) return;
    var l = lang();
    var parts = k.split('-');
    var dt = new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
    var heading = WD_FULL[l][dt.getDay()] + ', ' + MONTHS[l][dt.getMonth()] + ' ' + dt.getDate();
    var rows = evs.map(function(e){
      var t = TYPES[e.type] || ['\\u2022', e.type];
      var title = (l === 'es' && e.title_es) ? e.title_es : e.title;
      var desc = (l === 'es' && e.desc_es) ? e.desc_es : (e.desc || '');
      return '<div class="cal-event-row"><span class="ic">' + t[0] + '</span><div class="body">' +
        '<div class="ttl">' + title + '</div>' +
        (e.time ? '<div class="tm">' + e.time + '</div>' : '') +
        (desc ? '<div class="ds">' + desc + '</div>' : '') +
        '</div></div>';
    }).join('');
    modalBody.innerHTML = '<h3>' + heading + '</h3>' + rows;
    overlay.classList.add('show');
  }
  function closeModal(){ overlay.classList.remove('show'); }

  document.getElementById('calPrev').addEventListener('click', function(){
    viewMonth--; if (viewMonth < 0) { viewMonth = 11; viewYear--; } render();
  });
  document.getElementById('calNext').addEventListener('click', function(){
    viewMonth++; if (viewMonth > 11) { viewMonth = 0; viewYear++; } render();
  });
  document.getElementById('calModalClose').addEventListener('click', closeModal);
  overlay.addEventListener('click', function(e){ if (e.target === overlay) closeModal(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') closeModal(); });

  var langBtn = document.getElementById('langToggle');
  if (langBtn) langBtn.addEventListener('click', function(){ setTimeout(render, 0); });

  render();
})();
</script>
"""


def _events_by_date():
    """Validate + group CALENDAR_EVENTS by date, sorted chronologically within
    each day in the order given. Bad/unparseable dates are skipped with a
    printed warning rather than crashing the whole site build."""
    out = {}
    for ev in getattr(C, "CALENDAR_EVENTS", []) or []:
        d = ev.get("date", "")
        try:
            datetime.date.fromisoformat(d)
        except Exception:
            print(f"  [calendar] skipping event with bad date {d!r}: {ev.get('title')!r}")
            continue
        out.setdefault(d, []).append({
            "type": ev.get("type", "event"),
            "title": ev.get("title", ""),
            "time": ev.get("time", ""),
            "desc": ev.get("desc", ""),
            "title_es": ev.get("title_es", ""),
            "desc_es": ev.get("desc_es", ""),
        })
    return out


def _legend_html(events_by_date):
    types = getattr(C, "CALENDAR_EVENT_TYPES", {}) or {}
    used, seen = [], set()
    for evs in events_by_date.values():
        for e in evs:
            if e["type"] not in seen:
                seen.add(e["type"])
                used.append(e["type"])
    chips = []
    for t in used:
        icon, label = types.get(t, ("•", t.title()))
        chips.append(f'<span class="cal-legend-chip"><span class="ic">{icon}</span>{label}</span>')
    return '<div class="cal-legend">' + "".join(chips) + "</div>" if chips else ""


def build():
    events = getattr(C, "CALENDAR_EVENTS", None)
    if not events:
        print("CALENDAR_EVENTS is empty -- skipping calendar page.")
        return

    events_by_date = _events_by_date()
    if not events_by_date:
        print("No CALENDAR_EVENTS with valid dates -- skipping calendar page.")
        return

    types = getattr(C, "CALENDAR_EVENT_TYPES", {}) or {}

    title = f"Calendar - {C.BUSINESS_NAME}"
    desc = f"Upcoming events at {C.BUSINESS_NAME}."
    page_tag = getattr(C, "CALENDAR_PAGE_TAG", "CALENDAR")
    page_title = getattr(C, "CALENDAR_PAGE_TITLE", "What's Happening")
    page_intro = getattr(C, "CALENDAR_PAGE_INTRO", "")
    tag_es = ES.NAV_ES.get("CALENDAR", page_tag)
    intro_es = getattr(ES, "CALENDAR_PAGE_INTRO_ES", page_intro)
    intro_html = f'<p class="lead" data-es="{intro_es}">{page_intro}</p>' if page_intro else ""
    order_label_es = getattr(ES, "ORDER_LABEL_ES", C.ORDER_LABEL)
    call_label_es = getattr(ES, "CALL_LABEL_ES", "CALL")

    events_json = json.dumps(events_by_date, ensure_ascii=False).replace("</script>", "<\\/script>")
    types_json = json.dumps(types, ensure_ascii=False).replace("</script>", "<\\/script>")
    js = CALENDAR_JS.replace("__EVENTS_JSON__", events_json).replace("__TYPES_JSON__", types_json)

    body = f"""{S.nav('calendar')}
<div class="cal-wrap" id="calendar" data-section="CALENDAR">
  <div class="cal-hero" data-section="CALENDAR-HERO">
    <span class="sec-tag" data-es="{tag_es}">{page_tag}</span>
    <h2>{page_title}</h2>
    {intro_html}
  </div>
  <div class="cal-nav-row">
    <button class="cal-nav-btn" id="calPrev" type="button" aria-label="Previous month">&#8249;</button>
    <div class="cal-month-label" id="calMonthLabel"></div>
    <button class="cal-nav-btn" id="calNext" type="button" aria-label="Next month">&#8250;</button>
  </div>
  <div class="cal-grid" id="calWeekdays"></div>
  <div class="cal-grid" id="calGrid" style="margin-top:4px"></div>
  {_legend_html(events_by_date)}
  <div class="cta-buttons" style="margin-top:30px;justify-content:center">
    <a class="btn btn-primary" href="{C.ORDER_URL}" target="_blank" rel="noopener" data-es="{order_label_es}">{C.ORDER_LABEL}</a>
    <a class="btn btn-ghost" href="tel:{C.PHONE_TEL}" data-es="{call_label_es} {C.PHONE_DISPLAY}">CALL {C.PHONE_DISPLAY}</a>
  </div>
</div>
<div class="cal-modal-overlay" id="calModalOverlay">
  <div class="cal-modal">
    <button class="cal-modal-close" id="calModalClose" type="button" aria-label="Close">&times;</button>
    <div id="calModalBody"></div>
  </div>
</div>
{S.footer()}"""

    html = (S.head(title, desc, "calendar.html") + "<style>" + CALENDAR_CSS + "</style>"
            + S.age_gate() + body + S.back_to_top() + js + S.close_html())
    S.write_two_copies("calendar", html)


if __name__ == "__main__":
    build()
