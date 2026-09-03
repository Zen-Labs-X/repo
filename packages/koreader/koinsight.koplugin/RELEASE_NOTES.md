# v0.2.3

# ❗ KoInsight Github Organization

The KoInsight project now has its own Github Organization - github.com/Ko-Insight! This will enable us to bring in more collaborators and ensure the project lives on.

> [!CAUTION]
> The KoInsight docker image now lives at [ghcr.io/ko-insight/koinsight](https://ghcr.io/ko-insight/koinsight)! Make sure to update your compose files :)

# Changes

- Add button to show hidden books when no books are available - #122 by @binarymelon

# v0.2.2

# 🚨 Bugfix
- Fixes a bug where importing highlights for a book would mark all highlights for all other bugs as deleted 😅 (#87 

# ✨ Improvements

### Change book cover
Changing book cover has moved. Hover over the cover and click the edit button:

<img width="734" height="321" alt="image" src="https://github.com/user-attachments/assets/04ac9772-e91a-4d4d-a238-888a594f56f5" />

---

### Improved book statistics
Improved the visuals of the book statistics card

<img width="571" height="268" alt="image" src="https://github.com/user-attachments/assets/3af85004-7cb2-44e2-994d-5e85a1e263c9" />

---

### Hidden Raw data
Raw data and book reload are now hidden in an "Advanced" dropdown menu:

<img width="277" height="172" alt="image" src="https://github.com/user-attachments/assets/93838dbc-77d7-45ce-b0ab-7294fa7624d5" />

# v0.2.1

For v0.2 changes, [click here](https://github.com/GeorgeSG/KoInsight/releases/tag/v0.2.0)

This release contains:
- Minor improvements of annotations UI
- Various bugfixes
- Dependency upgrades

# v0.2.0

> [!CAUTION]
> **Upgrade of KoReader plugin required to sync with v0.2.0 of KoInsight**

# ✨ Annotations by @tku137 (#79)
<img width="1305" height="1089" alt="image" src="https://github.com/user-attachments/assets/69fdeffb-2ac4-40eb-bc57-b23f838cd909" />

Thanks to the awesome work of @tku137, we now have annotation sync and support in KoInsight. You should be able to sync your notes, bookmarks and highlights.

You can browse annotations per book - just go to the "Annotations" tab.

This unlocks a large amount of potential future improvements. 

# ✨ Sync on suspend by @tku137 (#66)
Added more options for sync and auto-sync from the KoReader plugin. Should fix issues with syncing from previous versions.

You can now enable "Aggressive Sync" mode, which will attempt to turn on WiFi and sync.

---

Thank you @tku137! <3

# v0.1.4

# ✨ Improvements

- See UI version in the footer by @dannoh [#32]
- Various plugin improvements by @tku137 and @cykirk [#9], [#43], [#57]
- Round page stats by @h3khaira [#60]
- Increase max upload size and make it configurable by @lolgame99 [#63]

Thanks to everyone for the improvements 🙏 

# Personal update

If you're reading this - I'm glad you still find KoInsight useful! I've struggled to find time and motivation to work on the project due to some personal reasons, but I do aim to at least maintain it. 

I'm open to PRs and suggestions as always. And I hope I get to reading again & actively developing KoInsight  again in the near future. :)
