# v0.3.0

- Clue banner is now tappable: tapping it pops up the full, untruncated
  clue so long clues that get cut off in the banner are still readable.
- Always show the clue for the word under the cursor, regardless of which
  cell within the word is focused (previously the banner blanked out on
  any cell that wasn't the word's first cell).
- Add a directional pad to the right of the keyboard for cell-by-cell
  navigation, handy when most cells are already filled. 
- The keyboard now  expands to fill the remaining width (shrink_unneeded_width off) instead
  of sitting shrunk-and-centered with empty side margins.

# v0.2.1

- fix: clu banner not shown
- only show clue banner on a word's starting cell

# v0.2.0

- Add dispatcher action and refactor menu system to support both traditional and quick dialog menus

# v0.1.0

- initial release
