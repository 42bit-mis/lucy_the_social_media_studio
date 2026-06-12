# Lucy v17 Step 18 · Start Here

## Sicher starten

```bash
python lucy.py
```

Der Startscreen bietet:

- **Legacy Safe Mode**: stabile v16-GUI für echte Arbeit.
- **Modular Preview Mode**: neue modulare GUI mit Command Center und migrierten Reitern.
- **Health + Smoke**: Diagnose.
- **Backup**: sichere State-Sicherung.

## Direkte Befehle

```bash
python lucy.py --legacy-gui
python lucy.py --modular-gui
python lucy.py --health
python lucy.py --smoke
python lucy.py --integration-smoke
python lucy.py --release-docs
```

## Safe-Regel

Riskante Produktivpfade bleiben noch geschützt: Full Visualizer Render, Full Demucs Run und echte Live-API-Posts werden später einzeln migriert.


## v18 Step 1 · Audio Engine Finalization

Der Audio Extractor ist der erste wirklich produktiv modularisierte Reiter. `core/audio_engine.py` kann jetzt echte ffmpeg-Exports ausführen, Progress melden, Cancel beachten, QC nach dem Export ausführen und eine Audio-Export-History schreiben.

Neue Commands:

```bash
python lucy.py --audio-export-smoke
python lucy.py --audio-execute path/to/file.wav --audio-profile mp3_320
python lucy.py --audio-history
```


## Current Package
This archive is **v18 Step 1 · Audio Engine Finalization**. The first productive modular engine is the Audio Extractor. Legacy v16 remains available as fallback.


## v18 Step 2 · Insights Engine Finalization

The Insights Dashboard is now the second productive modular area. It adds productive local analysis, track-growth tables, data quality scoring, bundle export, demo analysis, and import/export helpers.

Commands:

```bash
python lucy.py --insights-productive-smoke
python lucy.py --insights-demo
python lucy.py --insights-bundle
python lucy.py --insights-import path/to/snapshot.json
```

## v18 Step 7 · App Mode RC

Neue App-Modus-Befehle:

```bash
python lucy.py --mode-status
python lucy.py --set-default-mode modular
python lucy.py --launch-default
python lucy.py --safe-start
```

`python lucy.py` bleibt der sichere Startscreen. Legacy bleibt Fallback.


## v18 Step 8 RC Hardening

Nutze `python lucy.py --rc-status`, um zu sehen, ob diese Version bereit zum Testen ist.
Nutze `python lucy.py --rc-package`, um Manifest, Testmatrix und RC-Report zu erzeugen.
