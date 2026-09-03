# v1.3.0

<img width="100%" alt="Panels+ v1.3.0 banner" src="https://github.com/user-attachments/assets/658897e4-965f-4746-998e-226895e6697f" />

Built from tag: `v1.3.0`

Welcome to **The Touchy Update**! For this release, I focused on polishing several features I found myself missing while reading on my e-reader over the past few weeks. 

Why "The Touchy Update", you ask? Well, it introduces new **experimental OCR support** (activated via a long press on text). Ironically, it also brings **touchless functionality** to Kobo devices, allowing you to turn pages using physical buttons and compatible Bluetooth page-turners.

This update also includes quality-of-life improvements for rotation handling, dark mode support, and much more. Check out the details below:

## Highlights

<div align="center">

<table>
  <colgroup>
    <col style="width: 20%">
    <col style="width: 80%">
  </colgroup>
  <thead>
    <tr>
      <th align="center">Feature</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><strong>Word Lookup</strong></td>
      <td>
        <strong>Touch &amp; hold to select text and look up words, even in comics/manga</strong><br><br>
        Long-press a word inside a zoomed-in panel to select it and open the dictionary, just like you would on any regular text page. This now works on comic and manga pages too, which normally have no selectable text at all! Works across CBZ, CBR, and PDF. <em>Note: This is still experimental. Word detection is tricky on hand-lettered or stylized comic text and might not always get it exactly right.</em><br><br>
        <div align="center">
          <video src="https://github.com/user-attachments/assets/1e08f664-c036-4b15-bedf-bc4c4cf5cc00" width="40%" controls muted autoplay loop playsinline></video>
          <br>
          <em>🎥 Long-pressing to select text and trigger the dictionary popup on a comic page.</em>
          <br>
          <strong>IMPORTANT:</strong> To use this feature, you'll need to set up a couple of things first:
          <ul>
            <li><em>Install an OCR engine in KOReader by <a href="https://koreader.rocks/user_guide/#L2-ocr">following the official KOReader guide</a>.</em></li>
            <li><em>Install at least one dictionary. You can do this by <a href="https://www.youtube.com/watch?v=fthGMdpUfR0">following this tutorial for manual installation</a>, or by using KOReader's built-in online dictionary installer.</em></li>
          </ul>
          <em>(Note: Step-by-step instructions for the built-in installer are outside the scope of these release notes.)</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Dark Mode</strong></td>
      <td>
        <strong>Dark mode for the panel viewer</strong><br><br>
        The panel viewer now fully respects KOReader's night mode. Previously, switching to dark/night mode inverted the rest of the reader but left the panel viewer—panel art, borders, the bottom toolbar, everything—lit up bright white regardless.<br><br>
         <div align="center">
            <video src="https://github.com/user-attachments/assets/b0d8380c-e523-462c-a33e-21704fb79043" width="40%" controls muted autoplay loop playsinline></video>
            <br>
            <em>🎥 Switching to dark mode with the panel viewer seamlessly updating.</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Edge Zoom</strong></td>
      <td>
        <strong>One-handed zoom with edge swipes</strong><br><br>
        Swipe up along the left edge of the screen to zoom into the current panel, and swipe down to zoom back out. No pinch gesture is needed, so you can easily zoom in and out one-handed while holding the device.<br><br>
        <div align="center">
          <video src="https://github.com/user-attachments/assets/09c51cf0-8748-4701-b198-9468db39c442" width="40%" controls muted autoplay loop playsinline></video>
          <br>
          <em>🎥 Swiping up and down along the screen edge to zoom in and out seamlessly.</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Tap to Navigate</strong></td>
      <td>
        <strong>Tap the screen edges to move between panels</strong><br><br>
        A new toggle lets you tap the left or right edge of the screen to jump to the previous or next panel, instead of relying solely on swipes or on-screen buttons. Which side goes forward depends on whether you're reading comic-style or manga-style. Swipe navigation can also be turned off entirely if you prefer using only taps, buttons, or physical keys.<br><br>
        <div align="center">
          <video src="https://github.com/user-attachments/assets/c594bee5-a4c8-415a-a566-f87484d319a4" width="40%" controls muted autoplay loop playsinline></video>
          <br>
          <em>🎥 Tapping the screen edges to quickly jump between previous and next panels.</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Kobo Support</strong></td>
      <td>
       <strong>Added Kobo physical buttons and page-turner device support (<a href="https://github.com/OGKevin/kobo.koplugin">kobo.koreader support as well</a>)</strong><br><br>
        Pressing a physical page-turn button (or a Bluetooth remote) past the last panel on a page <strong>should</strong> automatically turn the page and open the first panel of the next one. Going backward from the first panel does the same in reverse. Corner and zoom gestures on Kobo hardware <strong>should</strong> be recognized out of the box too, with no extra setup needed.<br><br>
        I say <em>should</em> because I tested this against the kobo.koreader repo and tried to emulate the Kobo environment <a href="https://github.com/KristanLaimon/PanelsPlus/blob/main/runkobo.sh">with a small script</a>. However, since I don't actually own a Kobo device, I'm flying a bit blind here! I hope it works flawlessly for you Kobo users. If it doesn't, please open an issue in this repo and I'll fix it ASAP.
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Rotation Picker</strong></td>
      <td>
        <strong>Redesigned rotation menu</strong><br><br>
        The rotation button now opens a small visual picker with icons showing exactly how the page will be oriented for each option, instead of forcing you to cycle blindly through rotation states.<br><br>
        <div align="center">
          <video src="https://github.com/user-attachments/assets/cd59abe4-7c27-4210-8b89-a3472e856ba3" width="40%" controls muted autoplay loop playsinline></video>
          <br>
          <em>🎥 Opening the visual picker to select the exact screen orientation.</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Improved Comics Support</strong></td>
      <td>
        <strong>Smarter panel detection</strong><br><br>
        Comic reading mode has been polished all around. It now applies automatically to CBR, CBZ, and PDF files. Tiny false "panels" with no real artwork (credit strips, footer rules, stray marks) used to show up as their own swipeable panels. This is now much less frequent, and detection is generally far more reliable on typical Western comic layouts than in previous versions of Panels+.<br><br>
        <div align="center">
          <video src="https://github.com/user-attachments/assets/35d2af95-e447-4b2d-9e89-71aa68c15894" width="40%" controls muted autoplay loop playsinline></video>
          <br>
          <em>🎥 Smooth, accurate panel-by-panel navigation on a Western comic layout.</em>
        </div>
      </td>
    </tr>
    <tr>
      <td align="center"><strong>Expanded Format Support</strong></td>
      <td>
        <strong>Increased support for .PDF, .CBR, and .CBZ files</strong><br><br>
        Panel+ now features enhanced, native support for standard comic formats (<code>.CBR</code>, <code>.CBZ</code>) and <code>.PDF</code> files. <br><br><em>⚠️ Please note: Formats like <code>.epub</code>, <code>.mobi</code>, and similar are not officially supported by this plugin. Please use standard formats to read your manga, as text-based formats are not designed for comics/manga</em>
      </td>
    </tr>
  </tbody>
</table>

</div>

The main focus of this release was your feedback! When I posted the [last version on Reddit](https://www.reddit.com/r/koreader/comments/1vbjx0z/release_panels_read_manga_through_panels_the_easy/), the biggest feature requests came from [Kobo users](https://www.reddit.com/r/koreader/comments/1vbjx0z/release_panels_read_manga_through_panels_the_easy/) and from folks who wanted [OCR-powered dictionary lookups](https://www.reddit.com/r/koreader/comments/1vbjx0z/comment/p0updf9/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).

While I couldn't fit every single suggestion in—that would have taken forever, and I'm juggling other projects—I put a lot of effort into improving the overall experience, fixing obscure bugs, and adding several quality-of-life features.

## A Note on OCR Word Lookup

- **OCR is not installed by default.** Word lookup on comics/manga relies on KOReader's native OCR engine, which requires manual setup first. Please refer to the [KOReader OCR setup guide](PLACEHOLDER_OCR_SETUP_LINK) <!-- TODO: confirm/replace with the exact KOReader OCR install docs link -->.
- **It is genuinely experimental and can be flaky.** Reliably finding word boundaries in hand-lettered or stylized comic/manga text turned out to be a much harder problem than I anticipated (call it a skill issue on my part!). Expect the occasional incorrect word or missed tap.
- **Workaround:** While this stabilizes, I recommend binding a comfortable multi-swipe gesture to "Open dictionary lookup" as a fallback. It is much more reliable than the touch-and-hold OCR method for now.

And, an important QOL: When in zoom panning mode, now when trying to open koreader settings with a swipe down from top edge screen, it will (surprisingly) open the settings! instead of closing the panel and having to do the same gesture again.... 

And or course, even more improvements to memory/cpu usage in general.

## Fixes

- Prevented the detection of tiny false "panels" (such as credit strips, thin footer rules, or stray marks) that used to be rendered as empty, swipeable panels. This significantly improves the reading experience for comics and manga with non-standard layouts.
- Fixed an issue where word-lookup highlights appeared offset from the actual selected word.
- Fixed the OCR occasionally attempting to guess words from unreadable, noisy image crops instead of falling back to normal text selection.
- Fixed word/line highlight boxes occasionally rendering as large, solid black squares over the panel.
- Fixed the zoom-level label failing to update from "Original Size" to "Scaled" when zooming in.
- Fixed odd visual interactions between tap-based navigation and smooth panel transitions.
- Fixed a bug where swiping down on the left edge could unintentionally close the panel viewer instead of just zooming out.
- Implemented general stability and memory-usage improvements through internal code optimization and quality audits.

## Included Commits

- `477dae6` docs: Cleaning up readme
- `6f72250` feat: Added kobo.koplugin support for corner/zoom zoom gesture & page-turner events (bluetooth devices already included)
- `f3a8a97` submodule: Added testing dependency busted
- `03ae058` kobo-support: Added emulation script for kobo and generic devices
- `ecbb355` feat: Now PanelPlus apply to cbr, cbz and pdfs by default!
- `815b609` feat: Added initial code for text selection feature
- `356dc71` feat: Improved comics panel support (hard to do btw, experimental feature)
- `e08bb6d` feat: Improved and added word recognizing and dictionary look up (Works 50% of the times - EXPERIMENTAL)
- `00c163a` feat: Polished comic reading mode
- `46c52ec` feat: Improved dictionary words detection (still complicated to implement)
- `4419f52` chore: Deleting some .log files and ignoring internal docs
- `3fe62b7` feat: Added dark mode support
- `977322d` performance: Fixed some memory leaks due to last feat commits
- `afafa2d` feat: Added swipe and taps navigation additional config
- `88d83c3` fix: Fixed bug with "Original Size" not changint to "Scaled" when doing zoom
- `fd7bacc` fix: Fixed bug with tap navigation and smooth fps
- `7139db4` fix: Tune word-gap threshold and clamp vertical runaway in word finder
- `3ddaa4a` feat: Add OCR debug review mode for word-lookup accuracy
- `bb468d0` feat: Add OCR debug session report tool
- `e6dd100` fix: Mark touch & hold text selection as experimental in menu
- `2565231` Optimization and code audit
- `b4f4386` rotation: Improved rotation button option a lot

## Upgrading

Copy `panels_plus.koplugin` over your existing folder and restart KOReader. Your settings will be preserved! The new touch-and-hold text selection is disabled by default (marked as experimental in the menu), and all navigation and gesture options can be configured from the panel viewer's "More config..." menu.

## Author

- KristanLaimon

# v1.2.0

<img width="3168" height="1344" alt="final" src="https://github.com/user-attachments/assets/bea7ff8b-c7c3-4a24-86c1-b76c89a808e7" />

# Panels+ | Smooth and cropped

Built from tag: `v1.2.0`

Hello PanelsPlus Users!, this was a really fast update. Somehow, I got motivated by some [some users really loving the plugin in reddit](https://www.reddit.com/r/koreader/comments/1utu32e/koreader_manga_kindle_comic_converter_tips/), so I get myself to work on an even better update than the last one in my free time these days.

# New Features

| Feature | Description |
| :---: | :--- |
| **Feature 1 (Major feat)** | **Smooth panel-to-panel navigation**<br><br>Switching panels can now pan the camera from the current panel to the next instead of cutting instantly. It's off by default (**Classic**); the *Navigation transition* menu switches it to **Smooth** and exposes sliders for the pan's duration and how many discrete frames it's split into. The frame count matters most on e-ink: it can be dropped to a single frame so the pan costs almost nothing on displays that already handle partial refresh poorly, or raised toward 24 on faster screens for a genuinely smooth pan. |
| **Feature 2 (Major feat)** | **Panning across page boundaries**<br><br>The camera pan now also runs when a swipe crosses from the last panel of one page to the first panel of the next, as long as the next page's panels are already cached in the background — otherwise the crossing quietly falls back to an instant cut rather than blocking the gesture on detection. |
| **Feature 3 (Major feat - Implicit)** | **A fourth crop option: "No crop"**<br><br>Alongside Strict, Loose, and With margin, a panel can now be shown **without cropping** at all: the viewer centers a screen-shaped window on the panel's own position on the page, so nearby page content that would normally be cut away stays visible, bounded only by the page's own edges (padded with white beyond them). Useful for panels sitting close to the page edge or to each other, where every other crop mode ends up clipping something. |
| **Feature 4 (Minor feature)** | **Loose crop can go up to 100%**<br><br>The bleed slider's cap went from 40% to 100%, and the bleed distance is now measured off the panel's *larger* dimension instead of its smaller one, so very wide or very tall panels bleed a proportionate amount instead of an oddly small one. |
| **Feature 5 (Buf-fixes and overall performance)** | **Kindle specific-bugs stability improvements and old Koreaders versions support**<br><br> |


<div align="center">
  <video src="https://github.com/user-attachments/assets/04ee9d71-915b-42e4-94de-ba0f8c84ab19" controls style="max-width: 100%;"></video>
  <cap>Features 1 to 3: Now optionally you can move trough pannels with animation, and animation includes CROSS-PAGE changes!, and "No Cut" feature, so you can see the panel surroundings even with the traditional crop (not animations)</cap>
</div>

## Important Notes about transition animation
The animation has FPS in transitions so it repaints a lot, its recommended to use this feature at 8fps in non ink-based devices (aka. Kindle), in case for ink-devices, I'd recommend 1 fps at most, but even that, its kinda strange, because it repaints the screen a lot and, moves weird due to ink-based-screens nature. Works far better in koreader for linux and mobile, and modern kobo devices, but if you really like it, there's no problem, its always accesible!, you can play with it if its to your taste!



## More Fixes

- Fixed a leaked transition-canvas image on every panel viewer close.
- "No crop" mode's page tiles used during a boundary-crossing pan are now freed instead of held for the rest of the session.
- Panning from a larger panel to a smaller one no longer risks its starting offset being silently clamped mid-animation.
- Native (Outline) detection now skips both its shared-context render and its per-probe fallback outright when free memory is under `native_detect_min_free_bytes` (100MB), instead of attempting up to 29 full-resolution renders — this plugin's single largest allocation — right when memory is already tight.
- Loose crop's bleed distance is now derived from the panel's larger dimension, so wide or tall panels no longer bleed a disproportionately small amount.
- The smooth-navigation frame count is a real, saved setting now (a "Transition frames" slider, 1–24) instead of the placeholder toggle it briefly shipped as; its floor was set to 1 specifically so e-ink readers can pick the least possible animation.

## Some new renaming 
- "Auto mode" 'modes' has been renamed to a more accurate naming, now deep mode, fast mode and auto mode. (not gutter and outline weird names)

## Included Commits

- `6bddc58` feat: Implemented smooth panning (Basic)
- `48f774b` feat: Added animation panning transitions across pages
- `aafdf69` feat: Expanded loose crop percentage cap (Until 100%, maybe doesn't have sense, but its funny)
- `a82d7f9` feat: No crop mode (and smooth navigation compatibility)
- `3fd874e` feat-fix: Fixed possible memory leaks and improved smooth navigation from bigger to smaller panels
- `47274ea` fix: Fixing more memory leaks happening in my kindle for many reasons
- `e86049e` feat-docs-fix: Improved performance in low memory devices (kindle!)
- `de7ddab` enhance: Setting minimum FPS for smooth transitions to 1 (foe e-ink-readers)

## Upgrading

Copy `panels_plus.koplugin` over your existing folder and restart KOReader. Your settings are kept; smooth navigation defaults to **Classic** (off) until you turn it on from the *Navigation transition* menu.

## Author

- KristanLaimon

Thanks for using PanelsPlus+, any bug you found, pls create an Issue and I'll fix it ASAP 👍🏻.

# v1.0.0-RC5

<img width="1923" height="817" alt="Panels+ Release Candidate 5 banner" src="https://github.com/user-attachments/assets/14ad347d-845b-42fb-a4e5-72efb34c428b" />

# Panels+ | Performance Update + Useful utilities

Built from tag: `v1.0.0-RC5`

This time, the release focuses on speed and pages/panels the panel detector used to miss. Opening panel view no longer stalls for seconds in very-low-end devices (yes, I'm looking at you `Kindle`), swiping between panels is smoother, and panels are now found on dark-background pages and in rows of small panels where detection previously gave up.

## Highlights

### Panel detection on dark pages
KOReader's default detector recognizes panels by searching for *white* gaps. On pages with dark backgrounds or inverted colors, detection previously failed completely. 
* **Dynamic Background Detection:** Panels+ now measures the page’s specific background color instead of assuming white.
* **Inverted Page Support:** Dark-mode and white-on-black pages are now detected with the same accuracy as standard pages.

<div align="center">
  <img src="https://github.com/user-attachments/assets/1e3db109-f35e-4908-ad6a-a1c343a0fc25" alt="Normal page" width="18%" /> &nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/65e92ff1-ecbd-4c90-973a-0b0518bcd4f2" alt="Panel 1" width="18%" />
  <img src="https://github.com/user-attachments/assets/821c677e-df36-4542-a50c-1ba541585384" alt="Panel 2" width="18%" />
  <img src="https://github.com/user-attachments/assets/3a3a1afd-cb8f-42f1-85f6-f377368f3948" alt="Panel 3" width="18%" />
  <img src="https://github.com/user-attachments/assets/921d8416-f7a9-49f4-a322-aa6ed35ed794" alt="Panel 4" width="18%" />
  <br><sub>Left: Normal page (no plugin) &nbsp;&nbsp;&nbsp;&#124;&nbsp;&nbsp;&nbsp; Right: Zoomed panels (Panels 1–4)</sub>
</div>



### Much faster panel detection
Opening the panel view previously required rasterizing the full page at high resolution multiple times, causing severe slowdowns on e-readers.
* **Single Reduced-Size Render:** Initial detection now runs against a lightweight, low-resolution ink map.
* **Reused Rasterizations:** The fallback detection path reuses a single rasterization across all probe points rather than re-rendering per probe.
* **Result:** Significantly faster startup when entering panel view, especially on lower-end hardware like Kindles.

### Smoother panel switching
Navigating between panels is now fluid and responsive.
* **Eliminated UI Stalls:** Removed the forced full Garbage Collection (GC) trigger that ran on every panel switch.
* **Background Pre-rendering:** The next panel renders in the background while you read the current one, making swipes feel instant.
* **Smart Memory Management:** Pre-rendering automatically turns off when system RAM is low to prevent crashes.

### Choose your detector
A new **Panel Detection** menu allows you to switch detection algorithms on the fly to handle tricky comic layouts.
* **Detector Modes:**
  * **Auto:** Attempts Gutter mode first and gracefully falls back to Outline mode.
  * **Gutter Mode:** Uses a fast, gap-based detector optimized for clean panel margins.
  * **Outline Mode:** Uses KOReader’s native, literal contour detector for irregular layouts.
* **Quick Toggle:** Cycle modes directly inside the panel viewer using the top-bar button.
* **Additional Controls:** Toggles added for pre-rendering behavior and detection performance logs. More info in [Modes.md](../MODES.md).

<p align="center" style="margin: 2rem 0;">
  <img src="https://github.com/user-attachments/assets/3d17c44e-262b-4047-9dd2-eabb7a025fa3" alt="Normal page (no plugin activated yet)" width="50%">
  <br>
  <sub>New button "Auto mode" that cycles through <strong>Auto</strong>, <strong>Gutter</strong> & <strong>Outline</strong> when pressing</sub>
</p>

### A third crop mode: "With margin"
Provides more flexibility over how panels fit on your screen, grouped into a dedicated control row in the viewer UI.
* **"With Margin" Mode:** Adds a small, comfortable zoom-out buffer around the panel without revealing surrounding page content.
* **Splash Page Guard:** Full-page and splash panels automatically bypass the margin zoom-out to avoid wasting screen real estate.
* **Long-Press Configuration:** 
  * Long-press the **Loose Crop** button to adjust the bleed area.
  * Long-press the **With Margin** button to tune the zoom-out padding. Both are now hinted as "(Long press config)" in their label.
* **Reorganized UI:** Crop and detector-mode buttons are now grouped together in their own row since both control how the current page is detected/cropped.

<div align="center">
  <video src="https://github.com/user-attachments/assets/aa34d5db-8e47-4b68-bd5b-fc90d3da6493" controls width="50%"></video>
  <br>
  <div style="display: inline-block; text-align: left; font-size: 0.9em; margin-top: 0.5rem;">
    * Margin and loose cropping are configurable by long-pressing those buttons when they are actually selected
  </div>
</div>

## Fixes

- Rows of small panels separated by narrow gutters are now split into individual panels instead of being returned as one. The minimum detectable gutter went from roughly 15px to roughly 7px on a 1600px-wide page.
- Panels separated by non-square or tilted gutters (up to 6 degrees) are now split using slanted line projections instead of being returned as a single grouped panel.
- Panel detection no longer re-rasterizes the full page for every probe point.
- Fixed bad page rendering handling where detector failures permanently disabled the batched fast-path session-wide, preventing high memory usage and KOReader crashes over long sessions.
- Removed the forced garbage collection that ran on every panel switch.
- Prefetch jobs scheduled for pages you have already turned past are now cancelled instead of all running anyway, and no scheduled work survives closing the document.
- The panel cache holds 12 pages instead of 2, so stepping back a page no longer re-detects it from scratch.
- Fixed the low-memory check for pre-rendering, which compared bytes against a kilobyte threshold and so never actually triggered.
- Colour pages are now converted once before scanning rather than being read pixel by pixel through the slow path.

## Documentation

This release adds a `docs/` folder describing how the plugin works, with diagrams:

- [Architecture](../ARCHITECTURE.md) — module map and what happens between a long hold and a panel on screen.
- [Panel detection](../DETECTION.md) — how panels are found, why there are two detectors, and every tuning knob.
- [Detector modes](../MODES.md) — reader-facing guide to Auto, Gutter, and Outline modes and how to diagnose misread pages.
- [Performance](../PERFORMANCE.md) — what each step costs, the memory budget, and how to measure it on your own device.

## Included Commits

- `3c01185` perf(detector): probe a whole page against one rasterization
- `c3b1fe6` feat(detector): detect panels from a low-resolution ink map
- `ddcc5a8` perf(viewer): stop forcing a full GC and warm the next panel
- `681e382` fix(cache): cancel stale prefetch work and keep more pages
- `0a50b89` feat(menu): expose detector choice, prerender and timing logs
- `5788415` docs: document the panel pipeline, detection and performance
- `c5e26fe` fix(viewer): compare prerender headroom in bytes, not kilobytes
- `3046f4d` perf(detector): sample the ink map from a greyscale buffer
- `02eb292` docs: avoid a mermaid reserved word in the module diagram
- `3c57e00` fix(detector): split panel rows separated by narrow gutters
- `30c7550` fix(detector): split panels whose gutters are not square
- `f25541b` feat(viewer): cycle Auto, Fast and Exact mode from the panel view
- `bb8fe6a` docs: cover tilted gutters and the viewer mode button
- `3880511` refactor(viewer-ui): Better names in new ui option
- `62db13f` fix: Fixed bad page rendering handling making crash koreader over time
- `42b5eb1` docs: Updated docs
- `ebd4683` chore(git): ignore vendored koreader reference tree
- `f6ccd6b` feat: Add adjustable "With margin" crop mode
- `9b5c617` feat: Make loose crop's bleed amount configurable via long-press
- `ea303d9` ui: Hint that Loose crop and With margin are long-press configurable
- `ced709c` ui: Move crop button to the second button row
- `0fd0edf` ui: Give detector and crop buttons their own third row

## Upgrading

Copy `panels_plus.koplugin` over your existing folder and restart KOReader. Your settings are kept; the detector and cache values tuned in this release are applied automatically.

## Author

- KristanLaimon

# v1.0.0-RC4

<img width="1922" height="818" alt="Panels+ Release Candidate 4 banner" src="https://github.com/user-attachments/assets/0377fbfc-baa2-4e01-bd22-acaad0b71871" />

# Panels+ | Quality of Life Update

Built from tag: `v1.0.0-RC4`

This release focuses on improving the panel-focused reading experience. It adds more control over the viewer UI, improves gesture behavior while Panels+ is active, and makes zooming and navigation feel smoother.

## Highlights

<div align="center">

| Feature | Description |
| :---: | :--- |
| **Feature 1** | **Toggle the bottom progress bar**<br><br>Added an option to hide or show KOReader's bottom progress bar while reading in focused-panel mode.<br><br><p align="center"><img width="360" alt="Bottom progress bar toggle option" src="https://github.com/user-attachments/assets/349d7107-5a76-48d3-bfaf-9288307a88b7" /></p> |
| **Feature 2** | **Use configured document gestures inside Panels+**<br><br>Document gestures configured in KOReader can now be used while reading through the Panels+ viewer. |
| **Feature 3** | **Switch back to KOReader native panel focus zoom**<br><br>Added an easy way to return to KOReader's native panel focus zoom behavior when preferred.<br><br><p align="center"><img width="360" alt="Native panel focus zoom option" src="https://github.com/user-attachments/assets/871b9536-deb5-4413-a0f0-063475e3a6fb" /></p> |
| **Feature 4** | **Mouse wheel zoom and improved panning**<br><br>Added mouse wheel zoom support and improved panning behavior for smoother navigation. |

</div>

## Fixes

- Fixed a `refreshfunc` issue that could affect viewer refresh behavior.
- Fixed spread and pinch gesture handling while a panel is focused.
- Spread and pinch gestures are no longer incorrectly forwarded as normal gestures.
- This also fixes the issue where zoom in and zoom out could be implicitly disabled.

## Included Commits

- `59a1b9c` feat: Added toggle bottom progress bar
- `51704ed` fix: Spread and Pinch gesture forwarded to plugins when panel focused
- `a50d0f7` fix: Fixed `refreshfunc` bug
- `0f4ae71` feat: Now user document gestures usable when using plugin
- `1b69e63` feat: Easily switch to native focus zoom
- `f15da0f` feat: Mouse zooming support and panning features

## Author

- KristanLaimon

# v1.0.0-RC3

<img width="1922" height="818" alt="ChatGPT Image May 23, 2026, 11_29_03 AM" src="https://github.com/user-attachments/assets/328c9f07-d54b-49f3-bb92-a818eeafef72" />

# Bugs, memory-leak and performance update

This time, I noticed that, when using for some time, the plugin used to crash koreader due to not freeing previous-already-read pannels. It's fixed now.


## Commits
- df4aa69 CI: Now pipeline publishes zip (i hope so) (KristanLaimon)
- eb5b0b4 fix: Fixing small memory leak when using plugin for long documents (KristanLaimon)
- b7ad029 docs: Update download link text in README.md (Kristan Ruíz)
- cc48e8a CI: Now fetches last tag instead of expecting last tag from merge (KristanLaimon)
- 6d64998 CI: Pipeline runnable from web now (KristanLaimon)
- 72d2bbf CI: Fixing github actions pipeline (KristanLaimon)

## Authors
- Kristan Ruíz
