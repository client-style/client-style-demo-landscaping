# Fernhollow Landscape Co. (Demo Landscaping) - LOG

Reverse-chronological. Each entry has a date and time (Pacific).

## CURRENT STATUS (as of 2026-10-09 10:37 PT)
- Built from the Demo Diner copy and **deployed once by hand** to Client Style's Cloudflare account (Client@maintain.style, 4e36bf72...): project `demo-landscaping`, live at https://demo-landscaping-2nd.pages.dev (200 on /, /menu.html, /quote.html; noindex; 0 broken images).
- **Not done (needs George):** GitHub repo `client-style/client-style-demo-landscaping`, repo secret CLOUDFLARE_API_TOKEN, worker secret GITHUB_TOKEN_DEMO_LANDSCAPING, register the site in Client Style admin and link it to the `demodiner` owner login (so the switcher shows both sites), then tag `demo-baseline`.

## 2026-10-09 10:37 PT - Created
- George asked for another demo site (not a restaurant, new hero) so agents can show the site switcher on one login. Chose a fictional landscaping company, Fernhollow Landscape Co.
- New hero style `seasons` (four season photo panels, active one opens wide, auto-cycles; markup in build_homepage.py, CSS/JS in theme.py, data in HERO_SEASONS). No other site uses it.
- Reuses the menu builder as "Services & prices" (NAV_MENU_LABEL, MENU_PAGE_* settings) and the reserve builder as a free-quote page written to quote.html (RESERVE_FILE). Small config hooks added to site_common.py, build_homepage.py, build_menu_items.py, build_all.py of THIS copy only; the template is unchanged.
- 11 Pexels photos downloaded to INCOMING with George's go-ahead (CREDITS.txt), cropped by WORKING/prep_images.py. Palette: forest green, marigold, leaf green; fonts Fraunces + DM Sans.
- Checked: desktop + 390px phone (no horizontal overflow), hero hover/autoplay, Spanish strings present for every page.
- Deploy gotcha unchanged: clear CLOUDFLARE_API_TOKEN/ACCOUNT_ID env vars and confirm `wrangler whoami` = client@maintain.style first. Cloudflare gave the name demo-landscaping-2nd.pages.dev (demo-landscaping was taken).

## 2026-10-09 - Fully connected
- Auto-deploy green (GitHub Actions -> Cloudflare Pages). Registered in client.style/admin (owner: client-style, repo: client-style-demo-landscaping) and linked to the demodiner owner login; site switcher shows both sites.
- Note: admin 'Add a site' form defaults GitHub owner to Admin-mAIntAIn-Style; must be changed to client-style for Client Style sites.
