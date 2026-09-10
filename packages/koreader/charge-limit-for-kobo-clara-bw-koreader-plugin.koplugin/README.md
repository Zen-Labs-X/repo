**ChargeLimit — KOReader plugin for KOBO CLARA BW**

Stops battery charging at a configurable percentage on a **KOBO CLARA BW**
(ROHM BD71827 PMIC), to avoid charging your kobo until 100%. 
It should work in all Kobo Clara BW models, but I cannot be 100% sure, if your device is not supported the plugin menu will not appear in your cabinet icon menu, even if the plugin appears in plugin management. 
Update: Users say it also works in **Kobo Clara Color, Libra Color and Kindle Paperwhite 12**. 
<p align="center">
  <img width="250" alt="WhatsApp Image 2026-08-28 at 19 09 33(2)" src="https://github.com/user-attachments/assets/03e631bf-edf3-4fa7-a54e-855de99d2ba3" />
  <img width="250" alt="WhatsApp Image 2026-08-28 at 19 09 33(1)" src="https://github.com/user-attachments/assets/e6e22cf4-d99e-480c-975f-8147e7370d7c" />
  <img width="250" alt="WhatsApp Image 2026-08-28 at 19 09 33" src="https://github.com/user-attachments/assets/1ce96852-4bb1-40d7-be70-79f5a01b0cd4" />
</p>

**Why limit the charge?**

Charging to 100% degrades your battery faster. Keeping your charge between 20% and 80% minimizes voltage stress, significantly extending your device's lifespan while still providing weeks of reading time.

**How it works**

The plugin periodically (every 60 seconds) reads the battery percentage from /sys/class/power_supply/bd71827_bat/capacity. When the configured limit is reached, it writes 0 to /sys/class/power_supply/bd71827_bat/charging to pause charging. Charging is resumed by writing 1 when the battery drops below the resume threshold. No other system files are modified.


- Stop threshold is selectable from fixed values: 80% / 85% / 90% / 95%.
- Resume threshold is always stop_at - 2, so it can never end up above
the stop threshold (this would cause charging to toggle on/off in a
loop).
- On a device where the expected sysfs file doesn't exist, the plugin
stays fully inactive (no menu, no scheduled checks).
- Whenever the plugin is disabled, or KOReader closes the widget, it
forces charging=1 as a fail-safe. The device should never get stuck
not charging.

**Installation**

1. Copy the chargelimit.koplugin folder into KOReader's plugins
directory on the device.
2. Restart KOReader.
3. Go to More tools → Plugin management → User plugins and confirm
ChargeLimit is loaded.
4. Open the Charge limit menu (appears only on supported devices) in the cabinet icon with the books closed,
pick a threshold, and enable it.

**Before updating or removing the plugin**

Always follow this order to avoid any ambiguity about the charging
state while iterating on the code:

1. Disable the plugin from the cabinet menu (Charge limit → Enable charge
limit → off). This immediately forces charging back on.
2. Replace or delete the plugin files.
3. Restart KOReader for the change to take effect.

**If something goes wrong**

The charging file is a runtime register on the PMIC, not something tied
to which app is running. If charging ever seems stuck off, either of
these resets it:

- **Unplug and replug the USB cable.**
- **Reboot the Kobo.** Firmware always boots with charging enabled.

**Optional: checking your chip**

Not sure if your device has the same chip? This is a quick, read-only
check — nothing is written, nothing to undo. It just requires SSH access to
the device and for you to write this: 

1. ssh root@"your kobo ip" (ex: ssh root@100.190.1.1)

2. ls /sys/class/power_supply/


If you see `bd71827_bat` and `bd71827_ac`, your device uses the same
ROHM BD71827 chip this plugin targets. If not, this plugin's paths
won't apply to your device.

**Trying this on a different Kobo model**

If you own a different Kobo model (Clara HD, Libra, etc.) and the
read-only chip check above confirms `bd71827_bat`/`bd71827_ac` exist on
your device, this plugin will very likely work as-is — no code changes
needed. Feel free to try it and report back.

If your device shows different power_supply names, don't install the
plugin as-is — follow "Adapting this for another device" instead.

**Adapting this for another device**

This plugin is hardcoded to the Kobo Clara BW's specific hardware: the
two paths (bd71827_bat/charging and bd71827_bat/capacity) only exist
because that model uses a ROHM BD71827 power chip. Different models may use different charging chips, exposed
under different names, with different capabilities.

Do not just swap in a path that looks similar and assume it behaves the
same way. If you want to adapt this for another device, follow the same
process this plugin was built from, in this order:

1. Enable SSH / shell access on your device (method varies by model and
   brand — search for your specific device).
2. Read-only exploration first. Run `ls /sys/class/power_supply/` to
   see what's exposed, then `cat` every file in the battery-related
   directories. This is always safe — reading never changes anything.
3. Look for a plausible enable/disable file (something readable *and*
   writable, with a name suggesting on/off charging control — not
   `register`, not anything related to voltage/current limits, and not
   anything unrelated like moisture/temperature protection).
4. Test with the charger connected, one write at a time, checking
   `status` and `current_now` before and after. Confirm the value
   returns to a normal charging state before trusting it in a plugin.
5. Only after that manual confirmation, update `CHARGE_PATH` and
   `CAPACITY_PATH` in `main.lua` to match what you found.

Skipping straight to step 5 with a guessed path is the actual risk here
— not because this code is unsafe, but because a different device's
chip may expose a file with a similar name that controls something
completely different. The safety of this plugin comes entirely from the
fact that its two paths were manually verified on real hardware before
being hardcoded — that verification doesn't transfer to a different
device automatically.

**Community reports**

Users have reported this also works on other devices sharing the same
BD71827 chip. One user confirmed it on a Kindle Paperwhite (12th gen) with root/shell access, verifying the same way this plugin
was originally validated: toggling `charging` to `0`/`1` over SSH and
confirming `status` switched between `Discharging` and `Charging` each
time.

Still, always run the read-only chip check above yourself before
installing on any device — even devices that share the same chip family
may expose it slightly differently.

**Disclaimer**

This plugin directly writes to low-level hardware control files on your
device. It was built and tested only on one Kobo Clara BW unit; it may
behave differently on other units, firmware versions, or after a Nickel
update. Use it at your own risk. I take no responsibility
for any damage, data loss, or reduced device functionality resulting
from its use. If you're not comfortable verifying the sysfs paths on
your own device before relying on this, don't enable it unattended.
