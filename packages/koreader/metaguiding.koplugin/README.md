# metaguiding.koplugin

A KOReader plugin that adds [bionic-reading](https://en.wikipedia.org/wiki/Bionic_Reading)-style **meta guiding** to EPUB books: the first letters of each word are bolded to guide eye fixation.

It works on **any** KOReader build by rewriting the book's text (wrapping word prefixes in `<b>`), so no engine/native changes are needed.

## How it works

| Before | After — *Apply to this file* |
|:---:|:---:|
| ![Original text](docs/before.jpg) | ![Bionic text](docs/after.jpg) |

The first letters of each word are bolded to guide your eyes. Found under **Tools → Typesetting → "Meta guiding (bionic)"**:

| Typesetting menu | Modes |
|:---:|:---:|
| ![Typesetting menu entry](docs/menu.jpg) | ![Apply / Restore / Generate](docs/modes.jpg) |

## Modes (Tools → Typesetting → "Meta guiding (bionic)")

1. **Apply to this file (in place)** — rewrites the current EPUB, keeping a one-time `.orig` backup, and reopens at your position. Best for day-to-day use.
2. **Restore original** — reverts from the `.orig` backup.
3. **Generate a separate copy** — writes a transformed copy elsewhere and opens it; the original is never modified.

### Notes
- Word prefix = `clamp(ceil(len * 0.5), 1, 4)` characters; words shorter than 2 chars are left as-is. UTF-8 safe (accented Latin, Cyrillic, Greek). CJK gets one "word" per ideograph.
- The transform preserves tags, entities (`Tom &amp; Jerry`), CDATA, comments, and the content of `<script>/<style>/<head>/<code>/<pre>` and pre-existing `<b>/<strong>`.
- **Reading position:** Apply keeps it via KOReader's own XPointer restore. Restore keeps it too, except it may land ±1–2 pages off if you navigated within the transformed version before restoring (the bolded DOM and the original paginate slightly differently). This is inherent to rewriting the file.
- If your document metadata is **hash-based**, rewriting the file changes its hash and can detach reading progress/annotations — use "Generate a separate copy" in that case.

## Install

Put the `metaguiding.koplugin/` folder into your KOReader `plugins/` directory:

| Device | Path |
|---|---|
| Kobo | `.adds/koreader/plugins/` |
| Kindle | `koreader/plugins/` |
| Android | `koreader/plugins/` under the app's data dir |
| Linux desktop | `~/.config/koreader/plugins/` |

**Download (recommended):** grab [`metaguiding.koplugin-0.1.zip`](https://github.com/luizcorreia/metaguiding.koplugin/releases/latest) from the [Releases](https://github.com/luizcorreia/metaguiding.koplugin/releases) page and extract it into `plugins/` (it already contains the `metaguiding.koplugin/` folder).

**Or clone:**
```sh
cd /path/to/koreader/plugins
git clone git@github.com:luizcorreia/metaguiding.koplugin.git
```

Restart KOReader. Generated copies land in `<koreader-data-dir>/metaguiding/`.

## Files
- `main.lua` — menu + the three modes.
- `bionic_transform.lua` — UTF-8 word tokenization + prefix wrapping.
- `xhtml_processor.lua` — state-machine scan that bolds only real text.
- `epub_processor.lua` — unpack/transform/repack via `ffi/archiver`.

## Tests
```sh
luajit tests/run_tests.lua                  # unit tests (no KOReader needed)
python3 tests/fixtures/make_epub.py         # build a sample EPUB
KOREADER_DIR=/path/to/koreader \
  luajit tests/run_e2e.lua                  # end-to-end via real ffi/archiver
python3 tests/verify_epub.py                # assertions on the generated EPUB
```
