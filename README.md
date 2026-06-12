# Lucy v17 Modular Step 17 · Modular Main Shell

Step 17 introduces the first experimental modular main GUI. It assembles all migrated real tabs into one Tk/ttk Notebook while keeping the full v16 GUI in `social_media_studio/legacy_app.py` as the safe fallback.

## Modular tabs in the new shell

- Update & Health
- API Keys / Credential Center
- Campaign Studio
- Video Composer (safe planning mode)
- Audio Extractor
- Stem Lab (safe planning/preflight mode)
- Posting Cockpit (review/dry-run mode)
- Insights Dashboard
- LinkedIn Hub

## Safe default

`python lucy.py` still starts the legacy v16 GUI.

The new modular shell starts only when requested:

```bash
python lucy.py --modular-gui
```

## Useful commands

```bash
python lucy.py --modular-main-smoke
python lucy.py --modular-tabs
python lucy.py --smoke
python lucy.py --health
python lucy.py --legacy-smoke
```

## Step 17 design decision

This is the first combined modular GUI, not the final production GUI. Full rendering, full Demucs automation and live API posting remain protected by safe planning/dry-run layers until they are migrated and tested one by one.


## Hotfix Navigation

Legacy Safe GUI und Modular Preview Shell haben oben rechts jetzt einen Button **🏠 Startmenü**. Der Button öffnet den Startscreen in einem neuen sicheren Prozess und schließt das aktuelle Fenster.


## Step 17 Health Polish

Lucy unterscheidet jetzt professionelle Health-Profile:

- Local Studio Health: lokale App-Bereitschaft ohne Tokens/Demucs.
- Production/API Health: Tokens, Plattform-Readiness und sichere Credentials.
- AI/Stem Health: PyTorch, Demucs und Stem-Bereitschaft.
- Overall Health: gewichtete Gesamtbewertung.

Dadurch kann eine lokale Entwicklungs-/Studio-Umgebung fair 100/100 erreichen, auch wenn optionale Plattform-Tokens oder Demucs noch fehlen.


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
