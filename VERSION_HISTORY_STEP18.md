# Lucy v17 · Step 18

## Modular App Integration Polish

Neu:

- Startscreen zeigt Health-Profile direkt.
- Modular Shell zeigt Local/API/AI/Overall Health oben an.
- Command Center als sicherer modularer Reiter.
- Neue CLI-Befehle: `--integration-smoke`, `--release-docs`, `--command-center-smoke`.
- Release-Dokumente vorbereitet: README_START_HERE, QUICK_COMMANDS, VERSION_HISTORY_STEP18.
- Smoke-Test erweitert auf Command Center, Startscreen und Release Docs.

## Status

- Legacy Safe GUI bleibt vollständig enthalten.
- Modular Preview GUI bleibt opt-in.
- Riskante Engines bleiben geschützt.


## v18 Step 1 · Audio Engine Finalization

Der Audio Extractor ist der erste wirklich produktiv modularisierte Reiter. `core/audio_engine.py` kann jetzt echte ffmpeg-Exports ausführen, Progress melden, Cancel beachten, QC nach dem Export ausführen und eine Audio-Export-History schreiben.

Neue Commands:

```bash
python lucy.py --audio-export-smoke
python lucy.py --audio-execute path/to/file.wav --audio-profile mp3_320
python lucy.py --audio-history
```


## v18 Step 2 · Insights Engine Finalization

The Insights Dashboard is now the second productive modular area. It adds productive local analysis, track-growth tables, data quality scoring, bundle export, demo analysis, and import/export helpers.

Commands:

```bash
python lucy.py --insights-productive-smoke
python lucy.py --insights-demo
python lucy.py --insights-bundle
python lucy.py --insights-import path/to/snapshot.json
```


## v18 Step 6 · Video Render Engine Migration

Der Video Composer bekommt einen produktiven modularen Safe Preview Render. Der Full Visualizer bleibt bewusst in Legacy geschützt.

Commands:
```bash
python lucy.py --video-preview-smoke
python lucy.py --video-preview-render path/to/audio.wav
python lucy.py --video-history
```
