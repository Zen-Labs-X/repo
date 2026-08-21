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