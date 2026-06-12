# Hotfix: Stem Demucs Segment auf safe integer 7

## Problem aus Log

Demucs startete mit:

```text
--segment 8
```

Danach brach Demucs ab:

```text
FATAL: Cannot use a Transformer model with a longer segment than it was trained for. Maximum segment is: 7.8
```

## Ursache

Der vorherige Hotfix hat `7.8` auf `8` gerundet, damit ältere Demucs-CLI-Versionen keinen Float-Fehler werfen. Für `htdemucs` ist `8` aber zu lang, weil das Modell maximal `7.8` erlaubt.

## Lösung

Demucs bekommt jetzt einen sicheren Integer-Floor:

```text
7.8 -> 7
10  -> 7
12  -> 7
```

Dadurch wird sowohl der CLI-Integer-Fehler als auch der Transformer-Max-Segment-Fehler vermieden.

## Geänderte Dateien

```text
social_media_studio/core/stem_engine.py
social_media_studio/legacy_app.py
```

## Tests

```text
compileall: OK
stems-dry-run: OK, Command enthält --segment 7
stems-runner-smoke: OK
stems-tab-smoke: OK
modular smoke: OK
legacy smoke: OK
```
