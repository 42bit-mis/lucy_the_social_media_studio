# Lucy v18 Step 7 · Modular App Mode RC

## Ziel
Die modulare GUI ist jetzt als **Modular Production Candidate** klar wählbar. Legacy bleibt Safe-Fallback.

## Neu
- `social_media_studio/core/app_modes.py`
- Persistenter Default-Modus: `start`, `legacy`, `modular`
- Startscreen zeigt Default-Modus und kann ihn setzen
- `--launch-default` startet den gespeicherten Default
- `--safe-start` führt Smoke/Health aus und startet den empfohlenen sicheren Modus
- Modular Shell Branding von Preview auf Production Candidate aktualisiert
- doppeltes `tk.Tk()` in `main_shell.py` behoben

## Neue Commands
```bash
python lucy.py --mode-status
python lucy.py --set-default-mode start
python lucy.py --set-default-mode legacy
python lucy.py --set-default-mode modular
python lucy.py --launch-default
python lucy.py --safe-start
python lucy.py --app-mode-smoke
```

## Sicherheit
- `python lucy.py` öffnet weiter den Startscreen.
- Legacy bleibt jederzeit über `python lucy.py --legacy-gui` verfügbar.
- Modular Candidate bleibt bewusst wählbar über `python lucy.py --modular-gui`.
