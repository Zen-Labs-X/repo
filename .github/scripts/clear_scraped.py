#!/usr/bin/env python3
"""Remove auto-scraped KOReader plugin folders.

Deletes every `packages/koreader/<id>.koplugin/` or `.kopatch/` whose `.meta` carries the
`zenpm:auto-scraped` marker written by scrape_koplugins.py. Hand-added plugins
(no marker) are left untouched.

Use --dry-run to preview. The plugin_categories.json cache is kept by default
so manual category corrections survive a re-scrape; pass --clear-cache to wipe
it too.
"""

import argparse
import os
import shutil
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KOREADER_DIR = os.path.join(REPO_ROOT, "packages", "koreader")
CATEGORY_CACHE = os.path.join(os.path.dirname(__file__), "plugin_categories.json")
SCRAPED_MARKER = "zenpm:auto-scraped"


def is_scraped(meta_path):
    try:
        with open(meta_path, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") and SCRAPED_MARKER in line:
                    return True
                # Marker lives in the header; stop once past the comments.
                if line.strip() and not line.startswith("#"):
                    return False
    except OSError:
        return False
    return False


def main():
    parser = argparse.ArgumentParser(description="Clear auto-scraped plugins.")
    parser.add_argument("--dry-run", action="store_true",
                        help="List what would be removed without deleting.")
    parser.add_argument("--clear-cache", action="store_true",
                        help="Also delete plugin_categories.json (kept by default "
                             "so manual category edits survive a re-scrape).")
    args = parser.parse_args()

    if not os.path.isdir(KOREADER_DIR):
        print(f"No such directory: {KOREADER_DIR}", file=sys.stderr)
        return 1

    removed = 0
    kept = 0
    for entry in sorted(os.listdir(KOREADER_DIR)):
        path = os.path.join(KOREADER_DIR, entry)
        meta = os.path.join(path, ".meta")
        if not os.path.isdir(path) or not os.path.isfile(meta):
            continue
        if is_scraped(meta):
            if args.dry_run:
                print(f"would remove {entry}")
            else:
                shutil.rmtree(path)
                print(f"removed {entry}")
            removed += 1
        else:
            kept += 1

    if args.clear_cache and os.path.isfile(CATEGORY_CACHE):
        if args.dry_run:
            print(f"would remove {os.path.relpath(CATEGORY_CACHE, REPO_ROOT)}")
        else:
            os.remove(CATEGORY_CACHE)
            print(f"removed {os.path.relpath(CATEGORY_CACHE, REPO_ROOT)}")

    verb = "would remove" if args.dry_run else "removed"
    print(f"\n{verb} {removed} scraped plugin(s); kept {kept} manual.",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
