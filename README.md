# Fernhollow Landscape Co. (demo)

A **fictional** landscaping company, the **second demo site** next to Demo Diner. Two jobs:

1. **Sales demos for agents**: one Client Style login (`demodiner`) owns two sites, so the demo can show the site switcher, then edit a restaurant and a non-restaurant business.
2. **Safe testing** of Client Style on a business that is not a restaurant.

Nothing here is real: 555 phone, placeholder address, example.com email, made-up prices. A green ribbon on every page says so. Hidden from Google (`NOINDEX = True`).

## What's special about this build
- **Seasons hero** (`HERO_STYLE = "seasons"`): four photo panels (spring, summer, fall, winter); the active one opens wide, the rest fold to strips. Hover, tap or Tab picks one; it cycles every 5 seconds. A new hero style, used by no other site (others: classic, collage, fullbleed, diagonal, parallax). Code: `build_homepage.py` (markup), `theme.py` (CSS + JS). Photos and captions come from `HERO_SEASONS` in `brand_config.py`.
- **Look** in `build-scripts/theme.py`: forest green, marigold, leaf-green glow, Fraunces + DM Sans.
- **Services & prices page** (`menu.html`) reuses the menu builder, so Client Style's *Menu & prices* tab edits services; six sections, photos on some items (`MENU_ITEM_IMAGES = True`).
- **Free quote page** (`quote.html`, built by `build_reserve.py`) with radios and checkboxes left in default browser style on purpose, the same demo moment as Demo Diner.
- **Spanish toggle** (ESP/ENG) on every page (`es_translations.py`).
- **Client Style hooks**: `CUSTOM_CSS` / `CUSTOM_JS` in `brand_config.py`.

## Things to try in a demo (type into Client Style)
1. "Change this month's offer to Spring Cleanup Package for $199."
2. "Add Lawn Dethatching to Lawn Care for $120."
3. "Change our hours to Mon-Sat 6am-6pm."
4. "Make the checkboxes and radio buttons on the quote page green with a check mark when selected."
5. "Add a banner that says We're closed Thanksgiving Day."
6. Schedule a change for later, then show it go live and undo it.
7. Use the site switcher to jump between Demo Diner and Fernhollow.

## Rebuild by hand
```
python build-scripts/build_all.py
```
Pages are written to the folder root and to `site/`. Only `site/` is deployed (CI copies `assets/` into it).

## Reset between demos
`reset_demo.ps1` puts every tracked file back to the `demo-baseline` tag (create the tag after the first deploy).

## Photos
Free-license Pexels photos, see `CREDITS.txt`.
