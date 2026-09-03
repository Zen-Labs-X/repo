# v1.2.0

### Playground — faster, and it stays where you put it

- Opening it takes about a second instead of half a minute.
- **Show before** and **Side by side** now work on every page in the window, not
  just the one you opened it from.
- Turning a page while looking at *before*, or at both halves, keeps you there
  instead of dropping back to the new style.

# v1.1.0

## Playground

Try style changes without touching the book.

- **Playground** (top of the plugin menu, or **Try** on the quick screen) draws the page you are on with your settings, before anything happens to the book.
- **Change anything while it is open.** The whole plugin menu opens on top of it; nothing reaches the book until you press **Apply**. **Cancel** leaves the book exactly as it was.
- **Turn pages inside it** (◀ ▶, swipe, or the page-turn keys) to check how a change lands around a chapter break or an image.
- **Compare before and after:** tap to flip in place, or view them side by side. **⤢** — or a long press — hides the controls and shows the page at exactly 1:1.
- **The book is never re-rendered until you apply.** The page is drawn by KOReader's own engine in a separate process, which touches nothing: not the rendering hash, not your saved settings, not crengine's cache.
- **Memory-aware.** How many pages one render covers is sized from what the device has free, and a playground that will not fit is refused with a message rather than risking a crash.
- **Not available inside the playground:** typography & hyphenation, header & footer, and the book's own style tweak — they change the live book and cannot be held back.

# v1.0.0

- initial release
