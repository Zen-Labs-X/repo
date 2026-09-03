# v1.075

## What's Changed
* KOReader v2026.07 support by @marcopiraccini in https://github.com/Kaito0/panelreader.koplugin/pull/4


**Full Changelog**: https://github.com/Kaito0/panelreader.koplugin/compare/v1.07...v1.075

# v1.07

## What's Changed
* Add physical button navigation to panel viewer by @marcopiraccini in https://github.com/Kaito0/panelreader.koplugin/pull/2
* panel_viewer: add pinch-to-zoom and pan, reduce switch ghosting by @marcopiraccini in https://github.com/Kaito0/panelreader.koplugin/pull/3

## New Contributors
* @marcopiraccini made their first contribution in https://github.com/Kaito0/panelreader.koplugin/pull/2

**Full Changelog**: https://github.com/Kaito0/panelreader.koplugin/compare/v1.0.51...v1.07

# v1.0.51

+ Better centering,  boundaries and image scaling
+ Added horizonal offset option ( average ~2px dif)


Note: For now recommended method is YOLO. 

Recommended Workflow: KCC (Kindle Comic Converter) -> Device resolution -> Crop Margins (2.0 power) -> File Fusion (Batch) -> process_manga.py

# V1.0.41

- New panel image viewer 
- If a JSON panel file is found, PanelReader is enabled automatically. If no JSON is available, built-in Panel zoom is used as a fallback.
- Settings are moved to built in Panel Zoom submenu
- RTL/LTR direction option / auto pick from  JSON

# v1.0.314

Magi and Yolo algs support

## process_manga.py

Chapter archives, PIL coords, image formats

## PanelReader plugin

Handles chapter-based manga archives
