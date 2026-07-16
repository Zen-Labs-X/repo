# Kamare (kamare.koplugin)

**kamare** is a manga reader plugin for [KOReader](https://github.com/koreader/koreader) that 
connects to [Kavita](https://github.com/Kareadita/Kavita).

This KOReader plugin provides a seamless way to read manga from Kavita without going through OPDS, 
featuring a custom renderer that also supports long-strip formats commonly used in manhwa.

## Features

- **Direct Kavita Integration** - Browse your library without OPDS limitations
- **Multiple Reading Modes** - Page, scroll (long-strip), and dual-page modes
- **Smart Prefetching** - Fast page turns through caching
- **Progress Tracking** - Syncs with Kavita and KOReader reading stats
- **Optimized Renderer** - Custom-built for fluid manga reading experience

Tested with Kindle Paperwhite (2nd gen) and Kobo Libra Colour.

## Screenshots

<table>
<tr>
<td align="center" valign="top">
<img src="doc/main-screen.png" alt="Library home">
<br><b>Library Home</b>
<br>Browse by On Deck, Recently Updated, and Want to Read
</td>
<td align="center" valign="top">
<img src="doc/series-screen.png" alt="Chapter list">
<br><b>Chapter List</b>
<br>View all chapters with progress tracking
</td>
</tr>
</table>

## Reading Modes

<table>
<tr>
<td align="center" valign="top">
<img src="doc/page-mode.png" alt="Page mode">
<br><b>Page Mode</b>
<br>Classic single-page view
</td>
<td align="center" valign="top">
<img src="doc/scroll-mode.png" alt="Scroll mode">
<br><b>Scroll Mode</b>
<br>For webtoons and long-strip formats
</td>
<td align="center" valign="top">
<img src="doc/dual-page-mode.png" alt="Dual page mode">
<br><b>Dual Page Mode</b>
<br>More Book like horizontally or on wider screens
</td>
</tr>
</table>

## Installation & Setup

1. Download the latest `kamare.koplugin.zip` from the [releases page](https://github.com/fpammer/kamare.koplugin/releases/latest).
2. Extract the ZIP and copy the `kamare.koplugin` folder into the `plugins` directory of your KOReader installation.
3. Restart KOReader to load the plugin.
4. Open the plugin from the KOReader menu (🔍) and add your Kavita server from the burger menu (top-left).:
<p align="center">
<img src="doc/server-setup.png" width="500" alt="Server setup">
</p>
5. Enter a server name, URL (with protocol eg. https://kavita.hostname.zone), and Kavita API key

### Getting Your Kavita API Key

1. Log into your Kavita web interface
2. Go to **Settings** → **Account** → **API Key**
3. Generate a new key if needed and type it to the setup dialog

## Configuration

Access settings while reading by tapping the screen. Customize your experience:

- **View Modes**: Switch between scroll, page, and dual-page modes
- **Page Direction**: LTR or RTL
- **Prefetching**: Prefetch next pages for smooth reading
- **Render Quality**: Balance between quality and speed (also helps with older devices, or crazy files)

<details>
<summary><b>View all settings</b></summary>

<table>
<tr>
<td align="center" valign="top">
<img src="doc/settings-general.png" alt="General settings">
<br><b>General</b>
</td>
<td align="center" valign="top">
<img src="doc/settings-page.png" alt="Page settings">
<br><b>Page</b>
</td>
<td align="center" valign="top">
<img src="doc/settings-zoom.png" alt="Zoom settings">
<br><b>Zoom</b>
</td>
</tr>
</table>

</details>
