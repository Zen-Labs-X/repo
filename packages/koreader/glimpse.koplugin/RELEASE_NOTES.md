# v1.6.0

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

# v1.5.1

## Since 1.5.0

**Gallery**
- Wide top/bottom layouts now show 4 columns instead of 3, so more images fit at once.
- Thumbnails line up on the left with the heading, and the page number is now the prominent label (the image count moved to the corner).

**Viewer**
- The mini map no longer stretches across the screen on wide landscape images. It stays the height of the zoom controls, with the image letterboxed inside.

**New setting**
- Numbered indicator instead of dots: shows a compact "3 / 42" counter in place of the row of dots, handy when a book has so many images that the dots get very wide.

**Changed setting**
- Respect KOReader top menu activation (renamed, moved to Advanced): the top-edge tap opens KOReader's menu only when KOReader itself is set to open its menu on a tap.

**Other**
- Settings reorganised into clearer groups.

# v1.5.0

### Major
- **Choose where Glimpse opens.** Portrait can slide in from the left/right edge or open as a top/bottom band, with a live preview in the Layout dialog.
- **Mini map while zoomed.** A corner overview marks what you're viewing; tap it to jump. Docks to the zoom controls or stands alone.
- **Glimpse speaks your language.** Initial machine translation for 22 languages, loaded to match KOReader. Managed on Crowdin, so anyone can help.

### Minor
- **Looping navigation** (optional): arrows and swipes wrap around at the ends, Gallery pages too.
- **Toggle several ⋯ settings at once** without the menu closing.
- Bookmarked pages show a bookmark glyph in the dots; caption now matches the bookmark pill.
- **Snappier zoom and image switching**, plus much smoother panning with the mini map on.
- Fixes: top-band corners and margins, ⋯ menu centring, caption behind a bookmark label, a stuck ⋯ button state, and update-checker freezes/retries.

# v1.3.0

# Glimpse 1.3.0

A big update since 1.2.0: bookmarked pages join the Gallery, the image filter got smarter, zoom got more flexible, and the whole viewer feels quicker and more polished. I've also put a lot of focus on customizability, as that's how I want a plugin to be! 

Now, the Bookmarks feature is not meant to replace the vanilla Bookmarks functionality in KOReader. It's a way of easily storing references that you want to look at later! To add a bookmark in your book, configure your Gestures and look for "Toggle bookmark".

As always, please feedback and preferably post them in Issues on Github. And yes, localization is coming, it's just a hazzle! 

---

## 🔖 Your bookmarks, in the Gallery

- **See your bookmarked pages alongside the images.** Turn on *Include Bookmarks in Gallery* and the pages you've dog-eared show up as thumbnails, in reading order among the pictures. It's a fast way to keep a glossary, a family tree, or a map that lives in the text just a swipe away.
- **Remove a bookmark right from Glimpse.** Long-press it in the Gallery, or use the viewer's ⋯ menu, and it's deleted from the book itself, not just hidden.

## 🎯 A smarter filter, with fewer good images wrongly hidden

- **Maps, family trees, diagrams, charts and timelines** named as such are now recognized as reference content, so an endpaper map or a family tree that used to slip under the size cutoff is kept.
- **Illustrated non-fiction is treated more gently.** When a book already keeps lots of figures (cookbooks, science, how-to), Glimpse automatically relaxes its size floor for that book so smaller diagrams come through too, while novels stay strict so their decorative bits don't leak in. *(Tuned across a 200+ book library.)*

## 🔍 Zoom, your way

- **Choose how far you can zoom**, from 150% up to 400% (*Advanced → Maximum zoom*).
- **Optional on-screen zoom controls**, a small +/fit/− strip for zooming without pinching. The +/− dim at the limits, and the middle button snaps back to a fitted view.

## ⚡ Snappier, flashless viewing

- **Switching between images no longer flashes the whole screen** each time you flip with the arrows or a swipe. *(New Advanced → Fast image switching, on by default. Turn it off if a previous image ever ghosts through on a slower panel.)*
- **Menus and controls open faster**, especially on e-ink, with cleaner shadows that fade in instead of flashing dark first.

## 🧭 A tidier, clearer menu

- **New "Enable Glimpse" switch** turns the whole plugin on or off without unbinding your gesture.
- **New Gestures sub-menu** to turn the viewer's touch gestures on or off individually: *double-tap to zoom*, *swipe to navigate*, *pinch to zoom*. Handy if one conflicts with how you hold your device.
- **The Gallery is now always one tap away** at the bottom of the ⋯ menu.
- **Clearer wording throughout**, with shorter labels and an option to silence the occasional "format not supported" message.

## ✨ Viewer polish

- **A new Gallery / Ignored switcher.** Just tap to switch. It stretches to fill the width, so it reads clearly on any screen.
- **Bookmarked-page thumbnails are cached to disk**, so reopening the Gallery after closing a book shows them instantly instead of re-rendering.
- Assorted alignment and night-mode fixes for the page dots, zoom controls, and captions.

## 🐛 Fixes

- **Auto-rotation works even with the ⋯ menu open.** The menu closes and the viewer re-lays-out for the new orientation.
- **Removing a bookmark clears its dogear from the page immediately**, while Glimpse is still open.
- A stray long-press on an image no longer flashes the whole screen.
- On a book with no reference images, the Gallery's Back button reliably closes Glimpse.

# v1.2.0

## What's new since 1.0.0

**🖼️ A proper gallery, with a place for filtered-out images**
- Two views: your **Gallery** (the images Glimpse keeps) and an **Ignored** pile (everything the filter set aside, plus anything you've ignored yourself). A button at the bottom flips between them.
- **Long-press any image** to move it. Rescue a map the filter wrongly hid, or ignore one you never want to see, without switching to "show all images."

**🔍 Sharper, better zoom**
- Zoomed-in maps and detail now stay crisp instead of going blurry. Glimpse re-loads the image at full resolution when you zoom in.
- Pinch smoothly from best-fit up to 150%, or double-tap to jump in and back out.
- Fixed: panning around a zoomed image could accidentally close Glimpse.

**📖 "Show in Book" now lands on the exact image**
- Previously it dropped you at the top of the chapter. Now it jumps straight to the image you were looking at.

**🌙 Night-mode fixes**
- "Invert in Night Mode" now works the right way round (it was sometimes reversed for some users).
- Fixed a white drawer in dark mode on some Android/Boox devices. It's properly dark now.

**⚡ Less ghosting (e-ink)**
- Opening, closing, and swiping between images no longer cause "ghosts" of the previous image behind, especially noticeable on Kindle and other e-ink screens.
- New option to turn off the drawer's drop-shadow if it causes ghosting on your device or just for cosmetic preference.

**💾 Behind the scenes**
- Glimpse's scan is now stored alongside the book, so it travels with the file between devices.
- A rotated image stays rotated, even after an unexpected shutdown.
