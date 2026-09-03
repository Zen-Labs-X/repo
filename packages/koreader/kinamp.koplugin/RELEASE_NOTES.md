# 3.0.0

KinAMP3 is a huge update of this application:

- Completely redesigned **Koreader plugin**. Read the documentation about using it.
- **OGG format** support
- **AAC radio** encoding support, as well as PLS and M3U stations - around 90% of the stations from the database are supported
- File **metadata** support
- Icecast radio metadata support

KinAMP has now an experimental **Kobo support** too - Koreader plugin only.

On Kindles it is included in the **KindleTweaks KPM** repository. Read the documentation about installing it using `kpm`.

# 3.0beta

This is a huge update of KinAMP. The main feature is the completely new Koreader plugin interface. For quick access, assign it to the lower right corner tap in the *Gesture manager*. 

It has many new features, the main ones are listed below:
- Music - **OGG** file format support
- Music - Track metadata decoding
- Radio - AAC, M3U and PLS internet radio stations accepted
- Radio - Station metadata decoded for ICY compatible stations
- Koreader - Completely new interface, with floating player window; no more menu access; with Playlist and Radio editor

# 2.2

**Changelog:**
- **Sleep mode**: KinAMP will stop and the device go to sleep mode after the end of the playlist or after a set time. Enable it with the *Sleep* button.
- **Update from the app**: You can check for updates and update the app from the *About* dialog
- Some UI tweaks.

# 2.1

The most important addition is the volume slider, because sometimes even the minimal volume was too loud on my headphones. Note that there's a ~2 seconds delay between setting the slider and the volume.

- Updated UI
- Volume slider
- Possibility to add a radio station manually from the URL (still, only MP3 streams are supported).
- KUAL menu fixed
- Native `faad` library removes the need of `libm`

# 2.0

**Big KinAMP update ! **

New features:

- Internet radio mode (mp3 streams only)
- AAC file format support
- Koreader plugin

**Editing radio stations**

Open the *KinAMP Radio List Editor* from Kual to add or remove radio stations. Currently only MP3 streams are supported (so no mpeg1/2 or aac streams).

To switch to radio mode, click the radio icon in the bottom left corner.

**Running KinAMP from Koreader**

The Kinamp plugin can be accessed from the *"Tools"* menu. You can edit and start the playlist, jump to a song or play a radio station.

**Important** This is a big update, so there can be bugs. If you find one, please file an issue so I can fix it.
