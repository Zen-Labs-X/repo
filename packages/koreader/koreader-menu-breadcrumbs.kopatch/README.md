# KOReader menu breadcrumbs

A KOReader user patch that shows the current hierarchy in the Reader and File
Manager top menus.

```text
Taps and gestures › Gesture manager
```

The breadcrumb appears below the tab icons after entering a submenu. Tap it to
open the complete path: each level is shown on its own line and can be tapped
to jump directly to that menu. Existing footer, Back, swipe, paging, and tab
navigation continue to work normally.

## Install

1. Download [`2-menu-breadcrumbs.lua`](./2-menu-breadcrumbs.lua).
2. Create a `patches` directory inside the KOReader data directory if it does
   not already exist.
3. Copy the file into that directory.
4. Restart KOReader.

Typical destinations include:

- Kindle: `koreader/patches/2-menu-breadcrumbs.lua`
- Kobo: `.adds/koreader/patches/2-menu-breadcrumbs.lua`
- Pocketbook: `koreader/patches/2-menu-breadcrumbs.lua`
- Android: `koreader/patches/2-menu-breadcrumbs.lua`

The patch should appear under **Tools → Patch management** after restart. To
uninstall it, remove the file and restart KOReader.

## Behavior

- Breadcrumbs are added to the shared `TouchMenu`, so they work in both Reader
  and File Manager top menus.
- The icon tab is not named; the path starts at the first submenu.
- Long paths are truncated from the left so the current menu remains visible.
- Tapping a breadcrumb opens a clickable, one-level-per-line path dialog.
- Right-to-left interfaces mirror the separator.
- Root menus and unrelated list, file chooser, and dialog widgets are unchanged.

## Compatibility

The patch wraps internal `TouchMenu` methods without modifying KOReader files.
KOReader updates may change those internals; if the patch stops loading, remove
it and report the KOReader version in an issue.

For general user-patch documentation, see the
[KOReader user guide](https://koreader.rocks/user_guide/#L2-userpatches) and
[KOReader wiki](https://github.com/koreader/koreader/wiki/User-patches).

## Development

Run the navigation-state regression test with:

```sh
luajit spec/menu_breadcrumbs_spec.lua
```

## License

GNU Affero General Public License v3.0 or later. See [LICENSE](./LICENSE).
