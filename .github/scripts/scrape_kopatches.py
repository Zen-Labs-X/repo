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
    cache_release_notes,
    cache_readme,
    discover,
    existing_repo_refs,
    existing_repository_identities,
    existing_scraped_meta,
    fetch_releases,
    fetch_repo,
    fetch_tree,
    is_inactive,
    load_blacklist,
    looks_like_koreader_patch_repo,
    make_id,
    newest_prerelease,
    newest_stable_release,
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


def is_eligible_patch_repo(repo, exclude_forks):
    return (
        repo.get("stargazers_count", 0) >= MIN_STARS
        and not repo.get("archived")
        and (not exclude_forks or not repo.get("fork"))
        and not is_inactive(repo)
        and looks_like_koreader_patch_repo(repo)
    )


def patch_assets(repo):
    branch = repo.get("default_branch") or "main"
    branch_url = urllib.parse.quote(branch, safe="")
    tree = fetch_tree(repo["full_name"], branch)
    if any(
        item.get("type") == "tree"
        and any(part.lower().endswith(".koplugin") for part in item.get("path", "").split("/"))
        for item in tree
    ):
        return None

    assets = []
    for item in tree:
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
    blacklist = load_blacklist()
    discovered = discover(PATCH_QUERIES)
    print(f"Discovered {len(discovered)} candidate patch repos.",
          file=sys.stderr)

    eligible_manual_refs = {
        normalize_repo_ref(full_name)
        for full_name, repo in discovered.items()
        if normalize_repo_ref(full_name) in known_refs
        and normalize_repo_ref(full_name) not in blacklist
        and is_eligible_patch_repo(repo, args.exclude_forks)
    }

    updated = []
    for record in existing_scraped_meta(PATCH_CATEGORY, eligible_manual_refs):
        if record["ref"] in blacklist:
            continue
        repo = fetch_repo(record["ref"])
        if not repo:
            print(f"Could not refresh {record['rel_path']}: repo not found",
                  file=sys.stderr)
            continue

        canonical_ref = normalize_repo_ref(repo.get("full_name", record["ref"]))
        if canonical_ref:
            known_refs.add(canonical_ref)
        canonical_identity = repository_identity(canonical_ref)
        if canonical_identity:
            known_repository_identities.add(canonical_identity)

        full_name = repo.get("full_name", record["ref"])
        assets = patch_assets(repo)
        if assets is None:
            print(f"Skipping unsupported mixed patch/plugin repository {full_name}",
                  file=sys.stderr)
            continue
        if not assets:
            print(f"Could not refresh {record['rel_path']}: no patch files",
                  file=sys.stderr)
            continue
        releases = fetch_releases(full_name)
        if releases is None:
            print(f"Could not refresh {record['rel_path']}: releases unavailable",
                  file=sys.stderr)
            continue
        release = newest_stable_release(releases)
        prerelease = newest_prerelease(releases)

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
            repo, release, known_ids, PATCH_CATEGORY, meta_id=record["id"],
            kind=KIND_PATCH, name_override=record["name"], patch_assets=assets,
            readme_url=readme_url, readme_hash=readme_hash,
            release_notes_url=release_notes_url, release_notes_hash=release_notes_hash,
            prerelease=prerelease, prerelease_notes_url=prerelease_notes_url,
            prerelease_notes_hash=prerelease_notes_hash,
            releases=releases, preserved_fields=record["fields"], scraped_at=scraped_at,
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
        if not is_eligible_patch_repo(repo, args.exclude_forks):
            continue

        candidate_id = make_id(repo.get("name", ""), set())
        candidate_identity = repository_identity(repo.get("full_name", full_name))
        if candidate_id in known_ids or candidate_identity in known_repository_identities:
            print(f"Skipping duplicate package {full_name}", file=sys.stderr)
            continue

        assets = patch_assets(repo)
        if assets is None:
            print(f"Skipping unsupported mixed patch/plugin repository {full_name}",
                  file=sys.stderr)
            continue
        if not assets:
            continue
        full_name = repo.get("full_name", full_name)
        releases = fetch_releases(full_name)
        if releases is None:
            print(f"Could not add {full_name}: releases unavailable", file=sys.stderr)
            continue
        release = newest_stable_release(releases)
        prerelease = newest_prerelease(releases)

        meta_id, meta_text, summary = build_meta(
            repo, release, known_ids, PATCH_CATEGORY, kind=KIND_PATCH,
            patch_assets=assets, releases=releases, scraped_at=scraped_at,
        )
        known_refs.add(norm)
        if candidate_identity:
            known_repository_identities.add(candidate_identity)

        dest_dir = os.path.join(KOREADER_DIR, package_dir_name(meta_id, KIND_PATCH))
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
            repo, release, known_ids, PATCH_CATEGORY, meta_id=meta_id,
            kind=KIND_PATCH, patch_assets=assets, readme_url=readme_url,
            readme_hash=readme_hash, release_notes_url=release_notes_url,
            release_notes_hash=release_notes_hash, prerelease=prerelease,
            prerelease_notes_url=prerelease_notes_url,
            prerelease_notes_hash=prerelease_notes_hash, releases=releases,
            scraped_at=scraped_at,
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

    print(f"\n{len(updated)} refreshed patch package(s).", file=sys.stderr)
    print(f"\n{len(added)} new patch package(s).", file=sys.stderr)

    write_results(added, updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
