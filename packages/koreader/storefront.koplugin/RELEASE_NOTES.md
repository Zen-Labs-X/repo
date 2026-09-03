# 26.8.23

## What's New in 26.8.23

### Features & Improvements

* **Custom screensaver folder**: You can now choose a custom folder location for your screensavers using a built-in folder browser in the settings, or reset back to default at any time.
* **Automatic doc refresh**: The *README* and wiki views now automatically refresh whenever content changes, so you always see the latest details without needing to manually reload.
* **Clearer screensaver messaging**: Improved in-app status messages and logging when managing and applying screensavers.
* **New fonts**: Added *Fast Sans*, *Fast Serif*, and *Fast Sans Dotted* to the font catalog.
* **Cleaner Updates tab**: Removed the redundant search bar from the Updates screen to keep the page focused strictly on pending updates.
* **Better dialog sizing for translations**: Adjusted spacing and sizing across settings, filters, and info dialogs so translated text won't get clipped or cut off.
* **Screensaver sorting**: Tweaked the sort ordering for screensavers so browsing and finding wallpapers is smoother.
* **Installed item count**: Fixed how item counts are calculated and displayed on the Installed tab.

### Fixes

* **Font detection on WSL**: Fixed font path resolution issues when running KOReader in WSL environments.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.18.2...26.8.23

# 26.8.18.2

- Some small code syntax fixes

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.18.1...26.8.18.2

# 26.8.18.1

- hotfix for some users with a font missing

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.18...26.8.18.1

# 26.8.18

# Storefront: Screensavers

This release brings screensaver/wallpaper support directly into Storefront. You can now browse, download, and manage screensavers on your device without needing to hook up a cable or manually transfer images.

### What's New
- Update tab UI to accommodate the Screensavers
- **Screensaver Catalog**: Browse a curated list of wallpapers categorized by themes like Nature, Minimalist, Sci-Fi, Architecture, Art, and more.
- **Direct Download & Setup**: Download screensavers directly to your device's screensaver directory with a single tap.
- **Configure in Storefront**: You can set and configure the screensaver directly in Storefront. 
- **Cache management**: Go to the settings menu for more granular cache management/deletion for readmes, wiki, and screensaver thumbnails.
- **E-Reader Friendly**: All wallpapers in the catalog are formatted and optimized specifically for e-ink screens.
- **Community Submissions**: You can now submit your own screensavers to be included in the shared catalog.

Submit your own screensavers to the catalog here: https://ultimatejimmy.github.io/storefront-screensavers/
<img width="543" height="751" alt="screensavers" src="https://github.com/user-attachments/assets/bc5b7d17-a773-4df8-9d96-8d02cd42916e" />


**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.9...26.8.18

# 26.8.9

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
