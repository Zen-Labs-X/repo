Neo Quick Settings v1.20 - Changelog
🚀 New Features
✨ Menu Shortcut Capture (Capture Mode):

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
🙏 Special Thanks
Zenos UI / AnthonyGress: We were inspired by the Zenos UI plugin and utilized some of its code for our interface components and basic architectures. Endless thanks to [AnthonyGress](https://github.com/AnthonyGress) for his contributions and support to the open-source community!