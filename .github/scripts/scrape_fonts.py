#!/usr/bin/env python3
"""Cache installable KOReader font packages from upstream releases."""

import argparse
import io
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile

from scrape_common import REPO_ROOT, scraper_timestamp, write_results

UPSTREAM = "nicoverbruggen/ebook-fonts"
UPSTREAM_URL = f"https://github.com/{UPSTREAM}"
JUNICODE_UPSTREAM = "psb1558/Junicode-font"
JUNICODE_UPSTREAM_URL = f"https://github.com/{JUNICODE_UPSTREAM}"
JUNICODE_PACKAGE_ID = "font-junicode"
FONTS_ROOT = os.path.join(REPO_ROOT, "packages", "koreader", "fonts")


def request(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "zenpm-font-scraper")
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req) as response:
            return response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not download {url}: {exc}") from exc


def slugify(value):
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value


def release_version(release):
    return (release.get("name") or release.get("tag_name") or "source").lstrip("vV")


def archive_files(url, suffixes=(".ttf", ".otf")):
    with zipfile.ZipFile(io.BytesIO(request(url))) as archive:
        return {
            os.path.basename(info.filename): archive.read(info)
            for info in archive.infolist()
            if not info.is_dir() and info.filename.lower().endswith(suffixes)
        }


def preview_images(tag):
    source_url = f"{UPSTREAM_URL}/archive/refs/tags/{urllib.parse.quote(tag, safe='')}.zip"
    with zipfile.ZipFile(io.BytesIO(request(source_url))) as archive:
        images = {}
        for info in archive.infolist():
            match = re.search(r"/examples/(core|extra)/([^/]+\.png)$", info.filename)
            if match:
                images[(match.group(1), match.group(2))] = archive.read(info)
        return images


def package_meta(package_id, family, version, tag, published_at, updated_at, asset_size):
    path = f"packages/koreader/fonts/{package_id.removeprefix('font-')}"
    return "\n".join([
        f"# {family} font family for KOReader",
        f"# Cached from {UPSTREAM_URL} release {tag}",
        "# zenpm:auto-scraped-font",
        f"id={package_id}",
        f"name={family}",
        f"version={version}",
        f"description=E-reader-optimized {family} font family, including all available styles.",
        "author=nicoverbruggen",
        "category=fonts",
        "platforms=koreader",
        "dependencies=",
        f"source={UPSTREAM_URL}",
        "source_type=release",
        f"updated_at={updated_at}",
        f"published_at={published_at}",
        f"featured_image={path}/assets/featured.png",
        "assets.0.arch=any",
        f"assets.0.asset={package_id}.zip",
        f"assets.0.url={path}/{package_id}.zip",
        f"assets.0.size={asset_size}",
        "",
    ])


def junicode_package_meta(version, tag, published_at, updated_at, asset_size):
    path = f"packages/koreader/fonts/{JUNICODE_PACKAGE_ID.removeprefix('font-')}"
    return "\n".join([
        "# Junicode font family for KOReader",
        f"# Cached from {JUNICODE_UPSTREAM_URL} release {tag}",
        "# zenpm:auto-scraped-font",
        f"id={JUNICODE_PACKAGE_ID}",
        "name=Junicode",
        f"version={version}",
        "description=Junicode font family, including all available TrueType styles.",
        "author=psb1558",
        "category=fonts",
        "platforms=koreader",
        "dependencies=",
        f"source={JUNICODE_UPSTREAM_URL}",
        "source_type=release",
        f"updated_at={updated_at}",
        f"published_at={published_at}",
        "assets.0.arch=any",
        f"assets.0.asset={JUNICODE_PACKAGE_ID}.zip",
        f"assets.0.url={path}/{JUNICODE_PACKAGE_ID}.zip",
        f"assets.0.size={asset_size}",
        "",
    ])


def content_matches(path, content):
    try:
        with open(path, "rb") as file:
            return file.read() == content
    except OSError:
        return False


def is_generated_font_package(path):
    try:
        with open(os.path.join(path, ".meta"), encoding="utf-8") as file:
            return "# zenpm:auto-scraped-font" in file.read()
    except OSError:
        return False


def write_if_changed(path, content):
    if content_matches(path, content):
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as file:
        file.write(content)
    return True


def family_zip(files, directory="fonts"):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for filename, content in sorted(files.items()):
            entry = zipfile.ZipInfo(f"{directory}/{filename}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, content)
    return output.getvalue()


def latest_zip_asset(release, upstream):
    assets = [
        asset for asset in release.get("assets", [])
        if asset.get("name", "").lower().endswith(".zip")
    ]
    if len(assets) != 1:
        raise RuntimeError(f"Latest {upstream} release must have exactly one ZIP asset")
    return assets[0]


def cache_junicode(updated_at, dry_run=False):
    release = json.loads(request(f"https://api.github.com/repos/{JUNICODE_UPSTREAM}/releases/latest"))
    tag = release.get("tag_name", "")
    if not tag:
        raise RuntimeError("Latest Junicode release has no tag name")

    archive_asset = latest_zip_asset(release, "Junicode")
    font_files = archive_files(archive_asset["browser_download_url"], (".ttf",))
    if not font_files:
        raise RuntimeError("Latest Junicode release has no TrueType font files")

    package_dir = os.path.join(FONTS_ROOT, JUNICODE_PACKAGE_ID.removeprefix("font-"))
    archive = family_zip(font_files, JUNICODE_PACKAGE_ID.removeprefix("font-"))
    meta = junicode_package_meta(
        tag.lstrip("vV"), tag, release.get("published_at", ""), updated_at,
        len(archive),
    ).encode()
    targets = {
        os.path.join(package_dir, ".meta"): meta,
        os.path.join(package_dir, f"{JUNICODE_PACKAGE_ID}.zip"): archive,
    }

    changed = False
    if dry_run:
        changed = any(not content_matches(path, content) for path, content in targets.items())
        changed = changed or os.path.exists(os.path.join(package_dir, "fonts"))
        changed = changed or os.path.exists(os.path.join(package_dir, "scripts"))
    else:
        for path, content in targets.items():
            changed = write_if_changed(path, content) or changed
        for stale_path in (os.path.join(package_dir, "fonts"), os.path.join(package_dir, "scripts")):
            if os.path.isdir(stale_path):
                shutil.rmtree(stale_path)
                changed = True

    return changed, JUNICODE_PACKAGE_ID.removeprefix("font-")


def main():
    parser = argparse.ArgumentParser(description="Cache KOReader font packages.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    args = parser.parse_args()
    updated_at = scraper_timestamp()

    release = json.loads(request(f"https://api.github.com/repos/{UPSTREAM}/releases/latest"))
    assets = {asset["name"]: asset["browser_download_url"] for asset in release.get("assets", [])}
    manifest_url = assets.get("manifest.json")
    if not manifest_url:
        raise RuntimeError("Latest ebook-fonts release has no manifest.json asset")
    manifest = json.loads(request(manifest_url))
    tag = release.get("tag_name", "")
    if not tag:
        raise RuntimeError("Latest ebook-fonts release has no tag name")
    published_at = release.get("published_at", "")
    version = release_version(release)
    images = preview_images(tag)

    collections = manifest.get("collections", [])
    expected_dirs = set()
    all_font_files = {}
    changed = False
    total = 0
    for collection in collections:
        collection_name = collection.get("name", "")
        archive_url = collection.get("archives", {}).get("other")
        if not archive_url:
            raise RuntimeError(f"Release manifest has no cross-device archive for {collection_name}")
        available_files = archive_files(archive_url)
        for font in collection.get("fonts", []):
            family = font.get("family", "").strip()
            filenames = [os.path.basename(urllib.parse.urlparse(url).path) for url in font.get("files", [])]
            if not family or not filenames:
                raise RuntimeError(f"Invalid {collection_name} font entry: {font!r}")
            missing = [filename for filename in filenames if filename not in available_files]
            if missing:
                raise RuntimeError(f"Release archive is missing {family}: {', '.join(missing)}")
            preview_name = family.replace(" ", "-") + ".png"
            preview = images.get((collection_name, preview_name))
            if preview is None:
                raise RuntimeError(f"Release source is missing preview image for {family}")

            package_id = "font-" + slugify(family)
            dirname = package_id.removeprefix("font-")
            expected_dirs.add(dirname)
            package_dir = os.path.join(FONTS_ROOT, dirname)
            font_files = {filename: available_files[filename] for filename in filenames}
            for filename, content in font_files.items():
                existing = all_font_files.setdefault(filename, content)
                if existing != content:
                    raise RuntimeError(f"Conflicting font file in release: {filename}")
            archive = family_zip(font_files, dirname)
            meta = package_meta(
                package_id, family, version, tag, published_at, updated_at, len(archive)
            ).encode()
            targets = {
                os.path.join(package_dir, ".meta"): meta,
                os.path.join(package_dir, "assets", "featured.png"): preview,
                os.path.join(package_dir, f"{package_id}.zip"): archive,
            }
            total += 1
            if args.dry_run:
                changed = changed or any(not content_matches(path, content) for path, content in targets.items())
                changed = changed or os.path.exists(os.path.join(package_dir, "fonts"))
                changed = changed or os.path.exists(os.path.join(package_dir, "scripts"))
            else:
                for path, content in targets.items():
                    changed = write_if_changed(path, content) or changed
                for stale_path in (os.path.join(package_dir, "fonts"), os.path.join(package_dir, "scripts")):
                    if os.path.isdir(stale_path):
                        shutil.rmtree(stale_path)
                        changed = True

    junicode_changed, junicode_dir = cache_junicode(updated_at, args.dry_run)
    expected_dirs.add(junicode_dir)
    changed = junicode_changed or changed

    all_archive = family_zip(all_font_files)
    all_archive_path = os.path.join(FONTS_ROOT, "ebook-fonts-all.zip")
    if args.dry_run:
        changed = changed or not content_matches(all_archive_path, all_archive)
    else:
        changed = write_if_changed(all_archive_path, all_archive) or changed

    if os.path.isdir(FONTS_ROOT):
        for entry in os.listdir(FONTS_ROOT):
            path = os.path.join(FONTS_ROOT, entry)
            if entry.startswith("font-") or not os.path.isdir(path):
                continue
            if entry not in expected_dirs and is_generated_font_package(path):
                if args.dry_run:
                    changed = True
                else:
                    shutil.rmtree(path)
                    changed = True

    if changed:
        state = "would update" if args.dry_run else "updated"
        print(f"{state} {total} cached ebook-fonts package(s) and Junicode.", file=sys.stderr)
    else:
        print(f"font cache is current ({total} ebook-fonts packages and Junicode).", file=sys.stderr)
    updated = [{"id": "fonts", "name": "fonts", "kind": "fonts", "path": "packages/koreader/fonts"}] if changed else []
    write_results([], updated)


if __name__ == "__main__":
    main()
