# Release Notes

Here's everything new, improved, and fixed since the last stable release (**v26.8.2.1**).

### New Features

* **In-app ratings and voting:** You can now upvote or downvote plugins directly within the storefront to share feedback and highlight community favorites.
* **Ignore updates:** Skip updates for individual plugins if you'd prefer to stay on your current version. Ignored updates won't trigger update badges or prompts.
* **Font viewer sizing controls:** The font viewer now automatically matches your text size settings, with new buttons to easily scale the sample text up or down.
* **Korean language support:** Added Korean translations for the plugin interface.

### Performance & Reliability

* **E-ink performance boost:** Optimized the rating and voting system so dialogs load much faster and smoother on low-powered e-readers.
* **Faster README images:** Improved how images inside plugin details and READMEs are fetched and rendered.
* **Catalog fallbacks:** Added fallback catalog sources and improved initial setup logic to make sure new installs load the catalog right away, even if a primary server is temporarily down.

### User Interface & Bug Fixes

* **Dynamic button & tab sizing:** Buttons and menu tabs now automatically adjust their layout to fit translated text of varying lengths cleanly.
* **Update count fixes:** Fixed minor display bugs where ignored versions could mess with update counts or refresh indicators.
* **UI Polish:** Visual cleanup around deletion prompts, restart buttons, and dialog layouts.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.2.1...26.8.9