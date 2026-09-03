# v0.12.6

## Release Highlights
* Audiobooks: Added Audiobookshelf support for streaming audiobooks and podcasts, and you can now pair an audiobook with its ebook to read along as it plays
* Text-to-Speech: Added a lyric-style view that shows the sentences around the one being read, plus per-book offline voice downloads and steadier pauses between sentences
* Library: You can now browse the web inside Readest to add books, choose which chapters to import from a web novel, hide covers for privacy, and watch download progress right on the shelf
* Sharing: Added Nearby BookDrop to send and receive books between nearby devices over your local network, including KOReader devices
* Reading: Added customizable keyboard and mouse shortcuts, Yomitan dictionary support, a full-screen book cover view, and right-to-left page order for comics and fixed-layout books
* Reading: The Notebook is now a full writing workspace, where your notes save as you type, sync across devices, and link back to the passage they came from
* Footnotes: Footnote popups no longer get cut off, let you select and look up text, and can jump straight to the note's place in the book
* PDF: You can now select text across page boundaries, copy paragraphs without broken line breaks, and see the printed page numbers as reference pages
* Sync: Your book groups and shelves now sync, file sync between devices settles reliably, highlights you delete in KOReader come across, and your progress survives an OPDS re-download
* More: Fixed crashes on launch, garbled AZW3 books, the reading position drifting after rotating the screen, and unreadable highlights on e-ink screens

## What's Changed
* fix(ios): App Review launch crash, CarPlay crash on connect, and main thread hangs by @chrox in https://github.com/readest/readest/pull/5590
* fix(opds): make the title bar draggable in the online library view by @chrox in https://github.com/readest/readest/pull/5592
* fix(opds): filter incompatible download formats and offer one-click EPUB by @chrox in https://github.com/readest/readest/pull/5593
* fix(sync): drop the Origin header from OAuth token requests by @chrox in https://github.com/readest/readest/pull/5604
* fix(android): stop claiming APKs and other downloads as openable books by @chrox in https://github.com/readest/readest/pull/5610
* feat(localsend): send and receive books over the local network by @chrox in https://github.com/readest/readest/pull/5611
* fix(library): release TXT sources and chapter HTML during import by @ChuwuYo in https://github.com/readest/readest/pull/5607
* fix(library): checkpoint, serialize, and pool folder imports by @chrox in https://github.com/readest/readest/pull/5615
* fix(translation): gate Enable Translation on book availability by @chrox in https://github.com/readest/readest/pull/5617
* docs(readme): restore the Sponsors / TestMu AI section by @chrox in https://github.com/readest/readest/pull/5619
* fix(translate): send Bing language codes in the Azure provider by @chrox in https://github.com/readest/readest/pull/5620
* fix(library): stop a long press from selecting and then deselecting a book by @chrox in https://github.com/readest/readest/pull/5621
* fix(ci): stop cargo pulling the flutter SDK for the localsend dep by @chrox in https://github.com/readest/readest/pull/5622
* fix(reader): isolate the book cell to drop the Linux black corner by @PolybiusPro in https://github.com/readest/readest/pull/5618
* fix(popup): stop mounting the filtered pointer triangle at rest by @chrox in https://github.com/readest/readest/pull/5628
* fix(localsend): let Readest devices discover each other by @chrox in https://github.com/readest/readest/pull/5626
* fix(sync): recover KOReader progress when a chapter is not well-formed XML by @chrox in https://github.com/readest/readest/pull/5630
* fix(ci): gate build_tauri_app on tauri paths and give webdriver its own timeout by @chrox in https://github.com/readest/readest/pull/5644
* feat(ci): Added new step to release workflow to send release notes to a Discord channel by @sloaner in https://github.com/readest/readest/pull/5637
* fix(reader): commit settled image zoom into the layout size, closes #5633 by @chrox in https://github.com/readest/readest/pull/5639
* fix(novel): retry transient fetch failures and backfill work metadata by @chrox in https://github.com/readest/readest/pull/5650
* fix(markdown): title imported books after the file, not the first heading by @chrox in https://github.com/readest/readest/pull/5653
* fix(sanitizer): render Persian/Arabic half-space by converting misused RLM to ZWNJ by @shahram7 in https://github.com/readest/readest/pull/5651
* fix(reader): stop iOS 16 WebContent crash when opening a book by @chrox in https://github.com/readest/readest/pull/5654
* feat(reader): flash the target of in-page footnote jumps, closes #5647 by @chrox in https://github.com/readest/readest/pull/5655
* fix(koplugin): extract self-update with ffi/archiver on KOReader 2026.07+ by @chrox in https://github.com/readest/readest/pull/5656
* fix(reader): render fixed-layout pages as authored in dark mode, closes #5649 by @chrox in https://github.com/readest/readest/pull/5657
* fix(reader): disable text autosizing in fixed-layout books, closes #5641 by @chrox in https://github.com/readest/readest/pull/5659
* ci: raise nightly and release build timeouts to 90 minutes by @chrox in https://github.com/readest/readest/pull/5664
* fix(opds): stop auto-downloaded books from vanishing on restart by @chrox in https://github.com/readest/readest/pull/5665
* fix(iap): re-verify restored iOS one-time purchases with the server by @chrox in https://github.com/readest/readest/pull/5669
* chore(deps): bump the github-actions group with 6 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5668
* fix(ui): size the alert surface off its container, not its content by @WantenMN in https://github.com/readest/readest/pull/5662
* fix(koplugin): push reading stats in bounded chunks, closes #5666 by @chrox in https://github.com/readest/readest/pull/5670
* feat(reader): jump to the start or end of the book with Home/End by @chrox in https://github.com/readest/readest/pull/5673
* fix(sync): never show a future Last Synced time from a clock-skewed peer by @chrox in https://github.com/readest/readest/pull/5674
* fix(reader): update progress during Auto Scroll and put slider overlay values on top by @chrox in https://github.com/readest/readest/pull/5676
* fix(reader): reach the last page of the book on iOS by @chrox in https://github.com/readest/readest/pull/5678
* feat(reader): scroll Auto Scroll smoothly at low speeds by @chrox in https://github.com/readest/readest/pull/5679
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5682
* fix(library): allow unchecking Read books in place for registered folders, closes #5680 by @chrox in https://github.com/readest/readest/pull/5685
* fix(reader): keep table label columns from collapsing by @chrox in https://github.com/readest/readest/pull/5686
* feat(tts): scroll to the current chapter when opening Offline Audio by @gfreitash in https://github.com/readest/readest/pull/5684
* feat(koplugin): LocalSend receive and send for KOReader devices by @chrox in https://github.com/readest/readest/pull/5687
* fix(sync): create the replica bundle dir before downloading, closes #5675 by @chrox in https://github.com/readest/readest/pull/5700
* chore(koplugin): build nightly plugin zip and default to device targets by @chrox in https://github.com/readest/readest/pull/5699
* feat(sync): add cloud shelves and safe provider deletion by @chrox in https://github.com/readest/readest/pull/5701
* fix(android): gate gamepad polling on controller connection by @chrox in https://github.com/readest/readest/pull/5702
* fix(dictionary): recover StarDict searches after an empty result by @chrox in https://github.com/readest/readest/pull/5705
* feat(tts): symmetric minimal mini-player with centered play button by @chrox in https://github.com/readest/readest/pull/5707
* fix(reader): remove header controls duplicated by the mobile footer bar by @chrox in https://github.com/readest/readest/pull/5708
* feat(sync): optional document metadata on KOSync progress uploads by @chrisbutler in https://github.com/readest/readest/pull/5704
* feat(reader): resume Auto Scroll when reopening a book by @chrox in https://github.com/readest/readest/pull/5710
* fix(reader): support page turner key combinations by @chrox in https://github.com/readest/readest/pull/5709
* feat(reader): right-to-left page order for fixed-layout books by @chrox in https://github.com/readest/readest/pull/5712
* fix(reader): avoid wide word gaps from authored text-wrap pretty, closes #5582 by @chrox in https://github.com/readest/readest/pull/5718
* fix(reader): restore scrolled PDF highlights by @chrox in https://github.com/readest/readest/pull/5719
* fix(sync): remove the mixed-fleet info toast, closes #5720 by @chrox in https://github.com/readest/readest/pull/5726
* fix(sync): sync the reference page count and stop import wiping configs, closes #5716 by @chrox in https://github.com/readest/readest/pull/5727
* fix(reader): highlight search results visible across chapter boundary by @WantenMN in https://github.com/readest/readest/pull/5725
* fix(reader): drop the 500-result cap from in-book search by @chrox in https://github.com/readest/readest/pull/5728
* fix(annotator): drop the selection when the instant dictionary opens, closes #5585 by @chrox in https://github.com/readest/readest/pull/5730
* fix(reader): neutralize fixed backgrounds and drop negative margins by @chrox in https://github.com/readest/readest/pull/5729
* fix(library): optimize bookshelf covers in background, closes #5632 by @chrox in https://github.com/readest/readest/pull/5731
* fix(eink): make e-ink highlights and chips visible, closes #5667 by @chrox in https://github.com/readest/readest/pull/5735
* feat(wordlens): add the en-vi gloss pack, sync incrementally by @chrox in https://github.com/readest/readest/pull/5737
* feat(wordlens): add the en-hu gloss pack by @chrox in https://github.com/readest/readest/pull/5738
* fix(wordlens): key the manifest diff on pack routing fields too by @chrox in https://github.com/readest/readest/pull/5739
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5740
* feat(library): add hide-covers privacy option for the bookshelf by @WantenMN in https://github.com/readest/readest/pull/5733
* feat(tts): queue chapter downloads with per-book persistence by @gfreitash in https://github.com/readest/readest/pull/5690
* feat(library): show download progress overlay on book covers by @WantenMN in https://github.com/readest/readest/pull/5736
* feat(annotator): support text selection tools in footnote popups by @chrox in https://github.com/readest/readest/pull/5744
* feat(reader): pair local audiobooks with ebooks by @chrox in https://github.com/readest/readest/pull/5754
* fix(tts): make sentence and paragraph pauses consistent by @chrox in https://github.com/readest/readest/pull/5753
* fix(reader): keep chapter images openable after repeated footnote popups by @chrox in https://github.com/readest/readest/pull/5756
* docs: add contributor code of conduct by @chrox in https://github.com/readest/readest/pull/5758
* fix(opds): honor the Manage Sync Books toggle for automatic cloud uploads by @chrox in https://github.com/readest/readest/pull/5759
* feat(opds): confirm auto-download toggles and allow catalog reordering by @chrox in https://github.com/readest/readest/pull/5760
* feat(i18n): add Georgian translations by @chrox in https://github.com/readest/readest/pull/5763
* fix(cbz): order split chapter folders base-first by @chrox in https://github.com/readest/readest/pull/5762
* fix(opds): drop the webview Origin header on native requests by @NoaHimesaka1873 in https://github.com/readest/readest/pull/5765
* feat(dictionaries): add bundled plugin and Yomitan support by @chrox in https://github.com/readest/readest/pull/5764
* feat: package for nix by @dastarruer in https://github.com/readest/readest/pull/5605
* fix(reader): translate iframe text without duplicating TTS by @Columpio in https://github.com/readest/readest/pull/5772
* fix(tts): allow chapters sharing sentences with earlier packs to download by @gfreitash in https://github.com/readest/readest/pull/5768
* fix(deps): resolve open Dependabot alerts by @chrox in https://github.com/readest/readest/pull/5778
* fix(nix): update pnpmDeps hash and verify dep hashes on PRs by @chrox in https://github.com/readest/readest/pull/5779
* fix(library): recover from a failed startup instead of rendering a blank window by @chrox in https://github.com/readest/readest/pull/5789
* chore(deps): bump the github-actions group with 7 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5796
* docs: use git input instead of github input by @dastarruer in https://github.com/readest/readest/pull/5791
* feat: Audiobookshelf integration with audiobook streaming and podcasts by @chrox in https://github.com/readest/readest/pull/5801
* fix(reader): extend pull-to-bookmark to fixed layout and yield to late selection by @chrox in https://github.com/readest/readest/pull/5802
* feat(reader): expose data-eink on the book document for per-device custom CSS by @chrox in https://github.com/readest/readest/pull/5803
* fix(android): keep the reader alive when a Bluetooth controller connects (#5799) by @chrox in https://github.com/readest/readest/pull/5804
* fix(reader): render markdown in the note bubble popup, closes #5785 by @chrox in https://github.com/readest/readest/pull/5805
* feat(reader): add inline note editing by @libbybar in https://github.com/readest/readest/pull/5780
* feat(reader): expose book title and series as data attributes for custom UI CSS, closes #5776 by @chrox in https://github.com/readest/readest/pull/5806
* feat(reader): show PDF page labels as reference pages, closes #5822 by @chrox in https://github.com/readest/readest/pull/5824
* feat(rsvp): add exact WPM entry and 10 WPM nudge to the speed dropdown, closes #5820 by @chrox in https://github.com/readest/readest/pull/5825
* fix(translate): follow Bing regional host and show why a translation failed by @chrox in https://github.com/readest/readest/pull/5826
* feat(reader): join PDF line wraps into paragraphs when copying, closes #5814 by @chrox in https://github.com/readest/readest/pull/5828
* fix(annotator): hide the range editor handles while a lookup popup is open, closes #5815 by @chrox in https://github.com/readest/readest/pull/5829
* feat(reader): show the book cover full screen from the sidebar and book details, closes #5813 by @chrox in https://github.com/readest/readest/pull/5827
* perf(sync): merge stat_pages pushes in one upsert_stat_pages RPC by @chrox in https://github.com/readest/readest/pull/5832
* feat(reader): select text across PDF pages as one selection, closes #5809 by @chrox in https://github.com/readest/readest/pull/5831
* fix(koplugin): pull reading stats in bounded pages by @chrox in https://github.com/readest/readest/pull/5833
* feat(stats): tier stat_pages history into R2 segments behind a 7-day hot window by @chrox in https://github.com/readest/readest/pull/5835
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5840
* fix(audiobookshelf): hide ABS books without a server row and backfill covers unauthenticated by @chrox in https://github.com/readest/readest/pull/5841
* fix(stats): survive PostgREST's row cap when building archive segments by @chrox in https://github.com/readest/readest/pull/5844
* chore(stats): enable the archive compaction cron by @chrox in https://github.com/readest/readest/pull/5845
* fix(sync): send S3 object keys in SigV4 canonical form by @chrox in https://github.com/readest/readest/pull/5849
* fix(nix): match the Android AVD ABI to the host architecture (#5732) by @chrox in https://github.com/readest/readest/pull/5850
* fix(koplugin): stop auto sync from prompting for Wi-Fi on book open and wake by @chrox in https://github.com/readest/readest/pull/5848
* fix(backup): export only live library books and reclaim orphaned book files by @chrox in https://github.com/readest/readest/pull/5851
* fix(reader): keep the reading position across screen rotations by @chrox in https://github.com/readest/readest/pull/5855
* fix(sync): sync highlight deletions from KOReader to Readest by @chrox in https://github.com/readest/readest/pull/5853
* feat(reader): pair an Audiobookshelf audiobook and read along (#5807) by @chrox in https://github.com/readest/readest/pull/5856
* feat(reader): let users pick the Hardcover book a file syncs to, closes #5846 by @chrox in https://github.com/readest/readest/pull/5857
* feat(toc): wrap long headings onto multiple lines instead of truncating by @chrox in https://github.com/readest/readest/pull/5858
* fix(bookorbit): list the open book under Unmatched KOReader Books for manual linking by @chrox in https://github.com/readest/readest/pull/5860
* fix(wordlens): build kaikki packs from the raw wiktextract dump by @chrox in https://github.com/readest/readest/pull/5861
* fix(reader): move a paired audiobook by audio and decode WebP covers (#5863) by @chrox in https://github.com/readest/readest/pull/5865
* fix(sync): stop OPDS re-downloads from losing reading progress (#5859) by @chrox in https://github.com/readest/readest/pull/5866
* fix(reader): resolve media that book scripts add after the section loads, closes #1812 by @chrox in https://github.com/readest/readest/pull/5868
* fix(sync): shelve an imported book on other devices without opening it first by @chrox in https://github.com/readest/readest/pull/5869
* feat(library): add From Web Browser import with an in-app browser (#5775) by @chrox in https://github.com/readest/readest/pull/5870
* fix(reader): render the IDPF EPUB 3 samples correctly (#480) by @chrox in https://github.com/readest/readest/pull/5872
* fix(windows): match the main window's scroll bar style in clip and browser windows by @chrox in https://github.com/readest/readest/pull/5873
* fix(library): rubber-band the bookshelf at both edges and keep the reader from overscrolling by @jadhavgaurav in https://github.com/readest/readest/pull/5867
* fix(android): stop the launch crash on covers that decode 1px tall by @chrox in https://github.com/readest/readest/pull/5874
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5875
* feat(ui): migrate to daisyUI 5 and Tailwind CSS 4 by @chrox in https://github.com/readest/readest/pull/5884
* fix(library): save the new data location when migrating an empty library by @jadhavgaurav in https://github.com/readest/readest/pull/5878
* fix(sync): apply pulled file-sync progress to the live reader by @chrox in https://github.com/readest/readest/pull/5886
* feat(reader): jump from a footnote popup to the location in the book by @chrox in https://github.com/readest/readest/pull/5889
* feat(library): select chapters when importing web novels by @chrox in https://github.com/readest/readest/pull/5892
* chore(deps): upgrade to TypeScript 7 by @chrox in https://github.com/readest/readest/pull/5893
* fix(ui): size toasts to their message and fade dialogs out whole by @chrox in https://github.com/readest/readest/pull/5894
* fix(library): refresh PDF metadata on re-import by @chrox in https://github.com/readest/readest/pull/5895
* fix(reader): do not truncate footnote popups by @alexander-pecheny in https://github.com/readest/readest/pull/5887
* fix(reader): make cross-page selection actually work by @alexander-pecheny in https://github.com/readest/readest/pull/5888
* chore(deps): bump the github-actions group with 6 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5902
* fix(android): migrate Google Play Billing to v9 by @chrox in https://github.com/readest/readest/pull/5896
* fix: folder import of Markdown, widget opens, comic zoom, selection handle and TTS word highlight by @chrox in https://github.com/readest/readest/pull/5903
* fix(ui): restore the daisyUI 4 loading dots animation by @chrox in https://github.com/readest/readest/pull/5906
* fix(sync): converge multi-device file sync (#5900) by @jadhavgaurav in https://github.com/readest/readest/pull/5905
* feat(tts): lyric-style sentence view in the Read Aloud player (#5755) by @chrox in https://github.com/readest/readest/pull/5908
* fix(tts): queue a lyric reload requested during an in-flight fetch by @chrox in https://github.com/readest/readest/pull/5909
* feat(shortcuts): add customizable keyboard and mouse bindings by @WhiteHades in https://github.com/readest/readest/pull/5907
* fix(translate): Chinese targets, provider rate limits, and translator popup layout by @chrox in https://github.com/readest/readest/pull/5913
* fix(android): avoid full PDF parsing during import by @chrox in https://github.com/readest/readest/pull/5914
* feat(localsend): brand the LAN transfer feature as Nearby BookDrop by @chrox in https://github.com/readest/readest/pull/5915
* fix(ui): paint modal boxes that sit outside an open daisyUI modal by @chrox in https://github.com/readest/readest/pull/5916
* fix(mobi): keep AZW3 text and TOC intact when section loads overlap by @chrox in https://github.com/readest/readest/pull/5920
* fix(sync): report third-party sync status in the reader menu (#5910) by @chrox in https://github.com/readest/readest/pull/5922
* fix(sync): resolve book groups and metadata on their own clock (#5911, #5912) by @chrox in https://github.com/readest/readest/pull/5921
* fix(ui): search cloud storage files on demand instead of while typing (#5923) by @chrox in https://github.com/readest/readest/pull/5925
* fix(reader): stop the a11y skip link from padding RTL sections with blank pages (#5924) by @chrox in https://github.com/readest/readest/pull/5926
* fix(ui): align the keyboard shortcuts header with its group titles by @chrox in https://github.com/readest/readest/pull/5927
* feat(reader): Notebook as a linked writing workspace by @chrox in https://github.com/readest/readest/pull/5928
* release: version 0.12.6 by @chrox in https://github.com/readest/readest/pull/5929

## New Contributors
* @sloaner made their first contribution in https://github.com/readest/readest/pull/5637
* @gfreitash made their first contribution in https://github.com/readest/readest/pull/5684
* @chrisbutler made their first contribution in https://github.com/readest/readest/pull/5704
* @NoaHimesaka1873 made their first contribution in https://github.com/readest/readest/pull/5765
* @libbybar made their first contribution in https://github.com/readest/readest/pull/5780
* @jadhavgaurav made their first contribution in https://github.com/readest/readest/pull/5867

**Full Changelog**: https://github.com/readest/readest/compare/v0.12.1...v0.12.6

# v0.12.1

## Release Highlight
* Text-to-Speech: Books that come with recorded narration now play their own audio in step with the text, and you can set the sleep timer to stop at the end of a chapter
* Library: Added full text search across your books with fuzzy and nearby-word matching, importing web novels from a link, bulk downloading from the shelf, and page counts in book details
* Annotations: Your notes and highlights now live in one hub, where you can export and import them as a file, copy a link back to any highlight, and write math formulas in your notes
* Reading: You can now pull down to add a bookmark, tap the page label to jump to any page, tap the footer to bring up the progress bar, and turn pages with an Apple Pencil double tap or squeeze
* Reading: Fixed layout books can now scroll horizontally, image descriptions show in the image viewer, search results group by chapter, and the mouse cursor gets out of the way while you read
* Sync: Added iCloud sync on iPhone, iPad and Mac, plus a BookOrbit integration that keeps your annotations, bookmarks, stats and reading status in step
* Translation: Translated text now keeps its bold, italic and other inline formatting, and the Azure and Yandex translators work again
* Styling: Added Ambient Mode on Android, a refreshed theme and background picker with separate looks for your library and reader, and cleaner popups throughout
* PDF: Sharper text on desktop and a readable footer in scrolled mode
* More: Markdown books now pick up their title and author automatically and show every heading in the contents, plus fixes for some crashes

## What's Changed
* fix(reader): resolve high-priority Sentry crashes by @chrox in https://github.com/readest/readest/pull/5231
* fix(android): drop the Sentry NDK integration that destabilizes the WebView (#5227) by @chrox in https://github.com/readest/readest/pull/5234
* fix(android): withdraw Android Auto opt-in to pass Play review by @chrox in https://github.com/readest/readest/pull/5235
* Contain updater and native auth rejections by @chrox in https://github.com/readest/readest/pull/5237
* Fix high-priority reader runtime errors by @chrox in https://github.com/readest/readest/pull/5236
* refactor: remove the auto upload books option in the main menu in favor of the settings in Readest manage sync settings by @chrox in https://github.com/readest/readest/pull/5243
* feat: style checked toggle by @dastarruer in https://github.com/readest/readest/pull/5242
* fix: set `GDK_BACKEND` to `x11` to fix rendering issues by @dastarruer in https://github.com/readest/readest/pull/5248
* feat: add setting to enable skeuomorphic book covers by @dastarruer in https://github.com/readest/readest/pull/5245
* chore: migrate away from numtide devshell by @dastarruer in https://github.com/readest/readest/pull/5131
* chore(deps): bump the github-actions group with 5 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5276
* docs: fix typo in README by @dastarruer in https://github.com/readest/readest/pull/5298
* fix(windows): enforce LF line endings and normalize test path separators by @LukashevychAndrii in https://github.com/readest/readest/pull/5302
* feat(theme): unify theme selector and bg texture selector styling by @dastarruer in https://github.com/readest/readest/pull/5305
* fix(reader): invalidate stale nav cache for encoded TOC hrefs (#5308) by @chrox in https://github.com/readest/readest/pull/5311
* fix(rss): sync feed subscriptions across devices (#5307) by @chrox in https://github.com/readest/readest/pull/5314
* feat(settings): rename "Column Gap" to "Additional Margin" by @chrox in https://github.com/readest/readest/pull/5315
* fix(library): disable skeuomorphic book covers by default by @chrox in https://github.com/readest/readest/pull/5316
* feat(reader): add collapsible chapter sections to search results by @WantenMN in https://github.com/readest/readest/pull/5282
* Load OPDS catalogs when opening the Integrations panel by @chloeroform in https://github.com/readest/readest/pull/5283
* perf(reader): improve Slide/Curl gesture responsiveness by @chihumyum in https://github.com/readest/readest/pull/5291
* fix(opds): keep same-host links on https when the feed is https (#5300) by @chrox in https://github.com/readest/readest/pull/5324
* fix(calibre): verify the cloud blob exists before a row-only push by @chrox in https://github.com/readest/readest/pull/5325
* feat(calibre): Check Readest status action, with faster cloud lookups by @chrox in https://github.com/readest/readest/pull/5332
* fix(macos): restore close-to-hide behavior on Tahoe by @liyafly in https://github.com/readest/readest/pull/5333
* fix(reader): keep system brightness on after swipe by @alexander-pecheny in https://github.com/readest/readest/pull/5292
* feat: calculate TTS gap based on rate by @dastarruer in https://github.com/readest/readest/pull/5326
* Show import options when clicking the bookshelf add button by @bcrave in https://github.com/readest/readest/pull/5247
* chore(deps): bump dependencies for open Dependabot advisories by @chrox in https://github.com/readest/readest/pull/5335
* fix(auth): move ProviderLogin out of the auth page module by @chrox in https://github.com/readest/readest/pull/5336
* fix(library): stop re-importing duplicate files from watched folders by @chrox in https://github.com/readest/readest/pull/5337
* fix(reader): align paragraph mode chrome with the TTS player (#5275) by @chrox in https://github.com/readest/readest/pull/5338
* feat(markdown): parse YAML frontmatter into book metadata by @chrox in https://github.com/readest/readest/pull/5344
* fix(reader): keep book fonts when proofread rules change (#5277) by @chrox in https://github.com/readest/readest/pull/5345
* fix(epub): fall back to cover-named zip entries by @chrox in https://github.com/readest/readest/pull/5339
* fix(metadata): make "Change cover image" work on iOS by @chrox in https://github.com/readest/readest/pull/5346
* fix(reader): keep the PDF footer readable in scrolled mode (#5342) by @chrox in https://github.com/readest/readest/pull/5347
* fix(pdf): keep desktop PDF text sharp (#5251) by @chrox in https://github.com/readest/readest/pull/5348
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5358
* fix(translate): restore Yandex Translate provider by @Columpio in https://github.com/readest/readest/pull/5256
* feat(markdown): support full heading depth in the TOC (#5357) by @chrox in https://github.com/readest/readest/pull/5363
* fix(reader): report image zoom against the image resolution, closes #5362 by @chrox in https://github.com/readest/readest/pull/5365
* fix(sync): pull the books delta in bounded pages for large libraries by @chrox in https://github.com/readest/readest/pull/5364
* fix: preserve U+200F/U+200E BiDi marks in Persian/Arabic ebooks (#5216) by @shahram7 in https://github.com/readest/readest/pull/5361
* feat(tts): add End of Chapter option to sleep timer by @nurumubu in https://github.com/readest/readest/pull/5355
* fix: disable hardcoded debug flag in AI logger by @fix2015 in https://github.com/readest/readest/pull/5370
* fix(translate): restore Yandex auto-detection and translated TTS by @Columpio in https://github.com/readest/readest/pull/5374
* fix(sync): stop a local-only delete from wiping the Drive copy (#5265) by @chrox in https://github.com/readest/readest/pull/5376
* fix(android): keep All Files Access on the Play build (#5372) (#2862) by @chrox in https://github.com/readest/readest/pull/5378
* feat(clip): capture login-walled articles with an in-app sign-in by @chrox in https://github.com/readest/readest/pull/5377
* fix(ios): unbreak the share extension build after the clip capture change by @chrox in https://github.com/readest/readest/pull/5379
* fix(window): cover the taskbar when entering fullscreen while maximized on Windows by @chrox in https://github.com/readest/readest/pull/5380
* fix(discord): keep the rich presence cover URL stable (#5352) by @chrox in https://github.com/readest/readest/pull/5382
* feat(library): import web novels from a URL (#5294) by @chrox in https://github.com/readest/readest/pull/5381
* fix(css): keep image invert effective in dark mode with color override by @chrox in https://github.com/readest/readest/pull/5383
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5384
* chore(deps): bump the github-actions group with 3 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5396
* feat(reader): add font size setting and honor custom fonts in paragraph mode by @chrox in https://github.com/readest/readest/pull/5403
* feat(reader): auto-hide the mouse cursor while reading (#5178) by @chrox in https://github.com/readest/readest/pull/5404
* fix(ios): declare NSPhotoLibraryAddUsageDescription so saving images works (#5397) by @chrox in https://github.com/readest/readest/pull/5405
* fix(layout): keep dropdown menus within viewport by @ChuwuYo in https://github.com/readest/readest/pull/5392
* fix(library): do not dedupe distinct PDFs with identical metadata by @chrox in https://github.com/readest/readest/pull/5412
* fix(reader): exclude trailing whitespace from double-click selection by @ChuwuYo in https://github.com/readest/readest/pull/5413
* feat(theme): add Ambient Mode on Android by @Jesusm1229 in https://github.com/readest/readest/pull/5394
* fix(ios): declare txt and md in fileAssociations so Files offers Readest again by @chrox in https://github.com/readest/readest/pull/5415
* fix(tts): read TTS section documents through the display transform pipeline (#5406) by @chrox in https://github.com/readest/readest/pull/5416
* fix(tts): cut Edge trailing silence on iOS playout so sentence pauses are honored (#5414) by @chrox in https://github.com/readest/readest/pull/5417
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5418
* feat(library): add scoped full text search with fuzzy and nearby modes by @WhiteHades in https://github.com/readest/readest/pull/5389
* fix(proofread): match Unicode punctuation next to letters by @ChuwuYo in https://github.com/readest/readest/pull/5421
* feat(dictionaries): add Babylon BGL dictionary format by @chrox in https://github.com/readest/readest/pull/5428
* fix(reader): normalize body text size in reflowable books by @ChuwuYo in https://github.com/readest/readest/pull/5422
* fix(reader): suppress the Android system selection menu natively (#5427) by @chrox in https://github.com/readest/readest/pull/5430
* fix(reader): eink popup pointer triangle rendered solid black above selections by @chrox in https://github.com/readest/readest/pull/5431
* fix(reader): let long press reach the first line on mobile (#5429) by @chrox in https://github.com/readest/readest/pull/5432
* fix(ci): pin the AppImage tauri-cli fork to a known-good rev by @chrox in https://github.com/readest/readest/pull/5433
* fix(search): keep search options on one line at any text scale by @chrox in https://github.com/readest/readest/pull/5434
* feat(reader): include book cover in annotation exports and Readwise sync (#5424) by @chrox in https://github.com/readest/readest/pull/5435
* fix(reader): give the toolbar controls a 44px touch target (#5401) by @chrox in https://github.com/readest/readest/pull/5437
* fix(library): keep subfolder groups for auto-imported books (#5423) by @chrox in https://github.com/readest/readest/pull/5436
* fix(library): release parsed book documents after import, closes #5387 by @chrox in https://github.com/readest/readest/pull/5439
* fix(sync): merge book metadata on its own clock so page turns cannot clobber edits by @chrox in https://github.com/readest/readest/pull/5442
* feat(annotations): export and import annotations as JSON, closes #5400 by @chrox in https://github.com/readest/readest/pull/5440
* fix(web): make CORS preflight responses cacheable for authenticated requests by @chrox in https://github.com/readest/readest/pull/5444
* feat(settings): add library/reader scope switcher to background image picker by @chrox in https://github.com/readest/readest/pull/5443
* feat(library): add bulk Download to the select-mode action bar (#5244) by @chrox in https://github.com/readest/readest/pull/5445
* feat(tts): fine-tune the mini player time info and transport (#5310) by @chrox in https://github.com/readest/readest/pull/5446
* fix(reader): lift the header into the notch on negative top margins by @chrox in https://github.com/readest/readest/pull/5447
* feat(popup): restyle popups by @dastarruer in https://github.com/readest/readest/pull/5351
* feat(reader): centralize notes and highlights in the annotations hub, closes #5398, #3870 by @chrox in https://github.com/readest/readest/pull/5448
* feat(stats): count TTS listening as reading time by @chrox in https://github.com/readest/readest/pull/5450
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5449
* fix(popup): center the marker glyph and compact the highlight style buttons by @chrox in https://github.com/readest/readest/pull/5451
* fix(android): stabilize the nightly e2e lane and the top-inset touch overlays by @chrox in https://github.com/readest/readest/pull/5453
* fix: install playwright browsers in nix flake by @dastarruer in https://github.com/readest/readest/pull/5454
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5458
* feat(about): copy the version label to the clipboard on click by @chrox in https://github.com/readest/readest/pull/5461
* fix(epub): parse OPF items and meta written with explicit closing tags by @chrox in https://github.com/readest/readest/pull/5463
* feat(annotator): add an opt-in Copy Link tool to the selection toolbar by @chrox in https://github.com/readest/readest/pull/5464
* feat(reader): tap the footer to show and dismiss the progress bar by @chrox in https://github.com/readest/readest/pull/5466
* fix(settings): drop the "Show" prefix from the footer widget labels by @chrox in https://github.com/readest/readest/pull/5469
* fix(library): render the book context menu in-app on Linux desktop by @chrox in https://github.com/readest/readest/pull/5467
* fix(sync): gate dictionary preferences on the Dictionaries toggle by @chrox in https://github.com/readest/readest/pull/5470
* fix(opds): use the cover advertised by the feed entry by @chrox in https://github.com/readest/readest/pull/5471
* feat(reader): show the image description in the image viewer by @chrox in https://github.com/readest/readest/pull/5472
* feat(library): give the "Then by" sort its own order, closes #5119 by @chrox in https://github.com/readest/readest/pull/5474
* fix(linux): explain the missing file picker in SteamOS Gaming Mode by @chrox in https://github.com/readest/readest/pull/5475
* fix(opds): apply the metadata advertised by the feed entry by @chrox in https://github.com/readest/readest/pull/5477
* fix(reader): stop the header hover strip from covering the page text by @chrox in https://github.com/readest/readest/pull/5478
* fix(reader): keep the aspect ratio of duokan fullscreen covers by @chrox in https://github.com/readest/readest/pull/5473
* fix(sync): handle OneDrive OAuth callbacks by @ChuwuYo in https://github.com/readest/readest/pull/5479
* feat(tts): play a book's own recorded narration (EPUB 3 Media Overlays) by @cubicruler in https://github.com/readest/readest/pull/5480
* fix(android): correct the package name in the native-tts unit test by @chrox in https://github.com/readest/readest/pull/5484
* feat(reader): horizontal scrolling mode for fixed layout books by @chrox in https://github.com/readest/readest/pull/5485
* feat(bookorbit): add BookOrbit integration with annotations, bookmarks, stats, and status sync by @chrox in https://github.com/readest/readest/pull/5487
* fix(library): select books in the recently read shelf and pull it with the grid by @chrox in https://github.com/readest/readest/pull/5486
* fix(library): make search history chips translucent like the search input by @chrox in https://github.com/readest/readest/pull/5488
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5489
* fix(reader): correct reading ruler transitions and line bounds by @ChuwuYo in https://github.com/readest/readest/pull/5490
* feat(reader): support adding bookmarks with a pull-down gesture by @chrox in https://github.com/readest/readest/pull/5493
* fix(opds): invalidate cached covers when the entry's updated value changes by @chrox in https://github.com/readest/readest/pull/5495
* fix(db): close only the target connection when closing a native database by @chrox in https://github.com/readest/readest/pull/5497
* fix(build): strip dangling sourceMappingURL comments from Tauri builds by @chrox in https://github.com/readest/readest/pull/5498
* fix(reader): style annotation toolbar customizer and flatten popup chrome by @dastarruer in https://github.com/readest/readest/pull/5496
* fix(opds): substitute percent-encoded {searchTerms} in OpenSearch templates (#5500) by @chrox in https://github.com/readest/readest/pull/5504
* fix(reader): render fixed layout documents edge to edge in scrolled mode by @chrox in https://github.com/readest/readest/pull/5503
* fix(auth): make the password sign-in form work with Android password managers by @chrox in https://github.com/readest/readest/pull/5505
* fix(koplugin): keep book metadata hash consistent with Readest by @chrox in https://github.com/readest/readest/pull/5508
* fix(koplugin): guard nil response on login/OTP failure by @jemyzhang in https://github.com/readest/readest/pull/5507
* feat(reader): support Apple Pencil double tap and squeeze as page turners by @chrox in https://github.com/readest/readest/pull/5511
* feat(send): clip locally opened html and xhtml pages with the browser extension by @chrox in https://github.com/readest/readest/pull/5512
* chore(deps): bump transitive dependencies for security advisories by @chrox in https://github.com/readest/readest/pull/5518
* fix(library): stop watched-folder scans from blocking the main thread by @chrox in https://github.com/readest/readest/pull/5517
* fix(reader): keep the reading ruler anchored to its text across repagination by @chrox in https://github.com/readest/readest/pull/5519
* test(reader): deflake DictionarySheet expand/collapse toggle test by @chrox in https://github.com/readest/readest/pull/5521
* feat(library): show the page count in book details (#5516) by @chrox in https://github.com/readest/readest/pull/5523
* feat(reader): jump to an entered page number from the progress label by @chrox in https://github.com/readest/readest/pull/5524
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5525
* fix(annotator): return to the selection toolbar after closing a lookup popup (#5213) by @ChuwuYo in https://github.com/readest/readest/pull/5526
* fix(kosync): stop re-prompting resolved sync conflicts on window re-activation (#5527) by @chrox in https://github.com/readest/readest/pull/5528
* fix(annotator): fall back to the selection toolbar when the dictionary quick action gets a multi-word selection by @chrox in https://github.com/readest/readest/pull/5529
* fix(android): deliver file picker results via a replayable plugin event by @chrox in https://github.com/readest/readest/pull/5531
* chore(deps): bump the github-actions group with 5 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5530
* feat(sync): support iCloud as a cloud sync provider on iOS and macOS by @chrox in https://github.com/readest/readest/pull/5532
* fix(reader): discard booknotes without a CFI to prevent an app crash by @chrox in https://github.com/readest/readest/pull/5533
* fix(tts): settle Edge TTS synthesis when the Tauri WebSocket dies before turn.end by @chrox in https://github.com/readest/readest/pull/5534
* fix(ios): restore Open With file associations by @chrox in https://github.com/readest/readest/pull/5535
* feat(macos): enable iCloud sync in direct-distribution builds by @chrox in https://github.com/readest/readest/pull/5537
* fix(window): avoid unavailable title-bar APIs on mobile by @chrox in https://github.com/readest/readest/pull/5536
* fix(annotator): re-anchor the note bubble when a highlight is resized (#5538) by @chrox in https://github.com/readest/readest/pull/5541
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5543
* feat(user): add a Danger Zone with Delete All Books by @chrox in https://github.com/readest/readest/pull/5542
* fix(iap): consume Google Play one-time purchases so storage add-ons can be repurchased by @chrox in https://github.com/readest/readest/pull/5545
* feat(tts): speak Japanese ruby readings instead of the base kanji by @chrox in https://github.com/readest/readest/pull/5546
* feat(a11y): name the open book in the window title by @chrox in https://github.com/readest/readest/pull/5547
* fix(rsvp): respect safe area insets in landscape by @chrox in https://github.com/readest/readest/pull/5548
* fix(layout): keep code block indentation when overriding book layout by @chrox in https://github.com/readest/readest/pull/5549
* fix(docker): apply db migrations on first boot and let the font CDN be overridden (#5550) by @chrox in https://github.com/readest/readest/pull/5551
* fix(reader): scrolled-mode toggle fallout, proofread and footer chrome by @chrox in https://github.com/readest/readest/pull/5552
* fix(translate): restore Azure Translator, keep paragraph layout, preserve inline formatting by @chrox in https://github.com/readest/readest/pull/5555
* fix(reader): keep the cursor visible while text is selected by @chrox in https://github.com/readest/readest/pull/5557
* feat(translate): preserve inline formatting with Google too by @chrox in https://github.com/readest/readest/pull/5556
* fix(annotator): draw the highlight color check in the content color by @chrox in https://github.com/readest/readest/pull/5564
* fix(tts): keep the WebView alive while paused so Bluetooth Play resumes (#5561) by @chrox in https://github.com/readest/readest/pull/5567
* chore(store): rebuild store listings and manage them from fastlane by @chrox in https://github.com/readest/readest/pull/5573
* chore(store): replace Play listing images instead of appending by @chrox in https://github.com/readest/readest/pull/5574
* feat(reader): render math in annotation notes by @PolybiusPro in https://github.com/readest/readest/pull/5571
* feat(reader): summarize annotation counts in the sidebar toolbar by @chrox in https://github.com/readest/readest/pull/5576
* Add support for Custom HTTP Headers in Kosync/BookOrbit integrations  by @heckler1 in https://github.com/readest/readest/pull/5570
* docs: update screenshots, closes #5368 by @chrox in https://github.com/readest/readest/pull/5577
* fix(tts): play Media Overlay narration via native AVPlayer on iOS by @Juansero29 in https://github.com/readest/readest/pull/5562
* fix: highlight swatch colors, window set-title ACL, and debug-build Sentry DSN by @chrox in https://github.com/readest/readest/pull/5578
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5579
* fix: fix occasional stuck when dismissing bookshelf menu by @chrox in https://github.com/readest/readest/pull/5580
* release: version 0.12.1 by @chrox in https://github.com/readest/readest/pull/5581

## New Contributors
* @LukashevychAndrii made their first contribution in https://github.com/readest/readest/pull/5302
* @liyafly made their first contribution in https://github.com/readest/readest/pull/5333
* @alexander-pecheny made their first contribution in https://github.com/readest/readest/pull/5292
* @bcrave made their first contribution in https://github.com/readest/readest/pull/5247
* @shahram7 made their first contribution in https://github.com/readest/readest/pull/5361
* @nurumubu made their first contribution in https://github.com/readest/readest/pull/5355
* @fix2015 made their first contribution in https://github.com/readest/readest/pull/5370
* @cubicruler made their first contribution in https://github.com/readest/readest/pull/5480
* @jemyzhang made their first contribution in https://github.com/readest/readest/pull/5507
* @PolybiusPro made their first contribution in https://github.com/readest/readest/pull/5571
* @heckler1 made their first contribution in https://github.com/readest/readest/pull/5570
* @Juansero29 made their first contribution in https://github.com/readest/readest/pull/5562

**Full Changelog**: https://github.com/readest/readest/compare/v0.11.20...v0.12.1

# v0.11.20

## Release Highlight
* Text-to-Speech: Read-aloud voices can now be downloaded per book for offline listening, and adjustable pauses between sentences and paragraphs
* Text-to-Speech: Added CarPlay support on iOS and more reliable Android Auto controls so you can listen while driving
* Sync: Added OneDrive as a cloud provider, you can now sync to several providers at once
* Reading: Added a right-edge swipe to change Auto Scroll speed, footnotes in Markdown books, and copying text now keeps its paragraph breaks
* Reading: Smoother page-turn animations, steadier text selection on iOS, and a redesigned custom theme editor that stays readable on mobile
* Annotations: You can now copy a highlight or note together with a deep link that jumps straight back to its spot in the book
* Library: You can now sort and filter your shelf by time remaining, and the Recently Read shelf and widget show only books you're currently reading
* PDF: Fixed a crash that could happen when turning pages or zooming large PDFs on iOS
* More: Fixed OPDS catalogs disappearing after a restart, and improved 32-bit Android stability

## What's Changed
* fix: Sentry high-priority crash batch (autoscroll, TTS, MOBI, book-open, PDF links) by @chrox in https://github.com/readest/readest/pull/5012
* docs: move source build instructions to CONTRIBUTING.md by @dastarruer in https://github.com/readest/readest/pull/5017
* fix(sentry): repair open-with crash-reporter arg and drop benign noise by @chrox in https://github.com/readest/readest/pull/5014
* fix(transfer): stop the progress render storm (READEST-2, max update depth) by @chrox in https://github.com/readest/readest/pull/5015
* fix: media-session teardown race + page_stat view migration idempotency by @chrox in https://github.com/readest/readest/pull/5019
* chore: add zed-editor support by @dastarruer in https://github.com/readest/readest/pull/5026
* chore(deps): bump the github-actions group with 9 updates by @dependabot[bot] in https://github.com/readest/readest/pull/5031
* fix(reader): guard foliate paginator null-document crashes (READEST-1H, 2X) by @chrox in https://github.com/readest/readest/pull/5020
* fix(reader): guard applyMarginAndGap against a torn-down view (READEST-2V) by @chrox in https://github.com/readest/readest/pull/5022
* fix(updater): never throw from an auto update check (READEST-J, READEST-22) by @chrox in https://github.com/readest/readest/pull/5028
* feat(sentry): upload browser source maps for symbolicated JS crashes by @chrox in https://github.com/readest/readest/pull/5027
* Footer obstruction fix by @bincent0929 in https://github.com/readest/readest/pull/5029
* fix(android): remove Android Auto opt-in from manifest to unblock Play review by @chrox in https://github.com/readest/readest/pull/5038
* feat(reader): subscribe to RSS/Atom/JSON feeds as periodical feed books by @chrox in https://github.com/readest/readest/pull/5039
* fix: add backticks to docstring for proper formatting by @dastarruer in https://github.com/readest/readest/pull/5040
* feat(sync): add Microsoft OneDrive as a cloud sync provider by @chrox in https://github.com/readest/readest/pull/5048
* chore(style): unified info bar font style by @chrox in https://github.com/readest/readest/pull/5045
* feat(sync): sync S3 config + credentials cross-device, fix backup leak of device-local fields by @chrox in https://github.com/readest/readest/pull/5051
* fix: fix malformed code block in docs by @dastarruer in https://github.com/readest/readest/pull/5059
* fix(opds): fix logic for temporary destination filename (#5024) by @chloeroform in https://github.com/readest/readest/pull/5058
* feat: add nicer issue templates by @dastarruer in https://github.com/readest/readest/pull/5060
* refactor: rename ColorPanel to ThemePanel by @dastarruer in https://github.com/readest/readest/pull/5042
* feat(tts): make inter-sentence and inter-paragraph gaps configurable by @muvox in https://github.com/readest/readest/pull/5057
* fix(android): reliable Android Auto media controls by @chrox in https://github.com/readest/readest/pull/5066
* feat(settings): Increase margin upper bounds by @GoatDamn-dev in https://github.com/readest/readest/pull/5071
* fix: only open last book if book is not marked as finished by @dastarruer in https://github.com/readest/readest/pull/5072
* feat(ios): CarPlay support and native TTS playout with Now Playing integration by @chrox in https://github.com/readest/readest/pull/5085
* fix(dictionary): let a web search entry lead the popup when it is first in the configured order by @chrox in https://github.com/readest/readest/pull/5086
* fix(sync): keep the cloud copy when deleting a book from the device only (#5084) by @chrox in https://github.com/readest/readest/pull/5087
* fix(android): stop 32-bit ARM builds aborting at launch (#5070) by @chrox in https://github.com/readest/readest/pull/5089
* fix(kosync): accept pulled progress from servers that omit document by @chrox in https://github.com/readest/readest/pull/5090
* fix(macos): skip the minidump handler in sandboxed App Store builds by @chrox in https://github.com/readest/readest/pull/5091
* feat(markdown): render footnotes in .md books (#5074) by @chrox in https://github.com/readest/readest/pull/5095
* fix(sync): carry reading progress onto the shelf row in file sync by @chrox in https://github.com/readest/readest/pull/5096
* chore(zed): enable typescript type checking across entire codebase by @dastarruer in https://github.com/readest/readest/pull/5098
* feat(sorting): add toggle to filter by time remaining by @dastarruer in https://github.com/readest/readest/pull/5079
* fix(i18n): merge the split cloud provider tip into one key by @chrox in https://github.com/readest/readest/pull/5102
* fix(epub): load chapters whose zip entry name needs percent-encoding by @chrox in https://github.com/readest/readest/pull/5100
* feat(koplugin): bind full annotation sync to a gesture, upload the open book by @chrox in https://github.com/readest/readest/pull/5106
* fix(sentry): stop the crash reporter booting a second copy of the app (#5052) by @chrox in https://github.com/readest/readest/pull/5107
* fix(reader): remove long-press to zoom images and tables by @chrox in https://github.com/readest/readest/pull/5108
* fix(android): give each gallery image its own name and report insert failures by @chrox in https://github.com/readest/readest/pull/5109
* fix(library): keep demo books out of the cloud book channel (#5049) by @chrox in https://github.com/readest/readest/pull/5110
* fix(sentry): drop the minidump crash reporter, it re-execs our own binary by @chrox in https://github.com/readest/readest/pull/5112
* fix(settings): keep the screen awake only while reading (#5104) by @chrox in https://github.com/readest/readest/pull/5113
* fix(sync): verify the sync passphrase and make a wrong one recoverable by @chrox in https://github.com/readest/readest/pull/5115
* fix(kosync): resolve element-offset XPointers and isolate percentage drift anchor to KOReader by @adagues in https://github.com/readest/readest/pull/5111
* fix(tts): use more intuitive icons in tts player by @dastarruer in https://github.com/readest/readest/pull/5117
* fix(opds): normalize XML MIME types by @yozlog in https://github.com/readest/readest/pull/5120
* fix(opds): escape malformed XML in proxy by @yozlog in https://github.com/readest/readest/pull/5121
* feat(sync): allow syncing to multiple providers at once (#5062) by @chrox in https://github.com/readest/readest/pull/5122
* feat(tts): persistent per-book audio cache with offline downloads by @chrox in https://github.com/readest/readest/pull/5126
* perf(sync): drop redundant deleted_at OR from stats pull cursor by @chrox in https://github.com/readest/readest/pull/5127
* fix(pdf): prevent iOS WebContent OOM crash on PDF page turn and zoom (#5118) by @chrox in https://github.com/readest/readest/pull/5129
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5130
* fix(deploy): restore webpack build so the Cloudflare worker fits 64 MiB by @chrox in https://github.com/readest/readest/pull/5136
* fix: change dictionary icon by @dastarruer in https://github.com/readest/readest/pull/5135
* chore(deps): bump actions/setup-node from 6.4.0 to 7.0.0 in the github-actions group by @dependabot[bot] in https://github.com/readest/readest/pull/5138
* fix: fix param name typo by @dastarruer in https://github.com/readest/readest/pull/5145
* fix(tts): keep Android system TTS reading with the screen locked (#4408) by @chrox in https://github.com/readest/readest/pull/5146
* fix(tts): show mini player immediately and keep it above bottom bar and footer by @chrox in https://github.com/readest/readest/pull/5144
* fix(sync): create Google Drive files atomically to stop stranding "Untitled" files in the Drive root by @chrox in https://github.com/readest/readest/pull/5150
* fix(sync): sync WebDAV server URL for configured-but-disabled providers (#5141) by @chrox in https://github.com/readest/readest/pull/5149
* test(tts): stop detached speak loops so no state dispatch escapes teardown by @chrox in https://github.com/readest/readest/pull/5151
* docs(design): default primary buttons to btn-contrast, reserve btn-primary for CTAs by @chrox in https://github.com/readest/readest/pull/5155
* chore: replace outdated `react-color` package with `react-colorful` by @dastarruer in https://github.com/readest/readest/pull/5128
* feat: redesign custom theme creation menu by @dastarruer in https://github.com/readest/readest/pull/5152
* chore: gate rust_lint on src-tauri changes and drop redundant btn-primary in WordLens by @chrox in https://github.com/readest/readest/pull/5156
* fix(layout): items overlap in footer on Android phone (#5004) by @gojodennis in https://github.com/readest/readest/pull/5158
* feat(tts): add 0.8x and 0.85x tts speech speed presets by @gojodennis in https://github.com/readest/readest/pull/5157
* fix(reader): return the turn promise from the captured view.next/prev wrappers by @chrox in https://github.com/readest/readest/pull/5159
* fix(reader): do not toggle bars on vertical pan swipes over fixed-layout pages by @chrox in https://github.com/readest/readest/pull/5160
* fix(payment): stop Google Play RTDN fallback from downgrading paying subscribers by @chrox in https://github.com/readest/readest/pull/5163
* feat(tts): refine the TTS player sheet and redesign the mini player by @chrox in https://github.com/readest/readest/pull/5162
* feat(tts): add mini player Player Style (full/minimal); keep Tauri off the edge proxy by @chrox in https://github.com/readest/readest/pull/5170
* feat(annotator): copy a highlight or note with its deep link by @chrox in https://github.com/readest/readest/pull/5171
* fix(transfer): stop bulk cloud uploads from freezing the library (#5047) by @chrox in https://github.com/readest/readest/pull/5172
* fix(library): anchor the native context menu popup at the pointer position by @chrox in https://github.com/readest/readest/pull/5182
* refactor: create primitive `Toggle` component by @dastarruer in https://github.com/readest/readest/pull/5173
* fix(reader): stop vertical swipes from turning or flashing the layered slide by @chrox in https://github.com/readest/readest/pull/5185
* fix(reader): stabilize iOS text selection with instant highlight and captured page turns by @chrox in https://github.com/readest/readest/pull/5184
* fix(koplugin): fix auto-sync push crash and UI-thread block on book open/close (#5006) by @chrox in https://github.com/readest/readest/pull/5186
* fix(ios): keep the App Group on the widget and share extensions in App Store builds by @chrox in https://github.com/readest/readest/pull/5188
* fix(opds): restore Calibre pipe-escaped commas in author names and join authors with & by @chrox in https://github.com/readest/readest/pull/5189
* perf(test): reduce unit test runtime by @chrox in https://github.com/readest/readest/pull/5190
* fix(opds): keep re-added catalogs from vanishing after app restart by @chrox in https://github.com/readest/readest/pull/5191
* test: remove redundant cases and silence passing logs by @chrox in https://github.com/readest/readest/pull/5192
* feat: use shorter quote in theme preview by @dastarruer in https://github.com/readest/readest/pull/5197
* fix(reader): keep the side panel resize handle from sticking over PDF pages by @chrox in https://github.com/readest/readest/pull/5198
* fix(library): keep the select-mode action bar from hiding the last book by @chrox in https://github.com/readest/readest/pull/5200
* feat: improve accuracy of time remaining calculation by @dastarruer in https://github.com/readest/readest/pull/5194
* fix(library): show only currently-reading books on recent shelf and widget by @chrox in https://github.com/readest/readest/pull/5201
* fix(reader): preserve paragraph breaks when copying text by @chrox in https://github.com/readest/readest/pull/5202
* feat(updater): show original text for auto-translated release notes by @chrox in https://github.com/readest/readest/pull/5203
* fix(reader): synchronize toolbar with layered page turns by @chihumyum in https://github.com/readest/readest/pull/5179
* ci(release): publish Send to Readest extension zip by @chrox in https://github.com/readest/readest/pull/5204
* fix(reader): support offline dictionary pronunciation by @chrox in https://github.com/readest/readest/pull/5205
* feat(reader): add right-edge swipe to adjust auto scroll speed by @chrox in https://github.com/readest/readest/pull/5206
* fix(applock): hide PIN entry while the biometric sheet is on screen by @chrox in https://github.com/readest/readest/pull/5207
* fix(reader): draw the theme background on the curl back face by @chrox in https://github.com/readest/readest/pull/5208
* chore: update agent memories by @chrox in https://github.com/readest/readest/pull/5209
* fix(reader): gate concurrent programmatic captured page turns by @chrox in https://github.com/readest/readest/pull/5211
* fix(reader): make the custom theme editor readable on mobile by @chrox in https://github.com/readest/readest/pull/5212
* fix(reader): keep TTS media session and volume control with volume-key paging by @chrox in https://github.com/readest/readest/pull/5218
* fix(reader): keep captured turns aligned with the finger by @chihumyum in https://github.com/readest/readest/pull/5217
* fix(ios): re-attach App Group to widget/share extensions in App Store builds by @chrox in https://github.com/readest/readest/pull/5219
* release: version 0.11.20 by @chrox in https://github.com/readest/readest/pull/5220

## New Contributors
* @bincent0929 made their first contribution in https://github.com/readest/readest/pull/5029
* @chloeroform made their first contribution in https://github.com/readest/readest/pull/5058
* @muvox made their first contribution in https://github.com/readest/readest/pull/5057
* @GoatDamn-dev made their first contribution in https://github.com/readest/readest/pull/5071
* @adagues made their first contribution in https://github.com/readest/readest/pull/5111
* @yozlog made their first contribution in https://github.com/readest/readest/pull/5120
* @gojodennis made their first contribution in https://github.com/readest/readest/pull/5158
* @chihumyum made their first contribution in https://github.com/readest/readest/pull/5179

**Full Changelog**: https://github.com/readest/readest/compare/v0.11.18...v0.11.20

# v0.11.18

## Release Highlight
* Reading: Added Auto Scroll, a hands-free mode that scrolls the page for you at an adjustable pace, plus middle-click autoscroll on the desktop
* Reading: Added slide and page-curl animations when turning pages for a more natural feel
* Reading: Fixed page turning and the reading ruler for vertical right-to-left books, PDF text selection when system font scaling is on, and header/footer readability over light PDFs in dark mode
* Text-to-Speech: Redesigned read-aloud as a mini player with an expandable full player, and playback now keeps going even after you close the book
* Text-to-Speech: Online voices now play gap-free with chapter seeking and lock-screen controls, plus Android Auto support so you can listen in the car
* Sync: Added S3-compatible cloud storage and a new Cloud Sync screen to choose and switch between your sync providers
* Integrations: Added a Calibre plugin to push books and custom columns into Readest, and improved OPDS sign-in and auto-download for self-hosted catalogs
* Library: New books dropped into watched folders now import automatically, and you can sort your shelf by reading progress
* More: Added a speak button in the dictionary popup, a cleaner theme switcher, and per-rule toggles for proofreading

## What's Changed
* fix(reader): remember last read position for markdown files by @chrox in https://github.com/readest/readest/pull/4871
* fix(layout): respect author vertical-align on inline images (#4866) by @chrox in https://github.com/readest/readest/pull/4878
* fix(reader): fix fixed-layout spread spine seam and zoomed-out blank page (#4857) by @chrox in https://github.com/readest/readest/pull/4873
* fix(reader): correct reading ruler direction for vertical-rl books (#4865) by @chrox in https://github.com/readest/readest/pull/4879
* chore(deps): bump the github-actions group with 5 updates by @dependabot[bot] in https://github.com/readest/readest/pull/4884
* feat(proofread): editable Find pattern and per-rule enable/disable toggle (#4859) by @chrox in https://github.com/readest/readest/pull/4888
* fix(android): avoid black screen when external cache dir is unavailable by @chrox in https://github.com/readest/readest/pull/4889
* fix(macos): minimize instead of hide on macOS 26 to avoid black window (#4875) by @chrox in https://github.com/readest/readest/pull/4890
* fix(ios): keep App Group entitlement on widget/share extensions in App Store builds by @chrox in https://github.com/readest/readest/pull/4891
* fix(sync): WebDAV upload-after-enable and deletion propagation (#4856, #4860) by @chrox in https://github.com/readest/readest/pull/4892
* feat(library): add "Progress Read" sort option (#4427) by @chrox in https://github.com/readest/readest/pull/4893
* fix(auth): surface OAuth callback errors on desktop deeplink (#4881) by @chrox in https://github.com/readest/readest/pull/4894
* fix(ios): release screen brightness on background so auto-brightness resumes (#4885) by @chrox in https://github.com/readest/readest/pull/4896
* fix(koplugin): fold duplicate stats book rows so synced time shows in KOReader by @chrox in https://github.com/readest/readest/pull/4895
* fix(updater): disable in-app updater on non-AppImage Linux (#4874) by @chrox in https://github.com/readest/readest/pull/4897
* fix(reader): apply page margin changes live on all platforms (#4898) by @chrox in https://github.com/readest/readest/pull/4900
* fix(reader): turn pages horizontally for vertical-rl books (#624) by @chrox in https://github.com/readest/readest/pull/4899
* fix(window): enter fullscreen from maximized windows (#4034) by @chrox in https://github.com/readest/readest/pull/4903
* fix(window): keep Linux window opaque so it can't turn invisible (#3682) by @chrox in https://github.com/readest/readest/pull/4904
* feat(android): Android Auto media support for TTS playback by @chrox in https://github.com/readest/readest/pull/4907
* ci(nightly): fix nightly update detection broken by AppImage bundling hang by @chrox in https://github.com/readest/readest/pull/4909
* feat(library): auto-import new books from watched folders (#3889) by @chrox in https://github.com/readest/readest/pull/4902
* fix(reader): open annotation deep link when a different book is open (#4887) by @chrox in https://github.com/readest/readest/pull/4910
* fix(reader): keep running header/footer readable over light PDFs in dark mode (#4901) by @chrox in https://github.com/readest/readest/pull/4911
* fix(reader): distinguish two-finger scroll from pinch-zoom on touchscreens (#4858) by @chrox in https://github.com/readest/readest/pull/4912
* feat(settings): redesign theme mode toggle as a segmented control (#4831) by @chrox in https://github.com/readest/readest/pull/4913
* feat(sentry): add crash reporting for Android, iOS, desktop, and web by @chrox in https://github.com/readest/readest/pull/4914
* fix(ios): stop share extension hijacking shared .txt files by @chrox in https://github.com/readest/readest/pull/4917
* fix(test): make Android double-tap e2e pass on default-config CI devices by @chrox in https://github.com/readest/readest/pull/4921
* fix(nix): get nix devshell working by @dastarruer in https://github.com/readest/readest/pull/4883
* feat(calibre): add Readest calibre plugin to push books and metadata by @chrox in https://github.com/readest/readest/pull/4918
* fix(turso): bump plugin submodule to serialize connection operations by @chrox in https://github.com/readest/readest/pull/4927
* feat(koplugin): pull sync on device wake with book open by @chrox in https://github.com/readest/readest/pull/4928
* fix: Sentry production hardening (release/OS tags, unhandled-rejection & render-loop guards) by @chrox in https://github.com/readest/readest/pull/4929
* fix: change formatter to nixpkgs-fmt by @dastarruer in https://github.com/readest/readest/pull/4932
* feat(tts): gapless Web Audio playback engine for Edge TTS with chapter timeline and seek by @chrox in https://github.com/readest/readest/pull/4931
* feat(tts): keep TTS playing when the book is closed by @chrox in https://github.com/readest/readest/pull/4941
* fix(koplugin): key library pull cursor on synced_at to stop stale library (#4934) by @chrox in https://github.com/readest/readest/pull/4944
* feat(metadata): surface calibre custom columns from EPUB metadata by @chrox in https://github.com/readest/readest/pull/4939
* fix(sync): propagate group membership for already-synced books (#4942) by @chrox in https://github.com/readest/readest/pull/4946
* fix: real fix for library-save storage-permission crash + narrowed view-transition filter by @chrox in https://github.com/readest/readest/pull/4943
* fix(transfer): persist queue when clearing completed/failed/all by @chrox in https://github.com/readest/readest/pull/4947
* fix(opds): crawl subdirectories when auto-downloading directory-style catalogs by @chrox in https://github.com/readest/readest/pull/4948
* fix(widget): round iOS cover thumbnail size to whole pixels by @chrox in https://github.com/readest/readest/pull/4950
* feat(reader): slide and page curl turn animations (#555) by @chrox in https://github.com/readest/readest/pull/4940
* fix(reader): open books without a View Transition to avoid timeout (READEST-9) by @chrox in https://github.com/readest/readest/pull/4949
* feat(sentry): tag events with the WebView engine and version by @chrox in https://github.com/readest/readest/pull/4952
* feat(reader): middle mouse button autoscroll in scrolled mode by @chrox in https://github.com/readest/readest/pull/4955
* feat(reader): add TTS speak button to dictionary popup (#4876) by @chrox in https://github.com/readest/readest/pull/4957
* chore(agent): update agent memories by @chrox in https://github.com/readest/readest/pull/4958
* fix(reader): fix PDF text selection misplaced by OS font scaling (#49) by @chrox in https://github.com/readest/readest/pull/4960
* fix: more production crashes (View Transition noise, book-dir race, stats transaction) by @chrox in https://github.com/readest/readest/pull/4962
* fix(sync): decouple Readest Cloud storage quota from third-party cloud sync by @chrox in https://github.com/readest/readest/pull/4971
* feat(sync): propagate tags and reading status through third-party file sync by @chrox in https://github.com/readest/readest/pull/4973
* perf(koplugin): defer and cache Library group covers (#4954) by @chrox in https://github.com/readest/readest/pull/4974
* feat(sync): route library sync exclusively to the selected cloud provider by @chrox in https://github.com/readest/readest/pull/4975
* feat(settings): unified Cloud Sync chooser with Readest Cloud as a first-class provider by @chrox in https://github.com/readest/readest/pull/4976
* test(reader): harden fixed-layout wheel double-scroll test against CI flake by @chrox in https://github.com/readest/readest/pull/4978
* fix(sync): abort the file-sync run on auth failure instead of marching the library by @chrox in https://github.com/readest/readest/pull/4981
* chore(i18n): translate the cloud sync provider-selection strings by @chrox in https://github.com/readest/readest/pull/4980
* feat(sync): incremental file sync and per-book transfers for the active provider by @chrox in https://github.com/readest/readest/pull/4982
* fix(reader): gate route View Transitions on API support (READEST-9) by @chrox in https://github.com/readest/readest/pull/4989
* feat(sync): S3-compatible cloud sync provider by @chrox in https://github.com/readest/readest/pull/4990
* fix(reader): center the lone PDF page in portrait auto-spread (#4984) by @chrox in https://github.com/readest/readest/pull/4992
* fix(android): background TTS media controls + lock-screen scrubber/seek + Edge click fix by @chrox in https://github.com/readest/readest/pull/4994
* feat(reader): redesign the TTS control as a mini player with an expandable player sheet by @chrox in https://github.com/readest/readest/pull/4996
* feat(reader): Auto Scroll reading mode for scrolled flow by @chrox in https://github.com/readest/readest/pull/4999
* fix(reader): gate captured slide/curl turn on scrollLocked like push by @chrox in https://github.com/readest/readest/pull/5000
* fix(reader): let page margins shrink into the safe-area inset (#4761) by @chrox in https://github.com/readest/readest/pull/5001
* fix(opds): auth negotiation and auto-download fixes for self-hosted catalogs by @chrox in https://github.com/readest/readest/pull/5002
* release: version 0.11.18 by @chrox in https://github.com/readest/readest/pull/5003

## New Contributors
* @dastarruer made their first contribution in https://github.com/readest/readest/pull/4883

**Full Changelog**: https://github.com/readest/readest/compare/v0.11.17...v0.11.18

# v0.11.17

## Release Highlight
* Sync: Added WebDAV and Google Drive sync for your books and reading data
* Widgets: Added home-screen reading widgets on mobile so you can jump straight back into your book
* Reading: You can now open and read Markdown(.md) files
* Reading: You can select a word by double-clicking it, and search gained regex and nearby-words modes
* Reading: Added a sticky progress bar with chapter markers, and keyboard shortcuts to fine-tune text selection
* Library: Added a Recently Read shelf to quickly pick up where you left off, plus a separate background texture for your library
* Text-to-Speech: Added offline voices on iOS, a setting to highlight by word or by sentence
* PDF: Smoother pinch-zoom and panning, faster scrolling on mobile, and a new contrast option in the view menu
* More: Customize the highlight toolbar across all books, filter exported annotations by color and style

## What's Changed
* fix(widget): avoid recycling aliased source bitmap for 2:3 covers by @chrox in https://github.com/readest/readest/pull/4850
* ci(release): add GitHub artifact attestation to release and nightly builds by @chrox in https://github.com/readest/readest/pull/4851
* release: version 0.11.17 (hotfix for an Android crash) by @chrox in https://github.com/readest/readest/pull/4852


**Full Changelog**: https://github.com/readest/readest/compare/v0.11.16...v0.11.17
