## v1.14 Release Notes

### Changes since v1.13

#### New Features
- **Bold dialog labels and status verbs via PTF** — Error dialogs, OTA update dialogs, and search info dialogs now use bold formatting for key labels, making them easier to scan at a glance.
- **Gemini 3 thinking budget auto-conversion** — The `thinking_budget` setting now automatically converts to Gemini 3's expected format. Disabled by default in the sample config.

#### Bug Fixes
- **Dictionary popup AI buttons** — AI buttons in the dictionary popup no longer disappear after customizing the dict button layout (#187).
- **Gemini thinking config** — Fixed `thinkingConfig` to use camelCase (required by Gemini API), and fixed a bug where `thinking_budget=0` was silently ignored instead of disabling thinking.
- **Server error messages** — Non-200 HTTP responses now surface the server's actual error message instead of a generic "fetchJSON: failed to parse" message.
- **Error dialog polish** — Error messages are now formatted with bold labels and clearer structure.
- **Silenced noise logs** — Unprocessed SSE event logs for `web_search_call` lifecycle events and Responses API annotation events are now suppressed.
- **OTA and search info dialogs** — Polished the layout and text of OTA update and search tool info dialogs.
- **PO file format** — Normalized `.po` file format to 1-space alignment, eliminating diff noise from `msgattrib -i` misuse.

#### Internal Improvements
- `assistant_utils` is now imported as `ASUtils` consistently across the codebase.
- String concatenation loops replaced with `string.buffer` / `table.concat` for better performance.
- OTA updater path construction routed through `FFIUtil.joinPath` for cross-platform safety.
- Gemini `thinking_budget` handling consolidated into a single handler.
- Bold formatting centralized through `bold_format` helper, keeping translatable strings contiguous.
- Removed unused shell translation script.