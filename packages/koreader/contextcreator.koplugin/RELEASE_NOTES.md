# v0.1.4-beta

Large amount of bug fixes, quality of life updates and new features. Far more polished now! I plan to upgrade the graph visualisation in the next release but here are the changes for this one:

Within KOreader:

- Can now rename/delete profiles within koreader by long pressing a profile in the profile menu to rename or delete it, the change syncs to the web and other devices seamlessly
- Profile renames/deletes now sync both ways properly (previously deletes on the webapp end didnt reflect within KOreader)
- Fixes to reading progress processing
- Context lists are now collapsible by context type
- Lists are refreshed live
- Per device covers are available in the webapp
- Faster sync (polling interval reduced while maintaining performance)
- Schema migration safety, explicit and version aware migration for the on disk doc with forward and backward compatibility
- Ability to set aliases as main context name
- Variety of small fixes that were annoying

Webapp:

- Added page routing in case you wanted to bookmark a specific book and context profile
- Covers are completely customisable, can select from a custom cover or any of the covers from koreader devices you have synced with the server
- Home page has been reworked, reading progress on cards, author sorting can be done by first or last name based on your choice, few more smaller changes to make the home page easier to use and better looking.
- Graph: adding dot points uses the same clean inline flow as adding a relationship, contexts with no dot points always show, type filter legend counts only whats on screen based on timeline, can promote an alias to the main context name from the node window
- Profiles: stopped letting multiple profiles have the same name, added better styling for a variety of dialog box popups that used default browser popups
- Timeline fixes: defaults to 0% on new loadup and jump to current is completely fixed now after being buggy for a while
- Import/export for all contexts now exports a zipped folder of per book jsons including covers and import all takes a folder.
- Other ui fixes: top bar stays fixed when scrolling, wider windows where appropriated, alignment fixes etc
- Reorganisation of file structure in the repo for frontend stuff which was much needed
- Fixes to attaching imported jsons to your own books

# v0.1.3-alpha

Within KOreader:
- Reworked windows and buttons to be more responsive to smaller screens
- Reworked certain menus so that going back to the previous menu is available without needing to cancel and start again when creating contexts
- Added ability to open context after highlighting which opens any exactly matched contexts or asks for confirmation on fuzzy matched contexts
- Added ability to give contexts aliases and promote aliases to the main context name

WebUI:
- Reworked the homescreen for better customisability and sorting options.
- Implemented corresponding changes to reflect the plugin additions mentioned previously
- Fixed book cover syncing problem

Ensure to pull the latest docker image if using the webapp too!
- docker pull mcurmi05/koreader-context-creator:latest
