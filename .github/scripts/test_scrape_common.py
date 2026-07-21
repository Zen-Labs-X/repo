#!/usr/bin/env python3
"""Tests for README caching used by the KOReader package scrapers."""

import base64
import os
import tempfile
import unittest

import scrape_common


class ReadmeCacheTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = scrape_common.REPO_ROOT
        self.fetch_readme = scrape_common.fetch_readme
        self.temp_dir = tempfile.TemporaryDirectory()
        scrape_common.REPO_ROOT = self.temp_dir.name
        self.package_dir = os.path.join(self.temp_dir.name, "packages", "test")

    def tearDown(self):
        scrape_common.REPO_ROOT = self.repo_root
        scrape_common.fetch_readme = self.fetch_readme
        self.temp_dir.cleanup()

    def test_caches_readme_and_uses_its_blob_sha(self):
        scrape_common.fetch_readme = lambda _repo: ("# Cached\n", "blob-sha", True)

        url, readme_hash, changed, resolved = scrape_common.cache_readme(
            "owner/repo", self.package_dir
        )

        self.assertEqual(url, "packages/test/README.md")
        self.assertEqual(readme_hash, "blob-sha")
        self.assertTrue(changed)
        self.assertTrue(resolved)
        with open(os.path.join(self.package_dir, "README.md"), encoding="utf-8") as fh:
            self.assertEqual(fh.read(), "# Cached\n")

    def test_unavailable_readme_keeps_existing_cache(self):
        os.makedirs(self.package_dir)
        cache_path = os.path.join(self.package_dir, "README.md")
        with open(cache_path, "w", encoding="utf-8") as fh:
            fh.write("# Cached\n")
        scrape_common.fetch_readme = lambda _repo: (None, None, False)

        _url, _hash, changed, resolved = scrape_common.cache_readme(
            "owner/repo", self.package_dir
        )

        self.assertFalse(changed)
        self.assertFalse(resolved)
        self.assertTrue(os.path.exists(cache_path))

    def test_fetch_readme_decodes_github_content(self):
        original_http_json = scrape_common.http_json
        scrape_common.http_json = lambda _url: (
            200,
            {"content": base64.b64encode(b"# README\n").decode(), "sha": "blob-sha"},
            {},
        )
        try:
            self.assertEqual(
                scrape_common.fetch_readme("owner/repo"),
                ("# README\n", "blob-sha", True),
            )
        finally:
            scrape_common.http_json = original_http_json

    def test_build_meta_includes_readme_fields(self):
        repo = {
            "owner": {"login": "owner"},
            "name": "example.koplugin",
            "full_name": "owner/example.koplugin",
            "html_url": "https://github.com/owner/example.koplugin",
            "default_branch": "main",
            "stargazers_count": 20,
            "updated_at": "2026-07-16T12:34:56Z",
            "description": "Example package",
        }

        _package_id, meta_text, _summary = scrape_common.build_meta(
            repo, None, set(), "utility", readme_url="packages/test/README.md",
            readme_hash="blob-sha", preserved_fields={
                "icon_url": "packages/test/assets/icon.svg",
                "featured_image": "packages/test/assets/featured.png",
                "featured": "true",
                "featured_order": "10",
                "conflicts": "other-package",
                "incompatible_platforms": "android",
            },
        )

        self.assertIn("readme_url=packages/test/README.md\n", meta_text)
        self.assertIn("readme_hash=blob-sha\n", meta_text)
        self.assertIn("updated_at=2026-07-16T12:34:56Z\n", meta_text)
        self.assertIn("icon_url=packages/test/assets/icon.svg\n", meta_text)
        self.assertIn("featured_image=packages/test/assets/featured.png\n", meta_text)
        self.assertIn("featured=true\n", meta_text)
        self.assertIn("featured_order=10\n", meta_text)
        self.assertIn("platforms=koreader\n", meta_text)
        self.assertIn("conflicts=other-package\n", meta_text)
        self.assertIn("incompatible_platforms=android\n", meta_text)
        self.assertNotIn("install_url=", meta_text)
        self.assertNotIn("uninstall_url=", meta_text)

    def test_repository_identity_ignores_package_name_punctuation(self):
        self.assertEqual(
            scrape_common.repository_identity("https://github.com/xZenLabs/ZenMTP"),
            ("xzenlabs", "zenmtp"),
        )
        self.assertEqual(
            scrape_common.repository_identity("xZenLabs/zen-mtp.koplugin"),
            ("xzenlabs", "zenmtp"),
        )


if __name__ == "__main__":
    unittest.main()
