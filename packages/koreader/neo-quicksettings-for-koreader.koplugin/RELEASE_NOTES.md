# v1.21

Added a smart timer that automatically pauses in sleep mode.
Fixed a bug causing the timer to count faster than normal.
Added an independent language selection menu supporting 13 languages.
Added an option to hide the Min/Max buttons on sliders.
Fixed UI overflow issues caused by long translation texts.

# v1.20

Neo Quick Settings v1.20 - Changelog
New Features
Menu Shortcut Capture (Capture Mode):

One of the most revolutionary features has been added! You no longer need to get lost in hundreds of codes or functions when creating a custom button.
When you tap the "Capture Mode" option, the system redirects you to KOReader's native main menu. Simply navigate to any setting or feature you want and long press it.
The plugin automatically captures the exact menu path you took in the background (neo_menu_path) and assigns it to your custom button. You can turn absolutely any menu item into a quick setting button in seconds!
Advanced Icon Manager:

The button icon selection infrastructure has been completely revamped and moved to a powerful Icon Manager interface (neo_icon_picker).
Changing icons is now much more professional and easier with a new visual picker integrated with the system.
Dozens of new high-quality SVG icons have been added (e.g., from Fluent, HugeIcons, Lucide, MDI libraries).
Expanded Slider Options (Total of 15 Styles):

New styles have been added for brightness and warmth sliders. 11 new styles have been added to the existing 4, bringing the total number of slider styles to 15!
Newly added styles include: Square Notched, Outline, Fader, Dots, Cyber Bar, Retro Switch, Split Rail, Stepped Bars, Fluid Pill, Battery Indicator, Pearls, Piano Keys, etc.
Slider codes have been heavily optimized and moved to common/neo_slider.lua for a more modular architecture.
Reading Goals:

Time Goal: Ability to set reading goals in minutes with a new button added to the quick settings panel.
Page Goal: Ability to set a target number of pages to read.
End of Chapter Shortcut: When the relevant button is held down or selected in the goal assignment window, the system automatically calculates the "pages left until the end of the chapter" and sets the goal accordingly (Integrated with "Ninja Engine").
Smart Toast Notifications:

Reading progress (pages/time read) and remaining goal messages are displayed in a custom, elegant, multi-line format.
Dynamic Width & Corner Radius: Toast notification boxes now smartly adjust their width according to the text length and have rounded corners (radius) conforming to KOReader standards.
Toast Position: You can now choose where the notifications will appear on the screen (Top, Bottom, Corners, etc., in 7 different positions) with transparent edge padding protection.
Detailed Reading Reminders:

A comprehensive reminder system under Reading Reminders:
Progress Reminders: Periodically notifies your progress when a specific time or page count is reached.
Goal Reminders: Notifies you of the remaining time/pages to your goal.
Ability to enter custom values and a logical separation infrastructure that prevents different reminder types from overlapping/conflicting.
🛠 Improvements & Bug Fixes
Significant code optimizations were made in the general structure of the plugin. Common functions have been separated into new modules like common/utils.lua and common/neo_toggle.lua.
Fixed critical issues where button definitions (button_defs) went into infinite loops or crashed KOReader due to require function scoping.
Session time read and page tracking are now hooked to start silently in the background when a book is opened (onReaderReady).
Cleaned up duplicated sub-menus that were accidentally copied into custom button creation and "Add/Remove" areas.
Fixed the "unfinished string" error in notification screens.
Updated version information in _meta.lua to 1.20.
.
 Special Thanks
Zenos UI / AnthonyGress: We were inspired by the Zenos UI plugin and utilized some of its code for our interface components and basic architectures. Endless thanks to [AnthonyGress](https://github.com/AnthonyGress) for his contributions and support to the open-source community!

# v1.10

Neo Quick Settings Changelog (v1.10)

***Improvements & Fixes

**Performance Boost: Fixed lags and improved performance during fast panning/sliding gestures on brightness and warmth sliders.
**Fluid Layout: Prevented the slider knob from disappearing while dragging to ensure a smoother visual experience.
**Visual Glitch Fix: Resolved the visual misalignment that caused brightness/warmth values to draw slightly above the slider track.
**Persistence Fix: Fixed the issue where disabling the plugin via the Plugin Management menu would reset and reactivate after a device restart. 

******Note: Special thanks to @renandeivison for writing the amazing fluidity code, detecting the visual alignment glitch, and reporting the plugin naming bug! Your contributions are greatly appreciated!

# Koreader-plugin

# Neo QuickSettings for KOReader

A highly customizable, powerful, and visually rich quick settings panel plugin for KOReader. **Neo QuickSettings** redefines how you interact with your device by giving you full control over your shortcuts, sliders, and UI appearance.

##  Features

- ** Visual Icon Picker:** No more guessing icon names! A fully visual, searchable icon picker screen lets you browse through hundreds of icons (Dark, Solid, Mixed) and assign them to your buttons instantly.
- ** Custom Buttons (Scripts):** Create, edit, and manage your own custom buttons with assigned actions. Includes a robust Draft/Discard system so you can test your edits without breaking your setup.
- ** Favorite Groups:** Organize your most-used actions into neat, tabbed sub-menus (Favorite Groups) to keep your quick settings panel clean and organized.
- ** SimpleUI Integration:** Seamlessly send your favorite shortcuts directly to the SimpleUI launcher.
- ** Advanced Sliders:** Take control of your reading environment with up to 4 customizable sliders for Frontlight (Brightness) and Warmth. Choose between smooth sliding or notched step-by-step styles.
- ** Rich Customization:** Limitless UI tweaking. Hide/show specific buttons, change button labels, adjust icon scale, toggle borders, and arrange everything exactly as you like it.

##  Installation

1. Download the plugin package.
2. Extract the contents and copy the `neo_quicksetting.koplugin` folder into your device's KOReader plugins directory:
   - `koreader/plugins/`
3. **Important: Inside the downloaded package, there is an icons folder. You must copy the entire contents of this folder and place them inside KOReader's core icons directory:- koreader/icons/
4. Restart KOReader.
5. You can now access Neo QuickSettings from the KOReader top menu or assign it to a gesture!

##  Usage
Once installed, open the QuickSettings panel. To customize your experience, long-press any button or tap the "Settings" gear icon to enter the **Appearance Options** and **Add/Remove Buttons** menus.

**Full Changelog**: https://github.com/yanllsama/Neo-QuickSettings-for-KOReader/commits/koreader-patches
