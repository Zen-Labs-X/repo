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

    def test_package_meta_uses_a_cached_install_asset_and_font_category(self):
        meta = scrape_fonts.package_meta(
            "font-nv-bitter", "NV Bitter", "4.1", "v2026.07.21",
            "2026-07-21T13:18:47Z", "2026-07-24T12:34:56Z", 123,
        )

        self.assertIn("author=nicoverbruggen\n", meta)
        self.assertIn("category=fonts\n", meta)
        self.assertIn("assets.0.url=packages/koreader/fonts/nv-bitter/font-nv-bitter.zip\n", meta)
        self.assertIn("updated_at=2026-07-24T12:34:56Z\n", meta)
        self.assertIn("published_at=2026-07-21T13:18:47Z\n", meta)
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
