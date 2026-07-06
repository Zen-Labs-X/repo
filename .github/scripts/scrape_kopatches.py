#!/usr/bin/env python3
"""Scrape GitHub for KOReader user patch repos and generate package .meta files."""

import argparse
import os
import re
import sys
import urllib.parse

from scrape_common import (
    KIND_PATCH,
    KOREADER_DIR,
    MIN_STARS,
    PATCH_CATEGORY,
    build_meta,
    discover,
    existing_repo_refs,
    existing_scraped_meta,
    fetch_repo,
    fetch_tree,
    is_inactive,
    normalize_repo_ref,
    package_dir_name,
    token,
    write_results,
)

PATCH_QUERIES = (
    f"topic:koreader-user-patch stars:>={MIN_STARS} fork:true",
    f"KOReader.patches in:name stars:>={MIN_STARS} fork:true",
)


def looks_like_koreader_patch_repo(repo):
    name = repo.get("name", "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]
    if "koreader-user-patch" in topics:
        return True
    return name == "koreader.patches" or "koreader.patches" in name


def patch_assets(repo):
    branch = repo.get("default_branch") or "main"
    branch_url = urllib.parse.quote(branch, safe="")
    assets = []
    for item in fetch_tree(repo["full_name"], branch):
        if item.get("type") != "blob":
            continue
        path = item.get("path", "")
        filename = path.rsplit("/", 1)[-1]
        if not re.match(r"^[0-9].*\.lua$", filename):
            continue
        path_url = urllib.parse.quote(path, safe="/")
        assets.append({
            "name": filename,
            "path": path,
            "url": f"https://raw.githubusercontent.com/{repo['full_name']}/{branch_url}/{path_url}",
            "size": item.get("size", 0),
        })
    return sorted(assets, key=lambda item: item["path"].lower())


def main():
    parser = argparse.ArgumentParser(description="Scrape KOReader patches.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print planned .meta files without writing.")
    parser.add_argument("--exclude-forks", action="store_true",
                        help="Exclude forked repositories (default: include).")
    args = parser.parse_args()

    if not token():
        print("Warning: GITHUB_TOKEN not set — limited to 60 req/hr.",
              file=sys.stderr)

    known_refs, known_ids = existing_repo_refs()
    discovered = discover(PATCH_QUERIES)
    print(f"Discovered {len(discovered)} candidate patch repos.",
          file=sys.stderr)

    updated = []
    for record in existing_scraped_meta(PATCH_CATEGORY):
        repo = fetch_repo(record["ref"])
        if not repo:
            print(f"Could not refresh {record['rel_path']}: repo not found",
                  file=sys.stderr)
            continue

        assets = patch_assets(repo)
        if not assets:
            print(f"Could not refresh {record['rel_path']}: no patch files",
                  file=sys.stderr)
            continue

        _meta_id, meta_text, summary = build_meta(
            repo, None, known_ids, PATCH_CATEGORY, meta_id=record["id"],
            kind=KIND_PATCH, name_override=record["name"], patch_assets=assets
        )
        summary["path"] = record["rel_path"]

        if meta_text == record["content"]:
            continue

        if args.dry_run:
            print(f"\n--- {record['path']} ---")
            print(meta_text, end="")
        else:
            with open(record["path"], "w", encoding="utf-8") as fh:
                fh.write(meta_text)
            print(f"Updated {record['path']}", file=sys.stderr)

        updated.append(summary)

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

        repo = fetch_repo(full_name) or item
        if not looks_like_koreader_patch_repo(repo) and not looks_like_koreader_patch_repo(item):
            continue
        if repo.get("archived") or is_inactive(repo):
            continue

        assets = patch_assets(repo)
        if not assets:
            continue

        meta_id, meta_text, summary = build_meta(
            repo, None, known_ids, PATCH_CATEGORY, kind=KIND_PATCH,
            patch_assets=assets
        )
        known_refs.add(norm)

        dest_dir = os.path.join(KOREADER_DIR, package_dir_name(meta_id, KIND_PATCH))
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

    print(f"\n{len(updated)} refreshed patch package(s).", file=sys.stderr)
    print(f"\n{len(added)} new patch package(s).", file=sys.stderr)

    write_results(added, updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
