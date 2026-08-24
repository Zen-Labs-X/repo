**Fixes the in-app updater**

Installing an update crashed KOReader before it could finish. Bookends unpacked the downloaded file using a KOReader helper that was removed from KOReader itself in mid-2026, so on current versions that call failed and took the reader down with it. It now unpacks using the same library KOReader uses internally.

The download was never the problem, so nothing was left half-installed — the previous version stayed in place and came back on restart.

**If you're on v5.23.0 or earlier you'll need to install this one by hand.** The updater is the thing that was broken, so it can't update itself. Download the zip below, unzip it, and copy the `bookends.koplugin` folder over the existing one in your KOReader `plugins` directory. Updates after this one work normally again.

Everything in [v5.23.0](https://github.com/AndyHazz/bookends.koplugin/releases/tag/v5.23.0) is included — auto preset by file type, the progress-marker fix, the new tokens, and Ukrainian and European Portuguese translations.
