* **New "Heartbeat" feature, that sends KOReader status (on/off) to the Home Assistant `sensor.koreader_status`**(BETA)[^1]
 _Feedback welcome!_
* Split `main.lua` into `messages.lua`
* Remove custom InfoMessage HA icon 
  (I could not justify the extra installation step, nore the two imports for the icon check in `main.lua`)

[^1]: A new `sensor.koreader_status` is automatically created in Home Assistant.
On KOReader start and resume (with a 4-second delay), the sensor is set to `on`
On suspend, the sensor is set to `off`
**Caveats:**
This feature assumes homeassistant.koplugin is configured correctly (IP, port, token, etc.) and that KOReader has Wi-Fi connectivity. The state update is sent only once on start/resume/suspend and will fail silently if Home Assistant is unreachable or KOReader is offline.

**Full Changelog**: https://github.com/moritz-john/homeassistant.koplugin/compare/v2.6.0...v2.7.0