# Lucy v18 Step 6 · Video Render Engine Migration

## Ziel
Der Video Composer bekommt den ersten produktiven modularen Safe-Render-Pfad. Der volle Legacy-Visualizer bleibt weiterhin als Fallback geschützt.

## Neu
- `execute_preview_render()`
- `build_safe_preview_render_command()`
- `qc_video_output()`
- `load_video_render_history()` / `save_video_render_history()`
- `video_preview_render_smoke()`
- GUI-Button: Safe Preview rendern
- GUI-Cancel-Vorbereitung

## Neue Commands
```bash
python lucy.py --video-preview-smoke
python lucy.py --video-preview-render path/to/audio.wav
python lucy.py --video-preview-render path/to/audio.wav --video-cover cover.png --video-output preview.mp4
python lucy.py --video-history
python lucy.py --video-tab-preview
```

## Safe Scope
Der modulare Render erzeugt bewusst einen sicheren Poster/Black Preview MP4 mit Audio und QC. Full Visualizer, Timeline, Layer und Batch bleiben bis zur nächsten Engine-Migration im Legacy-Fallback.

## Tests
- compileall OK
- video-preview-smoke OK
- modular smoke 45 OK / 0 Fehler
- health OK
