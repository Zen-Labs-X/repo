## Audiobook Read-Along v0.1.17.48

**Download, unzip, and copy `audiobook.koplugin/` to your KOReader plugins directory. Restart KOReader.**

### Included
- Plugin (all Lua files)
- Bundled espeak-ng (cross-compiled for Kobo armv7l)
- Bundled MBROLA voice support + 7 default voices (US English, French, German, Spanish, Chinese, Portuguese)
- Bundled Piper neural TTS + en_US-danny-low voice
- Bundled BlueALSA (BT audio bridge for BlueZ Kobo devices)
- Bundled kindle-gst-play (GStreamer WAV player for Cat 2 Kindles)
- Bundled kindle-gst-play-native (KinAMP-parity fallback for audio-less PW4-class Kindles)
- Bundled wav-play (ALSA player for PocketBook and other devices without aplay)
- Android TTS helper and MediaSession helpers (pre-built tts_helper.dex, media_session_helper.dex)

### Install paths
| Platform | Path |
|----------|------|
| Kobo | `.adds/koreader/plugins/` |
| Kindle | `koreader/plugins/` |
| Linux | `~/.config/koreader/plugins/` |
| Android | `/sdcard/koreader/plugins/` |

See [README](https://github.com/stradichenko/audiobook.koplugin/blob/master/README.md) for full documentation.


**Full Changelog**: https://github.com/stradichenko/audiobook.koplugin/compare/v0.1.17.47...v0.1.17.48