# v1.13 Release Notes

## Stream Response Performance

Streaming responses previously caused noticeable UI lag, especially on e-ink devices with limited refresh capabilities. Each token triggered a separate screen update, leading to choppy rendering and slow perceived response times.

This release introduces two performance improvements:

- **Coalesced UI updates**: Incoming stream content is now buffered and flushed to the screen at 500ms intervals instead of on every token. This dramatically reduces the number of screen redraws, making the reading experience much smoother and more responsive.
- **Cleaner reasoning separation**: When a model outputs its internal reasoning before the final answer, the UI now clears the reasoning content and starts the answer fresh, avoiding visual clutter and making the response easier to read.

## Cleanup

- Removed a long-unused plain-text rendering code path and the associated `render_markdown` configuration option (which was always effectively enabled). This simplifies the viewer code and eliminates dead code.

## Other Improvements

- Built-in prompt section headers (e.g. "What It Is", "Role & Function", "Evolution & Connections" in Term X-Ray, and similar headers in Grammar, ELI5, Key Points, and Historical Context prompts) are now localized. Users in supported languages will see these headers in their own language. All 40+ language translations have been updated.
- Fixed the Azure OpenAI sample endpoint URL in the configuration template.
- Internal naming improvements to reduce confusion between built-in and user-defined prompts.

---

**Stats**: 70 files changed, +41,440 / -32,086 lines (mostly translation updates).