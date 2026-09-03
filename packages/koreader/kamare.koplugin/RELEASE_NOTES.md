# v0.9.21

Bugfixes for a few networking related issues that lead to libraries not loading consistently.

# v0.9.20

This is a huge rewrite of the renderer and prefetching to be non blocking and using async http calls.

Some other interesting changes:
* add contrast/color boost options
* fixed page margins
* add reading lists
* so many more fixes

# v0.9.19

End of chapter behavior (#10) now has 3 options: 
1. Stop: page navigation stops at chapter end.
2. Ask: dialog gives options to either close chapter or continue with next chapter
3. Auto: if there is an available next chapter, continue to next chapter

# v0.9.18

Fix issue with page navigation in pan mode that was found through pull request #5.

# v0.9.17

Compatibility fix for KOReader 2026.03
