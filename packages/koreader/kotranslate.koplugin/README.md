# KoTranslate — KOReader Plugin

**KoTranslate** is a KOReader plugin that provides machine translation with multiple providers. It works seamlessly with the [**KOTranslate** Android companion app](https://github.com/omer-faruq-android-apps/kotranslate) for truly offline translation, and supports 7 online translation services including DeepL, Google Cloud, Microsoft Azure, Yandex, Lingva, MyMemory, and LibreTranslate.

---

## Features

- **9 Translation Providers:**
  - **Default:** KOReader built-in Google Translate
  - **Offline:** KOTranslate companion app (Google ML Kit, no internet)
  - **DeepL:** Free tier 500K chars/month (API key required)
  - **Google Cloud:** Translation API (API key required)
  - **Microsoft Azure:** Free tier 2M chars/month (API key required)
  - **Yandex:** Translate API (API key required)
  - **Lingva:** Free, no API key (proxied Google Translate)
  - **MyMemory:** Free, 5000 chars/day, no API key
  - **LibreTranslate:** Free, self-hosted or public instances
- **56 Languages Supported:** Including English, Spanish, French, German, Chinese, Japanese, Arabic, and more
- **SQLite Cache:** All translations cached locally for instant reuse
- **Highlight Override:** Overrides KOReader's built-in Translate button (like assistant.koplugin)
- **Auto-Detection:** Automatically uses `localhost:8787` on Android KOReader
- **Remote Language Management:** View and manage companion app languages from KOReader
- **PC-Editable Configuration:** Single config file inside the plugin folder
- **Zero Binary Dependencies:** Pure Lua implementation

---

## Requirements

- **KOReader** (any recent version with plugin support)
- **For Offline Mode:**
  - Android device with **KOTranslate** companion app installed, OR
  - External Android phone on the same WiFi network
- **For Online Modes (free, no API key):**
  - Internet connection (Lingva, MyMemory, LibreTranslate)
- **For Online Modes (API key required):**
  - API key from the provider (DeepL, Google Cloud, Microsoft, Yandex)
  - Internet connection

---

## Installation

### Step 1: Install Plugin Files

1. **Download** or copy the `kotranslate.koplugin` folder
2. **Place it** in your KOReader plugins directory:
   - **Android:** `/sdcard/koreader/plugins/`
   - **Kobo:** `.adds/koreader/plugins/`
   - **Kindle:** `koreader/plugins/`

### Step 2: Create Configuration File

**IMPORTANT:** The plugin requires a configuration file to work.

1. Navigate to the plugin folder: `kotranslate.koplugin/`
2. Find the file: `kotranslate_configuration_sample.lua`
3. **Rename** or **copy** it to: `kotranslate_configuration.lua`
   - **Option A (Rename):** `kotranslate_configuration_sample.lua` → `kotranslate_configuration.lua`
   - **Option B (Copy):** Keep the sample and create a copy named `kotranslate_configuration.lua`

4. **(Optional)** Edit `kotranslate_configuration.lua` on your PC:
   - Change translation provider (default is `"default"`)
   - Add API keys for paid services (DeepL, Google, Microsoft, Yandex)
   - Adjust companion app address
   - Enable/disable cache
   - Change source/target languages

### Step 3: Restart KOReader

1. **Restart KOReader**
2. The plugin will appear in **Menu → Plugins → KoTranslate**

**Note:** If you skip Step 2, the plugin will create a default configuration file automatically, but it's recommended to use the sample file as a template.

---

## Quick Start

### For Android KOReader Users (Same Device)

1. **Install KOTranslate APK** on your Android device
2. **Open KOTranslate** → Tap **"Start Server"**
3. **Download language models** (e.g., English, Spanish)
4. **In KOReader** → Menu → Plugins → KoTranslate:
   - Mode: **Offline (Companion App)** (default)
   - Source Language: **English**
   - Target Language: **Spanish** (or your choice)
5. **Highlight any text** → Tap **"Translate"** → Done!

**Note:** The plugin automatically detects `localhost:8787` on Android — no configuration needed.

### For Kobo/Kindle Users (External Device)

1. **Install KOTranslate APK** on your **Android phone**
2. **Open KOTranslate** → Note the **IP address** (e.g., `192.168.1.42`)
3. **Download language models**
4. **Connect your Kobo/Kindle** to the **same WiFi network**
5. **In KOReader** → Menu → Plugins → KoTranslate:
   - Tap **"Companion App Address"**
   - Enter: `http://192.168.1.42:8787`
   - Save
6. **Set languages:**
   - Source Language: **English**
   - Target Language: **Your choice**
7. **Highlight any text** → Tap **"Translate"** → Done!

### For Free Online Providers (No API Key)

1. **In KOReader** → Menu → Plugins → KoTranslate:
   - Tap **"Provider"** → Select **"Lingva"** or  **"MyMemory"**
2. **Set target language**
3. **Highlight any text** → Tap **"Translate"** → Done!

### For Paid Online Providers (API Key Required)

1. **Edit the configuration file** on your PC:
   - Navigate to your KOReader plugins folder
   - Open `kotranslate.koplugin/kotranslate_configuration.lua`
   - Add your API key(s) in the `api_keys` section
   - Save and restart KOReader
2. **In KOReader** → Menu → Plugins → KoTranslate:
   - Tap **"Provider"** → Select the provider with your API key
3. **Highlight any text** → Tap **"Translate"** → Done!

**Supported paid providers:** DeepL, Google Cloud, Microsoft Azure, Yandex

---

## Usage

### Translating Text

#### From Highlight Menu
1. **Highlight any text** in your book
2. Tap **"Translate"** in the highlight menu
3. View the translation in a popup dialog

#### From Plugin Menu
1. Open **Menu → Tools → KoTranslate**
2. Tap **"Translate Input Text"**
3. Enter text manually
4. Tap **"Translate"**

### Switching Providers

1. Open **Menu → Tools → KoTranslate**
2. Tap **"Provider: ..."** at the top
3. Select from 9 available providers
4. Providers requiring API keys are disabled until keys are configured

### Changing Languages

1. Open **Menu → Tools → KoTranslate**
2. Tap **"Source Language: ..."** to change source
3. Tap **"Target Language: ..."** to change target
4. Select from the list of 56 languages

### Testing Connection

1. Open **Menu → Tools → KoTranslate**
2. Tap **"Test Connection"**
3. For offline mode: Shows companion app status and IP
4. For online mode: Performs a test translation

### Managing Companion App Languages

1. Open **Menu → Tools → KoTranslate**
2. Tap **"Manage Companion Languages"**
3. View downloaded and available languages
4. **Note:** To download/delete models, use the companion app directly

### Cache Management

1. Open **Menu → Tools → KoTranslate**
2. View **"Cache: X entries (Y KB)"** at the bottom
3. Tap **"Clear Cache"** to delete all cached translations

---

## Configuration

### Settings Location

All settings are stored inside the plugin folder:
```
kotranslate.koplugin/kotranslate_configuration.lua
```

**How to edit:**
1. Connect your e-reader to your PC
2. Navigate to the plugin folder
3. Open `kotranslate_configuration.lua` in any text editor (Notepad, VS Code, etc.)
4. Modify the settings (see table below)
5. Save the file
6. Restart KOReader to apply changes

**Template file:** A sample configuration file is provided as `kotranslate_configuration_sample.lua` for reference.

This file is a valid Lua file that returns a table with key-value pairs.

### Available Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `mode` | Translation provider ID | `default` |
| `source_lang` | Source language code or `auto` | `auto` |
| `target_lang` | Target language code | `tr` |
| `enable_cache` | Enable translation cache | `false` |
| `companion_address` | Companion app URL | `http://192.168.1.100:8787` |
| `api_keys.deepl_api_key` | DeepL API key | (empty) |
| `api_keys.google_api_key` | Google Cloud API key | (empty) |
| `api_keys.microsoft_api_key` | Microsoft Azure API key | (empty) |
| `api_keys.yandex_api_key` | Yandex API key | (empty) |
| `microsoft_region` | Azure region | `global` |
| `lingva_instance` | Lingva instance URL | `lingva.ml` |
| `libre_instance` | LibreTranslate instance URL | `libretranslate.com` |
| `libre_api_key` | LibreTranslate API key | (empty) |
| `mymemory_email` | MyMemory email for higher limits | (empty) |

### Cache Database

Translations are cached in:
```
<KOReader data directory>/kotranslate_cache.sqlite3
```

The cache stores:
- Source and target language
- Original and translated text
- Provider (offline/online)
- Usage statistics
- Book path (for per-book filtering)

---

## Architecture

### Plugin Structure

```
kotranslate.koplugin/
├── _meta.lua                                    # Plugin metadata
├── main.lua                                     # Entry point, menu, Translator override
├── kotranslate_configuration.lua    # User-editable configuration file
├── kotranslate_providers.lua        # All translation provider implementations
├── kotranslate_cache.lua            # SQLite cache layer
├── kotranslate_client.lua           # HTTP client for companion app
├── kotranslate_ui.lua               # UI dialogs and popups
├── kotranslate_languages.lua        # Language code mappings
├── roadmap.md                                   # Full architecture documentation
└── README.md                                    # This file
```

### Key Components

| Module | Purpose |
|--------|--------|
| `main.lua` | Plugin init, menu, Translator.showTranslation override |
| `kotranslate_configuration.lua` | User-editable settings (API keys, provider, languages) |
| `kotranslate_providers.lua` | 7 online translation providers (DeepL, Google, Microsoft, Yandex, Lingva, MyMemory, LibreTranslate) |
| `kotranslate_client.lua` | REST API client for companion app (7 endpoints) |
| `kotranslate_cache.lua` | SQLite-based translation cache with usage tracking |
| `kotranslate_ui.lua` | Translation result viewer, copy/save buttons |
| `kotranslate_languages.lua` | 56 language codes and names |

### Translation Flow

```
User highlights text
       ↓
Plugin checks cache
       ↓
Cache hit? → Show cached result
       ↓
Cache miss → Translate via mode:
       ↓
Offline mode:
  1. Try localhost:8787 (Android)
  2. Try configured companion address
       ↓
Online mode:
  1. Call selected provider API
       ↓
Store in cache → Show result
```

---

## Supported Languages (56 Total)

Afrikaans (af), Albanian (sq), Arabic (ar), Belarusian (be), Bengali (bn), Bulgarian (bg), Catalan (ca), Chinese (zh), Croatian (hr), Czech (cs), Danish (da), Dutch (nl), English (en), Esperanto (eo), Estonian (et), Finnish (fi), French (fr), Galician (gl), Georgian (ka), German (de), Greek (el), Gujarati (gu), Hindi (hi), Hungarian (hu), Icelandic (is), Indonesian (id), Irish (ga), Italian (it), Japanese (ja), Kannada (kn), Korean (ko), Latvian (lv), Lithuanian (lt), Macedonian (mk), Malay (ms), Maltese (mt), Marathi (mr), Norwegian (no), Persian (fa), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Slovak (sk), Slovenian (sl), Spanish (es), Swahili (sw), Swedish (sv), Tagalog (tl), Tamil (ta), Telugu (te), Thai (th), Turkish (tr), Ukrainian (uk), Urdu (ur), Vietnamese (vi), Welsh (cy)

---

## Troubleshooting

### Translation fails with "Cannot reach companion app"

**Cause:** KOReader cannot connect to the companion app.

**Solutions:**
1. **Check companion app:** Ensure KOTranslate is running and shows "Server Running"
2. **Check address:** Verify the IP address in KOReader matches the one shown in KOTranslate
3. **Same WiFi:** Both devices must be on the same WiFi network
4. **Firewall:** Some routers block device-to-device communication
5. **Test connection:** Use "Test Connection" in the plugin menu

### Translation fails with "model_not_downloaded"

**Cause:** Required language models are not downloaded in the companion app.

**Solutions:**
1. **Open KOTranslate** on your Android device
2. **Download both source and target language models**
3. **Download English** if translating between non-English pairs (used as pivot)

### Translations are slow

**Cause:** Network latency or first-time model loading.

**Solutions:**
1. **Use cache:** Repeated translations are instant (cached)
2. **Offline mode:** Faster than online mode (no internet roundtrip)
3. **Pre-download models:** Ensure models are downloaded before translating

### Cache not working

**Cause:** Database corruption or permission issues.

**Solutions:**
1. **Clear cache:** Menu → KoTranslate → Clear Cache
2. **Check permissions:** Ensure KOReader can write to data directory
3. **Restart KOReader**

### "Invalid JSON response" error

**Cause:** Companion app returned malformed data or crashed.

**Solutions:**
1. **Restart companion app:** Stop and start the server
2. **Check companion app logs:** Use `adb logcat` to view errors
3. **Update companion app:** Ensure you have the latest version

### Online provider fails with API error

**Cause:** Invalid API key, quota exceeded, or provider issue.

**Solutions:**
1. **Check API key:** Open `kotranslate_configuration.lua` on your PC and verify the key
2. **Try a free provider:** Switch to Lingva, MyMemory, or LibreTranslate (no key needed)
3. **Check quota:** Some providers have daily/monthly limits
4. **Test connection:** Use "Test Connection" in the plugin menu

---

## Performance

### Cache Hit Rate
- **First translation:** ~1-3 seconds (network + ML Kit)
- **Cached translation:** Instant (<50ms)
- **Cache size:** ~1-2 KB per translation

### Network Usage
- **Offline mode:** Zero internet usage (LAN only)
- **Online mode:** ~500 bytes per request (varies by text length)

### Storage
- **Plugin size:** ~30 KB
- **Cache database:** Grows with usage (~1-2 KB per unique translation)
- **Recommended:** Clear cache periodically if it exceeds 10 MB

---

## Privacy & Data

### Offline Mode
- **No internet required:** All translation happens on the companion device
- **No data sent to Google servers:** ML Kit runs entirely on-device
- **LAN only:** Communication stays within your local network

### Online Mode
- **Data sent to Google:** Text is sent to Google Cloud Translation API
- **Google Privacy Policy applies:** See https://policies.google.com/privacy
- **API key security:** Store securely, do not share

### Cache
- **Local storage only:** Cache database never leaves your device
- **No telemetry:** Plugin does not send any usage data

---

## Companion App

This plugin requires the **KOTranslate** Android companion app for offline mode.

**Download:** Build from source using Docker (see companion app README)

**Repository:** https://github.com/omer-faruq-android-apps/kotranslate

---

## License & Attribution

This plugin uses:
- **Google ML Kit** (via companion app) — Subject to [ML Kit Terms of Service](https://developers.google.com/ml-kit/terms)
- **Google Cloud Translation API** (online mode) — Subject to [Google Cloud Terms](https://cloud.google.com/terms)

**Attribution:** Powered by Google

---

## Contributing

For issues, feature requests, or contributions, please refer to the main KOReader plugin repository.

---

## See Also

- **Companion App README:**  https://github.com/omer-faruq-android-apps/kotranslate/blob/main/README.md
- **KOReader Documentation:** https://github.com/koreader/koreader
