# ZenPM Default Package Repository

[Add to ZenPM](zenpm://add-repo?name=ZenLabs%20Repo&url=https://xzenlabs.github.io/repo/)

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
- `theme`
- `patches`

### Optional package fields

Each package in `manifest.json` may include:

| Field | Type | Description |
|---|---|---|
| `icon_url` | string | Path to package icon (e.g. `packages/<id>/assets/icon.png`) |
| `featured_image` | string | Path to a larger preview/featured image (e.g. `packages/<id>/assets/featured.png`) |
| `featured` | boolean | Marks a package for the featured section. |
| `featured_order` | non-negative integer | Display priority within featured packages; lower values appear first. Requires `featured=true`. |
| `updated_at` | string | Upstream package's last-updated timestamp from GitHub, in UTC ISO 8601 format. |
| `readme_url` | string | Path to the cached package README. |
| `readme_hash` | string | Git blob SHA of the cached README; changes when its source README changes. |
| `conflicts` | array of strings | Package IDs that must not be installed together. |

Install and uninstall behavior is handled by the client; packages do not declare script URLs.

These fields are optional. Omit them if no assets are available.

## Hosting

This repository is hosted via **GitHub Pages** at:

```
https://xzenlabs.github.io/repo/
```

All files are served as static content — no server-side logic required. ZenPM clients fetch `manifest.json` and resolve package scripts relative to this base URL.

## Contributing

### KOReader plugins and patches

KOReader packages are discovered automatically from GitHub on the 1st and 15th
of each month. A newly discovered package is proposed in its own pull request.

To be eligible, a repository must:

- be hosted on GitHub and not already be represented by a package in this repo;
- have at least 15 GitHub stars;
- not be archived; and
- have been pushed to within the last two years.

In addition, plugins must have `koplugin` in their name or be tagged with the
`koplugin` or `koreader-plugin` topic. Patches must be tagged with
`koreader-user-patch` or have `KOReader.patches` in their name, and must contain
at least one user-patch Lua file whose filename starts with a number (for
example, `2-example.lua`).

Forks are considered by default. Plugin packages use a release ZIP when one is
available, otherwise the repository's default-branch source archive; patch
packages install the matching Lua files directly. All generated packages use
the shared KOReader install and uninstall scripts. During each scan, the
repository README is cached beside the package and its Git blob SHA is included
in the manifest, allowing clients to refresh only when that hash changes.

### Refreshing KOReader packages locally

Run both scrapers with a GitHub token, then regenerate the manifest:

```sh
GITHUB_TOKEN=your_github_token python3 .github/scripts/scrape_koplugins.py
GITHUB_TOKEN=your_github_token python3 .github/scripts/scrape_kopatches.py
sh generate-manifest.sh
```

The token avoids GitHub's unauthenticated API limit and is required for a full
README cache refresh. GitHub Pages signs the generated manifest during deploy.
