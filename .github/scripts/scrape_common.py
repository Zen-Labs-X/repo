#!/usr/bin/env python3
"""Shared helpers for GitHub-backed KOReader package scrapers."""

import datetime
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
SCRAPED_MARKER = "zenpm:auto-scraped"

MIN_STARS = 15
MAX_INACTIVE_DAYS = 730

KIND_PLUGIN = "plugin"
KIND_PATCH = "patch"

PLUGIN_INSTALL_URL = "packages/koreader/install-plugin.sh"
PLUGIN_UNINSTALL_URL = "packages/koreader/uninstall-plugin.sh"
PATCH_INSTALL_URL = "packages/koreader/install-patch.sh"
PATCH_UNINSTALL_URL = "packages/koreader/uninstall-patch.sh"

VALID_CATEGORIES = ("utility", "games", "productivity", "media", "theme", "patches")
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


def fetch_release(full_name):
    status, data, _headers = http_json(f"{API}/repos/{full_name}/releases/latest")
    if status == 200:
        return data
    return None


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


def existing_scraped_meta(category=None):
    records = []
    for dirpath, _dirs, files in os.walk(KOREADER_DIR):
        if ".meta" not in files:
            continue
        meta_path = os.path.join(dirpath, ".meta")
        fields, scraped, content = parse_meta(meta_path)
        if category is not None and fields.get("category", "").strip() != category:
            continue
        ref = normalize_repo_ref(fields.get("source", ""))
        meta_id = fields.get("id", "").strip()
        if scraped and ref and meta_id:
            records.append({
                "path": meta_path,
                "rel_path": os.path.relpath(meta_path, REPO_ROOT),
                "ref": ref,
                "id": meta_id,
                "name": fields.get("name", "").strip(),
                "category": fields.get("category", "").strip(),
                "content": content,
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


def build_meta(repo, release, existing_ids, category, meta_id=None, kind=KIND_PLUGIN,
               name_override=None, patch_assets=None):
    owner = repo["owner"]["login"]
    repo_name = repo["name"]
    full_name = repo["full_name"]
    if meta_id is None:
        meta_id = make_id(repo_name, existing_ids)
    existing_ids.add(meta_id)

    name = name_override or display_name(repo_name)
    stars = repo.get("stargazers_count", 0)
    description = clean_description(repo.get("description"))
    default_branch = repo.get("default_branch", "main")
    install_url = PATCH_INSTALL_URL if kind == KIND_PATCH else PLUGIN_INSTALL_URL
    uninstall_url = PATCH_UNINSTALL_URL if kind == KIND_PATCH else PLUGIN_UNINSTALL_URL
    package_label = "patch" if kind == KIND_PATCH else "plugin"

    lines = [
        f"# {name} {package_label} for KOReader",
        f"# {repo['html_url']}",
        f"# {SCRAPED_MARKER}",
        f"id={meta_id}",
        f"name={name}",
    ]

    zip_assets = []
    version = "0.0.0-source"
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
        f"author={owner}",
        f"category={category}",
        "platforms=koreader",
        "dependencies=",
        f"source={repo['html_url']}",
        f"install_url={install_url}",
        f"uninstall_url={uninstall_url}",
        f"stars={stars}",
    ])

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
    }

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
