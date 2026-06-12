# Hotfix: Global Mousewheel + TorchCodec Preflight

## Fixes
- Globaler Mousewheel-Router für Legacy-GUI und Modular Shell.
- Scrollen funktioniert über Labels, Buttons, Entries und Comboboxes innerhalb der Reiter.
- Entfernt Enter/Leave-Unbind-Probleme, die Scrollen über Child-Widgets blockiert haben.
- Stem Preflight prüft nun TorchCodec.
- Verhindert Demucs-Abbruch nach 100% mit: `TorchCodec is required for save_with_torchcodec`.
- `requirements-stems.txt` enthält nun `torchcodec`.

## User-Fix falls Stem Preflight TorchCodec meldet
```bash
pip install torchcodec
```
