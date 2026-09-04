# 1.3.1

##### Plugin
- Add an "Automatically link by provider identifier" setting, which takes priority over ISBN and title+author matching when auto-linking a book: Goodreads via a `goodreads:<id>` metadata tag, Hardcover via its existing `hardcover:`/`hardcover-edition:` tags, StoryGraph via its existing `storygraph:`/`storygraph-edition:` tags. New auto-link priority order is identifier -> ISBN -> title+author. Fable has no matching identifier scheme yet.


---

Full changelog: [CHANGELOG.md](https://github.com/Lyfts/ShelfSync/blob/main/CHANGELOG.md#131)

# 1.3.0

##### Plugin
- Add Fable sync support alongside StoryGraph, Hardcover, and Goodreads (linking, progress/note updates, and background sync), using Fable's official API. Unlike the other services, Fable has a real login API, so the plugin logs in directly with your Fable email and password rather than a cookie/token fetched by hand — see the README's Fable authentication section, including a note for accounts that signed up via Google/Apple.
- The StoryGraph, Hardcover, Goodreads, and Fable sub-menus are now combined into a single **Providers** sub-menu (previously listed directly under ShelfSync), and **Common settings** is renamed to **Settings**.


---

Full changelog: [CHANGELOG.md](https://github.com/Lyfts/ShelfSync/blob/main/CHANGELOG.md#130)

# 1.2.1

##### Plugin
- Add an "Enabled" toggle to each service's menu (StoryGraph, Hardcover, Goodreads), on by default. Turning it off fully pauses that service — no linking, syncing, or other actions — without losing your saved cookie/API token, and turning it back on resumes right where it left off. A service is now also treated as off until you've actually saved a cookie/token for it, instead of quietly trying (and failing) in the background.


---

Full changelog: [CHANGELOG.md](https://github.com/Lyfts/ShelfSync/blob/main/CHANGELOG.md#121)

# 1.2.0

## 🍪 Goodreads cookies can now refresh themselves (with a little help)
Goodreads sessions periodically go stale from an AWS WAF bot-challenge on Goodreads' side - until now, that meant syncing just paused until you repasted a fresh cookie by hand. This release adds an optional way to automate that entirely.

[goodreads-cookie-refresher](https://github.com/Lyfts/goodreads-cookie-refresher) is a small, self-hosted Docker setup that keeps a real logged-in browser session alive on your network and hands the plugin a fresh cookie automatically — both for first-time setup and every time the saved cookie goes stale.

See [CHANGELOG.md](https://github.com/Lyfts/ShelfSync/blob/main/CHANGELOG.md#120) for changes in this release.

# 1.1.2

See [CHANGELOG.md](https://github.com/Lyfts/ShelfSync/blob/main/CHANGELOG.md#112) for changes in this release.
