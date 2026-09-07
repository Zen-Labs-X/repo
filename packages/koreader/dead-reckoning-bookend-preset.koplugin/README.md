# Dead Reckoning

#### It is important to remember to update your margins after installing this preset and to disable the native status bar.

A [Bookends](https://github.com/AndyHazz/bookends.koplugin) preset for [KOReader](https://github.com/koreader/koreader): a navigation-themed reading cockpit that surfaces session speed, a finish-date projection, and chapter ETA, with chapter waypoints ticked along the progress bar. Text renders in a soft, low-contrast grey so the telemetry stays out of the way of the book.

<img width="1264" height="1680" alt="Dead Reckoning preset shown on a KOReader page" src="https://github.com/user-attachments/assets/73f2291d-1fa5-47da-a78e-3a85ba82b157" />

## Layout

| Zone | Shows |
|---|---|
| Top-left | Book title, series name and number |
| Top-center | Weekday and date |
| Top-right | Clock, battery level (with a charging flag and a low-battery warning under 20%) |
| Bottom-left | Session pages read and pages-per-hour pace |
| Bottom-right | Chapter pages left and time-to-finish ETA |
| Bottom-center | Percent of book read, pages left, and projected finish date |
| Progress bar | Pac-man style bar with a tick for every chapter boundary |

## Requirements

- [KOReader](https://github.com/koreader/koreader)
- The [Bookends](https://github.com/AndyHazz/bookends.koplugin) plugin

## Installation

Drop `dead-reckoning.lua` into Bookends' preset folder:

```
<koreader-data-dir>/settings/bookends_presets/
```

Then open **Bookends → Preset library** in KOReader and select **Dead Reckoning** from the list.

## Support

If this preset's useful to you and you'd like to chip in:

- liberapay · [liberapay.com/bdkl](https://liberapay.com/bdkl/)
- bitcoin
  ```
  bc1qkge6zr45tzqfwfmvma2ylumt6mg7wlwmhr05yv
  ```
