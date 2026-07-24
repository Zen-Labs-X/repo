#!/usr/bin/env python3
"""Scrape GitHub for KOReader plugins and generate package .meta files."""

import argparse
import os
import sys

from scrape_common import (
    KIND_PLUGIN,
    KOREADER_DIR,
    MIN_STARS,
    VALID_CATEGORIES,
    build_meta,
    cache_readme,
    classify_category,
    discover,
    existing_meta_categories,
    existing_repository_identities,
    existing_repo_refs,
    existing_scraped_meta,
    fetch_release,
    fetch_repo,
    is_inactive,
    load_category_cache,
    make_id,
    normalize_repo_ref,
    package_dir_name,
    repository_identity,
    scraper_timestamp,
    save_category_cache,
    token,
    write_results,
)

PLUGIN_QUERIES = (
    f"topic:koplugin stars:>={MIN_STARS} fork:true",
    f"topic:koreader-plugin stars:>={MIN_STARS} fork:true",
    f"koplugin in:name stars:>={MIN_STARS} fork:true",
    f"koreader-plugin in:name stars:>={MIN_STARS} fork:true",
)


def is_koplugin(repo):
    name = repo.get("name", "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]
    if name.endswith(".koplugin") or "koplugin" in name:
        return True
    return "koplugin" in topics or "koreader-plugin" in topics


def main():
    parser = argparse.ArgumentParser(description="Scrape KOReader plugins.")
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
    discovered = discover(PLUGIN_QUERIES)
    print(f"Discovered {len(discovered)} candidate plugin repos.",
          file=sys.stderr)

    category_cache = load_category_cache()
    category_cache.update(existing_meta_categories())

    updated = []
    for record in existing_scraped_meta():
        if record["category"] == "patches":
            continue
        repo = fetch_repo(record["ref"])
        if not repo:
            print(f"Could not refresh {record['rel_path']}: repo not found",
                  file=sys.stderr)
            continue

        repo_norm = normalize_repo_ref(repo.get("full_name", record["ref"]))
        category = (
            category_cache.get(record["ref"])
            or category_cache.get(repo_norm)
            or (record["category"] if record["category"] in VALID_CATEGORIES else "")
            or classify_category(repo)
        )
        category_cache[repo_norm] = category

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
            repo, release, known_ids, category, meta_id=record["id"],
            kind=KIND_PLUGIN, name_override=record["name"],
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
        if not is_koplugin(repo) and not is_koplugin(item):
            continue
        if repo.get("archived") or is_inactive(repo):
            continue

        candidate_id = make_id(repo.get("name", ""), set())
        candidate_identity = repository_identity(repo.get("full_name", full_name))
        if candidate_id in known_ids or candidate_identity in known_repository_identities:
            print(f"Skipping duplicate package {full_name}", file=sys.stderr)
            continue

        category = category_cache.get(norm) or classify_category(repo)
        category_cache[norm] = category

        release = fetch_release(full_name)
        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, category, kind=KIND_PLUGIN, scraped_at=scraped_at
        )
        known_refs.add(norm)
        if candidate_identity:
            known_repository_identities.add(candidate_identity)

        dest_dir = os.path.join(KOREADER_DIR, package_dir_name(meta_id, KIND_PLUGIN))
        dest = os.path.join(dest_dir, ".meta")
        readme_url, readme_hash, _readme_changed, _readme_resolved = cache_readme(
            repo.get("full_name", full_name), dest_dir, args.dry_run
        )
        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, category, meta_id=meta_id,
            kind=KIND_PLUGIN, readme_url=readme_url, readme_hash=readme_hash,
            scraped_at=scraped_at,
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

    print(f"\n{len(updated)} refreshed plugin(s).", file=sys.stderr)
    print(f"\n{len(added)} new plugin(s).", file=sys.stderr)

    if not args.dry_run:
        save_category_cache(category_cache)

    write_results(added, updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
