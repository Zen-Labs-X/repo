# Kobo Dashboard

An e-ink optimized dashboard that displays calendar events, weather forecast, and current date. For Kobo e-readers and KOReader (never tested in Kindle KOReader or other devices).

Built with Docker Compose for easy deployment with three coordinated services: Calendar Processor (fetches iCal events), Screenshot Service (captures dashboard), and Web Server (serves dashboard URL).

FYI: This plugin is still being tested, and requires improvements!

![Kobo Dashboard screenshot](image.png)

## What is this?

This project generates a high-contrast PNG image showing:
- 📅 **Today's calendar events** from multiple calendars using iCal/iCS URLS (from Google, Outlook, iCloud)
- 🌤️ **Weather forecast** for your location
- 📆 **Current month calendar** with today highlighted
- 🕐 **Real-time updates** every few minutes (configurable)

The generated image is optimized for e-ink displays and can be automatically displayed on your Kobo e-reader using KOReader's Agenda plugin. The Kobo screen size is also configurable.
If your Kobo is black&white, feel free to modify the CSS to your liking. If you're not used to CSS, ping me and I can try helping :)

**PS:** I currently use a Raspberry Pi as my server, with Docker running. You can also run this on Docker on your computer, but remember to keep your PC on.
This plugin is not very accessible yet, since it needs a server to generate the images. You can also be creative and run this in a Heroku or similar, for free.

## Setup - Dashboard in Docker Container

### Step 1: Download and start setup

**The use of Docker containers is recommended.**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/paulakfleck/kobo-dashboard.git
   cd kobo-dashboard
   ```
2. **Copy the example configuration:**
   ```bash
   cp .env.example .env
   ```
3. **Edit `.env` with your settings. Please read carefully .env, it has vital information to understand how to set it up.**

### Step 2: Configure calendar and refresh interval

**Google Calendar (Recommended):**
1. Go to [Google Calendar](https://calendar.google.com)
2. Click on your calendar name in the left sidebar → Settings and sharing
3. Scroll down to "Integrate calendar"
4. Copy the **"Secret address in iCal format"** (.ics link). Don't commit this to a public repository or share it with anyone!
4.1. Private calendars work perfectly! You don't need to set it to public. That's actually dangerous and can index your calendar in Google Search, so don't do it if you don't want that.
5. Paste the iCal URL to your newly created `.env` following the instructions on the document. You can have more than one calendar.

**Outlook/Office 365:**
1. Go to outlook.office.com → Settings → Calendar → Shared calendars
2. Publish your calendar and copy the ICS link
3. Paste the iCal URL to your newly created `.env` following the instructions on the document. You can have more than one calendar.

**Apple iCloud:**
1. Go to icloud.com/calendar
2. Share calendar and copy the webcal:// URL
3. Replace `webcal://` with `https://`
4. Paste the iCal URL to your newly created `.env` following the instructions on the document. You can have more than one calendar.


**Configure the plugin:**
   
Open `main.lua` and edit the following parameters:
   ```lua
   local INTERVAL_S  = 60         -- Refresh every minute. Change as desired.
   ```

This is just the screen refresh/reload. This drains battery! I really recommend keeping your Kobo connected to a dock when using a very short refresh like this.

### Step 3: Run the Server

1. **Start the dashboard:**
   ```bash
   docker-compose up -d
   ```

The project runs on port `http://YOUR-SERVER-IP:3333/today.png`. This tutorial and plugin are not responsible for how you will setup ports on your machine, but ping me if you need any help and I can try to help. You can also find several tutorials online.


### Step 4: Setup KOReader on Your Kobo and Install the Plugin

1. **Install KOReader** on your Kobo (if not already installed)
2. Go to `.kobo/koreader/plugins/` or similar, depending on your Kobo.
3. Create a folder called `agenda.koplugin`
4. Copy `main.lua` file from this repository to `agenda.koplugin`
2. **Enable the Agenda plugin:**
   - Go to Tools → More tools → Plugin management
   - Enable "Agenda"
3. **Open Agenda plugin:**
   - Go to Tools → More tools → Agenda → Start

**That's it!** Your Kobo will now automatically fetch and display your personalized dashboard.
Currently, the only way to exit the plugin is to restarting the device :c I'm working on a better way to do it.

## Setup - KOReader recommended settings for optimal results:
- Menu → Settings → Power
- - Auto-suspend: `Off`
- - Auto-poweroff: `Off`
- Menu → Settings → Screen
- - Full refresh: `Always`

## Common Kobo Screen Sizes

Update `SCREENSHOT_WIDTH` and `SCREENSHOT_HEIGHT` in `.env` file for your device:

- **Kobo Clara HD**: 1448×1072
- **Kobo Libra H2O**: 1680×1264
- **Kobo Forma**: 1440×1920
- **Kindle Paperwhite**: 1236×1648
- **Kindle Oasis**: 1680×1264

## Troubleshooting

### "No calendar events showing"
1. Check your iCal URLs are correct
2. Make sure calendars are using correct private iCal links
3. Check logs: `docker logs kobo-calendar-processor`

### "Weather not updating"
1. Verify your latitude/longitude coordinates
2. Check network connectivity. The plugin could be out of service momentarily too.
3. Check logs: `docker logs kobo-screenshot-service`