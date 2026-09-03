# v1.30

**API and Limits: Switched to Open Library due to Google Books API restrictions, and HTTP errors when fetching page counts have been fixed.

**Book Map Layout: Fixed the issue where the Book Map would get cropped at the end when the physical page count (e.g., 384) differed from the native document page count (e.g., 564). The map now opens smoothly in its original dimensions without breaking the layout. Please note that due to current restrictions, page ticks may occasionally appear blank. This issue will be addressed in future updates.

**Progress Arrow: The progress arrow (▲) now points to your current page with pinpoint accuracy.

**Database Stability: The core infrastructure that accurately saves reading time and pages to the KOReader statistics database was preserved and fully secured while making these improvements.

**Fixed the page count glitch on the book status screen upon finishing a book

# v1.20

Added / Improved
Enhanced Ratio Accuracy (1.00+ and <1.00): Significantly improved the mathematical accuracy of statistical calculations and ratios. Data points and rates falling both below and above the 1.00 threshold are now calculated and displayed with precise accuracy.

# koreader-plugin

Changelog: Physical Page Sync v1.11
🐛 Bug Fixes
Removed Fractional Ratio Floor: Fixed an issue where the calculated ratio would get stuck at 1.00 in edge cases where the number of rendered screens is lower than the actual publisher page count (e.g., in very short books or when using very small fonts).
📝 Example (Problem & Solution)
NOTE

Imagine reading a book that is rendered on 355 screens on your device, while the official publisher edition has 412 physical pages.

Before: The system would calculate the ratio as 355 / 412 = 0.86, but due to a safety restriction, it would artificially force the UI to display "Ratio: 1.00".
After: The restriction has been completely removed. The system now accurately calculates and displays the exact mathematical ratio as "Ratio: 0.86 taps per page".

# koreader

📝 Physical Page Sync (Ninja Engine) - Changelog
Module: KOReader Statistics Plugin (statistics.koplugin) - Physical Page Sync Module

🚀 New Features & Improvements (v1.1)
Increased Mathematical Ratio Precision:

The math.ceil() function previously used for ratio calculation has been replaced with exact floating-point division.
Example: In the old system, for a book with 500 physical pages rendered across 850 KOReader screens, the ratio was calculated as math.ceil(850 / 500) = 2. This meant the engine waited for 2 screen turns to increment 1 physical page. By the end of the 850 screens, it would only record 425 pages instead of 500 (a significant margin of error).
In the new system, this ratio is precisely calculated and rounded to two decimal places (e.g., 1.70). The engine now knows exactly how to distribute the pages.
Transition to a Fractional Accumulator:

The page turn counter (cre_screen_counter) has been entirely rewritten to use a fractional accumulator (cre_fractional_counter) instead of an integer counter.
Thanks to this new system, the engine accumulates decimal values silently in the background (e.g., +1.0 per turn) and compares it against the precise float ratio (e.g., 1.70). Any leftover fractions are carried over to the next turn to ensure perfectly smooth distribution.
Result: By the time you reach the end of the book, the discrepancy between the recorded page count and the target physical page count has been reduced to absolutely 0%.
Updated UI Notifications:

The InfoMessage dialogs that appear when a ratio is calculated have been updated from integer (%d) to float format (%.2f).
When the module is enabled, instead of seeing "Ratio: 2 taps per page", you will now see an exact reading like "Ratio: 1.70 taps per page" for complete transparency.
State Saving Revision:

When the device goes to sleep or the book is closed (onCloseDocument, onReaderReady), the exact fractional state of the counter (e.g., 0.40) is now preserved and saved identically into the book's sidecar file. When you resume reading, the sync continues seamlessly from the exact millimeter you left off.
🐛 Bug Fixes
Fixed a "premature rounding" issue where the counter would unnecessarily halve the reading speed for books where the physical page count was very close to, but not exactly equal to, the screen count (Thanks to the community feedback on Reddit for pointing this out!).
