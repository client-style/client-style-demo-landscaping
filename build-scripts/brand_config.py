# -*- coding: utf-8 -*-
"""
brand_config.py -- Fernhollow Landscape Co. A FICTIONAL landscaping company used
for sales demos of mAIntAIn Style + Client Style (the second site on the demo
owner login, so agents can show switching between sites). Nothing here is a
real business: phone is a 555 number, the address is a placeholder.
Edit this file (or let Client Style edit it), then run build-scripts/build_all.py.
The look lives in theme.py; the quote form lives in build_reserve.py.
"""

# 1. IDENTITY
BUSINESS_NAME = "Fernhollow Landscape Co."
BRAND_SHORT   = "Fernhollow"
TAGLINE       = "A yard for every season."
SITE_TYPE     = "landscaping"
CITY_STATE    = "Anytown, USA"
ESTABLISHED   = "2009"
BADGE_LINE    = "Design &middot; Install &middot; Year-round care"

# 2. CONTACT (all fictional)
PHONE_DISPLAY = "(555) 010-0142"
PHONE_TEL     = "+15550100142"
ADDRESS_FULL  = "2200 Example Rd, Anytown, USA"
HOURS_TEXT    = "Mon&ndash;Sat 7am&ndash;5pm"
EMAIL         = "hello@example.com"
MAP_EMBED_URL = "https://www.google.com/maps?q=Kansas,USA&z=4&output=embed"   # middle of the map on purpose

# 3. SOCIAL
INSTAGRAM_URL    = ""
INSTAGRAM_HANDLE = ""
FACEBOOK_URL     = ""

# 4. QUOTES / SERVICES PAGE (this site reuses the menu + reserve builders)
ORDER_URL   = "__RESERVE__"          # internal link to the quote page
ORDER_LABEL = "FREE QUOTE"
MENU_MODE      = "items"
MENU_EMBED_URL = ""
NAV_MENU_LABEL    = "SERVICES"
NAV_RESERVE_LABEL = "QUOTE"
MENU_BTN_LABEL    = "See services &amp; prices"
MENU_PAGE_TAG     = "SERVICES"
MENU_PAGE_TITLE   = "Services &amp; prices"
MENU_PAGE_DESC    = "Lawn care, gardens, stonework, trees, irrigation and seasonal care from Fernhollow Landscape Co."
RESERVE_FILE      = "quote.html"

# 5. HOSTING / DEMO SETTINGS
PROJECT_SLUG    = "demo-landscaping"
LIVE_URL        = "https://demo-landscaping-2nd.pages.dev"  
SITE_URL        = ""
SOURCE_OF_TRUTH = "n/a - fictional demo business"
FOOTER_LABEL    = BUSINESS_NAME + " - Website Reference"
NOINDEX         = True     # hide the whole site from Google
RESERVE_ENABLED = True     # builds quote.html (the demo form page)
DEMO_BANNER     = "Demo site &middot; a pretend landscaping company by mAIntAIn Style &mdash; no real quotes, no real crews"

# 6. DESIGN TOKENS (deep forest green + marigold + fresh-leaf glow on warm cream)
COLORS = {
    "primary":        "#0F2A1C",
    "primary_bright": "#1D4A31",
    "glow":           "#9BD87A",
    "accent":         "#F0B33A",
    "accent_deep":    "#D1951F",
    "on_accent":      "#1A1405",
    "cream":          "#F4EFE0",
    "cream_muted":    "#B8C2B0",
    "bg_deep":        "#0B130E",
    "panel":          "#14221A",
    "ink":            "#14221A",
}
FOOTER_GLOW_COLOR    = "glow"
FOOTER_GLOW_STRENGTH = 0.36
FONT_HEADING       = "Fraunces"
FONT_BODY          = "DM Sans"
NAV_WORDMARK_BOLD  = True
GOOGLE_FONTS_HREF  = ("https://fonts.googleapis.com/css2?"
                      "family=Fraunces:wght@500;700&family=DM+Sans:wght@400;500;700&display=swap")

# 7-8. AGE GATE / COMPLIANCE (not needed)
AGE_GATE_ENABLED = False
AGE_GATE_MIN     = 21
AGE_GATE_TITLE   = "Are You 21 or Older?"
AGE_GATE_YES     = "Yes, enter"
AGE_GATE_NO      = "No"
AGE_GATE_BOUNCE  = "https://www.google.com"
AGE_GATE_DAYS    = 30
COMPLIANCE_LINES = []

# 9. HERO -- "seasons": four photo panels, the active one opens wide (new hero style)
LOGO_IMAGE   = ""
HERO_STYLE   = "seasons"
HERO_PHOTO   = "assets/hero_spring.jpg"
HERO_SLIDES  = ["assets/hero_spring.jpg"]
# (photo, name, Spanish name, one-line caption, Spanish caption)
HERO_SEASONS = [
    ("assets/hero_spring.jpg", "Spring", "Primavera", "Cleanups, new beds, first mow", "Limpieza, camas nuevas, primer corte"),
    ("assets/hero_summer.jpg", "Summer", "Verano", "Lawn care, irrigation, patios", "Cuidado del césped, riego, patios"),
    ("assets/hero_fall.jpg",   "Fall",   "Otoño",  "Leaf removal, planting, cutback", "Hojas, siembra, poda de camas"),
    ("assets/hero_winter.jpg", "Winter", "Invierno", "Snow clearing and ice control", "Retiro de nieve y control de hielo"),
]
HERO_HEADING = 'A yard for <span class="nw">every season</span>.'
HERO_SUB     = "Design, planting, stonework and year-round care. From the first tulip to the last snowfall, we keep your yard looking like someone loves it."
FAVICON_IMAGE = "assets/favicon.png"
TOTOP_ICON        = "assets/totop_sprout.svg"
TOTOP_ICON_ROTATE = 0

# 10. TRUST STRIP
TRUST_ITEMS = [
    ("Since " + ESTABLISHED, "Family-run crew"),
    ("Free quotes", "Site visit within the week"),
    ("Year-round", "Mow, plant, build, plow"),
    (HOURS_TEXT.replace("&ndash;", "-"), "Open today"),
]

# 11. FEATURE CARDS (icon, title, description, photo)
FEATURES = [
    ("1", "Lawn care that shows", "Weekly mowing, edging, feeding and aeration on a schedule that fits your lot, so the grass stays thick and even.", "assets/feat_lawn.jpg"),
    ("2", "Patios and stonework", "Flagstone patios, paver walkways and walls laid level and built to last through freeze and thaw.", "assets/feat_patio.jpg"),
    ("3", "Gardens that last", "Beds designed for your light and soil, planted by hand, mulched and edged. Color from spring to frost.", "assets/feat_planting.jpg"),
]

# 12. SPECIALS
SPECIALS_ENABLED = True
SPECIALS_TAG     = "THIS MONTH'S OFFER"
SPECIALS_TITLE   = "Fall Cleanup Package"
SPECIALS_BODY    = "Leaf removal, bed cutback and a final mow for $249 on lots up to a quarter acre. Book by October 31."
SPECIALS_CTA     = ORDER_LABEL

# 13. STORY
STORY_TAG   = "OUR STORY"
STORY_TITLE = "Rooted here since 2009."
STORY_BODY  = ("Fernhollow Landscape Co. is a pretend landscaping company. We built it so you can see exactly what a "
               "mAIntAIn Style website looks like, and how Client Style lets an owner change it just by asking. Swap the "
               "monthly offer, add a service, move the hours. It takes a sentence.")
STORY_IMAGE     = "assets/story_pond.jpg"
STORY_IMAGE_ALT = "Backyard stone pond edged with pavers and gravel"

# 14. CTA BAND
CTA_TITLE      = "Let's walk your yard"
CTA_SUB        = "Tell us what you have in mind and when. The form is a demo, so nothing is sent."
CTA_BUTTON     = ORDER_LABEL
CTA_BUTTON_URL = "__RESERVE__"

# 15. SERVICES & PRICES (fictional; this site reuses the menu builder)
MENU_INTRO = "Everything here is made up for the demo, including the prices."
# Photos: items may carry an optional 4th value, a site image path.
# True tells Client Style that build_menu_items.py can draw it.
MENU_ITEM_IMAGES = True
MENU_SECTIONS = [
    ("Lawn Care", "lawn", [
        ("Weekly Mowing", "Mow, edge, trim and blow clean. Priced per visit by lot size.", "from $55", "assets/feat_lawn.jpg"),
        ("Aeration & Overseed", "Core aeration plus premium seed, spring or fall.", "from $180"),
        ("Fertilizer Program", "A five-step feeding plan through the year.", "$45/visit"),
        ("Spring Cleanup", "Debris out, beds cut back, first mow of the year.", "from $225"),
    ]),
    ("Gardens & Planting", "gardens", [
        ("New Bed Design & Install", "Plan, soil prep, plants and mulch for a bed up to 100 sq ft.", "from $650", "assets/feat_planting.jpg"),
        ("Mulch & Edging", "Fresh mulch two inches deep with a crisp edge.", "$75/yd"),
        ("Seasonal Color Pots", "Planted containers swapped each season.", "$60 each"),
        ("Plant Health Visit", "A walk-through, pruning and a care plan.", "$95"),
    ]),
    ("Patios & Stonework", "stone", [
        ("Flagstone Patio", "Excavation, compacted base and hand-fit flagstone.", "$22/sq ft", "assets/feat_patio.jpg"),
        ("Paver Walkway", "Interlocking pavers in your pattern, edged and sanded.", "$18/sq ft"),
        ("Retaining Wall", "Block or natural stone, drained and backfilled.", "$48/ft"),
        ("Fire Pit Circle", "Stone ring and gravel pad, ready for evenings.", "from $1,400"),
    ]),
    ("Trees & Hedges", "trees", [
        ("Hedge Shaping", "Clean lines and a tidy top, clippings hauled away.", "from $120", "assets/svc_hedge.jpg"),
        ("Shrub Pruning", "Timed for each plant so it blooms and keeps its shape.", "from $85"),
        ("Tree Trimming", "Crown lifting and deadwood removal, up to 15 feet.", "from $200"),
        ("Stump Grinding", "Ground below grade and filled with topsoil.", "from $150"),
    ]),
    ("Irrigation", "irrigation", [
        ("Sprinkler Tune-Up", "Check every zone, fix heads, set the timer.", "$120", "assets/svc_sprinkler.jpg"),
        ("New Zone Install", "Trenched lines, heads and a controller hookup.", "from $850"),
        ("Drip Lines for Beds", "Water where roots need it, nothing wasted.", "from $280"),
        ("Fall Winterize", "Compressed-air blowout before the first freeze.", "$95"),
    ]),
    ("Fall & Winter Care", "seasonal", [
        ("Fall Leaf Removal", "Raked, blown and hauled. Priced by lot size.", "from $160"),
        ("Snow Plowing", "Driveway and walks, per push, with a seasonal option.", "$65/push"),
        ("Steps & Walkway Clearing", "Shoveled by hand and treated with ice melt.", "$40/visit", "assets/svc_snow.jpg"),
        ("Ice Melt Service", "Pet-safe de-icer on walks and steps.", "$25/visit"),
    ]),
]

# 16. CATERING (off)
CATERING_ENABLED  = False
CATERING_INTRO    = ""
CATERING_EMAIL    = EMAIL
CATERING_PACKAGES = []

# CLIENT STYLE HOOKS -- extra styling/scripts added through Client Style's AI
# chat and Add-ons tab. site_common.close_html() writes these last on EVERY
# page. Keep CSS as plain CSS (no <style> tags), JS as plain JavaScript (no
# <script> tags), and write both as raw triple-quoted strings.
CUSTOM_CSS = r"""
"""

CUSTOM_JS = r"""
"""
