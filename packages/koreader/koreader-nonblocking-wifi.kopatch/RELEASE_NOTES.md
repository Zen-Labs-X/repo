# v1.0.0

First release.

A KOReader user patch that stops the device from locking up while connecting to Wi-Fi. Replaces `NetworkMgr:reconnectOrShowNetworkMenu` with an asynchronous state machine — hardware bring-up, scan, association and DHCP run in subprocesses / 250 ms polls instead of blocking the UI thread. Keep reading and flipping pages while Wi-Fi connects. Works on **Kobo & other wpa_supplicant devices** and on **Kindle** (async scan); a no-op elsewhere.

Field-tested on Kobo Libra Colour (MTK) and a lipc Kindle; emulator-verified for success, failure/timeout and abort paths (worst measured event-loop stall < 0.2 s vs. 10.2 s stock).

### Install
Download `2-nonblocking-wifi.lua` below and drop it into your KOReader `patches/` directory, then restart. Pairs well with the wifiindicator plugin.
