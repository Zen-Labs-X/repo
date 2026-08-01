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
