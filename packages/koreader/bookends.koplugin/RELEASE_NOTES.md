**Chapter progress at any TOC depth**

The chapter progress tokens now take a depth suffix, the same way `%chap_title_1`…`%chap_title_9` already do: `%chap_read_N`, `%chap_pages_N`, `%chap_pages_left_N`, `%chap_pct_N`, `%chap_pct_left_N`, plus `%chap_time_left_N` and `%chap_time_left_N_eta`.

Without a number they track the deepest chapter, as before. With a depth, e.g. `%chap_read_1`, they measure against the top-level chapter instead. Useful for books with a very fine table of contents, where a plain `%chap_read` shows a tiny sub-section's length next to a top-level `%chap_title_1`.

Type them manually (they're not in the token picker). The README token reference lists the full set.