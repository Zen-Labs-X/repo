# v0.9.16

I prepared a new version that will make use of the new auth method that was introduced for plugins in kavita 0.8.9. Additionally I changed the way the thumbnails/metadata is retrieved for cover browser to hopefully fix a metadata display bug that was reported in #3.

Big Changes: 
* update to new auth method

Bugfixes:
* cover browser metadata loading could fail if kavita browser was not available. #3 

Additionally I am happy to add the first community contributions 🎉:
* fix KOReader crash when taking a screenshot (thanks @EduFdezSoy):
* allow RTL controls in all view modes (thanks @EduFdezSoy)
* add front light controls to settings (thanks @EduFdezSoy):

# v0.9.10

Big Changes:
* Another attempt at finally fixing the tiled rendering artifacts that remained

Small Changes:
* Small UI fixes

# v0.9.8

Big Changes:
* Dual Page mode for more book like experience on big readers or in landscape mode

Small Changes:
* Make sure wifi is connected when resuming from sleep
* Continue reading series with long press on series entry
* Some linting
