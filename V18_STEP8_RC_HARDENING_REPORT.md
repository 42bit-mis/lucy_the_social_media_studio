# Lucy v18 Step 8 · RC Hardening

## Ziel
Release-Candidate-Härtung der modularen Lucy-App. Keine riskanten neuen Engines, sondern Readiness, Testmatrix, Manifest, RC-Artefakte und Command-Center-Erweiterung.

## Neue Commands

```bash
python lucy.py --rc-status
python lucy.py --rc-smoke
python lucy.py --rc-test-matrix
python lucy.py --rc-manifest
python lucy.py --rc-package
python lucy.py --ready-for-testing
```

## Safe-Prinzip
Legacy bleibt enthalten. Modular ist Production Candidate, aber riskante Live-API-Posts, Full Demucs und Full Legacy Visualizer-Migration bleiben kontrolliert.
