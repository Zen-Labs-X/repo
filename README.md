# ZenPM Default Package Repository

[Add to ZenPM](zenpm://add-repo?name=ZenLabs%20Repo&url=https://xzenlabs.github.io/repo/)

## Requirements for automatic inclusion

KOReader plugins and user patches are discovered from GitHub every two hours.
To get a new package added automatically, meet **all the common requirements**
and the **plugin or patch requirements** below. No pull request to this repo is
needed for automatic discovery. Other package types are outside this process.

### Common requirements

- **Public GitHub repository with at least 5 stars.** Forks are eligible too.
- **Not archived.**
- **Recent activity:** the scraper rejects repositories whose GitHub
  `pushed_at` timestamp is more than 730 whole days old. It does not reject a
  repository if that timestamp is missing or cannot be parsed.
- **Not a duplicate:** the repository must not already be cataloged, its
  generated package ID must not already be taken, and its normalized
  owner/repository identity must not match an existing package. Package IDs
  are derived from repository names, so a name collision can prevent addition
  even when the repositories have different owners.

### Plugin requirements

Your repository must match **at least one** of these discovery signals:

- Its **repository name contains `koplugin`**, such as `example.koplugin`.
- Its **GitHub topics include `koplugin`, `koreader-plugin`, or
  `koreader-plugins`**.

A `.koplugin` folder inside a larger repository does **not** qualify by itself.

Repository name and topic checks are case-insensitive for plugins and patches.

Plugin discovery skips repositories tagged `koreader-user-patch` or whose
name contains `KOReader.patches`; those go through patch discovery instead.

**A GitHub release is not required.** The scraper uses ZIP assets from the
newest stable release when available; otherwise it uses the default-branch
source ZIP. Authors must still provide a layout that ZenPM can install;
catalog discovery does not validate the plugin's archive layout or functionality.

### User patch requirements

Your repository must match **at least one** of these discovery signals:

- Its **GitHub topics include `koreader-user-patch`**.
- Its **repository name contains `KOReader.patches`**.

It must also contain at least one file on the default branch whose filename
**starts with a digit and ends with `.lua`**, such as `2-example.lua`.
Subdirectories are scanned. Matching Lua files are installed directly, so
no release or ZIP is required.

Patch discovery rejects repositories containing a directory ending in
`.koplugin`; mixed plugin/patch repositories are not supported by that scanner.

### Exceptions and scan results

ZenFM (`xzenlabs/zen-fm`) and ZenPM (`xzenlabs/zen-pm`) are explicitly listed in
`EXTRA_PLUGIN_REPOS` in [scrape_koplugins.py](.github/scripts/scrape_koplugins.py).
They bypass the star minimum and plugin name/topic requirement. The other
eligibility checks still apply.

These rules govern **new additions**. Already scraped packages continue to be
refreshed without rechecking the star or inactivity threshold; blacklisted
repositories are excluded from refreshes too. GitHub API failures or rate
limits can delay discovery or addition, even when a repository qualifies.

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


Default package repository for [xZenLabs/zen-pm](https://github.com/xZenLabs/zen-pm) — the package manager for jailbroken Kindle and Kobo devices.

## How to use

Add this repo to your ZenPM instance:

```sh
zenpm repo add default https://xzenlabs.github.io/repo/
zenpm repo refresh
```

Or via the ZenPM Sources page: enter the URL `https://xzenlabs.github.io/repo/`.

## Local development

Serve the repository, including `manifest.json` and its relative package files,
with Python's standard library:

```sh
python3 .github/scripts/dev.py
```

The manifest is then available at `http://localhost:8000/manifest.json`.

## Packages

| Package | Version | Platform | Dependencies |
|---|---|---|---|
| KUAL | 2.7.37 | Kindle | — |
| Zen Reader | 1.0.0 | Kindle | kual |
| NickelMenu | 0.6.0 | Kobo | — |
| ZenPM (Kobo Launcher) | 0.1.0 | Kobo | nickelmenu |
| KOReader (Kobo) | 2026.03.0 | Kobo | ZenPM-kobo |

## Repository format

This repo follows the [ZenPM repository format](https://github.com/xZenLabs/zen-pm#repository-format) (schema v1).

- `manifest.json` — package catalog with all metadata (machine-readable)
- `packages/<platform>/<id>/versions.json` — generated version-picker data for one package
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
- `fonts`
- `wallpapers`
- `screensavers`

### Plain KOReader images

Add each wallpaper under `packages/koreader/wallpapers/<slug>/` as a `.jpg`
file, or each screensaver under `packages/koreader/screensavers/<slug>/` as a
`.png` or `.jpg` file. Each image directory also needs a `.meta` file; copy the
template from the category's README. Images are hosted and installed directly,
without wrapping them in a ZIP archive.

### Optional package fields

Each package in `manifest.json` may include:

| Field | Type | Description |
|---|---|---|
| `icon_url` | string | Path to package icon (e.g. `packages/<id>/assets/icon.png`) |
| `featured_image` | string | Path to a larger preview/featured image (e.g. `packages/<id>/assets/featured.png`) |
| `featured` | boolean | Marks a package for the featured section. |
| `featured_order` | non-negative integer | Display priority within featured packages; lower values appear first. Requires `featured=true`. |
| `updated_at` | string | Timestamp when ZenPM's scraper last refreshed the package, in UTC ISO 8601 format. |
| `published_at` | string | Timestamp of the upstream package's most recent GitHub release, in UTC ISO 8601 format. |
| `readme_url` | string | Path to the cached package README. |
| `readme_hash` | string | Git blob SHA of the cached README; changes when its source README changes. |
| `release_notes_url` | string | Path to the cached notes for the package's five latest stable releases. |
| `release_notes_hash` | string | SHA-256 hash of the cached stable release notes; changes when their source content changes. |
| `prerelease_version` | string | Version of the package's newest non-alpha prerelease. |
| `prerelease_published_at` | string | Publication timestamp of the package's newest non-alpha prerelease, in UTC ISO 8601 format. |
| `alpha_version` | string | Version of ZenOS's newest alpha prerelease. |
| `alpha_published_at` | string | Publication timestamp of ZenOS's newest alpha prerelease, in UTC ISO 8601 format. |
| `prerelease_notes_url` | string | Path to the cached notes for the package's five latest non-alpha prereleases. |
| `prerelease_notes_hash` | string | SHA-256 hash of the cached prerelease notes; changes when their source content changes. |
| `versions_url` | string | Path to the package's generated `versions.json`. The file contains up to 100 cached, non-draft GitHub releases with uploaded ZIP assets or source-code ZIP fallbacks. |
| `conflicts` | array of strings | Package IDs that must not be installed together. |
| `incompatible_platforms` | array of strings | Platforms on which a package cannot be installed. |

Each `versions.json` has a top-level `releases` array. Release entries use the
same `tag_name`, `name`, `prerelease`, and `assets` fields returned by ZenPM's
existing package-releases endpoint.

Install and uninstall behavior is handled by the client unless a platform-specific package declares script URLs.

These fields are optional. Release history may be empty when no downloadable
archive is available.

## Hosting

This repository is hosted via **GitHub Pages** at:

```
https://xzenlabs.github.io/repo/
```

All files are served as static content — no server-side logic required. ZenPM clients fetch `manifest.json` and resolve package scripts relative to this base URL.

## Contributing

### KOReader plugins and patches

See [Requirements for automatic inclusion](#requirements-for-automatic-inclusion)
for the exact rules for getting a new KOReader plugin or patch added.

During each scan, the
repository README, the five latest stable and non-alpha prerelease notes, and up
to 100 installable releases are cached in the repository metadata.
`generate-manifest.sh` writes each release list to the package's `versions.json`
and keeps only its `versions_url` in the catalog. Documentation content hashes
are included in the manifest, allowing clients to refresh only when the
corresponding content changes. Cached releases let clients populate their
version pickers without calling the GitHub API. When a release has no uploaded
ZIP asset, its automatically generated GitHub source-code ZIP is cached instead.

### Refreshing KOReader packages locally

Run both scrapers with a GitHub token, then regenerate the manifest:

```sh
GITHUB_TOKEN=your_github_token python3 .github/scripts/scrape_koplugins.py
GITHUB_TOKEN=your_github_token python3 .github/scripts/scrape_kopatches.py
sh generate-manifest.sh
```

The token avoids GitHub's unauthenticated API limit and is required for a full
README cache refresh. GitHub Pages signs the generated manifest during deploy.
