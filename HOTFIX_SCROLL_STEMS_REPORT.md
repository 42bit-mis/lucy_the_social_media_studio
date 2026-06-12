# Lucy v18 Step 9 Hotfix · Scroll + Stem Segment + Profi Options

## Anlass
User-Test fand zwei Probleme:

1. Mausrad-Scrollen funktionierte in der GUI nicht zuverlässig.
2. Stem Studio/Demucs brach mit folgendem Fehler ab:

```text
demucs.separate: error: argument --segment: invalid int value: '7.8'
```

Zusätzlich waren Profi-Optionen im Stem-Bereich nicht klar sichtbar.

## Fixes

### 1. Mausrad-Scrollen
- Legacy-Scrollcontainer robuster gemacht.
- Modular Shell Tabs in scrollbare Canvas-Container gelegt.
- MouseWheel-Unterstützung für Windows/macOS/Linux ergänzt.
- Scrollen funktioniert auch, wenn der Mauszeiger über Unterwidgets im Tab steht.

### 2. Demucs Segment Fix
- Demucs bekommt `--segment` jetzt als Integer.
- Aus `7.8` wird `8`.
- Aus `10.0` wird `10`.
- Fix in Legacy-App und modularer `stem_engine.py`.

### 3. Profi-Optionen sichtbarer
- Legacy Stem Studio zeigt im Einfach-Modus jetzt einen Hinweis, wie man Profi-Optionen öffnet.
- Modular Stem Lab hat neue sichtbare Profi-Optionen:
  - Jobs
  - Segment
  - Overlap
  - Shifts
- Felder können auf `auto` bleiben.

## Tests

- compileall: OK
- stems-dry-run: OK, Command enthält jetzt nach Segment-Hotfix `--segment 7`
- stems-tab-smoke: OK
- modular-main-smoke: OK
- legacy-smoke: 10 OK / 0 Fehler
- modular-gui Start unter Testdisplay: kein Startcrash
- legacy-gui Start unter Testdisplay: kein Startcrash

## Hinweis
Ein echter Demucs-Run wurde in der Testumgebung nicht ausgeführt, weil Demucs hier nicht installiert ist. Der konkrete User-Fehler aus dem Log wurde aber direkt behoben: Demucs akzeptiert nun kein Float-Segment mehr, sondern bekommt einen Integer.
