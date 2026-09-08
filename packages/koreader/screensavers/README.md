# KOReader screensavers

Put each screensaver in its own `packages/koreader/screensavers/<slug>/`
directory as a plain `.png` or `.jpg` file. Add a `.meta` beside it using this
template, setting `<ext>` to `png` or `jpg`:

```ini
id=screensaver-<slug>
name=<Display Name>
version=1.0.0
description=<Short description>
author=<Author>
category=screensavers
platforms=koreader
dependencies=
icon_url=packages/koreader/screensavers/<slug>/<filename>.<ext>
assets.0.arch=any
assets.0.asset=<filename>.<ext>
assets.0.url=packages/koreader/screensavers/<slug>/<filename>.<ext>
assets.0.size=<size in bytes>
```

Run `sh generate-manifest.sh` after adding or updating an image. Bump `version`
when replacing an existing image so installed copies receive an update; keep its
filename stable.
