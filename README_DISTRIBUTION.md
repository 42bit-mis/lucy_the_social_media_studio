# Lucy Distribution Notes

This package is prepared for testing and distribution.

## Start

```bash
python lucy.py
```

## Safe mode

```bash
python lucy.py --legacy-gui
```

## Modular candidate

```bash
python lucy.py --modular-gui
```

## Checks

```bash
python lucy.py --health
python lucy.py --smoke
python lucy.py --ready-for-testing
python lucy.py --distribution-smoke
```

## Install helpers

See `installers/` and `launchers/`.


Stem Lab Hinweis: Bei neuen torchaudio-Versionen benötigt Demucs zum Speichern zusätzlich TorchCodec. Installation: pip install torchcodec
