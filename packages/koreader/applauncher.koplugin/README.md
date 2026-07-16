# App Launcher (KOReader Plugin)

App Launcher is a lightweight launcher plugin for KOReader.
It collects the menu entries exposed by installed plugins and lets you organize them into icon-based top tabs for quick access.


https://github.com/user-attachments/assets/4654b274-e078-4e45-98fb-dcf3945ddd10



## Features

- Icon-based top menu tabs (TouchMenu)
- Organize plugin actions into categories (tabs)
- Favorites, Tools, Games, etc. (fully configurable)
- Long-press on an action to assign it to a category
- Long-press on a category (via Settings) to rename, change icon, or delete
- Cache of discovered actions with a manual refresh
- Works in both File Manager and Reader contexts

## Installation

1. Copy the plugin folder (e.g., `applauncher.koplugin`) to:

   `koreader/plugins/`

2. Restart KOReader.

## Usage

- Open from KOReader menu:
  - **Menu → Tools → App Launcher** (location may vary slightly by device / build)

- Open via gesture:
  - Assign a gesture to open the App Launcher.

- Top bar:
  - Each tab is a category.
  - Tabs show **icons only**.

### Assign actions to a category

1. Open **Settings → All apps**.
2. Long-press an action.
3. Select the category to assign it to.

### Manage categories (top menu tabs)

1. Open **Settings → Top menu**.
2. Tap a category.
3. Choose:
   - Rename
   - Change icon
   - Delete

## Icons

KOReader resolves icons by name (e.g., `star.full`) and searches in this order:

1. User icons directory: `koreader/icons` (ie `DataStorage:getDataDir()/icons` )
2. Default icon set: `resources/icons/mdlight`
3. Fallbacks: `resources/icons`, `resources`

### Adding custom icons

- Copy `myicon.svg` or `myicon.png` to:

  `koreader/icons` (ie, `DataStorage:getDataDir()/icons/`)

- The icon name becomes `myicon`.
- Then select it via **Settings → Top menu → (category) → Change icon**.

## How actions are discovered

App Launcher builds an internal cache by inspecting KOReader’s registered menu widgets and calling each plugin’s `addToMainMenu()` to collect the plugin-provided menu entries.

## Settings & data

App Launcher stores its configuration in:

- `settings/applauncher.lua`

It includes:

- Categories (tabs) with title and icon
- Assignments (action → category)
- Last opened tab index

## License

This plugin follows the same license terms as the KOReader project.
See `LICENSE` in this plugin folder.

## Credits

This plugin was created with Windsurf (AI).
