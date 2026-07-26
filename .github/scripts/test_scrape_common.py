#!/usr/bin/env python3
"""Tests for cached package metadata used by the KOReader scrapers."""

import base64
import json
import os
import tempfile
import unittest

import scrape_common


class CachedPackageMetadataTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = scrape_common.REPO_ROOT
        self.koreader_dir = scrape_common.KOREADER_DIR
        self.scrape_blacklist = scrape_common.SCRAPE_BLACKLIST
        self.fetch_readme = scrape_common.fetch_readme
        self.temp_dir = tempfile.TemporaryDirectory()
        scrape_common.REPO_ROOT = self.temp_dir.name
        self.package_dir = os.path.join(self.temp_dir.name, "packages", "test")

    def tearDown(self):
        scrape_common.REPO_ROOT = self.repo_root
        scrape_common.KOREADER_DIR = self.koreader_dir
        scrape_common.SCRAPE_BLACKLIST = self.scrape_blacklist
        scrape_common.fetch_readme = self.fetch_readme
        self.temp_dir.cleanup()

    def test_load_blacklist_normalizes_github_urls(self):
        scrape_common.SCRAPE_BLACKLIST = os.path.join(self.temp_dir.name, "blacklist.json")
        with open(scrape_common.SCRAPE_BLACKLIST, "w", encoding="utf-8") as fh:
            json.dump(["https://github.com/xZenLabs/zen-pm", "not a repo"], fh)

        self.assertEqual(scrape_common.load_blacklist(), {"xzenlabs/zen-pm"})

    def test_existing_scraped_meta_can_include_a_matching_manual_package(self):
        scrape_common.KOREADER_DIR = os.path.join(
            self.temp_dir.name, "packages", "koreader"
        )
        package_dir = os.path.join(scrape_common.KOREADER_DIR, "manual.koplugin")
        os.makedirs(package_dir)
        with open(os.path.join(package_dir, ".meta"), "w", encoding="utf-8") as fh:
            fh.write(
                "id=manual\n"
                "name=Manual\n"
                "category=utility\n"
                "source=https://github.com/owner/manual.koplugin\n"
            )

        self.assertEqual(scrape_common.existing_scraped_meta(), [])
        records = scrape_common.existing_scraped_meta(
            include_refs={"owner/manual.koplugin"}
        )
        self.assertEqual(len(records), 1)

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

    def test_fetch_releases_returns_an_empty_list_when_none_exist(self):
        original_http_json = scrape_common.http_json
        scrape_common.http_json = lambda _url: (404, None, {})
        try:
            self.assertEqual(scrape_common.fetch_releases("owner/repo"), [])
        finally:
            scrape_common.http_json = original_http_json

    def test_one_release_request_supplies_stable_and_prerelease_metadata(self):
        original_http_json = scrape_common.http_json
        requests = []

        def fake_http_json(url):
            requests.append(url)
            return 200, [
                {"tag_name": "v2.0.0-beta.1", "prerelease": True,
                 "published_at": "2026-07-20T00:00:00Z"},
                {"tag_name": "v1.0.0", "prerelease": False,
                 "published_at": "2026-07-21T00:00:00Z"},
                {"tag_name": "v2.0.0", "prerelease": False,
                 "published_at": "2026-07-24T00:00:00Z"},
                {"tag_name": "v2.0.0-beta.2", "prerelease": True,
                 "published_at": "2026-07-25T00:00:00Z"},
                {"tag_name": "v3.0.0-beta.1", "prerelease": True, "draft": True,
                 "published_at": "2026-07-26T00:00:00Z"},
            ], {}

        scrape_common.http_json = fake_http_json
        try:
            releases = scrape_common.fetch_releases("owner/repo")
            self.assertEqual(
                scrape_common.newest_stable_release(releases)["tag_name"],
                "v2.0.0",
            )
            self.assertEqual(
                scrape_common.newest_prerelease(releases)["tag_name"],
                "v2.0.0-beta.2",
            )
            self.assertEqual(len(requests), 1)
            self.assertTrue(requests[0].endswith("/releases?per_page=100"))
        finally:
            scrape_common.http_json = original_http_json

    def test_installable_releases_keeps_version_picker_metadata(self):
        releases = [
            {
                "tag_name": "v2.0.0-beta.1",
                "name": "Beta\nrelease",
                "prerelease": True,
                "assets": [
                    {
                        "name": "plugin.zip",
                        "browser_download_url": "https://example.com/plugin.zip",
                        "size": 123,
                        "digest": "sha256:abc",
                    },
                    {
                        "name": "source.tar.gz",
                        "browser_download_url": "https://example.com/source.tar.gz",
                    },
                ],
            },
            {
                "tag_name": "v1.0.0",
                "draft": True,
                "assets": [{
                    "name": "draft.zip",
                    "browser_download_url": "https://example.com/draft.zip",
                }],
            },
        ]

        self.assertEqual(scrape_common.installable_releases(releases), [{
            "tag_name": "v2.0.0-beta.1",
            "name": "Beta release",
            "prerelease": True,
            "assets": [{
                "name": "plugin.zip",
                "url": "https://example.com/plugin.zip",
                "size": 123,
                "digest": "sha256:abc",
            }],
        }])

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
        _package_id, meta_text, summary = scrape_common.build_meta(
            repo, release, set(), "utility", readme_url="packages/test/README.md",
            readme_hash="blob-sha",
            release_notes_url="packages/test/RELEASE_NOTES.md",
            release_notes_hash="notes-hash", prerelease=prerelease,
            prerelease_notes_url="packages/test/PRERELEASE_NOTES.md",
            prerelease_notes_hash="prerelease-notes-hash", preserved_fields={
                "author": "ZenLabs",
                "icon_url": "packages/test/assets/icon.svg",
                "featured_image": "packages/test/assets/featured.png",
                "featured": "true",
                "featured_order": "10",
                "dependencies": "manual-dependency",
                "install_url": "packages/test/install.sh",
                "uninstall_url": "packages/test/uninstall.sh",
                "conflicts": "other-package",
                "incompatible_platforms": "android",
            },
            releases=[{
                "tag_name": "v2.0.0-beta.1",
                "name": "Beta release",
                "prerelease": True,
                "assets": [{
                    "name": "example.koplugin.zip",
                    "browser_download_url": "https://example.com/example.koplugin.zip",
                    "size": 123,
                    "digest": "sha256:abc",
                }],
            }],
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
        self.assertIn("author=ZenLabs\n", meta_text)
        self.assertIn("icon_url=packages/test/assets/icon.svg\n", meta_text)
        self.assertIn("featured_image=packages/test/assets/featured.png\n", meta_text)
        self.assertIn("featured=true\n", meta_text)
        self.assertIn("featured_order=10\n", meta_text)
        self.assertIn("platforms=koreader\n", meta_text)
        self.assertIn("dependencies=manual-dependency\n", meta_text)
        self.assertIn("install_url=packages/test/install.sh\n", meta_text)
        self.assertIn("uninstall_url=packages/test/uninstall.sh\n", meta_text)
        self.assertIn("conflicts=other-package\n", meta_text)
        self.assertIn("incompatible_platforms=android\n", meta_text)
        self.assertEqual(
            summary["versions_path"],
            "packages/koreader/example.koplugin/versions.json",
        )
        fields = dict(
            line.split("=", 1) for line in meta_text.splitlines()
            if "=" in line and not line.startswith("#")
        )
        self.assertEqual(json.loads(fields["releases"]), [{
            "tag_name": "v2.0.0-beta.1",
            "name": "Beta release",
            "prerelease": True,
            "assets": [{
                "name": "example.koplugin.zip",
                "url": "https://example.com/example.koplugin.zip",
                "size": 123,
                "digest": "sha256:abc",
            }],
        }])

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
