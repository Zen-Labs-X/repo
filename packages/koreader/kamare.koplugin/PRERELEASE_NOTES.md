I prepared a new version that will make use of the new auth method that was introduced for plugins in kavita 0.8.9. Additionally I changed the way the thumbnails/metadata is retrieved for cover browser to hopefully fix a metadata display bug that was reported in #3.

Big Changes: 
* update to new auth method

Bugfixes:
* cover browser metadata loading could fail if kavita browser was not available. #3 

Additionally I am happy to add the first community contributions 🎉:
* fix KOReader crash when taking a screenshot (thanks @EduFdezSoy):
* allow RTL controls in all view modes (thanks @EduFdezSoy)
* add front light controls to settings (thanks @EduFdezSoy):