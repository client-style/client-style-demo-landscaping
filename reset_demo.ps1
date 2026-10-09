# Puts the Fernhollow demo back to its original state (the demo-baseline tag).
# Run from this folder:   powershell -File reset_demo.ps1
# It restores every tracked file, commits, and pushes, so the live demo resets too.
Set-Location $PSScriptRoot
git fetch origin --tags
# Only the site itself is restored. Deploy settings (.github) and the logs are left alone on purpose,
# so a reset can never break auto-deploy or erase LOG.md.
git checkout demo-baseline -- build-scripts assets site fernhollow_landscape_co_homepage.html fernhollow_landscape_co_menu.html fernhollow_landscape_co_reserve.html
if (git diff --cached --quiet) {
    Write-Host "Demo is already at baseline. Nothing to reset."
    exit 0
}
git commit -m "Reset demo to baseline"
git push origin main
Write-Host "Demo reset. The live site rebuilds in about a minute."
