# v0.9.7-beta.1

### This is a beta release.

<img width="1600" height="1282" alt="IMG_6390" src="https://github.com/user-attachments/assets/ca98b377-2d8c-45c6-b31a-9b34489e0900" />


It's been a while since I tinkered with my kindle. It's about time this plugin gets some love again.
The statistics show that there are still quite a few users enjoying it. (Unless someone is misusing my API key :D)
Well, here we go:

## Changes 

* Users can now select the shown hours directly in the settings: no need for the user patch anymore. 
* There is now an `Override Rotation` setting, which allows you to put the screensaver in landscape mode. 
* Adapted layouts for Today&Tomorrow, Today, Current for landscape modes. 
* Added icons to the settings menu, which hopefully make it a bit prettier and easier to read.


## Bugs fixed

* Fixed a crash in cover mode, when no cover is available for the last book


## What's Changed
* Landscape mode by @loeffner in https://github.com/loeffner/WeatherLockscreen/pull/35


**Full Changelog**: https://github.com/loeffner/WeatherLockscreen/compare/v0.9.6-beta.2...v0.9.7-beta.1

# v0.9.6-beta.2

### This is a beta release.

## Changes 

* Menus now use radio buttons, when the user can choose a predefined set of mutually exclusive options.

## Bugs fixed

* Fixed potential crashes.
* Several refactoring to make the code easier to read.
* Removed uneccessary files from the install zip.

## What's Changed
* Bugfixes and refactorings by @loeffner in https://github.com/loeffner/WeatherLockscreen/pull/29

**Full Changelog**: https://github.com/loeffner/WeatherLockscreen/compare/v0.9.6-beta.1...v0.9.6-beta.2

# v0.9.6-beta.1

### This is a beta release.

## New Features
* The sun and moon icons previously used as a fallback have been removed. Instead, you can now select one of the default screen savers as a fallback in case of a missing internet connection or a faulty API.
* New “Today-focused” display mode (with “feels like” information) by @moyencourt.
* The “Cover” display mode is now also available outside the reader (i.e., in the file browser).
* The “Cover” display mode has a new option to “Stretch to fill” the cover (in addition to “Zoom to fill” and “Fit to screen”).
* Thanks to @omer-faruq, the WeatherLockscreen plugin is now available in Turkish.


## Changes

* Some display modes have been renamed to be more descriptive:

  * Detailed → Today & Tomorrow
  * Minimal → Current
  * Today (new)

* Check out my [patches](https://github.com/loeffner/KOReader.patches) if you want to customize which hours are shown in the "Today & Tomorrow" and "Today" views.

## Bugs fixed

* Temperature was sometimes rounded incorrectly. This has been fixed by @moyencourt.
* The header font size (which shows the location and timestamp of the weather data) is now the same across all display modes. It has been increased slightly for some modes to make it easier to read.

## What's Changed
* Translation for Turkish by @omer-faruq in https://github.com/loeffner/WeatherLockscreen/pull/19
* fix: round to nearest integer by @moyencourt in https://github.com/loeffner/WeatherLockscreen/pull/23
* add day-focused display by @moyencourt in https://github.com/loeffner/WeatherLockscreen/pull/24
* Add option to configure the fallback by @loeffner in https://github.com/loeffner/WeatherLockscreen/pull/27
* Better cover option by @loeffner in https://github.com/loeffner/WeatherLockscreen/pull/28

## New Contributors
* @moyencourt made their first contribution in https://github.com/loeffner/WeatherLockscreen/pull/23

**Full Changelog**: https://github.com/loeffner/WeatherLockscreen/compare/v0.9.5-beta.1...v0.9.6-beta.1

# v0.9.5-beta.1

### This is a beta release.

## New Features
<img width="222" height="88" alt="image" src="https://github.com/user-attachments/assets/5612a89c-e793-44d0-bdc2-c7cde8ed292f" />

## Active Sleep Mode
- Now available to Kobo (thanks to a contribution by @omer-faruq)
- Active Sleep will now be disabled, when the battery falls below a configurable threshold  (idea and implementation by @omer-faruq)



## New Contributors
* @omer-faruq made their first contribution in https://github.com/loeffner/WeatherLockscreen/pull/16

**Full Changelog**: https://github.com/loeffner/WeatherLockscreen/compare/v0.9.4-beta.1...v0.9.5-beta.1

# v0.9.4-beta.1

### This is a beta release.

## New Features

https://github.com/user-attachments/assets/7907b5b1-c677-49d0-9727-9f1f5361d9dc

## Active Sleep Mode

- Device wakes from sleep periodically to update weather, then returns to sleep
- Low battery consumption 
- Only Kindle devices are currently supported. 
- Configurable intervals: 30 minutes, 1, 3, 6, 12 hours

> Currently, this feature is only supported in Kindle devices. I do not own a Kobo device and can not test this feature. If you want to help me get this feature to Kobo devices, please contact me. 

## Dashboard Mode

- Full-screen weather display that auto-refreshes
- Works on all devices (Kindle, Kobo, etc.)
- Configurable intervals: 30 minutes, 1, 3, 6, 12 hours
- Tap anywhere to dismiss the dashboard
- Higher battery consumption (device stays awake during display)

## Gesture support

The dashboard can be started with a configurable gesture. 
To enable it use the `Gesture manager`.

## Improved network handling

resolves #1. The device will enable Wi-Fi and search for available networks. 
This requires that the setting `Action when Wi-Fi is off:` is set to `Turn on`. 

## What's Changed
* Periodic refresh by @loeffner in https://github.com/loeffner/WeatherLockscreen/pull/14


**Full Changelog**: https://github.com/loeffner/WeatherLockscreen/compare/v0.9.3-beta.1...v0.9.4-beta.1
