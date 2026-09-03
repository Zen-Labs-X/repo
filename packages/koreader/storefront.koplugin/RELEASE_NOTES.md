# 26.9.3

## What's New

- **Non-touch device support**: You can now navigate and use Storefront entirely using physical buttons and page-turn keys.
- **Less screen flashing**: Reworked e-ink refresh behavior to cut down on unnecessary full-screen flashes while browsing around.
- **Better performance**: Noticeably snappier overall, especially on older and lower-powered e-readers.
- **Faster update checks**: The *Check Updates* button is much more responsive and loads faster.
- **Download reliability**: Fixed issues with downloads failing, including a bug that caused larger files to fail when running *Update All*.
- **UI fixes for long names**: Cleaned up button layouts so long version numbers no longer overflow or wrap awkwardly, and fixed folder picker issues with long screensaver directory names.
- **Smoother tab loading**: Cleaned up the loading and refresh behavior when viewing READMEs and the *Versions* tab.
- **Font tracking**: Improved font tracking/management.

**Full Changelog**: https://github.com/ultimatejimmy/storefront.koplugin/compare/26.8.23...26.9.3

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
