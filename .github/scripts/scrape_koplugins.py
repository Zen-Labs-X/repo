#!/usr/bin/env python3
"""Scrape GitHub for KOReader plugins and generate package .meta files.

Discovers repos with >15 stars that either carry the `koplugin` topic or have
`koplugin` in the name, then writes a fully-populated
`packages/koreader/<id>.koplugin/.meta` for each one not already in the repo.

Stdlib only — runs in GitHub Actions with no pip install. Reads GITHUB_TOKEN
from the environment for a 5000 req/hr rate limit (60/hr unauthenticated).
"""

import argparse
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
# Persisted owner/repo -> category map so categories survive reruns and can be
# corrected by hand without the scraper clobbering them.
CATEGORY_CACHE = os.path.join(os.path.dirname(__file__), "plugin_categories.json")

# Marker comment written into every auto-generated .meta so the clear utility
# can distinguish scraped plugins from hand-added ones.
SCRAPED_MARKER = "zenpm:auto-scraped"

MIN_STARS = 15  # Minimum stars to include (inclusive).
MAX_INACTIVE_DAYS = 730  # Skip repos with no push in ~2 years.
INSTALL_URL = "packages/koreader/install-plugin.sh"
UNINSTALL_URL = "packages/koreader/uninstall-plugin.sh"

# Arch tokens recognised in release asset filenames, longest/most-specific first.
# Maps a regex (word-boundary-ish) to the canonical arch label written to .meta.
ARCH_PATTERNS = [
    (r"aarch64|arm64", "arm64"),
    (r"armv7|armhf|armel", "armv7"),
    (r"x86[_-]?64|amd64", "x86_64"),
    (r"i686|i386|x86", "x86"),
    (r"\barm\b", "arm"),
    (r"kindle", "kindle"),
    (r"kobo", "kobo"),
]

# Valid manifest categories (must match generate-manifest.sh validation).
VALID_CATEGORIES = ("utility", "games", "productivity", "media", "theme")
DEFAULT_CATEGORY = "utility"

# Keyword -> category, most-specific categories checked first. Each keyword is
# matched against the repo name, description, and topics.
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


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def _token():
    return os.environ.get("GITHUB_TOKEN", "").strip()


def http_json(url):
    """GET a URL and parse JSON. Returns (status, parsed_or_None, headers)."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "zenpm-koplugin-scraper")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    tok = _token()
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode("utf-8")
            return resp.status, json.loads(data), dict(resp.headers)
    except urllib.error.HTTPError as e:
        # 404 is expected (e.g. no latest release) — let caller decide.
        body = e.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(body)
        except ValueError:
            parsed = None
        return e.code, parsed, dict(e.headers or {})


def _respect_rate_limit(headers):
    """Sleep if we are about to exhaust the search rate limit window."""
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


# --------------------------------------------------------------------------
# Search
# --------------------------------------------------------------------------

def search_repos(query):
    """Yield repo items for a search query, following pagination."""
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page,
        })
        url = f"{API}/search/repositories?{params}"
        status, data, headers = http_json(url)
        if status != 200 or not data:
            if status == 403:
                _respect_rate_limit(headers)
                continue
            print(f"Search failed ({status}) for {query!r}", file=sys.stderr)
            return
        items = data.get("items", [])
        for item in items:
            yield item
        _respect_rate_limit(headers)
        if len(items) < 100 or page >= 10:  # Search API caps at 1000 results.
            return
        page += 1


def discover():
    """Return a dict full_name -> repo item, merged across both queries."""
    found = {}
    # `fork:true` makes the Search API include forks (excluded by default).
    for query in (
        f"topic:koplugin stars:>={MIN_STARS} fork:true",
        f"topic:koreader-plugin stars:>={MIN_STARS} fork:true",
        f"koplugin in:name stars:>={MIN_STARS} fork:true",
        f"koreader-plugin in:name stars:>={MIN_STARS} fork:true",
    ):
        for item in search_repos(query):
            found.setdefault(item["full_name"], item)
    return found


# --------------------------------------------------------------------------
# Existing-plugin detection (idempotency)
# --------------------------------------------------------------------------

def normalize_repo_ref(ref):
    """Reduce a GitHub URL/ref to lowercase 'owner/repo'. Returns '' if none."""
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


def existing_repo_refs():
    """Scan all packages/**/.meta files for known source repos and ids."""
    known_refs = set()
    known_ids = set()
    pkg_root = os.path.join(REPO_ROOT, "packages")
    for dirpath, _dirs, files in os.walk(pkg_root):
        if ".meta" not in files:
            continue
        meta = os.path.join(dirpath, ".meta")
        try:
            with open(meta, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line.startswith("source="):
                        ref = normalize_repo_ref(line[len("source="):])
                        if ref:
                            known_refs.add(ref)
                    elif line.startswith("id="):
                        known_ids.add(line[len("id="):].strip())
        except OSError:
            continue
    return known_refs, known_ids


# --------------------------------------------------------------------------
# Field derivation
# --------------------------------------------------------------------------

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def make_id(repo_name, existing_ids):
    stripped = re.sub(r"\.koplugin$", "", repo_name, flags=re.IGNORECASE)
    base = slugify(stripped) or slugify(repo_name)
    candidate = base
    n = 2
    while candidate in existing_ids:
        candidate = f"{base}-{n}"
        n += 1
    return candidate


def display_name(repo_name):
    name = re.sub(r"\.koplugin$", "", repo_name, flags=re.IGNORECASE)
    name = re.sub(r"[_-]+", " ", name).strip()
    return name.title() if name else repo_name


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
    """Best-effort category from repo name, description, and topics."""
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
    # Normalise keys and drop anything no longer a valid category.
    return {
        k.lower(): v for k, v in data.items()
        if v in VALID_CATEGORIES
    }


def existing_meta_categories():
    """owner/repo -> category already written in packages/**/.meta."""
    result = {}
    pkg_root = os.path.join(REPO_ROOT, "packages")
    for dirpath, _dirs, files in os.walk(pkg_root):
        if ".meta" not in files:
            continue
        ref = ""
        category = ""
        try:
            with open(os.path.join(dirpath, ".meta"), "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line.startswith("source="):
                        ref = normalize_repo_ref(line[len("source="):])
                    elif line.startswith("category="):
                        category = line[len("category="):].strip()
        except OSError:
            continue
        if ref and category in VALID_CATEGORIES:
            result[ref] = category
    return result


def save_category_cache(cache):
    with open(CATEGORY_CACHE, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(cache.items())), fh, indent=2)
        fh.write("\n")


# --------------------------------------------------------------------------
# Meta building
# --------------------------------------------------------------------------

def build_meta(repo, release, existing_ids, category):
    """Return (meta_id, meta_text, summary_dict) for one repo."""
    owner = repo["owner"]["login"]
    repo_name = repo["name"]
    full_name = repo["full_name"]
    meta_id = make_id(repo_name, existing_ids)
    existing_ids.add(meta_id)

    name = display_name(repo_name)
    stars = repo.get("stargazers_count", 0)
    description = clean_description(repo.get("description"))
    default_branch = repo.get("default_branch", "main")

    lines = []
    lines.append(f"# {name} plugin for KOReader")
    lines.append(f"# {repo['html_url']}")
    lines.append(f"# {SCRAPED_MARKER}")
    lines.append(f"id={meta_id}")
    lines.append(f"name={name}")

    # Collect zip assets from the latest release, if any.
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

    lines.append(f"version={version}")
    lines.append(f"description={description}")
    lines.append(f"author={owner}")
    lines.append(f"category={category}")
    lines.append("platforms=koreader")
    lines.append("dependencies=")
    lines.append(f"source={repo['html_url']}")
    lines.append(f"install_url={INSTALL_URL}")
    lines.append(f"uninstall_url={UNINSTALL_URL}")
    lines.append(f"stars={stars}")

    summary = {
        "id": meta_id,
        "name": name,
        "repo": full_name,
        "url": repo["html_url"],
        "stars": stars,
        "version": version,
        "category": category,
    }

    if len(zip_assets) >= 2:
        # Multi-asset: emit assets.N.* blocks for client arch selection.
        lines.append("source_type=release")
        for i, asset in enumerate(zip_assets):
            aname = asset.get("name", "")
            lines.append(f"assets.{i}.arch={detect_arch(aname)}")
            lines.append(f"assets.{i}.asset={aname}")
            lines.append(f"assets.{i}.url={asset.get('browser_download_url', '')}")
            lines.append(f"assets.{i}.size={asset.get('size', 0)}")
        summary["assets"] = len(zip_assets)
    elif len(zip_assets) == 1:
        # Single release asset: keep legacy source_asset/size fields.
        asset = zip_assets[0]
        lines.append("source_type=release")
        lines.append(f"source_asset={asset.get('name', '')}")
        lines.append(f"size={asset.get('size', 0)}")
        summary["assets"] = 1
    else:
        # No release asset: install from the source branch zip.
        codeload = (
            f"https://codeload.github.com/{full_name}/zip/refs/heads/{default_branch}"
        )
        lines.append("source_type=source")
        lines.append(f"source_url={codeload}")
        summary["assets"] = 0

    return meta_id, "\n".join(lines) + "\n", summary


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def fetch_release(full_name):
    status, data, _headers = http_json(
        f"{API}/repos/{full_name}/releases/latest"
    )
    if status == 200:
        return data
    return None


def fetch_repo(full_name):
    status, data, _headers = http_json(f"{API}/repos/{full_name}")
    if status == 200:
        return data
    return None


def is_koplugin(repo):
    name = repo.get("name", "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]
    if name.endswith(".koplugin") or "koplugin" in name:
        return True
    return "koplugin" in topics or "koreader-plugin" in topics


def is_inactive(repo):
    """True if the repo has had no push within MAX_INACTIVE_DAYS."""
    pushed = repo.get("pushed_at")
    if not pushed:
        return False
    try:
        when = datetime.datetime.strptime(pushed, "%Y-%m-%dT%H:%M:%SZ")
    except (ValueError, TypeError):
        return False
    age = datetime.datetime.utcnow() - when
    return age.days > MAX_INACTIVE_DAYS


def main():
    parser = argparse.ArgumentParser(description="Scrape KOReader plugins.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print planned .meta files without writing.")
    parser.add_argument("--exclude-forks", action="store_true",
                        help="Exclude forked repositories (default: include).")
    args = parser.parse_args()

    if not _token():
        print("Warning: GITHUB_TOKEN not set — limited to 60 req/hr.",
              file=sys.stderr)

    known_refs, known_ids = existing_repo_refs()
    discovered = discover()
    print(f"Discovered {len(discovered)} candidate repos.", file=sys.stderr)

    # Category persistence: existing .meta wins, then the cache, then heuristic.
    # Seed the cache with whatever the committed .meta files already declare so a
    # hand-edited category is never lost on rerun.
    category_cache = load_category_cache()
    category_cache.update(existing_meta_categories())

    added = []
    for full_name, item in sorted(discovered.items()):
        norm = normalize_repo_ref(full_name)
        if norm in known_refs:
            continue
        if item.get("stargazers_count", 0) < MIN_STARS:
            continue
        if item.get("archived"):
            continue
        if item.get("fork") and args.exclude_forks:
            continue
        if is_inactive(item):
            continue

        # The search item carries topics+stars, but fetch full detail for
        # default_branch and an authoritative star count.
        repo = fetch_repo(full_name) or item
        if not is_koplugin(repo) and not is_koplugin(item):
            continue
        # Re-check with authoritative detail (archived/pushed_at may differ).
        if repo.get("archived") or is_inactive(repo):
            continue

        # Resolve category: cached value (incl. existing .meta) wins so manual
        # corrections persist; otherwise classify by keywords.
        category = category_cache.get(norm) or classify_category(repo)
        category_cache[norm] = category

        release = fetch_release(full_name)
        meta_id, meta_text, summary = build_meta(repo, release, known_ids, category)
        known_refs.add(norm)

        dest_dir = os.path.join(KOREADER_DIR, f"{meta_id}.koplugin")
        dest = os.path.join(dest_dir, ".meta")

        if args.dry_run:
            print(f"\n--- {dest} ---")
            print(meta_text, end="")
        else:
            os.makedirs(dest_dir, exist_ok=True)
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(meta_text)
            print(f"Wrote {dest}", file=sys.stderr)

        added.append(summary)

    print(f"\n{len(added)} new plugin(s).", file=sys.stderr)

    if not args.dry_run:
        save_category_cache(category_cache)

    # Machine-readable summary for the workflow.
    gh_output = os.environ.get("GITHUB_OUTPUT")
    payload = json.dumps(added)
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as fh:
            fh.write(f"added_count={len(added)}\n")
            fh.write(f"added={payload}\n")
    print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
