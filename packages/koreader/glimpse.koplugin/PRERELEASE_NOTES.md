Glimpse v1.2.13 (pre-release)

From your test-bench report:

• [5.5] Bookmarked-page thumbnails are now cached to disk. The first render of each page is unchanged, but once a page has been rendered, reopening the Gallery — even after closing and reopening the book — shows it instantly instead of re-rendering. The cache is size-capped and rebuilds itself if you change the book's font or margins.

• [5.4] Removing a bookmark now clears its dogear from the page immediately, while Glimpse is still open, instead of only after Glimpse closes.

Note on [5.5]: this speeds up *repeat* opens, not the very first render pass (that's KOReader's own ~500ms/page cost). Curious whether the second open now feels instant with your 20-bookmark book.