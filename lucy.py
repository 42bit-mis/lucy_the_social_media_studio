#!/usr/bin/env python3
"""Lucy v18 Step 7 modular launcher.

Keeps the full v16 app as social_media_studio.legacy_app while exposing
a modular production candidate via --modular-gui.
"""
from social_media_studio.app import main

if __name__ == "__main__":
    raise SystemExit(main())
