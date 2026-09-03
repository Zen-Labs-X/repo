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

# v1.0.0

Glimpse 1.0.0 — first stable release.

Peek at maps, family trees and other reference images from anywhere in an EPUB without losing your place. Open Glimpse (ideally via a gesture), swipe through the book's reference images, zoom and pan, then close — you're right back where you were reading.

Highlights
- Smart scan that filters out covers, ornaments, dividers and publisher chrome.
- Spoiler-safe by default: only images up to your current chapter, switchable to the whole book.
- Remembers the last image, zoom and pan per book.
- Pinterest-style gallery, per-image (multi-line) captions, hide/restore, rotate 90°, and a configurable Quick Actions menu.
- Night-mode friendly: transparent line-art illustrations get a white backing so they stay visible.
- In-app updates with backup and rollback.

EPUB and other crengine-rendered zip/HTML formats. Install: unzip the koplugin into KOReader's plugins/ folder and restart.
