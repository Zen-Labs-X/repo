# v1.7.0

## [1.7.0](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.6.1...v1.7.0) (2026-09-03)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.7.0/total.svg)](#)


### Features

* add option to invert icons in day mode ([0be8491](https://github.com/Euphoriyy/appearance.koplugin/commit/0be849140fd9cfb08cfeae2ea43d586d1d3e5ad8))
* **book/font_color:** add separator after fixed-layout docs option ([55c9978](https://github.com/Euphoriyy/appearance.koplugin/commit/55c997882372d07ac4be33c07dc482513738e4bf))
* **book:** add toggle for setting the font color on fixed-layout docs ([fe4d20b](https://github.com/Euphoriyy/appearance.koplugin/commit/fe4d20b696fd3c63468dd402d3e87fe659136765))
* **book:** apply font color to fixed-layout docs ([e575ad8](https://github.com/Euphoriyy/appearance.koplugin/commit/e575ad85da26fb70b9050a293ed9111179047f34))
* **themes:** add almonds, french blue, grape, and velvet ([b1f24bc](https://github.com/Euphoriyy/appearance.koplugin/commit/b1f24bc51a68549d0ef5c48e7914fffe0c8355c0))
* **themes:** add golden green and pastel pink ([9fae1ef](https://github.com/Euphoriyy/appearance.koplugin/commit/9fae1ef733f452c513a88264ee87b9863d6e19ba))
* **themes:** sync icon inversion settings on applying theme presets ([96657a3](https://github.com/Euphoriyy/appearance.koplugin/commit/96657a3febc7d97acbdbdf7d7f105a0206760715))
* **ui:** add toggleable color-accurate flashing refreshes (e-ink) ([fdcf202](https://github.com/Euphoriyy/appearance.koplugin/commit/fdcf20253acb63d304ae0b3c82c2cf7b9db8c66c))
* **widgets/colorwheelwidget:** add dithering refresh on show (e-ink) ([98881a0](https://github.com/Euphoriyy/appearance.koplugin/commit/98881a04a39460c3c80234eca4832ab1d122f713))


### Bug Fixes

* **book:** skip color replacement when colors are at defaults ([da59099](https://github.com/Euphoriyy/appearance.koplugin/commit/da590995796f5387c5b6ab706619f9fa073d86ee))
* **themes:** keep menu open on resetting themes ([e53134d](https://github.com/Euphoriyy/appearance.koplugin/commit/e53134d6aa19820182f72fe15c0111d06ad2c641))
* **themes:** use correct icon inversion defaults on reset ([c58297b](https://github.com/Euphoriyy/appearance.koplugin/commit/c58297b629009db22ba199b0c0246ceee5fccbf5))
* **ui/background_image:** preserve location and pagination on reload ([88a20bb](https://github.com/Euphoriyy/appearance.koplugin/commit/88a20bb4701332b1358517ef89c09729af20a83b))
* **ui/font_face:** override font for already loaded widgets ([95685af](https://github.com/Euphoriyy/appearance.koplugin/commit/95685af31cfc7864cb13820708c86b619cbecb53)), closes [#79](https://github.com/Euphoriyy/appearance.koplugin/issues/79)
* **ui:** prevent excess color-accurate refreshes (e-ink) ([c383ca0](https://github.com/Euphoriyy/appearance.koplugin/commit/c383ca0fc1bf5008b6af816c06bda8b499c4f747))


### Performance Improvements

* optimize toggling night mode ([5f45d30](https://github.com/Euphoriyy/appearance.koplugin/commit/5f45d302d35b24a0b49faea54e51de8e8aadd513))

# v1.6.1

## [1.6.1](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.6.0...v1.6.1) (2026-08-19)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.6.1/total.svg)](#)


### Bug Fixes

* add link color to footnote popup widget ([3f632e8](https://github.com/Euphoriyy/appearance.koplugin/commit/3f632e8bb9acaa167ba318cec529cd89d897943f))
* apply link color changes properly ([26730f1](https://github.com/Euphoriyy/appearance.koplugin/commit/26730f148eca80806f0d6865f87418e18fdb99c9))
* **book:** prevent extra inversion of grayscale colors ([fa68be9](https://github.com/Euphoriyy/appearance.koplugin/commit/fa68be9b4cfb263e4cd7420d50987353688d3722))
* correct inverted night colors in rolling docs ([6dde78a](https://github.com/Euphoriyy/appearance.koplugin/commit/6dde78a3861c4121f1b49cace21c02e87ad38f4b)), closes [#76](https://github.com/Euphoriyy/appearance.koplugin/issues/76)
* show bookmark colors in the bookmarks list ([c99bd6c](https://github.com/Euphoriyy/appearance.koplugin/commit/c99bd6ce2f9ca670e7bb2da23cdc1e1dff1ebe65)), closes [#78](https://github.com/Euphoriyy/appearance.koplugin/issues/78)
* **ui:** remove SimpleUI patches to prevent crashes ([a568326](https://github.com/Euphoriyy/appearance.koplugin/commit/a5683266fade21a18621d9c590adfb6130e50441))

*Supported KOReader Version: **v2026.07***

# v1.6.0

## [1.6.0](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.5.1...v1.6.0) (2026-07-27)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.6.0/total.svg)](#)

> [!IMPORTANT]  
> This release resolves issues that cause crashes when loading documents or attempting to update from within the plugin. Please update manually.


### Features

* **ui/dict_font_face:** add toggle for changing the titlebar font ([3b173ef](https://github.com/Euphoriyy/appearance.koplugin/commit/3b173efb7f99b59fd431d7d9b2ee223d9029e129))


### Bug Fixes

* **book/background_color:** forward saturation argument ([4830dd0](https://github.com/Euphoriyy/appearance.koplugin/commit/4830dd0ea9617d038cfda5c352ec3fd8d7c9ab48)), closes [#67](https://github.com/Euphoriyy/appearance.koplugin/issues/67)
* **lib/updater:** implement function for unpacking archives ([64b160d](https://github.com/Euphoriyy/appearance.koplugin/commit/64b160d47b3d3d0af8e98e880f619cebc25ae6fd))
* **meta:** remove deprecated name field ([83850c1](https://github.com/Euphoriyy/appearance.koplugin/commit/83850c14eeb5cb56283483e2b5cf7f66ca24a84c))
* **ui/font_face:** refresh titlebar font after applying changes ([128189f](https://github.com/Euphoriyy/appearance.koplugin/commit/128189f0f04534271797a910195c357d2befd9e0))
* **ui:** correct font detection behavior ([d1cd4ad](https://github.com/Euphoriyy/appearance.koplugin/commit/d1cd4addfe672e99e60f60dd2f5751cfb84d6edd))

*Supported KOReader Version: **v2026.07***

# v1.5.1

## [1.5.1](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.5.0...v1.5.1) (2026-05-16)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.5.1/total.svg)](#)


### Bug Fixes

* **ui/background_image:** clear SimpleUI widget cache before setupLayout in reload_filemanager ([510fc06](https://github.com/Euphoriyy/appearance.koplugin/commit/510fc0684261bb3ae3a43036e87b2170de37c13e)), closes [#58](https://github.com/Euphoriyy/appearance.koplugin/issues/58)
* **ui/background_image:** properly reload and repaint SimpleUI homescreen on background changes ([c496164](https://github.com/Euphoriyy/appearance.koplugin/commit/c496164549c9ceecda1437b18dbc09b4b8fac4f6))
* **ui/background_image:** skip image reload when adjusting transparency settings ([bce6862](https://github.com/Euphoriyy/appearance.koplugin/commit/bce686289729cc94dbb23fb4dfe9a24a623793cc))
* **ui/transparency:** correct grammar in bottom bar transparency menu label ([f8e82e4](https://github.com/Euphoriyy/appearance.koplugin/commit/f8e82e47092d51a7b6333a87841b769d2824ca9a))

*Supported KOReader Version: **v2026.03***

# v1.5.0

## [1.5.0](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.4.0...v1.5.0) (2026-05-06)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.5.0/total.svg)](#)


### Features

* add about menu, in-plugin updater, and background update checks ([93d553b](https://github.com/Euphoriyy/appearance.koplugin/commit/93d553bb828c73d97f64e90d0a17365c956a9a8f)), closes [#41](https://github.com/Euphoriyy/appearance.koplugin/issues/41)
* **book/highlight_colors:** add option for setting the default color ([d50be25](https://github.com/Euphoriyy/appearance.koplugin/commit/d50be253726d9fedcc520b3a07d8a7f634694df0))
* **book:** apply background and font colors to footnote popups ([cc27611](https://github.com/Euphoriyy/appearance.koplugin/commit/cc27611d036f466297bf94c148879743f4432840)), closes [#45](https://github.com/Euphoriyy/appearance.koplugin/issues/45)
* **main:** implement method to delete plugin settings ([d2e22b5](https://github.com/Euphoriyy/appearance.koplugin/commit/d2e22b52410761b53259817d20ca2d5e8a22989b)), closes [#48](https://github.com/Euphoriyy/appearance.koplugin/issues/48)
* migrate plugin settings and add menu to plugin ([46319df](https://github.com/Euphoriyy/appearance.koplugin/commit/46319dfd7f42d92b264ad2f774c74f704cde8aa6)), closes [#49](https://github.com/Euphoriyy/appearance.koplugin/issues/49)
* **themes:** add option to reset theme link color ([487e515](https://github.com/Euphoriyy/appearance.koplugin/commit/487e5153073c227be3de1da68637866743661bea))
* **ui/background_image:** add transparency level and background color blending ([836a259](https://github.com/Euphoriyy/appearance.koplugin/commit/836a2598dd9a09235c421008eab32876a643a2d4)), closes [#42](https://github.com/Euphoriyy/appearance.koplugin/issues/42)
* **ui/transparency:** add transparent SimpleUI bottom bar setting ([09deecc](https://github.com/Euphoriyy/appearance.koplugin/commit/09deecc071a4e762d86c78010a321aaa59e1aedb)), closes [#32](https://github.com/Euphoriyy/appearance.koplugin/issues/32)
* **ui:** add optional system fonts support ([e9d6e97](https://github.com/Euphoriyy/appearance.koplugin/commit/e9d6e9766836fa25829de275db02f8f6187db5db))
* **widgets/colorwheelwidget:** add border to color wheel for better visibility ([c1aecdb](https://github.com/Euphoriyy/appearance.koplugin/commit/c1aecdb9cd3626499287f42fa1ecbf484a192dde))


### Bug Fixes

* **book/background_color:** only use Android recolor paths when using the C blitter ([92bf77e](https://github.com/Euphoriyy/appearance.koplugin/commit/92bf77e2c295cae746e04876e888948717ad3c5d))
* **book/link_color:** clear computed_hex when reverting to default link color ([7d02958](https://github.com/Euphoriyy/appearance.koplugin/commit/7d029587b12f44815f01e9bcc55957c573b2a318))
* **book/link_color:** disable "Reset color" when no custom link color is set ([915d266](https://github.com/Euphoriyy/appearance.koplugin/commit/915d266a26ee159c89bb4e88e7fd68d31214b056))
* **themes:** only show reset link color button when theme has a link color set ([e3e94fd](https://github.com/Euphoriyy/appearance.koplugin/commit/e3e94fdaabb4f9d464e3ad09d9a185bfc6bf6389))
* **ui/background_color:** correct highlight background inversion for buttons ([aad9439](https://github.com/Euphoriyy/appearance.koplugin/commit/aad9439ab0ca84246b91ae035564859ce93b2bf1))
* **ui/background_image:** restore compatibility with SimpleUI's currently reading module ([3be99bc](https://github.com/Euphoriyy/appearance.koplugin/commit/3be99bc1df114315c372438746d7985218a1c857)), closes [#51](https://github.com/Euphoriyy/appearance.koplugin/issues/51)


### Performance Improvements

* **book/background_color:** skip color application for fixed-layout docs when color is default ([f770bb8](https://github.com/Euphoriyy/appearance.koplugin/commit/f770bb800399a53f16c877194d29b5ab406dbe6e))
