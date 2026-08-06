DoctorBattery v1.2.0
✨ New Features
🇵🇹 Portuguese Translation
Added full Portuguese language support.
Special thanks to @CookieCaptainD  for providing the Portuguese translation and helping make DoctorBattery accessible to more users.

🖥️ System Information

A brand-new System Information section has been added to provide a more complete overview of the device.

New categories include:

📱 Device Information
⚙️ Hardware Information
💾 Storage Information
🧠 Memory Information
🔋 Battery Information
🖥️ CPU Information
🌐 Network Information
📂 Operating System Information
📦 Environment Information
🔍 Hardware Scan

Added a new Hardware Scan tool. (🔍 Hardware Scan)

This feature scans the device for battery- and hardware-related paths, making it easier to identify where different e-readers expose system information.

The collected information will help improve DoctorBattery compatibility across a wider range of devices.

Current scan targets include:

/sys/class/power_supply/
/sys/devices/
/proc/
/proc/device-tree/
/proc/sys/
/etc/
/dev/
/var/
/usr/
/mnt/

The goal is to progressively support as many Kindle, Kobo, Android, and Linux-based e-readers as possible.

🛠 Improvements
General code improvements and internal refinements.
Expanded infrastructure for future hardware compatibility.