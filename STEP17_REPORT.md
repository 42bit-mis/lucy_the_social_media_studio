# Lucy v17 Step 17 – Start Screen & App Mode Chooser

## Ziel
Ein sicherer Startbildschirm, der bewusst zwischen Legacy Safe Mode und Modular Preview Mode unterscheidet.

## Neuer Standard
`python lucy.py` startet jetzt den Start Screen.

## Direkte Modi
- `python lucy.py --legacy-gui` startet die stabile v16 Legacy-GUI.
- `python lucy.py --modular-gui` startet die experimentelle modulare Preview-GUI.
- `python lucy.py --start-screen` startet explizit den neuen Start Screen.

## Diagnose
- `python lucy.py --start-screen-smoke`
- `python lucy.py --modular-main-smoke`
- `python lucy.py --smoke`
- `python lucy.py --health`

## Sicherheit
Legacy v16 bleibt vollständig in `social_media_studio/legacy_app.py` enthalten.

## Step 17 Hotfix A – Legacy Button Loop

Fix: `python lucy.py --legacy-gui` now calls `start_legacy_gui()` directly instead of reopening the Start Screen.

Validation:
- compileall: OK
- start-screen-smoke: OK
- modular smoke: OK
- legacy-gui under xvfb: window opened, timeout only because GUI stayed open
- start-screen under xvfb: window opened, timeout only because GUI stayed open
