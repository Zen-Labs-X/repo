# v1.5.2.2

Test build for the coming 1.6.0 release. Not a public release.

**Changed since v1.5.2.1**
- The update check now gives up after about 5 seconds instead of holding the screen for up to a minute. The banner says that a tap cancels it, and its text changes while the check tries again.

---

**New formats**
- FB2 and MOBI books now work. Glimpse finds the images inside them the same way that it does in an EPUB. ([#3](https://github.com/Fank1/glimpse/issues/3))
- A MOBI always uses "All images". The format holds the whole book as one document, so Glimpse cannot tell which chapter an image belongs to. Your own setting comes back on an EPUB.

**Compact panel**
- Glimpse can now open as a small card that floats over the page, instead of the full drawer. Drag it by the grip in its top-right corner. Glimpse puts it back where you left it.
- Switch size from the ⋯ menu, or in Settings under Layout. The panel changes at once, while Glimpse is open.
- The card keeps the image, the indicator, the ⋯ menu, and your zoom controls and mini map. It leaves out the captions, the bookmark label, the navigation buttons and the reset button. Swipe changes image. Double-tap resets the zoom.
- While the card is on, the ⋯ menu dims the rows that the card cannot show. Swipe, pinch and double-tap stay on, whatever Settings → Gestures says.
- The card now works in night mode. Its border, its shadow and its indicator match the design instead of disappearing into the dark page.
- Open the Gallery from the card and Glimpse switches to the large panel, so the thumbnails stay big enough to use. Close the Gallery and the card comes back.

**Zoom**
- Maximum zoom takes a custom value, from 100% to 1000%, in place of the fixed presets. A high value lets a small image fill the screen. ([#13](https://github.com/Fank1/glimpse/issues/13))
- Zooming in is much quicker, and it stays quick however far you go. Each step used to cost more than the step before it.
- You can zoom all the way to the value that you set. "+" greys out at your maximum, and not before it.
- Change Maximum zoom while Glimpse is open and the new limit applies at once.

**Viewer**
- The image indicator goes away when you zoom past the fitted view, in both panel sizes, so the image gets the whole row.
- The rectangle on the mini map that marks your position has rounded corners.
- A pressed button keeps its outline.
- Turn every Quick Action off and the ⋯ button opens the Gallery directly. Turn one back on and the menu returns. The button follows the setting at once.

**Updates**
- The update check gives up sooner when the network does not answer. It used to hold the screen for up to a minute. It now stops after about 5 seconds and says what went wrong.
- The banner says that a tap cancels the check, and its text changes while the check tries again, so the screen no longer looks frozen.

**Translations**
- "Show Mini Map" is corrected in 15 languages.

# v1.5.2.1

Test build for the coming 1.6.0 release. Not a public release.

**New formats**
- FB2 and MOBI books now work. Glimpse finds the images inside them the same way that it does in an EPUB. ([#3](https://github.com/Fank1/glimpse/issues/3))
- A MOBI always uses "All images". The format holds the whole book as one document, so Glimpse cannot tell which chapter an image belongs to. Your own setting comes back on an EPUB.

**Compact panel**
- Glimpse can now open as a small card that floats over the page, instead of the full drawer. Drag it by the grip in its top-right corner. Glimpse puts it back where you left it.
- Switch size from the ⋯ menu, or in Settings under Layout. The panel changes at once, while Glimpse is open.
- The card keeps the image, the indicator, the ⋯ menu, and your zoom controls and mini map. It leaves out the captions, the bookmark label, the navigation buttons and the reset button. Swipe changes image. Double-tap resets the zoom.
- While the card is on, the ⋯ menu dims the rows that the card cannot show. Swipe, pinch and double-tap stay on, whatever Settings → Gestures says.
- The card now works in night mode. Its border, its shadow and its indicator match the design instead of disappearing into the dark page.
- Open the Gallery from the card and Glimpse switches to the large panel, so the thumbnails stay big enough to use. Close the Gallery and the card comes back.

**Zoom**
- Maximum zoom takes a custom value, from 100% to 1000%, in place of the fixed presets. A high value lets a small image fill the screen. ([#13](https://github.com/Fank1/glimpse/issues/13))
- Zooming in is much quicker, and it stays quick however far you go. Each step used to cost more than the step before it.
- You can zoom all the way to the value that you set. "+" greys out at your maximum, and not before it.
- Change Maximum zoom while Glimpse is open and the new limit applies at once.

**Viewer**
- The image indicator goes away when you zoom past the fitted view, in both panel sizes, so the image gets the whole row.
- The rectangle on the mini map that marks your position has rounded corners.
- A pressed button keeps its outline.
- Turn every Quick Action off and the ⋯ button opens the Gallery directly. Turn one back on and the menu returns. The button follows the setting at once.

**Translations**
- "Show Mini Map" is corrected in 15 languages.

# readme-assets

Image assets referenced by README.md. Not a software release.

# v1.3.3.18

Pre-release 1.3.3.18. New since last build: caption no longer hidden behind the bookmark label; top-band controls clear the rounded corners and its ⋯ menu opens centred; much smoother panning with the mini map on. See CHANGELOG.md (Unreleased) for the full pre-release pile.

# v1.3.3.17

Glimpse v1.3.3.17
