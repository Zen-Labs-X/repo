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
    cache_release_notes,
    cache_readme,
    classify_category,
    discover,
    existing_meta_categories,
    existing_repository_identities,
    existing_repo_refs,
    existing_scraped_meta,
    fetch_releases,
    fetch_repo,
    is_inactive,
    load_blacklist,
    load_category_cache,
    looks_like_koreader_patch_repo,
    make_id,
    newest_prerelease,
    newest_alpha_release,
    newest_stable_release,
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
    f"topic:koreader-plugins stars:>={MIN_STARS} fork:true",
    f"koplugin in:name stars:>={MIN_STARS} fork:true",
)

EXTRA_PLUGIN_REPOS = {
    "xzenlabs/zen-fm": {"id": "zenfm", "name": "ZenFM"},
    "xzenlabs/zen-pm": {"id": "zenpm", "name": "ZenPM"},
}


def is_koplugin(repo):
    if normalize_repo_ref(repo.get("full_name", "")) in EXTRA_PLUGIN_REPOS:
        return True
    name = repo.get("name", "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]
    if name.endswith(".koplugin") or "koplugin" in name:
        return True
    return (
        "koplugin" in topics
        or "koreader-plugin" in topics
        or "koreader-plugins" in topics
    )


def is_eligible_koplugin(repo, exclude_forks):
    extra = normalize_repo_ref(repo.get("full_name", "")) in EXTRA_PLUGIN_REPOS
    return (
        (extra or repo.get("stargazers_count", 0) >= MIN_STARS)
        and not repo.get("archived")
        and (not exclude_forks or not repo.get("fork"))
        and not is_inactive(repo)
        and is_koplugin(repo)
        and not looks_like_koreader_patch_repo(repo)
    )


def main():
    parser = argparse.ArgumentParser(description="Scrape KOReader plugins.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print planned .meta files without writing.")
    parser.add_argument("--exclude-forks", action="store_true",
                        help="Exclude forked repositories (default: include).")
    parser.add_argument("--package", metavar="ID",
                        help="Refresh only an existing package ID (skips discovery).")
    args = parser.parse_args()
    package_id = (args.package or "").strip()
    if args.package is not None and not package_id:
        parser.error("--package requires a non-empty package ID")
    scraped_at = scraper_timestamp()

    if not token():
        print("Warning: GITHUB_TOKEN not set — limited to 60 req/hr.",
              file=sys.stderr)

    known_refs, known_ids = existing_repo_refs()
    known_repository_identities = existing_repository_identities()
    blacklist = load_blacklist()
    discovered = {}
    if package_id:
        print(f"Refreshing only plugin package {package_id}.", file=sys.stderr)
    else:
        discovered = discover(PLUGIN_QUERIES)
        for ref in EXTRA_PLUGIN_REPOS:
            if ref in blacklist:
                continue
            repo = fetch_repo(ref)
            if repo:
                discovered.setdefault(repo.get("full_name", ref), repo)
            else:
                print(f"Could not discover required plugin {ref}", file=sys.stderr)
        print(f"Discovered {len(discovered)} candidate plugin repos.",
              file=sys.stderr)

    category_cache = load_category_cache()
    category_cache.update(existing_meta_categories())
    eligible_manual_refs = {
        normalize_repo_ref(full_name)
        for full_name, repo in discovered.items()
        if normalize_repo_ref(full_name) in known_refs
        and normalize_repo_ref(full_name) not in blacklist
        and is_eligible_koplugin(repo, args.exclude_forks)
    }

    records = existing_scraped_meta(include_refs=eligible_manual_refs)
    if package_id:
        records = [record for record in records if record["id"] == package_id]
        if not records:
            print(f"Could not find scraped plugin package {package_id!r}.",
                  file=sys.stderr)
            return 1

    updated = []
    for record in records:
        if record["ref"] in blacklist or record["category"] == "patches":
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

        full_name = repo.get("full_name", record["ref"])
        releases = fetch_releases(full_name)
        if releases is None:
            print(f"Could not refresh {record['rel_path']}: releases unavailable",
                  file=sys.stderr)
            continue
        release = newest_stable_release(releases)
        prerelease = newest_prerelease(releases)
        alpha = newest_alpha_release(releases) if record["id"] == "zen-ui" else None
        package_dir = os.path.dirname(record["path"])
        release_notes_url, release_notes_hash, release_notes_changed, release_notes_resolved = cache_release_notes(
            releases, package_dir, args.dry_run
        )
        if not release_notes_resolved:
            print(f"Could not refresh {record['rel_path']}: release notes unavailable",
                  file=sys.stderr)
            continue
        prerelease_notes_url, prerelease_notes_hash, prerelease_notes_changed, prerelease_notes_resolved = cache_release_notes(
            releases, package_dir, args.dry_run, "PRERELEASE_NOTES.md", prerelease=True
        )
        if not prerelease_notes_resolved:
            print(f"Could not refresh {record['rel_path']}: prerelease notes unavailable",
                  file=sys.stderr)
            continue
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
            release_notes_url=release_notes_url, release_notes_hash=release_notes_hash,
            prerelease=prerelease, prerelease_notes_url=prerelease_notes_url,
            prerelease_notes_hash=prerelease_notes_hash,
            releases=releases, preserved_fields=record["fields"], scraped_at=scraped_at,
            alpha=alpha,
        )
        summary["path"] = record["rel_path"]
        summary["versions_path"] = os.path.join(
            os.path.dirname(record["rel_path"]), "versions.json"
        )

        if (meta_text == record["content"] and not readme_changed
                and not release_notes_changed and not prerelease_notes_changed):
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
        if release_notes_changed:
            summary["release_notes_path"] = os.path.join(
                os.path.dirname(record["rel_path"]), "RELEASE_NOTES.md"
            )
        if prerelease_notes_changed:
            summary["prerelease_notes_path"] = os.path.join(
                os.path.dirname(record["rel_path"]), "PRERELEASE_NOTES.md"
            )

        updated.append(summary)

    added = []
    for full_name, item in sorted(discovered.items()):
        norm = normalize_repo_ref(full_name)
        if norm in blacklist or norm in known_refs:
            continue
        repo = item
        if is_koplugin(repo) and looks_like_koreader_patch_repo(repo):
            print(f"Skipping unsupported mixed patch/plugin repository {full_name}",
                  file=sys.stderr)
            continue
        if not is_eligible_koplugin(repo, args.exclude_forks):
            continue

        extra = EXTRA_PLUGIN_REPOS.get(norm)
        candidate_id = extra["id"] if extra else make_id(repo.get("name", ""), set())
        candidate_identity = repository_identity(repo.get("full_name", full_name))
        if candidate_id in known_ids or candidate_identity in known_repository_identities:
            print(f"Skipping duplicate package {full_name}", file=sys.stderr)
            continue

        category = category_cache.get(norm) or classify_category(repo)
        category_cache[norm] = category

        releases = fetch_releases(full_name)
        if releases is None:
            print(f"Could not add {full_name}: releases unavailable", file=sys.stderr)
            continue
        release = newest_stable_release(releases)
        prerelease = newest_prerelease(releases)
        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, category, meta_id=candidate_id,
            kind=KIND_PLUGIN, name_override=extra["name"] if extra else None,
            releases=releases, scraped_at=scraped_at
        )
        known_refs.add(norm)
        if candidate_identity:
            known_repository_identities.add(candidate_identity)

        dest_dir = os.path.join(KOREADER_DIR, package_dir_name(meta_id, KIND_PLUGIN))
        dest = os.path.join(dest_dir, ".meta")
        release_notes_url, release_notes_hash, _release_notes_changed, _release_notes_resolved = cache_release_notes(
            releases, dest_dir, args.dry_run
        )
        prerelease_notes_url, prerelease_notes_hash, _prerelease_notes_changed, _prerelease_notes_resolved = cache_release_notes(
            releases, dest_dir, args.dry_run, "PRERELEASE_NOTES.md", prerelease=True
        )
        readme_url, readme_hash, _readme_changed, _readme_resolved = cache_readme(
            repo.get("full_name", full_name), dest_dir, args.dry_run
        )
        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, category, meta_id=meta_id,
            kind=KIND_PLUGIN, name_override=extra["name"] if extra else None,
            readme_url=readme_url, readme_hash=readme_hash,
            release_notes_url=release_notes_url, release_notes_hash=release_notes_hash,
            prerelease=prerelease, prerelease_notes_url=prerelease_notes_url,
            prerelease_notes_hash=prerelease_notes_hash,
            releases=releases, scraped_at=scraped_at,
        )
        if readme_url:
            summary["readme_path"] = readme_url
        if release_notes_url:
            summary["release_notes_path"] = release_notes_url
        if prerelease_notes_url:
            summary["prerelease_notes_path"] = prerelease_notes_url

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
