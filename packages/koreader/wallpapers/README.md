# KOReader wallpapers

Put each wallpaper in its own `packages/koreader/wallpapers/<slug>/` directory
as a plain `.jpg` file. Add a `.meta` beside it using this template:

```ini
id=wallpaper-<slug>
name=<Display Name>
version=1.0.0
description=<Short description>
author=<Author>
category=wallpapers
platforms=koreader
dependencies=
icon_url=packages/koreader/wallpapers/<slug>/<filename>.jpg
assets.0.arch=any
assets.0.asset=<filename>.jpg
assets.0.url=packages/koreader/wallpapers/<slug>/<filename>.jpg
assets.0.size=<size in bytes>
```

Run `sh generate-manifest.sh` after adding or updating an image. Bump `version`
when replacing an existing image so installed copies receive an update; keep its
filename stable.
