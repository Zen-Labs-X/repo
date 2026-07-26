#!/usr/bin/env python3
"""Tests for cached package documentation used by the KOReader scrapers."""

import base64
import os
import tempfile
import unittest

import scrape_common


class CachedDocumentationTests(unittest.TestCase):
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

    def test_caches_latest_release_notes_and_uses_a_content_hash(self):
        release = {"body": "## Fixed\n\n- A bug\n"}

        url, notes_hash, changed, resolved = scrape_common.cache_release_notes(
            release, self.package_dir
        )

        self.assertEqual(url, "packages/test/RELEASE_NOTES.md")
        self.assertEqual(
            notes_hash,
            "e087032c83e5567ca2c40122aff26c80d53d5bad2ca400bae30e53269f1f8902",
        )
        self.assertTrue(changed)
        self.assertTrue(resolved)
        with open(os.path.join(self.package_dir, "RELEASE_NOTES.md"), encoding="utf-8") as fh:
            self.assertEqual(fh.read(), release["body"])

    def test_missing_latest_release_removes_cached_release_notes(self):
        os.makedirs(self.package_dir)
        cache_path = os.path.join(self.package_dir, "RELEASE_NOTES.md")
        with open(cache_path, "w", encoding="utf-8") as fh:
            fh.write("# Cached\n")

        url, notes_hash, changed, resolved = scrape_common.cache_release_notes(
            {}, self.package_dir
        )

        self.assertIsNone(url)
        self.assertIsNone(notes_hash)
        self.assertTrue(changed)
        self.assertTrue(resolved)
        self.assertFalse(os.path.exists(cache_path))

    def test_caches_prerelease_notes_in_a_separate_file(self):
        release = {"body": "## Beta\n"}

        url, _notes_hash, changed, resolved = scrape_common.cache_release_notes(
            release, self.package_dir, filename="PRERELEASE_NOTES.md"
        )

        self.assertEqual(url, "packages/test/PRERELEASE_NOTES.md")
        self.assertTrue(changed)
        self.assertTrue(resolved)

    def test_unavailable_release_keeps_existing_release_notes(self):
        os.makedirs(self.package_dir)
        cache_path = os.path.join(self.package_dir, "RELEASE_NOTES.md")
        with open(cache_path, "w", encoding="utf-8") as fh:
            fh.write("# Cached\n")

        _url, _notes_hash, changed, resolved = scrape_common.cache_release_notes(
            None, self.package_dir
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

    def test_fetch_release_distinguishes_a_missing_release(self):
        original_http_json = scrape_common.http_json
        scrape_common.http_json = lambda _url: (404, None, {})
        try:
            self.assertEqual(scrape_common.fetch_release("owner/repo"), {})
        finally:
            scrape_common.http_json = original_http_json

    def test_fetch_prerelease_chooses_the_most_recent_published_version(self):
        original_http_json = scrape_common.http_json
        scrape_common.http_json = lambda _url: (200, [
            {"tag_name": "v2.0.0-beta.1", "prerelease": True,
             "published_at": "2026-07-20T00:00:00Z"},
            {"tag_name": "v2.0.0", "prerelease": False,
             "published_at": "2026-07-24T00:00:00Z"},
            {"tag_name": "v2.0.0-beta.2", "prerelease": True,
             "published_at": "2026-07-25T00:00:00Z"},
            {"tag_name": "v3.0.0-beta.1", "prerelease": True, "draft": True,
             "published_at": "2026-07-26T00:00:00Z"},
        ], {})
        try:
            self.assertEqual(
                scrape_common.fetch_prerelease("owner/repo")["tag_name"],
                "v2.0.0-beta.2",
            )
        finally:
            scrape_common.http_json = original_http_json

    def test_build_meta_includes_cached_documentation_fields(self):
        repo = {
            "owner": {"login": "owner"},
            "name": "example.koplugin",
            "full_name": "owner/example.koplugin",
            "html_url": "https://github.com/owner/example.koplugin",
            "default_branch": "main",
            "stargazers_count": 20,
            "description": "Example package",
        }

        release = {"published_at": "2026-07-20T01:02:03Z"}
        prerelease = {
            "tag_name": "v2.0.0-beta.1",
            "published_at": "2026-07-25T01:02:03Z",
        }
        _package_id, meta_text, _summary = scrape_common.build_meta(
            repo, release, set(), "utility", readme_url="packages/test/README.md",
            readme_hash="blob-sha",
            release_notes_url="packages/test/RELEASE_NOTES.md",
            release_notes_hash="notes-hash", prerelease=prerelease,
            prerelease_notes_url="packages/test/PRERELEASE_NOTES.md",
            prerelease_notes_hash="prerelease-notes-hash", preserved_fields={
                "icon_url": "packages/test/assets/icon.svg",
                "featured_image": "packages/test/assets/featured.png",
                "featured": "true",
                "featured_order": "10",
                "conflicts": "other-package",
                "incompatible_platforms": "android",
            },
            scraped_at="2026-07-24T12:34:56Z",
        )

        self.assertIn("readme_url=packages/test/README.md\n", meta_text)
        self.assertIn("readme_hash=blob-sha\n", meta_text)
        self.assertIn("release_notes_url=packages/test/RELEASE_NOTES.md\n", meta_text)
        self.assertIn("release_notes_hash=notes-hash\n", meta_text)
        self.assertIn("prerelease_version=2.0.0-beta.1\n", meta_text)
        self.assertIn("prerelease_published_at=2026-07-25T01:02:03Z\n", meta_text)
        self.assertIn("prerelease_notes_url=packages/test/PRERELEASE_NOTES.md\n", meta_text)
        self.assertIn("prerelease_notes_hash=prerelease-notes-hash\n", meta_text)
        self.assertIn("updated_at=2026-07-24T12:34:56Z\n", meta_text)
        self.assertIn("published_at=2026-07-20T01:02:03Z\n", meta_text)
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
