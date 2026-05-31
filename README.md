# ZenPM Default Package Repository

[Add to ZenPM](zenpm://add-repo?name=ZenLabs&url=https://zen-labs-x.github.io/repo/)

## Signature Verification

All package indexes in this repository are signed with an ed25519 key. Verify `index.json` with the public key below:

```
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAsWdhAiVzFSIr8yYgFRHWWwAp2NAh/WKXMqaOkYXVN3k=
-----END PUBLIC KEY-----
```

**Verification command:**
```sh
openssl pkeyutl -verify -pubin -inkey zenpm-key.pub -in index.json -rawin -sigfile index.json.sig
```

**Files:**
- `index.json` — package index
- `index.json.sig` — ed25519 signature of the index
- `zenpm-key.pub` — public key distributed with ZenPM


Default package repository for [Zen Package Manager](https://github.com/Zen-Labs-X/ZenPM) — the package manager for jailbroken Kindle and Kobo devices.

## How to use

Add this repo to your ZenPM instance:

```sh
zenpm repo add default https://zen-labs-x.github.io/repo/
zenpm repo refresh
```

Or via the ZenPM Sources page: enter the URL `https://zen-labs-x.github.io/repo/`.

## Packages

| Package | Version | Platform | Dependencies |
|---|---|---|---|
| KUAL | 2.7.37 | Kindle | — |
| Zen Reader | 1.0.0 | Kindle | kual |
| NickelMenu | 0.6.0 | Kobo | — |
| ZenPM (Kobo Launcher) | 0.1.0 | Kobo | nickelmenu |
| KOReader (Kobo) | 2026.03.0 | Kobo | ZenPM-kobo |

## Repository format

This repo follows the [ZenPM repository format](https://github.com/Zen-Labs-X/ZenPM#repository-format) (schema v1).

- `index.json` — package catalog with all metadata (machine-readable)
- `packages/<id>/scripts/install.sh` — install script
- `packages/<id>/scripts/uninstall.sh` — uninstall script

## Hosting

This repository is hosted via **GitHub Pages** at:

```
https://zen-labs-x.github.io/repo/
```

All files are served as static content — no server-side logic required. ZenPM clients fetch `index.json` and resolve package scripts relative to this base URL.

## Contributing


