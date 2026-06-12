# Lucy v17 Step 17 Test Report

## Scope

Step 17 introduces the experimental Modular Main Shell. The default launcher still starts the v16 legacy GUI unless `--modular-gui` is used.

## Checks performed

- `python -m compileall -q .` → OK
- `python lucy.py --modular-main-smoke` → OK, 9/9 modular tabs
- `python lucy.py --modular-tabs` → OK
- `python lucy.py --smoke` → OK, 37 OK · 0 Fehler
- `python lucy.py --health` → OK, 92/100
- `python lucy.py --legacy-smoke` → OK, 10 OK · 0 Fehler
- `xvfb-run python lucy.py --modular-gui` → no start crash; process timed out because window stayed open
- `xvfb-run python lucy.py` → no start crash; process timed out because legacy window stayed open

## Safe notes

- The new modular GUI is opt-in via `--modular-gui`.
- `python lucy.py` still starts the v16 legacy fallback.
- Full render/Demucs/live API execution remains protected behind planning/dry-run layers.
