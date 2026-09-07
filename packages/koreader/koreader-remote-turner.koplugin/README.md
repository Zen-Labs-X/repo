# KOReader Remote Turner

Remote-control KOReader from your phone or desktop. Turn pages forward/backward and send sleep commands wirelessly via WebSocket — no network file shares, no cloud, just direct LAN communication.

## Architecture

```
┌─────────────────────┐        WebSocket        ┌──────────────────┐
│   Flutter App        │ ◄─────────────────────► │   KOReader Plugin │
│                     │      port 9090          │  (remote_turner   │
│  Android / iOS /    │                          │   .koplugin)      │
│  Windows / macOS /  │                          │                  │
│  Linux              │                          │  Lua / LuaSocket  │
│                     │                          │                  │
│  kaeru + kaeru_ui   │                          │  UIManager events │
└─────────────────────┘                          └──────────────────┘
```

- **Flutter app**: Listens for hardware volume buttons (or on-screen buttons), sends `next_page` / `prev_page` / `sleep` messages via WebSocket.
- **KOReader plugin**: Pure-Lua WebSocket client connects to the app, receives messages, and dispatches `GotoViewRel` / `RequestSuspend` events.

## Features

- Volume button page turning (Android foreground service, iOS KVO, desktop KeyboardListener)
- On-screen manual buttons + auto-connect
- Multi-key binding per action (chip + record UI)
- Authentication via SHA-256 challenge/response
- Event logging with JSONL persistence
- Theme: Light / Dark / System
- Locales: English, Vietnamese, Japanese, Chinese (Simplified)
- KOReader plugin with auto-discovery via UDP broadcast

## Build

### Prerequisites

- Flutter SDK (stable) + Dart
- For Linux: `clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev`
- For macOS: Xcode + CocoaPods
- For Windows: Visual Studio (C++ workload)
- For Android: Android SDK (API 34+)

### All platforms

```bash
make android      # APK
make ios          # unsigned IPA
make windows      # EXE installer (Inno Setup)
make macos        # DMG (unsigned)
make linux        # DEB package
make koplugin     # KOReader plugin zip
```

### Release

```bash
npm install
npx semantic-release
```

CI (GitHub Actions) runs semantic-release on push to `main`, then builds all platform artifacts and uploads them to the release.

## Usage

### 1. Install the KOReader plugin

Copy `remote_turner.koplugin/` to KOReader's plugins directory (`koreader/plugins/`) or install via the `.koplugin.zip` from releases.

On KOReader: **Menu → Tools → Remote Turner → Connect**.

### 2. Run the Flutter app

Launch the app — it starts a WebSocket server on port `9090` by default. The KOReader plugin auto-discovers the server via UDP broadcast, or you can enter the IP manually in plugin settings.

### 3. Turn pages

Press hardware volume buttons (or use on-screen buttons). The app sends `next_page` / `prev_page` / `sleep` actions to KOReader over the WebSocket connection.

## Development

### Stack

| Layer | Tech |
|-------|------|
| State | kaeru (`Ref`, `Computed`, `Watch`) |
| UI    | kaeru_ui (VText chains, `.row()`, `.column()`, `.card()`, `.box.bg().rounded().border().make()`) |
| Navigation | Bottom tab (Home, Logs, Settings, About) — responsive `NavigationRail`/`NavigationBar` |
| Backend | Dart `HttpServer` + `WebSocket` (no external server deps) |
| Plugin | Pure Lua + LuaSocket (`websocket.lua`, no external deps) |

### Key files

```
lib/
  app.dart                    # Root widget, responsive layout, tab navigation
  main.dart                   # Entry point, theme mode wrapper
  pages/
    home_page.dart            # Status, start/stop, stats, mini log
    logs_page.dart            # Full event log viewer
    settings_page.dart        # Key binding, port, theme, auth
    about_page.dart           # App info, links
  services/
    keyboard_listener.dart    # Hardware key detection, multi-key config
    websocket_server.dart     # WS server + auth + idle timer
    platform_service.dart     # Android/iOS volume key channels
    event_logger.dart         # JSONL log read/write
    settings_service.dart     # SharedPreferences helpers
    password_auth.dart        # SHA-256 challenge/response
  widgets/
    connection_status.dart    # Status dot + text
remote_turner.koplugin/
  main.lua                    # Plugin init, connect, message loop
  websocket.lua               # RFC-6455 WebSocket client (LuaSocket)
  _meta.lua                   # Plugin metadata
```

### Icon

Edit `icon.svg` then regenerate all platform icons:

```bash
bash scripts/generate-icons.sh
```

## KOReader Plugin API

| Action | KOReader Event |
|--------|---------------|
| `next_page` | `GotoViewRel(1)` |
| `prev_page` | `GotoViewRel(-1)` |
| `sleep` | `RequestSuspend` |

Events are broadcast via `UIManager:broadcastEvent()`, which works for both page mode (PDF/DJVU) and scroll mode (ePUB/CREngine).

## License

[AGPL-3.0 license](./LICENSE)
