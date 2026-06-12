# v18 Step 1 · Audio Engine Finalization

## Ziel
Der Audio Extractor wird der erste vollständig produktiv modulare Reiter.

## Neu
- `core/audio_engine.py` führt echte ffmpeg-Jobs aus.
- Progress-Callback und Cancel-Check sind angebunden.
- QC nach Export prüft Datei, Audiospur und Dauer.
- Export-History wird geschrieben.
- `tab_audio_extractor_real.py` nutzt jetzt `execute_audio_job()`.

## Commands
```bash
python lucy.py --audio-export-smoke
python lucy.py --audio-execute path/to/source.wav --audio-profile mp3_320
python lucy.py --audio-history
python lucy.py --audio-tab-preview
python lucy.py --smoke
```

## Safe-Fallback
Die vollständige v16 bleibt weiterhin in `social_media_studio/legacy_app.py`.
