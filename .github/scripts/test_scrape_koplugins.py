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
    def test_koreader_plugin_topic_variants_are_discovered_and_eligible(self):
        for topic in ("koreader-plugin", "koreader-plugins"):
            with self.subTest(topic=topic):
                repo = {
                    "name": "example",
                    "full_name": "owner/example",
                    "topics": [topic],
                }
                self.assertTrue(scrape_koplugins.is_koplugin(repo))

        self.assertIn(
            f"topic:koreader-plugin stars:>={scrape_common.MIN_STARS} fork:true",
            scrape_koplugins.PLUGIN_QUERIES,
        )
        self.assertIn(
            f"topic:koreader-plugins stars:>={scrape_common.MIN_STARS} fork:true",
            scrape_koplugins.PLUGIN_QUERIES,
        )

    def test_patch_repository_with_plugin_metadata_is_not_eligible(self):
        repo = {
            "name": "page_scrubber.koplugin",
            "full_name": "owner/page_scrubber.koplugin",
            "topics": ["koreader-plugin", "koreader-user-patch"],
            "stargazers_count": 26,
            "archived": False,
            "fork": False,
        }

        self.assertFalse(scrape_koplugins.is_eligible_koplugin(repo, False))

    def test_extra_repo_is_added_below_threshold_with_fixed_id(self):
        repo = {
            "owner": {"login": "xZenLabs"},
            "name": "zen-fm",
            "full_name": "xZenLabs/zen-fm",
            "html_url": "https://github.com/xZenLabs/zen-fm",
            "default_branch": "main",
            "stargazers_count": 7,
            "description": "ZenFM",
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
                temp_dir, "packages", "koreader", "zenfm.koplugin", ".meta"
            )
            with open(meta_path, encoding="utf-8") as fh:
                meta = fh.read()
            self.assertIn("id=zenfm\n", meta)
            self.assertIn("name=ZenFM\n", meta)
            self.assertIn("version=1.1.0\n", meta)
            self.assertIn("source=https://github.com/xZenLabs/zen-fm\n", meta)

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

    def test_package_filter_refreshes_only_the_requested_plugin(self):
        repo = {
            "owner": {"login": "xZenLabs"},
            "name": "zen-os",
            "full_name": "xZenLabs/zen-os",
            "html_url": "https://github.com/xZenLabs/zen-os",
            "default_branch": "main",
            "stargazers_count": 446,
            "description": "A clean, minimal UI for KOReader",
            "topics": ["koplugin"],
            "archived": False,
            "fork": False,
        }
        releases = [{
            "tag_name": "v2.0.0",
            "published_at": "2026-08-13T12:00:00Z",
            "assets": [],
        }, {
            "tag_name": "v2.1.0-beta1",
            "published_at": "2026-08-14T12:00:00Z",
            "prerelease": True,
            "assets": [],
        }, {
            "tag_name": "v2.1.0-alpha2",
            "published_at": "2026-08-15T12:00:00Z",
            "prerelease": True,
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

            target_dir = os.path.join(
                scrape_common.KOREADER_DIR, "zen-ui.koplugin"
            )
            other_dir = os.path.join(
                scrape_common.KOREADER_DIR, "other.koplugin"
            )
            os.makedirs(target_dir)
            os.makedirs(other_dir)
            target_meta_path = os.path.join(target_dir, ".meta")
            other_meta_path = os.path.join(other_dir, ".meta")
            with open(target_meta_path, "w", encoding="utf-8") as fh:
                fh.write(
                    "# zenpm:auto-scraped\n"
                    "id=zen-ui\n"
                    "name=Zen UI\n"
                    "version=1.0.0\n"
                    "description=Old description\n"
                    "author=AnthonyGress\n"
                    "category=theme\n"
                    "platforms=koreader\n"
                    "dependencies=\n"
                    "source=https://github.com/AnthonyGress/zen_ui.koplugin\n"
                )
            with open(other_meta_path, "w", encoding="utf-8") as fh:
                fh.write(
                    "# zenpm:auto-scraped\n"
                    "id=other\n"
                    "name=Other\n"
                    "version=1.0.0\n"
                    "description=Other plugin\n"
                    "author=owner\n"
                    "category=utility\n"
                    "platforms=koreader\n"
                    "dependencies=\n"
                    "source=https://github.com/owner/other.koplugin\n"
                )

            try:
                with mock.patch.object(scrape_koplugins, "discover") as discover, mock.patch.object(
                    scrape_koplugins, "fetch_repo", return_value=repo
                ) as fetch_repo, mock.patch.object(
                    scrape_koplugins, "fetch_releases", return_value=releases
                ), mock.patch.object(
                    scrape_koplugins, "cache_release_notes",
                    return_value=(None, None, False, True),
                ) as cache_release_notes, mock.patch.object(
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
                    return_value="2026-08-13T12:01:00Z",
                ), mock.patch.object(
                    scrape_koplugins, "write_results"
                ) as write_results, mock.patch.object(
                    sys, "argv", ["scrape_koplugins.py", "--package", "zen-ui"]
                ):
                    self.assertEqual(scrape_koplugins.main(), 0)
            finally:
                scrape_common.REPO_ROOT = original_root
                scrape_common.KOREADER_DIR = original_common_koreader_dir
                scrape_koplugins.KOREADER_DIR = original_plugin_koreader_dir

            discover.assert_not_called()
            fetch_repo.assert_called_once_with("anthonygress/zen_ui.koplugin")
            self.assertEqual(cache_release_notes.call_args_list, [
                mock.call(releases, target_dir, False),
                mock.call(
                    releases, target_dir, False, "PRERELEASE_NOTES.md",
                    prerelease=True,
                ),
            ])
            with open(target_meta_path, encoding="utf-8") as fh:
                meta = fh.read()
            self.assertIn("version=2.0.0\n", meta)
            self.assertIn("prerelease_version=2.1.0-beta1\n", meta)
            self.assertIn("alpha_version=2.1.0-alpha2\n", meta)
            self.assertIn("source=https://github.com/xZenLabs/zen-os\n", meta)
            with open(other_meta_path, encoding="utf-8") as fh:
                self.assertIn("version=1.0.0\n", fh.read())
            added, updated = write_results.call_args.args
            self.assertEqual(added, [])
            self.assertEqual([item["id"] for item in updated], ["zen-ui"])


if __name__ == "__main__":
    unittest.main()
