# Lucy Stem Environment Fix

TorchCodec is **not** an NVIDIA requirement. Your issue is a compatibility problem between Python 3.14, PyTorch/TorchAudio and TorchCodec/FFmpeg DLL loading on Windows.

Recommended stable setup:

```powershell
cd C:\Path\To\Lucy
py -3.12 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip uninstall -y torch torchaudio torchcodec demucs
python -m pip install numpy Pillow psutil keyring soundfile
python -m pip install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cpu
python -m pip install demucs
python -m demucs --help
```

Use:

```powershell
python lucy.py --stems-env-doctor
```

Do not use global Python 3.14 for Stem Lab.
