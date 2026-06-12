# Hotfix: Stem Environment Doctor

## Why
TorchCodec is not an NVIDIA requirement. The reported issue is caused by an incompatible Windows Stem environment:

- Python 3.14
- PyTorch/TorchAudio newer save pipeline
- TorchCodec installed but not loadable
- FFmpeg DLL/shared-library compatibility

## What changed

- TorchCodec is no longer treated as a hard requirement.
- `--stems-env-doctor` was added for a human-readable Stem environment diagnosis.
- `--stems-stable-install` prints the recommended Windows commands.
- Stem Safe Runner now performs a deep compatibility check before heavy Demucs work.
- Python 3.13/3.14 + risky TorchAudio/TorchCodec combinations are blocked before a long run.
- Requirements no longer force `torchcodec`.

## Recommended Stem setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip uninstall -y torch torchaudio torchcodec demucs
python -m pip install numpy Pillow psutil keyring soundfile
python -m pip install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cpu
python -m pip install demucs
python lucy.py --stems-env-doctor
```

## Commands

```bash
python lucy.py --stems-env-doctor
python lucy.py --stems-stable-install
python lucy.py --stems-runner-smoke
```
