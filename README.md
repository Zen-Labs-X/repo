# ZenPM Default Package Repository

[Add to ZenPM](zenpm://add-repo?name=ZenLabs&url=https://xzenlabs.github.io/repo/)

## Key Generation

Generate an ed25519 key pair:

```sh
openssl genpkey -algorithm ed25519 -out zenpm-key
openssl pkey -in zenpm-key -pubout -out zenpm-key.pub
```

- `zenpm-key` — private key (keep secret, add to `.gitignore`)
- `zenpm-key.pub` — public key (commit to repo, distributed with ZenPM)

Add the private key as a GitHub Actions secret named `ZENPM_PRIVATE_KEY` so the deploy workflow can sign `manifest.json` automatically:

```sh
gh secret set ZENPM_PRIVATE_KEY --body "$(cat zenpm-key)"
```

The signing is handled automatically on every push to `main` — no manual re-signing needed.

## Signature Verification

All package manifests in this repository are signed with an ed25519 key. Verify `manifest.json` with the public key below:

```
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAsWdhAiVzFSIr8yYgFRHWWwAp2NAh/WKXMqaOkYXVN3k=
-----END PUBLIC KEY-----
```

**Verification command:**
```sh
openssl pkeyutl -verify -pubin -inkey zenpm-key.pub -in manifest.json -rawin -sigfile manifest.json.sig
```

**Manual re-signing (if needed):**

```sh
openssl pkeyutl -sign -inkey zenpm-key -in manifest.json -rawin -out manifest.json.sig
```

**Files:**
- `manifest.json` — package manifest
- `manifest.json.sig` — ed25519 signature of the manifest
- `zenpm-key.pub` — public key distributed with ZenPM


Default package repository for [Zen Package Manager](https://github.com/Zen-Labs-X/ZenPM) — the package manager for jailbroken Kindle and Kobo devices.

## How to use

Add this repo to your ZenPM instance:

```sh
zenpm repo add default https://xzenlabs.github.io/repo/
zenpm repo refresh
```

Or via the ZenPM Sources page: enter the URL `https://xzenlabs.github.io/repo/`.

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

- `manifest.json` — package catalog with all metadata (machine-readable)
- `packages/<platform>/<id>/scripts/install.sh` — install script
- `packages/<platform>/<id>/scripts/uninstall.sh` — uninstall script
- `packages/<platform>/<id>/assets/` — optional icon (`icon.png`) and featured image (`featured.png`)

### Package fields

Each package metadata file must include a `category` set to one of:

- `utility`
- `games`
- `productivity`
- `media`

### Optional package fields

Each package in `manifest.json` may include:

| Field | Type | Description |
|---|---|---|
| `icon_url` | string | Path to package icon (e.g. `packages/<id>/assets/icon.png`) |
| `featured_image` | string | Path to a larger preview/featured image (e.g. `packages/<id>/assets/featured.png`) |

These fields are optional. Omit them if no assets are available.

## Hosting

This repository is hosted via **GitHub Pages** at:

```
https://xzenlabs.github.io/repo/
```

All files are served as static content — no server-side logic required. ZenPM clients fetch `manifest.json` and resolve package scripts relative to this base URL.

## Contributing

