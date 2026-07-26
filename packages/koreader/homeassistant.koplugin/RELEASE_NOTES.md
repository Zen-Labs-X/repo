- The "Heartbeat" / Home Assistant sensor feature now lives in a different plugin: https://github.com/moritz-john/heartbeat.koplugin
- This means that `koreader_sensor_name` and `sensor_resume_delay` can be deleted from your homeassistant.koplugin `config.lua` file.
- The new plugin allows you to change these values directly from within the KOReader GUI.

<img width="692" height="467" alt="heartbeat_settings" src="https://github.com/user-attachments/assets/33f13523-7ac4-4b26-b322-fa852acdbc1b" />

**Full Changelog**: https://github.com/moritz-john/homeassistant.koplugin/compare/v26.02.26...v26.03.19