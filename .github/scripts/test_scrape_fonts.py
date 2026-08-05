#!/usr/bin/env python3

import io
import json
import os
import tempfile
import unittest
import zipfile
from unittest import mock

import scrape_fonts


class FontScraperTests(unittest.TestCase):
    def test_collection_archive_url_selects_only_relaxed_fonts(self):
        collection = {
            "name": "core",
            "archives": {
                "kobo": "https://example.invalid/kobo-core-fonts.zip",
                "other": "https://example.invalid/other-core-fonts.zip",
                "relaxed": "https://example.invalid/relaxed-core-fonts.zip",
            },
        }

        self.assertEqual(
            scrape_fonts.collection_archive_url(collection),
            "https://example.invalid/relaxed-core-fonts.zip",
        )

    def test_collection_archive_url_requires_relaxed_fonts(self):
        with self.assertRaisesRegex(RuntimeError, "no relaxed archive for extra"):
            scrape_fonts.collection_archive_url({"name": "extra", "archives": {"other": "unused"}})

    def test_relaxed_filename_adds_the_upstream_variant_suffix(self):
        self.assertEqual(
            scrape_fonts.relaxed_filename("NV_Legible_Next-BoldItalic.ttf"),
            "NV_Legible_Next_R-BoldItalic.ttf",
        )

    def test_preview_images_reads_tagged_source_archive(self):
        source = io.BytesIO()
        with zipfile.ZipFile(source, "w") as archive:
            archive.writestr("ebook-fonts-v1/examples/core/Libron.png", b"preview")
        with mock.patch.object(scrape_fonts, "request", return_value=source.getvalue()):
            images = scrape_fonts.preview_images("v1")

        self.assertEqual(images, {("core", "Libron.png"): b"preview"})

    def test_family_zip_is_deterministic_and_uses_koreader_fonts_directory(self):
        files = {"Example-Regular.ttf": b"regular", "Example-Bold.ttf": b"bold"}
        archive = scrape_fonts.family_zip(files)

        self.assertEqual(archive, scrape_fonts.family_zip(files))
        with zipfile.ZipFile(io.BytesIO(archive)) as zip_file:
            self.assertEqual(
                zip_file.namelist(),
                ["fonts/Example-Bold.ttf", "fonts/Example-Regular.ttf"],
            )

    def test_family_zip_can_group_files_under_its_family_name(self):
        archive = scrape_fonts.family_zip({"NV_Bitter-Regular.ttf": b"regular"}, "nv-bitter")

        with zipfile.ZipFile(io.BytesIO(archive)) as zip_file:
            self.assertEqual(zip_file.namelist(), ["nv-bitter/NV_Bitter-Regular.ttf"])

    def test_package_meta_preserves_identity_and_advances_version_for_client_updates(self):
        package_id = "font-" + scrape_fonts.slugify("NV Bitter")
        meta = scrape_fonts.package_meta(
            package_id, "NV Bitter", "4.2", "v2026.08.05",
            "2026-08-05T19:18:11Z", "2026-08-05T20:49:38Z", 123,
        )

        self.assertEqual(package_id, "font-nv-bitter")
        self.assertIn("id=font-nv-bitter\n", meta)
        self.assertIn("version=4.2\n", meta)
        self.assertIn("author=nicoverbruggen\n", meta)
        self.assertIn("category=fonts\n", meta)
        self.assertIn("assets.0.url=packages/koreader/fonts/nv-bitter/font-nv-bitter.zip\n", meta)
        self.assertIn("updated_at=2026-08-05T20:49:38Z\n", meta)
        self.assertIn("published_at=2026-08-05T19:18:11Z\n", meta)
        self.assertNotIn("install_url=", meta)
        self.assertNotIn("uninstall_url=", meta)

    def test_caches_only_ttf_files_from_the_latest_junicode_release(self):
        source = io.BytesIO()
        with zipfile.ZipFile(source, "w") as archive:
            archive.writestr("Junicode_2.226/Junicode-Regular.ttf", b"ttf")
            archive.writestr("Junicode_2.226/Junicode-Regular.otf", b"otf")
            archive.writestr("Junicode_2.226/README.txt", b"readme")
        release = {
            "tag_name": "v2.226",
            "name": "Junicode version 2.226",
            "published_at": "2026-06-20T10:58:50Z",
            "assets": [{
                "name": "Junicode_2.226.zip",
                "browser_download_url": "https://example.invalid/Junicode_2.226.zip",
            }],
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            fonts_root = scrape_fonts.FONTS_ROOT
            scrape_fonts.FONTS_ROOT = temp_dir
            try:
                with mock.patch.object(
                    scrape_fonts,
                    "request",
                    side_effect=[json.dumps(release).encode(), source.getvalue()],
                ):
                    changed, dirname = scrape_fonts.cache_junicode("2026-07-26T12:34:56Z")
            finally:
                scrape_fonts.FONTS_ROOT = fonts_root

            self.assertTrue(changed)
            self.assertEqual(dirname, "junicode")
            archive_path = os.path.join(temp_dir, "junicode", "font-junicode.zip")
            with zipfile.ZipFile(archive_path) as archive:
                self.assertEqual(
                    archive.namelist(),
                    ["junicode/Junicode-Regular.ttf"],
                )
            with open(os.path.join(temp_dir, "junicode", ".meta"), encoding="utf-8") as meta:
                self.assertIn("version=2.226\n", meta.read())


if __name__ == "__main__":
    unittest.main()
