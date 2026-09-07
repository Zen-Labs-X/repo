# v0.1

First release.

Bionic-reading style **meta guiding** for EPUB books on KOReader — bolds the first letters of each word to guide eye fixation, by rewriting a copy of the book. Works on any KOReader build (no engine changes).

**Modes** (Tools → Typesetting → "Meta guiding (bionic)"):
- **Apply to this file (in place)** — rewrites the current EPUB, keeps a one-time `.orig` backup, reopens at your position.
- **Restore original** — reverts from the backup (position kept via XPointer, with a percentage fallback).
- **Generate a separate copy** — original untouched.

UTF-8-safe tokenization; the XHTML scan preserves tags, entities, CDATA, comments and opaque/already-bold elements.

**Install:** clone into KOReader's `plugins/` so the folder is `plugins/metaguiding.koplugin/`, then restart KOReader.
