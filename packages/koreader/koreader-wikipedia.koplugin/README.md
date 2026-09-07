# Offline Wikipedia for KOReader (ZIM plugin)

A KOReader plugin that opens [Kiwix ZIM files](https://library.kiwix.org/) **directly** — no conversion, no extraction, no companion server. Search articles, tap links to navigate, walk back through history. Tested against `wikipedia_en_all_mini_2026-03.zim` (19 M articles, 12.4 GB, ZIM v6 with zstd-compressed clusters), but any ZIM from the Kiwix library should work.

> ⚠️ **Disclaimer.** This project — Lua plugin, Python helper, and this README — was generated **entirely by AI**. It has been tested by the author on a Kindle Oasis but comes with **no warranty whatsoever**. Flashing files onto your e-reader, modifying KOReader, or running unofficial plugins can in principle brick the device, corrupt storage, or void warranty. **You use this software at your own risk.** The author accepts no responsibility for damaged devices, lost data, or any other consequence of using this code.

## What's in this repo

```
plugins/wikipediazim.koplugin/
  _meta.lua         plugin metadata
  main.lua          menu, search dialog, history, font-size persistence
  library.lua       auto-discovers ZIMs in /mnt/us/wikipedia/, groups
                    split parts by base name into one logical ZIM each
  zim.lua           ZIM file reader (header, dirent, URL ptr list, redirects)
  cluster.lua       FFI bindings for libzstd / liblzma + LRU cluster cache
  splitfile.lua     virtual file: reads a ZIM that's been split for FAT32
  htmlclean.lua     strips Vector skin chrome, infobox/navbox tables,
                    hatnotes, embedded <style> — drops ~70% of HTML weight
                    so MuPDF only renders the prose
  viewer.lua        full-screen ScrollHtmlWidget with link taps + A−/A+
                    font-size cycle
split_zim.py        Desktop-side helper: splits a >4 GB ZIM into FAT32-safe parts
```

The repo does **not** ship any ZIM files. They are huge (multiple GB), and you should always download the latest release directly from Kiwix.

## Prerequisites

1. **A KOReader-capable device.** Kindle (jailbroken, with KUAL), Kobo, PocketBook, reMarkable, Android, etc. This plugin is developed and tested on a **Kindle Oasis** with KOReader launched via KUAL. Other devices should work but are not verified.
2. **KOReader installed and working.** See <https://github.com/koreader/koreader> for installation. If you can't already open a book in KOReader, fix that first.
3. **A desktop computer** with Python 3.x for the `split_zim.py` helper (only needed if your device's storage is FAT32, which is the case on every Kindle).

## Step 1 — Download a ZIM file from Kiwix

Visit **<https://library.kiwix.org/>** and pick a library. Useful starting points:

- `wikipedia_en_all_mini` — full English Wikipedia, text only, ~12 GB.
- `wikipedia_en_simple_all` — Simple English Wikipedia, ~300 MB. Great for testing.
- `wikipedia_*_all` (any language) — full text + thumbnails. Larger.
- `wiktionary_*`, `wikibooks_*`, `wikiquote_*`, `gutenberg_*`, `stackoverflow_*`, etc. — all are valid ZIMs and will be searchable side by side.

Click any entry, then download the `.zim` file. Be patient — these are big.

You can install **as many ZIMs as you want**. The plugin auto-discovers every ZIM (or split set) in the configured folder and searches across all of them. Tag-style results show which library each match came from.

## Step 2 — Split the ZIM for FAT32 (FAT32 devices only)

Kindle storage is FAT32, which caps individual files at 4 GB. If your ZIM is larger than that, you must split it first. (Kobo/Android/Linux readers with exFAT or ext4 can skip this step and copy the `.zim` over as-is.)

From the project root on your desktop:

```
python split_zim.py "path\to\wikipedia_en_all_mini_2026-03.zim"
```

Default chunk size is 1 GiB → ~13 parts named `…zimaa`, `…zimab`, …, `…zimam`. Pass `--chunk 3500MB` if you'd rather have ~4 large parts; part count doesn't affect performance — the plugin opens all parts once at startup and seeks into whichever one holds the bytes it needs. Concatenated bytes equal the original byte-for-byte (verified via SHA-256 + 500 boundary-crossing reads in `splitfile.lua`'s self-test).

The original `.zim` is left untouched; only copy the `.zim??` parts to the device.

## Step 3 — Install the plugin and ZIMs on your device

1. **Connect the device by USB.** It mounts as a drive (e.g. `E:` on Windows, `/Volumes/Kindle` on macOS). Inside you'll see a `koreader/` folder.
2. **Copy the plugin folder.** Copy `plugins\wikipediazim.koplugin\` (the whole folder) into `koreader\plugins\` on the device:
   ```
   <device>/koreader/plugins/wikipediazim.koplugin/
       _meta.lua
       main.lua
       library.lua
       zim.lua
       cluster.lua
       splitfile.lua
       htmlclean.lua
       viewer.lua
   ```
3. **Create a `wikipedia/` folder at the device root** (on a Kindle this is `/mnt/us/wikipedia/`; on other devices it's whatever shows up at the top level when you plug in over USB). Drop your ZIM(s) into it:
   ```
   <device>/wikipedia/wikipedia_en_all_mini_2026-03.zimaa
   <device>/wikipedia/wikipedia_en_all_mini_2026-03.zimab
   …
   <device>/wikipedia/wiktionary_en_all_2024.zim
   <device>/wikipedia/simple_wikipedia_2025.zim
   ```
   Mix and match: split sets, single-file ZIMs, and multiple libraries can all live here together. The plugin groups split parts by base name into one logical ZIM each, then exposes every logical ZIM as a separate searchable library.
4. **Eject** the device.
5. Launch **KOReader** the way you normally do (KUAL → KOReader on Kindle; tap the launcher icon on Kobo/Android).

### Configuration inside KOReader

**No file picker needed** — the plugin scans `/mnt/us/wikipedia/` (or the equivalent on your device) automatically and groups any `.zim??` parts back into one logical ZIM per base name. Just open **Tools → More tools → Wikipedia (offline) → Search articles** and start typing.

If you keep your ZIMs somewhere else, use **Tools → More tools → Wikipedia (offline) → Set Wikipedia folder…** once. The submenu also has **Loaded ZIMs…** showing what was discovered (base name, part count, open/closed state) — handy for confirming the split parts collapsed into one logical ZIM and that all your libraries were picked up.

The path is saved in KOReader settings, so future sessions skip this step.

## Using it

From **Tools → More tools → Wikipedia (offline)**:

- **Search articles** — type a title prefix (e.g. `Albert E`). Capitalisation and spaces are normalised; matches scroll alphabetically. With one ZIM in the folder, results show plain titles. With multiple ZIMs, each result is tagged `[base]` so you can see which library it came from. Tap a result to open it; the article's owning ZIM is opened on demand the first time it's needed and cached after that.
- **Open main page** — opens the front page of the first ZIM.
- **Loaded ZIMs…** — diagnostic view: lists what was discovered, how many parts make up each logical ZIM, and which are currently open.

Inside an article:

- **Tap any link** — navigates to that article (push onto history).
- **Back** — returns to the previous article.
- **Home** — main page.
- **Search** — opens the search dialog without losing the article.
- **Close** — exits the viewer.
- **A− / A+** — cycle font size through `16, 18, 20, 22, 24, 26, 28, 32, 36`. The choice is persisted in KOReader's settings, so future articles open at the size you last chose.

The device's hardware page-turn buttons scroll the article (KOReader's standard ScrollHtmlWidget behaviour).

## Performance notes

The ZIM file handle is opened **once per KOReader session** (lazily, on first article open) and kept open. Every subsequent article — whether you searched for it or tapped a link — reuses that handle. There is no "reload"; you can verify by checking `koreader.log` for the single `wikipediazim: opened …` line per session.

| Operation | Cost (Kindle ARM) | Notes |
|---|---|---|
| Open ZIM (first time) | <50 ms | Reads 80-byte header + MIME list. Splitfile opens N FDs. |
| Title search | ~30–60 ms | ~24 disk seeks for binary search through 19 M entries |
| Cluster fetch + decompress | ~50–200 ms | ~2 MB compressed → libzstd via FFI |
| HTML clean | <5 ms | Strips chrome/infoboxes/styles → ~30% of original size |
| MuPDF render | ~200–800 ms | Dominant cost on Kindle CPU; heavily reduced by `htmlclean` |
| Cluster cache hit | <5 ms | Linked articles in same cluster (~200 articles each) |

If a load still feels slow, check `koreader.log`. The most common culprit is a very long article (e.g. "List of …" pages, ~500 KB even after cleaning) — those just take time on the device CPU.

## Caveats

- **Text-only.** The "mini" Wikipedia ZIM has no images. The viewer strips `<img>`, `<script>`, `<style>`, `<svg>`, `<figure>` to keep MuPDF rendering snappy on the device CPU. If you switch to a non-mini ZIM, images still won't render (KOReader's HTML widget doesn't load resources from inside a ZIM blob).
- **Title case.** Search auto-capitalises the first letter (Wikipedia URL convention). Searching `iphone` won't find `IPhone`; type `IPhone`.
- **Full-text search.** Not supported in v1. The ZIM has a Xapian full-text index (`X/fulltext/xapian`), but reading Xapian from Lua would mean shipping a port of libxapian. Title-prefix search is enough for almost all real-world lookups.
- **External links** (http/https/mailto) show a brief notice and don't navigate — you're offline.
- **LZMA2 clusters.** The `2026-03 mini` ZIM is 100% zstd. If you point the plugin at an older ZIM that uses LZMA2, decompression goes through `liblzma`, which KOReader bundles on most platforms.

## Troubleshooting

If the menu item doesn't appear, check `koreader/koreader.log` (also accessible from KOReader → Help → System statistics → Open log) for `wikipediazim` errors.

If `libzstd not available` appears: the linker couldn't find the library. KOReader on Kindle ships libzstd — you should not normally see this. If you do, please file an issue with the KOReader build version (Help → About).

## Credits

- **[Kiwix](https://kiwix.org/)** — for producing and freely hosting the ZIM files this plugin reads. Without their work this project would not exist. Please consider [donating to Kiwix](https://kiwix.org/en/support-us/) if you find this useful.
- **[KOReader](https://koreader.rocks/)** — for the e-reader application, the Lua plugin API, the bundled libzstd/liblzma/MuPDF, and the ScrollHtmlWidget that does all the heavy rendering.
- **Wikipedia / Wikimedia contributors** — for the actual content inside the ZIMs.

## License

This repository is released under the **Creative Commons Attribution-NonCommercial 4.0 International** license (CC BY-NC 4.0). You are free to use, modify, and redistribute it, including in modified form, **as long as the use is not commercial** and you give attribution. See [LICENSE](LICENSE) for the full text.

ZIM files, KOReader, and Wikipedia content are **not** covered by this repository's license — they are governed by their own (CC BY-SA, AGPL, etc.). See [LICENSE](LICENSE) for pointers.
