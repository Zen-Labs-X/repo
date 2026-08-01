-  Show README in a TextViewer popup on KOReader >= 2026.07

    Incorporates [#19](https://github.com/omer-faruq/appstore.koplugin/issues/19) (Readme in TextViewer) by @kerivin, gated behind a
    KOReader version check as discussed on the PR: TextViewer only gained
    Markdown rendering (text_format = "md") in v2026.07, so older versions
    keep the previous cache-to-file-then-open flow, and the "Clear cached
    README files" setting stays limited to that legacy path.
