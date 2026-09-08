# v1.8.0

## [1.8.0](https://github.com/Euphoriyy/appearance.koplugin/compare/v1.7.0...v1.8.0) (2026-09-08)
[![Github Downloads (by release)](https://img.shields.io/github/downloads/Euphoriyy/appearance.koplugin/v1.8.0/total.svg)](#)


### Features

* **book/font_color:** add dispatcher actions for toggling fixed page font color ([075f2ba](https://github.com/Euphoriyy/appearance.koplugin/commit/075f2baf0b620473a26f510b07490445bcd7ec19))
* **book/font_color:** add dispatcher actions for toggling fixed page link color ([182be74](https://github.com/Euphoriyy/appearance.koplugin/commit/182be74f9982f4cf441bef439c452f20cf62fc26))
* **book:** apply link color to fixed-layout docs ([96937ac](https://github.com/Euphoriyy/appearance.koplugin/commit/96937ac0bec17225b87d3a11282b98707c6f4e16)), closes [#94](https://github.com/Euphoriyy/appearance.koplugin/issues/94)
* **ui/misc:** add miscellaneous options for squaring corners ([94b7799](https://github.com/Euphoriyy/appearance.koplugin/commit/94b7799f82039791067e40ce2de517bf64070d7f))


### Bug Fixes

* **book/link_color:** update touchmenu items on reset ([1daf127](https://github.com/Euphoriyy/appearance.koplugin/commit/1daf1276c5c8d0a3594503f738602b19878e0e35))
* **book:** correct inversion of fixed-layout font color on Android ([1ee0793](https://github.com/Euphoriyy/appearance.koplugin/commit/1ee079375b4ee447181cf2eac88f31a6b629c3b6))
* **book:** refresh CSS on reader ready to fix inversion after restarts ([d3fd8e0](https://github.com/Euphoriyy/appearance.koplugin/commit/d3fd8e036b17e4590460f70f8a33d65ca9a0263c))
* **book:** refresh live changes to colors for fixed-layout docs ([63cf416](https://github.com/Euphoriyy/appearance.koplugin/commit/63cf41652b7c29a94d666c0e1777fd44ea2b8c88))
* **book:** remove faulty recolor skipping logic ([f98084e](https://github.com/Euphoriyy/appearance.koplugin/commit/f98084e9d145a098a2c3a6d247876882fe3818e9))
* **themes:** correct icon inversion when applying themes to "Both" ([1635526](https://github.com/Euphoriyy/appearance.koplugin/commit/16355262bc537beb6d3ce01b12ec0f05394e96aa))
* **themes:** keep menu open on resetting to current themes ([4c5ae8c](https://github.com/Euphoriyy/appearance.koplugin/commit/4c5ae8c0065a354776f9f8a5143a5baa62ec034e))
* **ui:** reload non-transparent icons on bg color changes ([843f08a](https://github.com/Euphoriyy/appearance.koplugin/commit/843f08a67ef7e310fc372f1157e83859559fc5a7))

*Supported KOReader Version: **v2026.07***

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

*Supported KOReader Version: **v2026.07***

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
