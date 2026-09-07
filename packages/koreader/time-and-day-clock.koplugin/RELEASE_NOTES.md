# v0.9.2

bug fixes : 

1) fixed a bug where the RTC clock was not working correctly, and battery drain was too fast because the Autosuspend loop was not triggered

2) fixed orientation issue and screen refresh issues on older kobo models (kobo Glo)

# v0.9.1

Bug Fixes : 

Battery & CPU Drain: Fixed an issue where AutoSuspend was forced to 5 seconds, causing continuous CPU wake loops. The plugin now relies entirely on wake locks and RTC alarms without modifying system autosuspend behaviors.

Power Management Cleanup: Completely removed deprecated never_suspend and custom_timeout options. They have been replaced by a single, streamlined "CPU wake duration" spinner.

Screen Rotation Fixes: Resolved bugs where custom clock rotation failed to restore correctly upon exiting the screensaver:

UI Customizer: Removed the redundant "Rotation" setting line from the Format tab.

# v0.9

This the first beta release of this plugin. It might be unstable so any bugs found in this version should be reported to issues to allow me to fix them.
