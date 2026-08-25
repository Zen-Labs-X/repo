### New

- Download plugins through a GitHub mirror or proxy — pick the source from the menu, or set a custom URL prefix (useful where GitHub is slow or blocked). (#31, thanks @THE-XSX)
- The custom download source can be set either in `appstore_configuration.lua` or in the UI; edits to the file are picked up again after you change it.
- Cache refreshes now show a progress bar naming the current stage, and can be stopped partway. (#27, thanks @iav)
- Hungarian translation added. (#29, thanks @koma52)
- All seven translations (tr, zh_CN, de, es, fr, hu, pt_BR) are now complete.

### Protection against overwriting the wrong plugin (#32, thanks @ksaMask123)

- An abandoned update no longer redirects the *next* install into the previous plugin's folder — the cause of plugins being silently overwritten by an unrelated one.
- An install now refuses to overwrite a directory that already belongs to a different plugin, and says which one.
- When the archive's folder name and your install record disagree, AppStore asks which directory to use instead of guessing.

### Performance

- Opening the plugin list no longer decodes every cached repository — only the rows on screen (11.8 s of a 19.7 s open on a Kindle 3 with 1465 repos cached went into rows nobody sees). (#26, thanks @iav)
- Non-touch devices: moving the D-pad cursor repaints only a bar on the focused row instead of the whole dialog — 1.23 s → 67 ms per step on a Kindle 3. (#25, thanks @iav)
- The plugin list is no longer rebuilt when only patch data changed.
- Lower memory use: parsed `_meta.lua` tables are no longer kept alive for every installed plugin.

### Reliability

- Every network call now has a deadline; a server that opens a connection and then goes silent no longer freezes the interface until KOReader is restarted. (#27, thanks @iav)
- A failed request no longer leaves KOReader's global socket timeouts raised for every other network call. (#27, thanks @iav)
- Losing Wi-Fi halfway through a refresh no longer replaces the cache with the partial result (previously 1479 cached repositories could be cut to the 300 that arrived first). (#27, thanks @iav)
- Downloaded archives are closed on every exit path, so failed downloads no longer leave a file handle open and the temporary file behind. (#27, thanks @iav)
- Errors now report why a request failed instead of a generic "request failed", and a Lua error is no longer labelled as an HTTP status. (#27, thanks @iav)
- The Back key closes AppStore's dialogs. (#25, thanks @iav)
- Fixed the custom mirror prefix dialog (and two other input dialogs) rendering with no buttons at all.
 
---

Thanks to @iav, @koma52, @THE-XSX and @ksaMask123 for their contributions to this release.