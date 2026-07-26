- This pre-release aims to test the following functionality contributed by @cb12tre


> [!NOTE]
> Contributor PR summary:
>
> ## Summary
>
> * Added configurable auto-stop timeout for FilebrowserPlus server, with support for disabling it (`0`) and restoring timer checks after KOReader restart if the server is still running.
> * Improved server lifecycle handling by scheduling/canceling auto-stop checks and avoiding duplicate stop notifications for automatic shutdowns.
> * Updated menu UX: tap now toggles server quickly, while long-press opens settings; main menu label now shows live `IP:port` when available.
>
> ## Details
>
> * New setting: `FilebrowserPlus_auto_stop_minutes` (default: 30).
> * New dialog: **Auto-stop timeout (min)**.
> * Added periodic `checkAutoStop()` scheduling via `UIManager:scheduleIn(...)`.
> * Added `getIPAddress()` helper for dynamic menu label.
> * Refined startup info message to include auto-stop and first-setup credentials only when relevant.
>
> ## Why
>
> These changes make FilebrowserPlus safer (server does not stay exposed indefinitely), faster to control from the main menu, and clearer to use thanks to dynamic status feedback.

