# Security Policy

## Supported Versions

Only the latest release of this project is actively maintained. Security fixes will not be backported to older versions.

| Version | Supported |
|---------|-----------|
| Latest release | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability in this project **please do not open a public GitHub issue.** Instead, report it privately so it can be addressed before any public disclosure.

**To report a vulnerability:**

1. Go to the [Security Advisories](https://github.com/xZenLabs/repo/security/advisories) page on GitHub.
2. Click **"Report a vulnerability"** and fill in the details.

Alternatively, you can reach out directly by opening a [private issue](https://github.com/xZenLabs/repo/issues) and marking it as confidential, or by contacting the maintainer through GitHub.

Please include:

- A clear description of the vulnerability and its potential impact
- Steps to reproduce, if applicable
- Any relevant file paths, code references, or log output

## Response

Reported vulnerabilities will be reviewed and responded to as promptly as possible. Once a fix is ready, a new release will be published and the advisory will be made public.

## Scope

This repository is the default package repository for the [Zen Package Manager (ZenPM)](https://github.com/xZenLabs/ZenPackageManager). It is served as static content via GitHub Pages and does not run a server, handle authentication, or process external user data. The primary security surface is:

- The package catalog (`manifest.json`), which is signed with an ed25519 key and verified by ZenPM clients before use
- The per-package `install.sh` / `uninstall.sh` scripts, which run on the user's device when a package is installed or removed
- The manifest signing and deploy workflow in `.github/`, which signs `manifest.json` on push using a private key stored as a secret

Out-of-scope reports (e.g. vulnerabilities in the ZenPM client itself, in the packaged software distributed through this repository, or in the underlying device OS) should be directed to the appropriate upstream project.
