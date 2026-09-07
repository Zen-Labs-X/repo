# stretch.koplugin

Typically, when viewing manga in MuPDF, selecting Fit to Width preserves the original aspect ratio, which means scrolling to see the bottom of pages.
 
This plugin stretches every page to fill the screen completely. Portrait pages scale to fit full-screen with no scrolling. Wide two-page spreads are automatically rotated and stretched to fill the screen in landscape.
 
The patch is based on [KOReader Issue #14683](https://github.com/koreader/koreader/issues/14683) and specifically builds on the work by [@HeiCo2](https://github.com/HeiCo2).

## Requirements
 
- [KOReader](https://koreader.rocks)
- A document rendered via the MuPDF engine (PDF, CBZ, CBR, FB2, etc.)

## Installation
 
1. Download `stretch.koplugin.zip` from [Releases](../../releases)
2. Unzip it
3. Copy the `stretch.koplugin` folder into your KOReader plugins directory (`koreader/plugins/`)
4. Restart KOReader

## Usage
 
The plugin hooks into KOReader's rendering pipeline at startup. Open any image-based or fixed-layout document and set the zoom mode to one of:
 
- **Fit to Width** + **Zoom to Content**
- **Fit to Width** + **Zoom to Page**

Both produce a full-screen stretched view with no scrolling.

This also works best with crop mode to set to:
- **Page Crop** + **none**

## License
 
MIT — see [LICENSE](LICENSE)
