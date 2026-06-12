# v18 Step 5 · Stem Engine Safe Runner

## Ziel

Der Stem Lab Reiter bekommt einen kontrollierten produktiven Runner für Demucs, bleibt aber safe-first. Demucs wird nur nach sauberem Preflight gestartet.

## Neue Engine-Funktionen

- `execute_stem_job()`
- `qc_stem_outputs()`
- `derive_synths_keys_approx()`
- `load_stem_run_history()` / `save_stem_run_history()`
- `stem_safe_runner_smoke()`

## Neue GUI-Funktionen

- Safe Runner starten
- Abbrechen
- Progress-Bar
- Preflight blockiert riskante Runs
- Run Result inklusive QC und History

## Neue Commands

```bash
python lucy.py --stems-runner-smoke
python lucy.py --stems-dry-run path/to/song.wav
python lucy.py --stems-run path/to/song.wav
python lucy.py --stems-history
```

## Safe-Entscheidung

Demucs wird nicht gestartet, wenn Preflight-Warnungen vorhanden sind. Ohne Demucs-Installation wird der Runner sauber blockiert und erklärt den Grund.

## Teststatus

- compileall: OK
- stems-runner-smoke: OK
- stems-tab-smoke: OK
- modular smoke: OK
- health: OK
