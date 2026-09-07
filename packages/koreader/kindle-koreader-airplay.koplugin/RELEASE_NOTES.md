# v1.1

## Install

1. Download the zip matching your Kindle's firmware:
   - `airplay.koplugin-sf-v1.1.zip` — firmware <=5.16.2.1.1 (Paperwhite 1-5, Voyage, Oasis 1-3)
   - `airplay.koplugin-hf-v1.1.zip` — firmware >=5.16.3 (Paperwhite 6/12, current Scribe, or any device updated past 5.16.2.1.1)
2. Unzip and copy `airplay.koplugin/` to your Kindle:
   ```
   cp -r airplay.koplugin /Volumes/Kindle/extensions/koreader/plugins/
   ```
3. Restart KOReader

**Not sure which one you need?** Check Settings → Device Info on the Kindle, or `cat /etc/prettyversion.txt` over SSH — anything 5.16.3 or newer is the hard-float (hf) build.

See [README](https://github.com/5kxh2dxqmd-afk/kindle-koreader-airplay/blob/main/README.md) for full setup instructions.

**Full Changelog**: https://github.com/5kxh2dxqmd-afk/kindle-koreader-airplay/compare/v1.3.1...v1.1

# v1-working

## Install

1. Download the zip matching your Kindle's firmware:
   - `airplay.koplugin-sf-v1-working.zip` — firmware <=5.16.2.1.1 (Paperwhite 1-5, Voyage, Oasis 1-3)
   - `airplay.koplugin-hf-v1-working.zip` — firmware >=5.16.3 (Paperwhite 6/12, current Scribe, or any device updated past 5.16.2.1.1)
2. Unzip and copy `airplay.koplugin/` to your Kindle:
   ```
   cp -r airplay.koplugin /Volumes/Kindle/extensions/koreader/plugins/
   ```
3. Restart KOReader

**Not sure which one you need?** Check Settings → Device Info on the Kindle, or `cat /etc/prettyversion.txt` over SSH — anything 5.16.3 or newer is the hard-float (hf) build.

See [README](https://github.com/5kxh2dxqmd-afk/kindle-koreader-airplay/blob/main/README.md) for full setup instructions.


**Full Changelog**: https://github.com/5kxh2dxqmd-afk/kindle-koreader-airplay/compare/v0-h264-continuous-decode-1...v1-working
