# Non-blocking Wi-Fi connect for KOReader

A [KOReader user patch](https://github.com/koreader/koreader/wiki/User-patches) that stops the device from locking up while KOReader connects to Wi-Fi on **Kobo and other wpa_supplicant devices**, and on **Kindle**. You can keep reading and flipping pages while the connection is established in the background.

## The problem

On devices where KOReader talks to `wpa_supplicant` directly (Kobo, Cervantes, …), the whole interactive connect sequence — hardware bring-up → scan → authenticate → DHCP — runs **synchronously in KOReader's single UI thread** (`NetworkMgr:reconnectOrShowNetworkMenu`). No input is processed until it finishes, so the device appears frozen for 10–30 seconds.

On Kindle, Amazon's `wifid` daemon handles association and DHCP by itself, but the **network scan** still busy-waits on the UI thread (`kindleScanThenGetResults`: a 250 ms `usleep` poll loop, up to 20 s — 40 s worst case with the automatic rescan), so the UI freezes for however long the scan takes.

It doesn't have to block: KOReader already restores Wi-Fi after resume fully asynchronously (`restore-wifi-async.sh`) — only the interactive path was written with blocking waits.

## What the patch does

Replaces `NetworkMgr:reconnectOrShowNetworkMenu` with an asynchronous state machine, preserving stock behavior and messages.

On wpa_supplicant devices (Kobo & co):

| Step | Stock | Patched |
|---|---|---|
| Hardware bring-up (`enable-wifi.sh`) | blocking `os.execute` in `turnOnWifi` — module loading plus hard-coded sleeps, **~4–5 s on MTK Kobos** (Libra Colour, Clara B/W/Colour, …) | runs in a forked subprocess, polled every 250 ms |
| Network scan | blocks in `scanThenGetResults` | runs in a forked subprocess, polled every 250 ms |
| WPA association | `waitForEvent(1s)` × 30 in UI thread | fast setup commands, then 250 ms `scheduleIn` polling of `wpa_state=COMPLETED` (same check as `restore-wifi-async.sh`) |
| DHCP (`obtain-ip.sh`) | blocking `os.execute` | subprocess, polled |

On Kindle (FW 5.x with lipc), only the scan needs fixing:

| Step | Stock | Patched |
|---|---|---|
| Network scan | `usleep(250 ms)` busy-wait on the UI thread until `wifid` finishes (up to 20 s) | runs in a forked subprocess, polled every 250 ms |
| Association + DHCP | one fast `ensureConnection` lipc call, `wifid` connects in the background | unchanged |

Success/failure semantics are preserved: `complete_callback` still reaches `enableWifi`'s connectivity check, failures still tear down Wi-Fi via `_abortWifiConnection()`, the fallback AP list is still shown for interactive failures, and preferred networks are tried in the same order.

## Measured

In the KOReader emulator with a simulated slow connection (5 s hardware bring-up + 2 s scan + 6 s association + 3 s DHCP), instrumented with a 100 ms event-loop heartbeat:

- stock synchronous flow: **event loop frozen for 10.2 s** (no input processed; the bring-up would add another ~5 s on MTK Kobos)
- this patch: **worst event-loop stall < 0.2 s** — UI fully responsive during the whole connect

## Install

1. Create the `patches` directory next to your KOReader settings if it doesn't exist:
   - Kobo: `.adds/koreader/patches/`
   - Kindle: `koreader/patches/`
2. Download **`2-nonblocking-wifi.lua`** from the
   [latest release](https://github.com/asxelot/koreader-nonblocking-wifi/releases/latest)
   (or clone this repo), drop it in that folder, and restart KOReader.

The patch is a no-op on other platforms.

## Status / caveats

Field-tested on:

- **Kobo Libra Colour** (MTK) — full async flow, including the subprocess hardware bring-up
- **Kindle** (lipc FW 5.x) — async scan

Emulator-verified for the success, failure/timeout, and abort paths. More tester reports welcome — please open an issue.

- The scan result list crosses a process boundary (LuaJIT `string.buffer` serialization); entries are expected to be plain tables.
- The per-state authentication popups ("Scanning…", "Authenticating…", …) are collapsed into static stage messages.
- The bottom of the file contains an emulator-only test harness (heartbeat + fake backend); it is inert on real devices.

Pairs well with [wifiindicator.koplugin](https://github.com/asxelot/wifiindicator.koplugin), which replaces the connection popups with a discreet corner icon.
