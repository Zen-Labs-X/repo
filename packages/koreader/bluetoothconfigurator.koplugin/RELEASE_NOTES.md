# v2.2.4

Restores the Reflowable documents and Fixed layout documents categories in the Bluetooth action picker.\n\nThe release archive uses the updater-compatible single bluetoothconfigurator.koplugin/ wrapper layout.

# v2.2.3

Adds controller input diagnostics. Fixes the in-plugin updater on current KOReader versions by using ffi/archiver, with staged validation, backup, and rollback. Normal key handling no longer performs diagnostic device lookups unless diagnostics are active.

# v2.2.2

Maintenance rebuild: fixes the in-plugin updater on current KOReader versions by using ffi/archiver instead of the removed Device:unpackArchive API. Plugin behavior remains v2.2.2.

# v2.2.1

Changes in this release:

- Simplifies the settings dialog title to "Bluetooth Configurator" while keeping Reader/File Manager context in the bindings section.
- Updates the key capture prompt to refer to a Bluetooth device instead of only a page turner.
- Adds a general dispatcher action, "Open Bluetooth Configurator", for reader and file manager contexts.
- Corrects the in-app version display to v2.2.1.
- Refreshes README usage wording for reader and file manager bindings.

# v2.2.0

Changes in this release:

- Adds separate Reader and File Manager binding sets, matching KOReader's gesture behavior.
- Enables bindings to fire while browsing the File Manager, not only while reading.
- Lets the same physical button trigger different actions in Reader and File Manager contexts.
- Filters the File Manager action picker to hide reader-only categories like Reader, Paging, Rolling, and Document.
- Keeps existing bindings migrated into the Reader binding set automatically.
- Flushes binding changes immediately so settings are less likely to be lost after restart.
- Updates README and metadata for hardware keyboard support and Minimal Phone validation.
- Cleans up debug logging and WIP hook code from the file-manager implementation.
