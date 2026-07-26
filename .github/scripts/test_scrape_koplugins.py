#!/usr/bin/env python3
"""Tests for reconciling manually added KOReader plugins."""

import os
import sys
import tempfile
import unittest
from unittest import mock

import scrape_common
import scrape_koplugins


class PluginScraperTests(unittest.TestCase):
    def test_zenpm_is_added_with_its_fixed_koplugin_id(self):
        repo = {
            "owner": {"login": "xZenLabs"},
            "name": "zen-pm",
            "full_name": "xZenLabs/zen-pm",
            "html_url": "https://github.com/xZenLabs/zen-pm",
            "default_branch": "main",
            "stargazers_count": 15,
            "description": "ZenPM",
            "topics": [],
            "archived": False,
            "fork": False,
        }
        releases = [{
            "tag_name": "v1.1.0",
            "published_at": "2026-07-25T12:00:00Z",
            "assets": [],
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            original_root = scrape_common.REPO_ROOT
            original_common_koreader_dir = scrape_common.KOREADER_DIR
            original_plugin_koreader_dir = scrape_koplugins.KOREADER_DIR
            scrape_common.REPO_ROOT = temp_dir
            scrape_common.KOREADER_DIR = os.path.join(
                temp_dir, "packages", "koreader"
            )
            scrape_koplugins.KOREADER_DIR = scrape_common.KOREADER_DIR
            try:
                with mock.patch.object(scrape_koplugins, "discover", return_value={}), mock.patch.object(
                    scrape_koplugins, "fetch_repo", return_value=repo
                ), mock.patch.object(
                    scrape_koplugins, "fetch_releases", return_value=releases
                ), mock.patch.object(
                    scrape_koplugins, "cache_release_notes",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_koplugins, "cache_readme",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_koplugins, "load_blacklist", return_value=set()
                ), mock.patch.object(
                    scrape_koplugins, "load_category_cache", return_value={}
                ), mock.patch.object(
                    scrape_koplugins, "save_category_cache"
                ), mock.patch.object(
                    scrape_koplugins, "scraper_timestamp",
                    return_value="2026-07-26T12:00:00Z",
                ), mock.patch.object(scrape_koplugins, "write_results"), mock.patch.object(
                    sys, "argv", ["scrape_koplugins.py"]
                ):
                    self.assertEqual(scrape_koplugins.main(), 0)
            finally:
                scrape_common.REPO_ROOT = original_root
                scrape_common.KOREADER_DIR = original_common_koreader_dir
                scrape_koplugins.KOREADER_DIR = original_plugin_koreader_dir

            meta_path = os.path.join(
                temp_dir, "packages", "koreader", "zenpm.koplugin", ".meta"
            )
            with open(meta_path, encoding="utf-8") as fh:
                meta = fh.read()
            self.assertIn("id=zenpm\n", meta)
            self.assertIn("name=ZenPM\n", meta)
            self.assertIn("version=1.1.0\n", meta)
            self.assertIn("source=https://github.com/xZenLabs/zen-pm\n", meta)

    def test_eligible_manual_package_is_refreshed_in_place(self):
        repo = {
            "owner": {"login": "owner"},
            "name": "manual.koplugin",
            "full_name": "owner/manual.koplugin",
            "html_url": "https://github.com/owner/manual.koplugin",
            "default_branch": "main",
            "stargazers_count": 15,
            "description": "Refreshed plugin",
            "topics": ["koplugin"],
            "archived": False,
            "fork": False,
        }
        releases = [{
            "tag_name": "v1.1.0",
            "published_at": "2026-07-25T12:00:00Z",
            "assets": [],
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            original_root = scrape_common.REPO_ROOT
            original_koreader_dir = scrape_common.KOREADER_DIR
            scrape_common.REPO_ROOT = temp_dir
            scrape_common.KOREADER_DIR = os.path.join(
                temp_dir, "packages", "koreader"
            )
            package_dir = os.path.join(scrape_common.KOREADER_DIR, "manual.koplugin")
            os.makedirs(package_dir)
            meta_path = os.path.join(package_dir, ".meta")
            with open(meta_path, "w", encoding="utf-8") as fh:
                fh.write(
                    "id=manual\n"
                    "name=Manual Plugin\n"
                    "version=1.0.0\n"
                    "description=Manual description\n"
                    "author=owner\n"
                    "category=utility\n"
                    "platforms=koreader\n"
                    "dependencies=manual-dependency\n"
                    "install_url=packages/manual/install.sh\n"
                    "source=https://github.com/owner/manual.koplugin\n"
                )
            try:
                with mock.patch.object(scrape_koplugins, "discover", return_value={
                    repo["full_name"]: repo,
                }), mock.patch.object(
                    scrape_koplugins, "fetch_repo", return_value=repo
                ), mock.patch.object(
                    scrape_koplugins, "fetch_releases", return_value=releases
                ), mock.patch.object(
                    scrape_koplugins, "cache_release_notes",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_koplugins, "cache_readme",
                    return_value=(None, None, False, True),
                ), mock.patch.object(
                    scrape_koplugins, "load_blacklist", return_value=set()
                ), mock.patch.object(
                    scrape_koplugins, "load_category_cache", return_value={}
                ), mock.patch.object(
                    scrape_koplugins, "save_category_cache"
                ), mock.patch.object(
                    scrape_koplugins, "scraper_timestamp",
                    return_value="2026-07-26T12:00:00Z",
                ), mock.patch.object(scrape_koplugins, "write_results") as write_results, mock.patch.object(
                    sys, "argv", ["scrape_koplugins.py"]
                ):
                    self.assertEqual(scrape_koplugins.main(), 0)
            finally:
                scrape_common.REPO_ROOT = original_root
                scrape_common.KOREADER_DIR = original_koreader_dir

            with open(meta_path, encoding="utf-8") as fh:
                meta = fh.read()
            self.assertIn("# zenpm:auto-scraped\n", meta)
            self.assertIn("version=1.1.0\n", meta)
            self.assertIn("dependencies=manual-dependency\n", meta)
            self.assertIn("install_url=packages/manual/install.sh\n", meta)
            self.assertIn("updated_at=2026-07-26T12:00:00Z\n", meta)
            write_results.assert_called_once()
            _added, updated = write_results.call_args.args
            self.assertEqual(len(updated), 1)


if __name__ == "__main__":
    unittest.main()
