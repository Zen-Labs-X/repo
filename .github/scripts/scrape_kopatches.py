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
    cache_readme,
    discover,
    existing_repo_refs,
    existing_repository_identities,
    existing_scraped_meta,
    fetch_release,
    fetch_repo,
    fetch_tree,
    is_inactive,
    make_id,
    normalize_repo_ref,
    package_dir_name,
    repository_identity,
    scraper_timestamp,
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
    scraped_at = scraper_timestamp()

    if not token():
        print("Warning: GITHUB_TOKEN not set — limited to 60 req/hr.",
              file=sys.stderr)

    known_refs, known_ids = existing_repo_refs()
    known_repository_identities = existing_repository_identities()
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
        release = fetch_release(repo.get("full_name", record["ref"]))

        package_dir = os.path.dirname(record["path"])
        readme_url, readme_hash, readme_changed, readme_resolved = cache_readme(
            repo.get("full_name", record["ref"]), package_dir, args.dry_run
        )
        if not readme_resolved:
            print(f"Could not refresh {record['rel_path']}: README unavailable",
                  file=sys.stderr)
            continue
        _meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, PATCH_CATEGORY, meta_id=record["id"],
            kind=KIND_PATCH, name_override=record["name"], patch_assets=assets,
            readme_url=readme_url, readme_hash=readme_hash,
            preserved_fields=record["fields"], scraped_at=scraped_at,
        )
        summary["path"] = record["rel_path"]

        if meta_text == record["content"] and not readme_changed:
            continue

        if args.dry_run and meta_text != record["content"]:
            print(f"\n--- {record['path']} ---")
            print(meta_text, end="")
        elif not args.dry_run and meta_text != record["content"]:
            with open(record["path"], "w", encoding="utf-8") as fh:
                fh.write(meta_text)
            print(f"Updated {record['path']}", file=sys.stderr)

        if readme_changed:
            summary["readme_path"] = os.path.join(
                os.path.dirname(record["rel_path"]), "README.md"
            )

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

        candidate_id = make_id(repo.get("name", ""), set())
        candidate_identity = repository_identity(repo.get("full_name", full_name))
        if candidate_id in known_ids or candidate_identity in known_repository_identities:
            print(f"Skipping duplicate package {full_name}", file=sys.stderr)
            continue

        assets = patch_assets(repo)
        if not assets:
            continue
        release = fetch_release(repo.get("full_name", full_name))

        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, PATCH_CATEGORY, kind=KIND_PATCH,
            patch_assets=assets, scraped_at=scraped_at,
        )
        known_refs.add(norm)
        if candidate_identity:
            known_repository_identities.add(candidate_identity)

        dest_dir = os.path.join(KOREADER_DIR, package_dir_name(meta_id, KIND_PATCH))
        dest = os.path.join(dest_dir, ".meta")
        readme_url, readme_hash, _readme_changed, _readme_resolved = cache_readme(
            repo.get("full_name", full_name), dest_dir, args.dry_run
        )
        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, PATCH_CATEGORY, meta_id=meta_id,
            kind=KIND_PATCH, patch_assets=assets, readme_url=readme_url,
            readme_hash=readme_hash, scraped_at=scraped_at,
        )
        if readme_url:
            summary["readme_path"] = readme_url

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
