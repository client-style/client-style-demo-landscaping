# -*- coding: utf-8 -*-
"""
build_all.py -- one command to (re)build the whole site from brand_config.py.
    python build-scripts/build_all.py
Picks the right menu builder from MENU_MODE, builds catering if enabled, and
regenerates the client guide PDFs (needs reportlab: pip install reportlab).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_config as C

def main():
    print("=== Building", C.BUSINESS_NAME, "site ===")
    import build_homepage; build_homepage.build()

    if C.MENU_MODE == "embed":
        import build_menu_embed; build_menu_embed.build()
    elif C.MENU_MODE == "items":
        import build_menu_items; build_menu_items.build()
    else:
        print("MENU_MODE = none -- no menu page.")

    if C.CATERING_ENABLED:
        import build_catering; build_catering.build()

    if getattr(C, "CALENDAR_EVENTS", None):
        import build_calendar_page; build_calendar_page.build()

    if getattr(C, "RESERVE_ENABLED", False):
        import build_reserve; build_reserve.build()

    # robots.txt + sitemap.xml for every page actually built (2026-09-27).
    import site_common as S
    site_dir = os.path.join(S.ROOT, "site")
    pages = [""] + [f for f in ("menu.html", "catering.html", "specials.html", "calendar.html", getattr(C, "RESERVE_FILE", "reserve.html"))
                    if os.path.exists(os.path.join(site_dir, f))]
    S.write_seo_files(pages)

    # Guides are optional (require reportlab). Don't fail the site build if missing.
    try:
        import editor_guide, setup_guide   # noqa: F401  (these build on import)
        print("Guides rebuilt.")
    except Exception as e:
        print("Guides skipped:", e)

    print("=== Done. Deploy the  site/  folder to Cloudflare Pages. ===")

if __name__ == "__main__":
    main()
