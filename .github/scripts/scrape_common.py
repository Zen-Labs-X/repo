#!/usr/bin/env python3
"""Shared helpers for GitHub-backed KOReader package scrapers."""

import base64
import binascii
import datetime
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KOREADER_DIR = os.path.join(REPO_ROOT, "packages", "koreader")
CATEGORY_CACHE = os.path.join(os.path.dirname(__file__), "plugin_categories.json")
SCRAPE_BLACKLIST = os.path.join(os.path.dirname(__file__), "scrape_blacklist.json")
SCRAPED_MARKER = "zenpm:auto-scraped"

MIN_STARS = 15
MAX_INACTIVE_DAYS = 730

KIND_PLUGIN = "plugin"
KIND_PATCH = "patch"

DEFAULT_PLUGIN_PLATFORMS = "koreader"

PRESENTATION_FIELDS = (
    "icon_url",
    "featured_image",
    "featured",
    "featured_order",
)

PLUGIN_IDENTITY_FIELDS = (
    "plugin_module",
    "plugin_module_aliases",
    "source_asset_aliases",
)

VALID_CATEGORIES = ("utility", "games", "productivity", "media", "theme", "patches", "fonts")
DEFAULT_CATEGORY = "utility"
PATCH_CATEGORY = "patches"

ARCH_PATTERNS = [
    (r"aarch64|arm64", "arm64"),
    (r"armv7|armhf|armel", "armv7"),
    (r"x86[_-]?64|amd64", "x86_64"),
    (r"i686|i386|x86", "x86"),
    (r"\barm\b", "arm"),
    (r"kindle", "kindle"),
    (r"kobo", "kobo"),
]

CATEGORY_KEYWORDS = [
    ("games", [
        "game", "games", "sudoku", "crossword", "nonogram", "solitaire",
        "puzzle", "2048", "chess", "wordsearch", "word search", "frotz",
        "trivia", "quiz", "arcade", "tetris", "minesweeper", "connections",
    ]),
    ("theme", [
        "theme", "ui", "look", "design", "redesign", "appearance", "skin",
        "style", "home screen", "homescreen", "home page", "homepage",
        "menu", "icon", "icons", "cover", "bookshelf", "ribbon", "charm",
        "minimal", "customize koreader", "customizable ui", "color scheme",
        "font",
    ]),
    ("media", [
        "comic", "manga", "manhwa", "manhua", "audiobook", "audio book",
        "audiobookshelf", "music", "podcast", "player", "image", "illustration",
        "panel", "video", "gallery", "reader", "rakuyomi", "suwayomi",
        "library", "opds", "anna", "z-library", "zlibrary", "download books",
        "rss", "feed", "telegram",
    ]),
    ("productivity", [
        "anki", "flashcard", "vocabulary", "dictionary", "note", "notes",
        "highlight", "annotation", "sync", "todo", "task", "planner", "tracker",
        "zotero", "obsidian", "readwise", "pomodoro", "calendar", "translate",
        "translation", "wallabag", "readeck", "instapaper", "bookmark",
        "summary", "summarize", "memo", "journal", "learning", "study",
        "spaced repetition", "stats", "streak", "hardcover", "storygraph",
    ]),
]


def token():
    return os.environ.get("GITHUB_TOKEN", "").strip()


def http_json(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "zenpm-koreader-scraper")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    tok = token()
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode("utf-8")
            return resp.status, json.loads(data), dict(resp.headers)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(body)
        except ValueError:
            parsed = None
        return e.code, parsed, dict(e.headers or {})


def respect_rate_limit(headers):
    remaining = headers.get("X-RateLimit-Remaining")
    reset = headers.get("X-RateLimit-Reset")
    if remaining is None:
        return
    try:
        if int(remaining) <= 1 and reset:
            wait = max(0, int(reset) - int(time.time())) + 1
            print(f"Rate limit reached; sleeping {wait}s", file=sys.stderr)
            time.sleep(wait)
    except ValueError:
        pass


def search_repos(query):
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        })
        status, data, headers = http_json(f"{API}/search/repositories?{params}")
        if status != 200 or not data:
            if status == 403:
                respect_rate_limit(headers)
                continue
            print(f"Search failed ({status}) for {query!r}", file=sys.stderr)
            return
        items = data.get("items", [])
        for item in items:
            yield item
        respect_rate_limit(headers)
        if len(items) < 100 or page >= 10:
            return
        page += 1


def discover(queries):
    found = {}
    for query in queries:
        for item in search_repos(query):
            found.setdefault(item["full_name"], item)
    return found


def fetch_repo(full_name):
    status, data, _headers = http_json(f"{API}/repos/{full_name}")
    if status == 200:
        return data
    return None


def fetch_releases(full_name):
    """Return up to 100 releases, [] when none exist, or None when unavailable."""
    status, data, _headers = http_json(f"{API}/repos/{full_name}/releases?per_page=100")
    if status == 404:
        return []
    if status != 200 or not isinstance(data, list):
        return None
    return data


def newest_stable_release(releases):
    """Return the newest published non-draft stable release."""
    stable_releases = [
        release for release in releases
        if not release.get("prerelease") and not release.get("draft")
    ]
    if not stable_releases:
        return {}
    return max(
        stable_releases,
        key=lambda release: release.get("published_at") or release.get("created_at") or "",
    )


def newest_prerelease(releases):
    """Return the newest non-draft prerelease from a fetched release list."""
    prereleases = [
        release for release in releases
        if release.get("prerelease") and not release.get("draft")
    ]
    if not prereleases:
        return {}
    return max(
        prereleases,
        key=lambda release: release.get("published_at") or release.get("created_at") or "",
    )


def installable_releases(releases):
    """Return release metadata needed by ZenPM's version picker."""
    result = []
    for release in releases or []:
        tag_name = str(release.get("tag_name") or "").strip()
        if release.get("draft") or not tag_name:
            continue

        assets = []
        for asset in release.get("assets") or []:
            name = str(asset.get("name") or "").strip()
            url = str(asset.get("browser_download_url") or "").strip()
            if not name.lower().endswith(".zip") or not url:
                continue
            cached_asset = {"name": name, "url": url}
            if asset.get("size"):
                cached_asset["size"] = asset["size"]
            if asset.get("digest"):
                cached_asset["digest"] = asset["digest"]
            assets.append(cached_asset)

        if not assets:
            source_url = str(release.get("zipball_url") or "").strip()
            if not source_url:
                continue
            assets.append({"name": "source-code.zip", "url": source_url})
        cached_release = {"tag_name": tag_name, "assets": assets}
        name = str(release.get("name") or "").replace("\r", " ").replace("\n", " ").strip()
        if name:
            cached_release["name"] = name
        if release.get("prerelease"):
            cached_release["prerelease"] = True
        result.append(cached_release)
    return result


def fetch_readme(full_name):
    """Return a repository README and its Git blob SHA, if GitHub has one."""
    status, data, _headers = http_json(f"{API}/repos/{full_name}/readme")
    if status == 404:
        return None, None, True
    if status != 200 or not isinstance(data, dict):
        return None, None, False

    try:
        content = base64.b64decode(data.get("content", "")).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError, ValueError):
        print(f"Could not decode README for {full_name}", file=sys.stderr)
        return None, None, False

    readme_hash = data.get("sha", "").strip()
    return content, readme_hash or None, True


def cache_readme(full_name, package_dir, dry_run=False):
    """Cache a GitHub README beside its package and return manifest fields."""
    content, readme_hash, resolved = fetch_readme(full_name)
    path = os.path.join(package_dir, "README.md")

    if not resolved:
        return None, None, False, False

    if content is None:
        changed = os.path.exists(path)
        if changed and not dry_run:
            os.remove(path)
        return None, None, changed, True

    try:
        with open(path, "r", encoding="utf-8") as fh:
            changed = fh.read() != content
    except OSError:
        changed = True

    if changed and not dry_run:
        os.makedirs(package_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)

    return os.path.relpath(path, REPO_ROOT), readme_hash, changed, True


def cache_release_notes(release, package_dir, dry_run=False, filename="RELEASE_NOTES.md"):
    """Cache a release body beside its package and return manifest fields."""
    if release is None:
        return None, None, False, False

    path = os.path.join(package_dir, filename)
    if not release:
        changed = os.path.exists(path)
        if changed and not dry_run:
            os.remove(path)
        return None, None, changed, True

    content = release.get("body") or ""
    release_notes_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    try:
        with open(path, "r", encoding="utf-8") as fh:
            changed = fh.read() != content
    except OSError:
        changed = True

    if changed and not dry_run:
        os.makedirs(package_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)

    return os.path.relpath(path, REPO_ROOT), release_notes_hash, changed, True


def fetch_tree(full_name, branch):
    branch_url = urllib.parse.quote(branch, safe="")
    status, data, _headers = http_json(
        f"{API}/repos/{full_name}/git/trees/{branch_url}?recursive=1"
    )
    if status == 200 and isinstance(data, dict):
        return data.get("tree", [])
    return []


def normalize_repo_ref(ref):
    if not ref:
        return ""
    ref = ref.strip()
    for prefix in (
        "https://api.github.com/repos/",
        "http://api.github.com/repos/",
        "https://github.com/",
        "http://github.com/",
    ):
        if ref.startswith(prefix):
            ref = ref[len(prefix):]
            break
    ref = ref.split("@", 1)[0]
    parts = [p for p in ref.split("/") if p]
    if len(parts) >= 2:
        return (parts[0] + "/" + parts[1]).lower()
    return ""


def repository_identity(ref):
    """Return a stable owner/package identity for duplicate detection."""
    normalized = normalize_repo_ref(ref)
    if not normalized:
        return None
    owner, repo = normalized.split("/", 1)
    repo = re.sub(r"\.(koplugin|kopatch)$", "", repo)
    return owner, re.sub(r"[^a-z0-9]", "", repo)


def looks_like_koreader_patch_repo(repo):
    name = repo.get("name", "").lower()
    topics = [topic.lower() for topic in repo.get("topics", [])]
    if "koreader-user-patch" in topics:
        return True
    return name == "koreader.patches" or "koreader.patches" in name


def load_blacklist():
    """Return normalized GitHub repository refs excluded from scraping."""
    try:
        with open(SCRAPE_BLACKLIST, "r", encoding="utf-8") as fh:
            values = json.load(fh)
    except (OSError, ValueError):
        return set()
    if not isinstance(values, list):
        return set()
    return {ref for value in values if (ref := normalize_repo_ref(str(value)))}


def parse_meta(meta_path):
    fields = {}
    scraped = False
    try:
        with open(meta_path, "r", encoding="utf-8") as fh:
            content = fh.read()
    except OSError:
        return fields, scraped, ""

    for line in content.splitlines():
        stripped = line.strip()
        if stripped == f"# {SCRAPED_MARKER}":
            scraped = True
            continue
        if stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        fields[key] = value
    return fields, scraped, content


def existing_repo_refs():
    known_refs = set()
    known_ids = set()
    pkg_root = os.path.join(REPO_ROOT, "packages")
    for dirpath, _dirs, files in os.walk(pkg_root):
        if ".meta" not in files:
            continue
        fields, _scraped, _content = parse_meta(os.path.join(dirpath, ".meta"))
        ref = normalize_repo_ref(fields.get("source", ""))
        if ref:
            known_refs.add(ref)
        meta_id = fields.get("id", "").strip()
        if meta_id:
            known_ids.add(meta_id)
    return known_refs, known_ids


def existing_repository_identities():
    identities = set()
    pkg_root = os.path.join(REPO_ROOT, "packages")
    for dirpath, _dirs, files in os.walk(pkg_root):
        if ".meta" not in files:
            continue
        fields, _scraped, _content = parse_meta(os.path.join(dirpath, ".meta"))
        identity = repository_identity(fields.get("source", ""))
        if identity:
            identities.add(identity)
    return identities


def existing_scraped_meta(category=None, include_refs=()):
    records = []
    include_refs = {normalize_repo_ref(ref) for ref in include_refs}
    for dirpath, _dirs, files in os.walk(KOREADER_DIR):
        if ".meta" not in files:
            continue
        meta_path = os.path.join(dirpath, ".meta")
        fields, scraped, content = parse_meta(meta_path)
        ref = normalize_repo_ref(fields.get("source", ""))
        meta_id = fields.get("id", "").strip()
        if category is not None and fields.get("category", "").strip() != category:
            continue
        if (scraped or ref in include_refs) and ref and meta_id:
            records.append({
                "path": meta_path,
                "rel_path": os.path.relpath(meta_path, REPO_ROOT),
                "ref": ref,
                "id": meta_id,
                "name": fields.get("name", "").strip(),
                "category": fields.get("category", "").strip(),
                "content": content,
                "fields": fields,
            })
    return records


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def make_id(repo_name, existing_ids):
    stripped = re.sub(r"\.koplugin$", "", repo_name, flags=re.IGNORECASE)
    stripped = re.sub(r"\.(ko)?patch(es)?$", "", stripped, flags=re.IGNORECASE)
    base = slugify(stripped) or slugify(repo_name)
    candidate = base
    n = 2
    while candidate in existing_ids:
        candidate = f"{base}-{n}"
        n += 1
    return candidate


def display_name(repo_name):
    name = re.sub(r"\.koplugin$", "", repo_name, flags=re.IGNORECASE)
    name = re.sub(r"\.(ko)?patch(es)?$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[_-]+", " ", name).strip()
    return name.title() if name else repo_name


def package_dir_name(meta_id, kind):
    if kind == KIND_PATCH:
        return f"{meta_id}.kopatch"
    return f"{meta_id}.koplugin"


def detect_arch(filename):
    low = filename.lower()
    for pattern, label in ARCH_PATTERNS:
        if re.search(pattern, low):
            return label
    return "any"


def clean_description(desc):
    if not desc:
        return ""
    desc = desc.replace("\r", " ").replace("\n", " ").strip()
    if len(desc) > 200:
        desc = desc[:197].rstrip() + "..."
    return desc


def classify_category(repo):
    haystack = " ".join([
        repo.get("name", ""),
        repo.get("description") or "",
        " ".join(repo.get("topics", [])),
    ]).lower()
    for category, keywords in CATEGORY_KEYWORDS:
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", haystack):
                return category
    return DEFAULT_CATEGORY


def load_category_cache():
    try:
        with open(CATEGORY_CACHE, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return {}
    return {
        k.lower(): v for k, v in data.items()
        if v in VALID_CATEGORIES
    }


def existing_meta_categories():
    result = {}
    pkg_root = os.path.join(REPO_ROOT, "packages")
    for dirpath, _dirs, files in os.walk(pkg_root):
        if ".meta" not in files:
            continue
        fields, _scraped, _content = parse_meta(os.path.join(dirpath, ".meta"))
        ref = normalize_repo_ref(fields.get("source", ""))
        category = fields.get("category", "").strip()
        if ref and category in VALID_CATEGORIES:
            result[ref] = category
    return result


def save_category_cache(cache):
    with open(CATEGORY_CACHE, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(cache.items())), fh, indent=2)
        fh.write("\n")


def is_inactive(repo):
    pushed = repo.get("pushed_at")
    if not pushed:
        return False
    try:
        when = datetime.datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, TypeError):
        return False
    age = datetime.datetime.utcnow() - when
    return age.days > MAX_INACTIVE_DAYS


def scraper_timestamp():
    """Return the current UTC time in the manifest timestamp format."""
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_meta(repo, release, existing_ids, category, meta_id=None, kind=KIND_PLUGIN,
               name_override=None, patch_assets=None, readme_url=None,
               readme_hash=None, release_notes_url=None, release_notes_hash=None,
               prerelease=None, prerelease_notes_url=None, prerelease_notes_hash=None,
               releases=None, preserved_fields=None, scraped_at=None):
    owner = repo["owner"]["login"]
    repo_name = repo["name"]
    full_name = repo["full_name"]
    if meta_id is None:
        meta_id = make_id(repo_name, existing_ids)
    existing_ids.add(meta_id)

    name = name_override or display_name(repo_name)
    author = (preserved_fields or {}).get("author") or owner
    stars = repo.get("stargazers_count", 0)
    updated_at = scraped_at or scraper_timestamp()
    published_at = release.get("published_at") if isinstance(release, dict) else ""
    prerelease_version = (
        (prerelease.get("tag_name") or "").lstrip("vV")
        if isinstance(prerelease, dict) else ""
    )
    prerelease_published_at = (
        prerelease.get("published_at") if isinstance(prerelease, dict) else ""
    )
    description = clean_description(repo.get("description"))
    default_branch = repo.get("default_branch", "main")
    package_label = "patch" if kind == KIND_PATCH else "plugin"
    platforms = (preserved_fields or {}).get(
        "platforms", DEFAULT_PLUGIN_PLATFORMS if kind == KIND_PLUGIN else "koreader"
    )
    dependencies = (preserved_fields or {}).get("dependencies", "")
    conflicts = (preserved_fields or {}).get("conflicts", "")
    incompatible_platforms = (preserved_fields or {}).get("incompatible_platforms", "")
    install_url = (preserved_fields or {}).get("install_url", "")
    uninstall_url = (preserved_fields or {}).get("uninstall_url", "")

    lines = [
        f"# {name} {package_label} for KOReader",
        f"# {repo['html_url']}",
        f"# {SCRAPED_MARKER}",
        f"id={meta_id}",
        f"name={name}",
    ]

    zip_assets = []
    version = "source"
    if release and isinstance(release, dict) and release.get("assets") is not None:
        tag = (release.get("tag_name") or "").lstrip("vV")
        if tag:
            version = tag
        for asset in release.get("assets", []):
            aname = asset.get("name", "")
            if aname.lower().endswith(".zip"):
                zip_assets.append(asset)

    lines.extend([
        f"version={version}",
        f"description={description}",
        f"author={author}",
        f"category={category}",
        f"platforms={platforms}",
        f"dependencies={dependencies}",
        f"source={repo['html_url']}",
    ])

    for field in PLUGIN_IDENTITY_FIELDS:
        value = (preserved_fields or {}).get(field, "")
        if value:
            lines.append(f"{field}={value}")

    if install_url:
        lines.append(f"install_url={install_url}")
    if uninstall_url:
        lines.append(f"uninstall_url={uninstall_url}")

    for field in PRESENTATION_FIELDS:
        value = (preserved_fields or {}).get(field, "")
        if value:
            lines.append(f"{field}={value}")

    if conflicts:
        lines.append(f"conflicts={conflicts}")
    if incompatible_platforms:
        lines.append(f"incompatible_platforms={incompatible_platforms}")

    lines.append(f"stars={stars}")
    if updated_at:
        lines.append(f"updated_at={updated_at}")
    if published_at:
        lines.append(f"published_at={published_at}")
    if prerelease_version:
        lines.append(f"prerelease_version={prerelease_version}")
    if prerelease_published_at:
        lines.append(f"prerelease_published_at={prerelease_published_at}")

    if readme_url and readme_hash:
        lines.extend([
            f"readme_url={readme_url}",
            f"readme_hash={readme_hash}",
        ])
    if release_notes_url and release_notes_hash:
        lines.extend([
            f"release_notes_url={release_notes_url}",
            f"release_notes_hash={release_notes_hash}",
        ])
    if prerelease_notes_url and prerelease_notes_hash:
        lines.extend([
            f"prerelease_notes_url={prerelease_notes_url}",
            f"prerelease_notes_hash={prerelease_notes_hash}",
        ])

    cached_releases = installable_releases(releases)
    if cached_releases:
        lines.append("releases=" + json.dumps(
            cached_releases, ensure_ascii=False, separators=(",", ":")
        ))

    summary = {
        "id": meta_id,
        "name": name,
        "kind": kind,
        "repo": full_name,
        "url": repo["html_url"],
        "stars": stars,
        "version": version,
        "category": category,
        "path": os.path.join("packages", "koreader", package_dir_name(meta_id, kind), ".meta"),
        "versions_path": os.path.join(
            "packages", "koreader", package_dir_name(meta_id, kind), "versions.json"
        ),
    }

    source_asset_aliases = {
        value.strip()
        for value in (preserved_fields or {}).get("source_asset_aliases", "").split(",")
        if value.strip()
    }
    canonical_zip_assets = [
        asset for asset in zip_assets
        if asset.get("name", "") not in source_asset_aliases
    ]

    if kind == KIND_PATCH and patch_assets is not None:
        lines.append("source_type=source")
        for i, asset in enumerate(patch_assets):
            lines.append(f"assets.{i}.arch=any")
            lines.append(f"assets.{i}.asset={asset['name']}")
            lines.append(f"assets.{i}.url={asset['url']}")
            lines.append(f"assets.{i}.size={asset.get('size', 0)}")
        summary["assets"] = len(patch_assets)
    elif len(zip_assets) >= 2:
        lines.append("source_type=release")
        if len(canonical_zip_assets) == 1:
            canonical_asset = canonical_zip_assets[0]
            lines.append(f"source_asset={canonical_asset.get('name', '')}")
            lines.append(f"size={canonical_asset.get('size', 0)}")
        for i, asset in enumerate(zip_assets):
            aname = asset.get("name", "")
            lines.append(f"assets.{i}.arch={detect_arch(aname)}")
            lines.append(f"assets.{i}.asset={aname}")
            lines.append(f"assets.{i}.url={asset.get('browser_download_url', '')}")
            lines.append(f"assets.{i}.size={asset.get('size', 0)}")
        summary["assets"] = len(zip_assets)
    elif len(zip_assets) == 1:
        asset = zip_assets[0]
        lines.append("source_type=release")
        lines.append(f"source_asset={asset.get('name', '')}")
        lines.append(f"size={asset.get('size', 0)}")
        summary["assets"] = 1
    else:
        codeload = f"https://codeload.github.com/{full_name}/zip/refs/heads/{default_branch}"
        lines.append("source_type=source")
        lines.append(f"source_url={codeload}")
        summary["assets"] = 0

    return meta_id, "\n".join(lines) + "\n", summary


def write_results(added, updated):
    gh_output = os.environ.get("GITHUB_OUTPUT")
    payload = json.dumps(added)
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as fh:
            fh.write(f"updated_count={len(updated)}\n")
            fh.write(f"updated={json.dumps(updated)}\n")
            fh.write(f"added_count={len(added)}\n")
            fh.write(f"added={payload}\n")
    print(payload)
