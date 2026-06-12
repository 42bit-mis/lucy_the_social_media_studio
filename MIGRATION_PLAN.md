# Lucy v17 Migration Plan · Status after Step 15

Completed so far:

1. Step 1: modular launcher, config, paths, security, logging.
2. Step 2: ffmpeg utils, project storage, API key facade, reports.
3. Step 3: platform wrappers.
4. Step 4: platform auth/capabilities.
5. Step 5: core engine shells.
6. Step 6: GUI tab shells and registry.
7. Step 7: Update & Health real modular tab.
8. Step 8: API Keys / Credential Center real modular tab.
9. Step 9: Audio Extractor real modular tab.
10. Step 10: Insights Dashboard real modular tab.
11. Step 11: Posting Cockpit real modular tab.
12. Step 12: LinkedIn Hub real modular tab.
13. Step 13: Campaign Studio real modular tab.
14. Step 14: Stem Lab safe planning/preflight tab.
15. Step 15: Video Composer safe planning/asset/encoder tab.

Next recommended step:

Step 17: start screen + modular main shell that can show migrated tabs together in a separate experimental window, while legacy remains the default production GUI.


## Step 17 completed

- Added `gui/main_shell.py`.
- Added `--modular-gui`, `--modular-main-smoke`, and `--modular-tabs`.
- All migrated real tabs can now run together in one experimental modular Notebook.
- Legacy v16 remains the default and fallback GUI.

## Next Step 17 recommendation

Start integrating the modular shell as an optional launcher choice inside the legacy workflow, then begin migrating one riskier engine at a time: first Audio Extractor full execution polish, then Posting API actions, then Video render pipeline, then Stem/Demucs execution.
