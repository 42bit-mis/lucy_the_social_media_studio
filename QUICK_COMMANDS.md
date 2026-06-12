# Lucy Quick Commands

```bash
python lucy.py                         # Startscreen
python lucy.py --legacy-gui            # sichere v16 Legacy-GUI
python lucy.py --modular-gui           # neue modulare Preview-GUI
python lucy.py --health                # Health Profile
python lucy.py --smoke                 # modulare Smoke-Tests
python lucy.py --integration-smoke     # Step-18 Integrationscheck
python lucy.py --backup                # Settings/Histories sichern
python lucy.py --legacy-smoke          # Legacy-v16 Smoke-Test
python lucy.py --modular-main-smoke    # modulare Shell prüfen
python lucy.py --release-docs          # Release-Dokumente erzeugen
```

## v18 Step 3 · Campaign Engine
```bash
python lucy.py --campaign-productive-smoke
python lucy.py --campaign-demo
python lucy.py --campaign-bundle
python lucy.py --campaign-task-board
python lucy.py --campaign-tab-preview
```


## v18 Step 6 · Video Render Engine
```bash
python lucy.py --video-preview-smoke
python lucy.py --video-preview-render path/to/audio.wav
python lucy.py --video-preview-render path/to/audio.wav --video-cover cover.png --video-output preview.mp4
python lucy.py --video-history
python lucy.py --video-tab-preview
```


## v18 Step 9 Distribution Commands

```bash
python lucy.py --distribution-status
python lucy.py --distribution-smoke
python lucy.py --write-launchers
python lucy.py --write-installers
python lucy.py --clean-source-zip
```
