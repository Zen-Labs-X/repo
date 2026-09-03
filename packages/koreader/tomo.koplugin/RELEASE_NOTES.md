# v2.7.3

<!-- © 2026 James Edward Honiball. All Rights Reserved. -->
<!-- Tomo™ (友) — Social Reading Companion for Kobo -->
<!-- Paste the text below (from "Tomo v2.7.3" down) as the GitHub Release body. -->

Tomo v2.7.3

Writing letters works the way it should now, and the app fits your screen — whatever screen that is.

**Letter writing fixed.** The Seal and close buttons now respond reliably to finger taps on every device. Slow, deliberate presses work too. If your pen drifts while tapping, Tomo still understands. And sealing an empty page now tells you the page is empty instead of doing nothing.

**The home page always fits on one screen.** No scrolling, no cut-off corners — on any Kobo or Kindle, portrait or landscape. When book rooms bloom, the ones that fit appear on home and the Conservatory holds them all.

**True colours while you draw.** On colour devices, ink now appears in its real colour as you draw — blue is blue, not orange — including the fine pens and the colour swatch.

**Better on Kindle.** Your current book is recognised the moment you open it, book rooms can now bloom from Kindle readers, and updates install reliably on more firmware versions.

**Comfortable to touch everywhere.** Buttons, toggles, room rows, and links across the app are properly sized for fingers on every screen, from the smallest Kobo to the Kindle Scribe.

Also in this release: messages no longer duplicate in rooms, pen pal letters keep their delivery time, long reading sessions stay signed in, and the settings screen no longer clips its controls on large devices.

---

**To install for the first time:** download `tomo.koplugin-v2.7.3.zip` below, unzip it, and copy the `tomo.koplugin` folder into KOReader's `plugins` folder. Full step-by-step instructions are in the README.

**Already have Tomo?** It updates itself over Wi-Fi the next time you open it.

Requires KOReader 2024.07 or later.

# v2.7.0

# v2.6.6

Crash report dedup and upload fix, Kindle device ID fallback, crash log parser, crash-loop detection, full crash field population, atomic OTA with rollback, last_seen tracking, postcrossing debounce, penpal matching fix, reading presence reporting.

# v2.6.5

Fixed OTA updater failing silently. Update now retries on failure and always re-prompts until successful. OTA failures now report to crash telemetry.

# v2.6.4

Username and user data now persist across OTA updates. All settings cached from Supabase to external storage.
