#!/usr/bin/env python3
"""Tests for reconciling scraped KOReader patch repositories."""

import os
import sys
import tempfile
import unittest
from unittest import mock

import scrape_common
import scrape_kopatches


class PatchScraperTests(unittest.TestCase):
    def test_renamed_repository_is_refreshed_without_duplicate_package(self):
        old_ref = "ameyrk99/koreader-patches-plugins"
        repo = {
            "owner": {"login": "ameyrk99"},
            "name": "koreader-bookshelf-screensaver",
            "full_name": "ameyrk99/koreader-bookshelf-screensaver",
            "html_url": (
                "https://github.com/ameyrk99/koreader-bookshelf-screensaver"
            ),
            "default_branch": "mainline",
            "stargazers_count": 15,
            "description": "Renamed patch repository",
            "topics": ["koreader-user-patch"],
            "archived": False,
            "fork": False,
        }
        assets = [{
            "name": "2-example.lua",
            "path": "2-example.lua",
            "url": "https://example.com/2-example.lua",
            "size": 123,
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            original_root = scrape_common.REPO_ROOT
            original_common_koreader_dir = scrape_common.KOREADER_DIR
            original_patch_koreader_dir = scrape_kopatches.KOREADER_DIR
            scrape_common.REPO_ROOT = temp_dir
            scrape_common.KOREADER_DIR = os.path.join(
                temp_dir, "packages", "koreader"
            )
            scrape_kopatches.KOREADER_DIR = scrape_common.KOREADER_DIR
            package_dir = os.path.join(
                scrape_common.KOREADER_DIR, "koreader-patches-plugins.kopatch"
            )
            os.makedirs(package_dir)
            meta_path = os.path.join(package_dir, ".meta")
            with open(meta_path, "w", encoding="utf-8") as fh:
                fh.write(
                    "# zenpm:auto-scraped\n"
                    "id=koreader-patches-plugins\n"
                    "name=Koreader Patches Plugins\n"
                    "version=source\n"
                    "category=patches\n"
                    f"source=https://github.com/{old_ref}\n"
                )
            try:
                with mock.patch.object(
                    scrape_kopatches, "discover",
                    return_value={repo["full_name"]: repo},
                ), mock.patch.object(
                    scrape_kopatches, "fetch_repo", return_value=repo
                ), mock.patch.object(
                    scrape_kopatches, "patch_assets", return_value=assets
                ), mock.patch.object(
                    scrape_kopatches, "fetch_releases", return_value=[]
                ), mock.patch.object(
                    scrape_kopatches, "cache_release_notes",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_kopatches, "cache_readme",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_kopatches, "load_blacklist", return_value=set()
                ), mock.patch.object(
                    scrape_kopatches, "scraper_timestamp",
                    return_value="2026-08-05T20:00:00Z",
                ), mock.patch.object(
                    scrape_kopatches, "token", return_value="token"
                ), mock.patch.object(
                    scrape_kopatches, "write_results"
                ) as write_results, mock.patch.object(
                    sys, "argv", ["scrape_kopatches.py"]
                ):
                    self.assertEqual(scrape_kopatches.main(), 0)
            finally:
                scrape_common.REPO_ROOT = original_root
                scrape_common.KOREADER_DIR = original_common_koreader_dir
                scrape_kopatches.KOREADER_DIR = original_patch_koreader_dir

            with open(meta_path, encoding="utf-8") as fh:
                meta = fh.read()
            self.assertIn("id=koreader-patches-plugins\n", meta)
            self.assertIn(
                "source=https://github.com/ameyrk99/"
                "koreader-bookshelf-screensaver\n",
                meta,
            )
            self.assertFalse(os.path.exists(os.path.join(
                temp_dir, "packages", "koreader",
                "koreader-bookshelf-screensaver.kopatch", ".meta",
            )))
            added, updated = write_results.call_args.args
            self.assertEqual(added, [])
            self.assertEqual(len(updated), 1)


if __name__ == "__main__":
    unittest.main()
