# v1.3.0

- adaptive spaced repetition algorithm added

# v1.2.0


1. **Delete button on study screen**
   - Added Delete button to rating buttons row (rightmost position)
   - Shows confirmation dialog before deleting card
   - Automatically loads next card after deletion
 
2. **Fullscreen mode for study screen**
   - New fullscreen mode toggle in Settings menu
   - Maximizes card display area (95% width, optimized height)
   - Adds small padding at top/bottom to prevent buttons from touching edges
   - Takes effect on next study session
 
3. **Tap-to-view full text**
   - Card frames now tappable on touch devices
   - Opens scrollable TextViewer popup showing complete card content
   - Works for both front (phrase) and back (full content) views
 
4. **Improved Add to Deck dialog**
   - Replaced MultiInputDialog with sequential InputDialog approach
   - First dialog: edit phrase with built-in scrolling
   - Second dialog: add note/meaning with sentence context
   - Properly handles very long text selections without overflow
 
5. **Context words = 0 support**
   - Context words setting now allows 0 value
   - When set to 0, sentence equals phrase (no context extraction)
   - Updated setting description and validation
 
6. **Minimum interval setting for spaced repetition**
   - New "Minimum interval (days)" setting with options: Default, 1d, 3d, 7d, 14d
   - Applies to Again button (smallest interval) with proportional scaling:
     * Again: min_interval
     * Hard: min_interval × 1.5
     * Good: min_interval × 2
     * Easy: min_interval × 4
   - Enforces minimum floor on all review card intervals
   - Scales initial intervals for new cards proportionally
   
 7. **Make rate buttons tappable anywhere in their column area, not just the button itself**

# v1.1.0

- export as md

# v1.0.0

- initial release
