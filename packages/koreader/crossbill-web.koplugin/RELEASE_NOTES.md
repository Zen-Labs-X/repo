# v0.29.0

Major UI changes. New landing page and library page, sessions page replaced by statistics page in books, lots of minor UI/UX consistency fixes etc.

## Docker Image
```bash
docker pull tumetsu/crossbill:v0.29.0
```


## What's Changed
* Settle one list-length strategy, and place every highlight in a chapter by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/688
* Bump backend/uv.lock in the release workflow, and guard it in CI by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/690
* Remove AI summaries from reading sessions by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/700
* Replace the sessions listing with a compact SessionCard by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/701
* Share the compact-viewport test helper by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/702
* Change sessions page into statistics page by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/703
* Add a reading-activity grid to the book statistics tab by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/706
* Use SectionTitles in the Settings page by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/707
* Split library browsing into its own page by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/708
* Add library-wide reading activity grid endpoint by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/709
* Serve the reader's latest highlights and notes on one timeline by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/712
* Stop related content from repeating one book, and hide weak matches by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/714
* Give the search results room to breathe by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/719
* Add bulk book summary regeneration by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/720
* List books matched by name on top of global search results by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/721
* Commit every search field on Enter, never while typing by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/723
* Move the global search read from /semantic/search to /search by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/722
* Search books from the app bar without embeddings by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/725
* Show empty state instead of hiding sections for new readers by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/726
* chore(deps-dev): Bump eslint from 10.8.0 to 10.9.1 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/691
* chore(deps): Bump axios from 1.19.0 to 1.20.0 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/692
* chore(deps): Bump @mui/material from 9.3.1 to 9.4.0 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/693
* chore(deps-dev): Bump @types/luxon from 3.7.3 to 3.7.5 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/694
* Show the app with screenshots on the README and the site frontpage by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/728


**Full Changelog**: https://github.com/Crossbill-App/crossbill-web/compare/v0.28.1...v0.29.0

# v0.28.1

## Docker Image
```bash
docker pull tumetsu/crossbill:v0.28.1
```


## What's Changed
* Give the six book tabs one shared PageHeader by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/685
* Fix the mobile filter drawer leaving the page unscrollable by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/686


**Full Changelog**: https://github.com/Crossbill-App/crossbill-web/compare/v0.28.0...v0.28.1

# v0.28.0

## Docker Image
```bash
docker pull tumetsu/crossbill:v0.28.0
```


## What's Changed
* Show each book's reading stage in the library list by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/651
* Add note and reading-session counts to the book stats strip by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/656
* Bump @tanstack/react-router from 1.170.18 to 1.170.32 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/563
* Add book blurb to the book header area (#653) by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/659
* Write and edit a chapter gist inline by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/658
* UI audit: the agreed findings in sections A–J by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/663
* MUI Guidelines based UI/UX improvements by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/667
* Normalise KOReader highlight timestamps to ISO in the backend by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/678
* Merge the two landing-page carousels into one recent-books row by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/679
* Fade every book tab in from one place by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/681
* Show highlight, note and flashcard counts on library book cards by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/682


**Full Changelog**: https://github.com/Crossbill-App/crossbill-web/compare/v0.27.2...v0.28.0

# v0.27.2

## Docker Image
```bash
docker pull tumetsu/crossbill:v0.27.2
```


## What's Changed
* Make the Railway deploy branch-aware and quiet about the environment by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/650
* Fix broken KOReader plugin link in README by @jdbway in https://github.com/Crossbill-App/crossbill-web/pull/647
* Replace "Preferences" with "Settings" in hamburger menu by @jdbway in https://github.com/Crossbill-App/crossbill-web/pull/646
* Lock body scroll while the filter drawer is open by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/649
* Bump @mui/icons-material from 9.2.0 to 9.3.1 by @dependabot[bot] in https://github.com/Crossbill-App/crossbill-web/pull/569


**Full Changelog**: https://github.com/Crossbill-App/crossbill-web/compare/v0.27.1...v0.27.2

# v0.27.1

## Docker Image
```bash
docker pull tumetsu/crossbill:v0.27.1
```


## What's Changed
* Stop pull-to-refresh from swallowing scrolls inside dialogs by @Tumetsu in https://github.com/Crossbill-App/crossbill-web/pull/645


**Full Changelog**: https://github.com/Crossbill-App/crossbill-web/compare/v0.27.0...v0.27.1
