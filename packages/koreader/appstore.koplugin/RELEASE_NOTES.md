# v1.13.0

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

# v1.12.0

-  Show README in a TextViewer popup on KOReader >= 2026.07

    Incorporates [#19](https://github.com/omer-faruq/appstore.koplugin/issues/19) (Readme in TextViewer) by @kerivin, gated behind a
    KOReader version check as discussed on the PR: TextViewer only gained
    Markdown rendering (text_format = "md") in v2026.07, so older versions
    keep the previous cache-to-file-then-open flow, and the "Clear cached
    README files" setting stays limited to that legacy path.
 - Multi-directory plugin path support (extra_plugin_paths) — plugins can now be discovered and installed from multiple configured directories instead of one fixed path; install destination is selectable, updates write back to the correct directory, and paths can be hidden/shown via a new "Manage plugin paths" screen.
- Added localization support (zh_CN, tr, es, fr, de, pt_BR).
- Added GPL-3.0 license.
- Fixed blank pages in the full changelog viewer.
- Fine-grained PAT rejection on GitHub search is now detected and explained to the user.

# v1.10.0

## Modifications via PR 16,17,20 by [iav](https://github.com/iav)
### Browser & installed-list navigation improvements

- Added pagination to the Installed Plugins and Installed Patches screens, with a configurable items-per-page setting.
- Added a compact toolbar (Switch tab / Refresh / Installed) to the plugin and patch browser.
- Added an installed checkmark next to plugins you already have in the browse list.
- Added a direct switch between Installed Plugins and Installed Patches without returning to the browser.
- Added hardware-keyboard shortcuts (R/F/S/T) and a Menu-key shortcut for refresh, filter, sort, and switch-tab actions.
- Cursor position and sort/filter selection are now preserved across page flips and list rebuilds on keyboard/D-pad devices.
- Fixed stale/ghosted screen content when switching between AppStore dialogs on e-ink screens.
- Reduced screen flashing when simply flipping pages, keeping the full-screen flash only for tab/filter/sort changes.

### Install message fix

- Fixed install/update success messages sometimes showing "nil" instead of the plugin's name.

### Update detection fix

- Fixed plugins with a "v"-prefixed version number (e.g. v1.4.2) being incorrectly flagged as needing an update.

# v1.9.1

- release options pagination when there are more than 8 assests.

# v1.9.0

 - Add release ignore feature to suppress update notifications for specific versions until newer release available
    - Add "Ignore this release" button to download options dialog for updates
