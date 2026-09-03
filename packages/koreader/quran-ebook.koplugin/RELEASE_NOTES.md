# v0.10.0

151 EPUB files across 42 languages — bilingual, interactive, word-by-word, and Arabic-only.

### New since v0.9.0

**Translation font fix** — translation and Latin text no longer inherits the Quranic body font (KFGQPC). Elements now use `font-family: initial`, so the reader's configured font is used for non-Arabic text instead of partially matching KFGQPC glyphs with mixed-weight fallback.

**Data cleanup** — fixed upstream data corruption in some translations (e.g. Maududi English) where replacement characters (U+FFFD) appeared instead of em-dashes. Suppressed duplicate surah name translations where the API returned a transliteration identical to the surah name (e.g. "Al-A'raf" for Al-A'raf).

**Spacing and typography** — tightened surah header padding and basmala line-height for a more compact layout. Unified cover separator to middle dot (·) across all languages, and went back to the classic surah header glyphs.

**KOReader plugin v1.6** — the plugin now detects whether the current book is a Quran EPUB (via dc:subject metadata or juz TOC entries) and skips juz/surah status bar injection for non-Quran books.

KOReader addons: [plugin](../../#install) · [word dictionary](../../#dictionary) · [grammar & i'rab](../../#grammar-dictionary-lookup) · [tafsir](../../#tafsir-commentary-lookup) · [surah overview](../../#surah-overview-lookup) · [setup tips](../../#koreader-settings)

## EPUBs

### Arabic

| Riwayah | | |
|---------|---|---|
| Hafs | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_inline_ar.epub) | Continuous flowing text, no translation |
| Warsh (experimental) | [epub](../../releases/download/v0.10.0/quran_warsh_kfgqpc_inline_ar.epub) | Arabic-only, Riwayat Warsh 'an Nafi' — see [known limitations](../../#other-riwayat-work-in-progress) |

### English

| Translator | Bilingual | Interactive | WBW |
|-----------|:---------:|:-----------:|:-------------|
| Sahih International | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-en-sahih.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-en-sahih.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-en-sahih.epub) |
| M.A.S. Abdel Haleem | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-en-haleem.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-en-haleem.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-en-haleem.epub) |
| Sayyid Abul Ala Maududi (Tafhim ul-Quran) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-en-maududi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-en-maududi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-en-maududi.epub) |
| Dr. Mustafa Khattab / The Clear Quran | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-en-khattab.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-en-khattab.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-en-khattab.epub) |
| Dr. Mustafa Khattab / The Clear Quran (annotated) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-en-khattab-fn.epub) |

### Other languages

<details><summary>Français, Deutsch, Español, Türkçe, اردو — Urdu, Bahasa Indonesia, Русский, বাংলা — Bengali</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| Français | Hamidullah | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-fr-hamidullah_enwbw.epub)<sup>en wbw</sup> |
| Deutsch | Bubenheim & Elyas | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-de-bubenheim_enwbw.epub)<sup>en wbw</sup> |
| Español | Isa Garcia | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-es-garcia.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-es-garcia.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-es-garcia_enwbw.epub)<sup>en wbw</sup> |
| Türkçe | Diyanet İşleri | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-tr-diyanet.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-tr-diyanet_enwbw.epub)<sup>en wbw</sup> |
| اردو — Urdu | Jalandhari | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ur-jalandhari.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ur-jalandhari_enwbw.epub)<sup>en wbw</sup> |
| اردو — Urdu | Sayyid Abul Ala Maududi (Tafheem-ul-Quran) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ur-maududi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ur-maududi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ur-maududi.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ur-maududi_enwbw.epub)<sup>en wbw</sup> |
| Bahasa Indonesia | Kementerian Agama | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-id-ministry.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-id-ministry.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-id-ministry.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-id-ministry_enwbw.epub)<sup>en wbw</sup> |
| Русский | Kuliev | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ru-kuliev_enwbw.epub)<sup>en wbw</sup> |
| বাংলা — Bengali | Taisirul Quran | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-bn-taisirul.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-bn-taisirul_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>فارسی — Persian, Bahasa Melayu, Português, Italiano, Nederlands, Norsk, Svenska, Bosanski, Soomaali, Hausa, Fulfulde, Kiswahili</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| فارسی — Persian | Hussein Taji Kal Dari | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-fa-dari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-fa-dari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-fa-dari.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-fa-dari_enwbw.epub)<sup>en wbw</sup> |
| Bahasa Melayu | Abdullah Muhammad Basmeih | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ms-basmeih_enwbw.epub)<sup>en wbw</sup><br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ms-basmeih_idwbw.epub)<sup>id wbw</sup> |
| Português | Helmi Nasr | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-pt-nasr.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-pt-nasr.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-pt-nasr_enwbw.epub)<sup>en wbw</sup> |
| Italiano | Hamza Roberto Piccardo | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-it-piccardo.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-it-piccardo.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-it-piccardo_enwbw.epub)<sup>en wbw</sup> |
| Nederlands | Sofian S. Siregar | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-nl-siregar.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-nl-siregar.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-nl-siregar_enwbw.epub)<sup>en wbw</sup> |
| Norsk | Einar Berg | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-no-berg.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-no-berg.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-no-berg_enwbw.epub)<sup>en wbw</sup> |
| Svenska | Knut Bernström | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-sv-bernstrom_enwbw.epub)<sup>en wbw</sup> |
| Bosanski | Besim Korkut | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-bs-korkut.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-bs-korkut.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-bs-korkut_enwbw.epub)<sup>en wbw</sup> |
| Soomaali | Mahmud Muhammad Abduh | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-so-abduh.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-so-abduh.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-so-abduh_enwbw.epub)<sup>en wbw</sup> |
| Hausa | Abubakar Mahmoud Gumi | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ha-gumi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ha-gumi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ha-gumi_enwbw.epub)<sup>en wbw</sup> |
| Fulfulde — Fula | Rowad Translation Center | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ff-ruwwad_enwbw.epub)<sup>en wbw</sup> |
| Kiswahili | Ali Muhsin Al-Barwani | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-sw-barwani.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-sw-barwani.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-sw-barwani_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>हिन्दी — Hindi, தமிழ் — Tamil, മലയാളം — Malayalam, پښتو — Pashto, کوردی — Kurdish, ئۇيغۇرچە — Uyghur, 中文, 한국어, 日本語, ไทย, Tiếng Việt, Filipino</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| हिन्दी — Hindi | Maulana Azizul Haque al-Umari | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-hi-umari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-hi-umari.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-hi-umari.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-hi-umari_enwbw.epub)<sup>en wbw</sup> |
| தமிழ் — Tamil | Abdul Hameed Baqavi | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ta-baqavi.epub)<br>[epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ta-baqavi_enwbw.epub)<sup>en wbw</sup> |
| മലയാളം — Malayalam | Abdul Hameed & Kunhi Mohammed | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ml-hameed.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ml-hameed.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ml-hameed_enwbw.epub)<sup>en wbw</sup> |
| پښتو — Pashto | Zakaria Abulsalam | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ps-abulsalam_enwbw.epub)<sup>en wbw</sup> |
| کوردی — Kurdish | Muhammad Saleh Bamoki | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ku-bamoki_enwbw.epub)<sup>en wbw</sup> |
| ئۇيغۇرچە — Uyghur | Muhammad Saleh | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ug-saleh.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ug-saleh.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ug-saleh_enwbw.epub)<sup>en wbw</sup> |
| 中文 — Chinese | Ma Jian | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-zh-majian.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-zh-majian.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-zh-majian_enwbw.epub)<sup>en wbw</sup> |
| 한국어 — Korean | Hamed Choi | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ko-choi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ko-choi.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ko-choi_enwbw.epub)<sup>en wbw</sup> |
| 日本語 — Japanese | Saeed Sato | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-ja-sato.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-ja-sato.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-ja-sato_enwbw.epub)<sup>en wbw</sup> |
| ไทย — Thai | King Fahad Quran Complex | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-th-fahad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-th-fahad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-th-fahad_enwbw.epub)<sup>en wbw</sup> |
| Tiếng Việt | Ruwwad Center | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-vi-ruwwad_enwbw.epub)<sup>en wbw</sup> |
| Filipino | Dar Al-Salam Center | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-tl-darsalam_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>Azərbaycanca, Oʻzbekcha, Тоҷикӣ — Tajik, Қазақша — Kazakh, Shqip — Albanian, Polski, Українська — Ukrainian, አማርኛ — Amharic, Yorùbá</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| Azərbaycanca | Alikhan Musayev | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-az-musayev.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-az-musayev.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-az-musayev_enwbw.epub)<sup>en wbw</sup> |
| Oʻzbekcha | Muhammad Sodiq Muhammad Yusuf | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-uz-yusuf_enwbw.epub)<sup>en wbw</sup> |
| Тоҷикӣ — Tajik | Khawaja Mirof & Khawaja Mir | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-tg-mirof.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-tg-mirof.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-tg-mirof_enwbw.epub)<sup>en wbw</sup> |
| Қазақша — Kazakh | Khalifa Altay | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-kk-altay.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-kk-altay.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-kk-altay_enwbw.epub)<sup>en wbw</sup> |
| Shqip — Albanian | Sherif Ahmeti | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-sq-ahmeti_enwbw.epub)<sup>en wbw</sup> |
| Polski | Józef Bielawski | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-pl-bielawski_enwbw.epub)<sup>en wbw</sup> |
| Українська — Ukrainian | Dr. Mikhailo Yaqubovic | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-uk-yaqubovic_enwbw.epub)<sup>en wbw</sup> |
| አማርኛ — Amharic | Sadiq and Sani | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-am-sadiq.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-am-sadiq.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-am-sadiq_enwbw.epub)<sup>en wbw</sup> |
| Yorùbá | Shaykh Abu Rahimah Mikael Aykyuni | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_bilin_ar-yo-mikael.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_interactive_ar-yo-mikael.epub) | [epub](../../releases/download/v0.10.0/quran_hafs_kfgqpc_wbw_ar-yo-mikael_enwbw.epub)<sup>en wbw</sup> |

</details>

Word-by-Word download links: **epub** = native-language word gloss, **epub**<sup>en wbw</sup> = English word gloss, **epub**<sup>id wbw</sup> = Indonesian word gloss. Cross-language WBW pairs English (or Indonesian) word-level meanings with a full sentence translation in the target language — useful for readers who understand basic English vocabulary but prefer reading a translation in their own language.

Many translations include translator footnotes where the source data provides them (Sahih International, Hamidullah, Garcia, Hamza Roberto Piccardo, Nasr, and others). Editions marked "with commentary" or "annotated" have especially extensive notes — Tafhim ul-Quran includes Sayyid Abul Ala Maududi's full tafseer-style commentary, and the annotated Clear Quran has 1,270 scholarly footnotes. See [KOReader Settings](../../#koreader-settings) for footnote popup setup.

**Note on Maududi footnotes:** A small number (~9%) of Tafhim ul-Quran footnotes are truncated in the upstream source data (ending mid-sentence). This is a known issue in the digitized text that all online sources share — not specific to this project.

### Updating EPUBs

Overwrite the old file with the new one, keeping the same filename. KOReader (and most e-readers) store your reading position, highlights, and settings separately — they will be preserved. Do **not** delete the book from within KOReader before replacing, as this will delete your data. After updating, you can force refresh metadata (cover, etc) by long-pressing the book in KOReader and selecting Refresh cached metadata.


## What's Changed
* Qcf by @zeeyado in https://github.com/zeeyado/quran-ebook/pull/11

## New Contributors
* @zeeyado made their first contribution in https://github.com/zeeyado/quran-ebook/pull/11

**Full Changelog**: https://github.com/zeeyado/quran-ebook/compare/v0.9.0...v0.10.0

# v0.9.0

151 EPUB files across 42 languages — bilingual, interactive, word-by-word, and Arabic-only.

### New since v0.8.0

**Cross-language word-by-word** — WBW mode now covers all 42 translation languages. Every translation gets an English-gloss WBW variant. Malay additionally gets an Indonesian-gloss variant. Languages with native WBW glosses keep their existing native-gloss WBW as well.

**Surah name font V4 and spacing** — switched from V2 to V4 classical calligraphy glyphs for surah headers across all layouts. Reduced surah header and basmala margins and line-height for a more compact appearance.

**EPUB metadata** — dc:title now uses full riwayah phrase ("برواية حفص عن عاصم") and middle dot (·) separator between title components. Translator moved to dc:author.

**Cover colors** — updated cover palette.

**KOReader plugin v1.5** — updated surah name regex for V4 trigger format, backwards-compatible with V2.

**Build hardening** — cover font path logged per build, hard failure on missing cover fonts. Fixed ZIP packaging subfolder structure for dictionary and plugin releases.

KOReader addons: [plugin](../../#install) · [word dictionary](../../#dictionary) · [grammar & i'rab](../../#grammar-dictionary-lookup) · [tafsir](../../#tafsir-commentary-lookup) · [surah overview](../../#surah-overview-lookup) · [setup tips](../../#koreader-settings)

## EPUBs

### Arabic

| Riwayah | | |
|---------|---|---|
| Hafs | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_inline_ar.epub) | Continuous flowing text, no translation |
| Warsh (experimental) | [epub](../../releases/download/v0.9.0/quran_warsh_kfgqpc_inline_ar.epub) | Arabic-only, Riwayat Warsh 'an Nafi' — see [known limitations](../../#other-riwayat-work-in-progress) |

### English

| Translator | Bilingual | Interactive | WBW |
|-----------|:---------:|:-----------:|:-------------|
| Sahih International | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-en-sahih.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-en-sahih.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-en-sahih.epub) |
| M.A.S. Abdel Haleem | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-en-haleem.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-en-haleem.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-en-haleem.epub) |
| Sayyid Abul Ala Maududi (Tafhim ul-Quran) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-en-maududi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-en-maududi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-en-maududi.epub) |
| Dr. Mustafa Khattab / The Clear Quran | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-en-khattab.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-en-khattab.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-en-khattab.epub) |
| Dr. Mustafa Khattab / The Clear Quran (annotated) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-en-khattab-fn.epub) |

### Other languages

<details><summary>Français, Deutsch, Español, Türkçe, اردو — Urdu, Bahasa Indonesia, Русский, বাংলা — Bengali</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| Français | Hamidullah | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-fr-hamidullah_enwbw.epub)<sup>en wbw</sup> |
| Deutsch | Bubenheim & Elyas | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-de-bubenheim_enwbw.epub)<sup>en wbw</sup> |
| Español | Isa Garcia | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-es-garcia.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-es-garcia.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-es-garcia_enwbw.epub)<sup>en wbw</sup> |
| Türkçe | Diyanet İşleri | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-tr-diyanet.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-tr-diyanet_enwbw.epub)<sup>en wbw</sup> |
| اردو — Urdu | Jalandhari | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ur-jalandhari.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ur-jalandhari_enwbw.epub)<sup>en wbw</sup> |
| اردو — Urdu | Sayyid Abul Ala Maududi (Tafheem-ul-Quran) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ur-maududi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ur-maududi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ur-maududi.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ur-maududi_enwbw.epub)<sup>en wbw</sup> |
| Bahasa Indonesia | Kementerian Agama | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-id-ministry.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-id-ministry.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-id-ministry.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-id-ministry_enwbw.epub)<sup>en wbw</sup> |
| Русский | Kuliev | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ru-kuliev_enwbw.epub)<sup>en wbw</sup> |
| বাংলা — Bengali | Taisirul Quran | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-bn-taisirul.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-bn-taisirul_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>فارسی — Persian, Bahasa Melayu, Português, Italiano, Nederlands, Norsk, Svenska, Bosanski, Soomaali, Hausa, Fulfulde, Kiswahili</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| فارسی — Persian | Hussein Taji Kal Dari | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-fa-dari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-fa-dari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-fa-dari.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-fa-dari_enwbw.epub)<sup>en wbw</sup> |
| Bahasa Melayu | Abdullah Muhammad Basmeih | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ms-basmeih_enwbw.epub)<sup>en wbw</sup><br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ms-basmeih_idwbw.epub)<sup>id wbw</sup> |
| Português | Helmi Nasr | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-pt-nasr.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-pt-nasr.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-pt-nasr_enwbw.epub)<sup>en wbw</sup> |
| Italiano | Hamza Roberto Piccardo | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-it-piccardo.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-it-piccardo.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-it-piccardo_enwbw.epub)<sup>en wbw</sup> |
| Nederlands | Sofian S. Siregar | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-nl-siregar.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-nl-siregar.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-nl-siregar_enwbw.epub)<sup>en wbw</sup> |
| Norsk | Einar Berg | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-no-berg.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-no-berg.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-no-berg_enwbw.epub)<sup>en wbw</sup> |
| Svenska | Knut Bernström | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-sv-bernstrom_enwbw.epub)<sup>en wbw</sup> |
| Bosanski | Besim Korkut | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-bs-korkut.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-bs-korkut.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-bs-korkut_enwbw.epub)<sup>en wbw</sup> |
| Soomaali | Mahmud Muhammad Abduh | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-so-abduh.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-so-abduh.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-so-abduh_enwbw.epub)<sup>en wbw</sup> |
| Hausa | Abubakar Mahmoud Gumi | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ha-gumi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ha-gumi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ha-gumi_enwbw.epub)<sup>en wbw</sup> |
| Fulfulde — Fula | Rowad Translation Center | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ff-ruwwad_enwbw.epub)<sup>en wbw</sup> |
| Kiswahili | Ali Muhsin Al-Barwani | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-sw-barwani.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-sw-barwani.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-sw-barwani_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>हिन्दी — Hindi, தமிழ் — Tamil, മലയാളം — Malayalam, پښتو — Pashto, کوردی — Kurdish, ئۇيغۇرچە — Uyghur, 中文, 한국어, 日本語, ไทย, Tiếng Việt, Filipino</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| हिन्दी — Hindi | Maulana Azizul Haque al-Umari | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-hi-umari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-hi-umari.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-hi-umari.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-hi-umari_enwbw.epub)<sup>en wbw</sup> |
| தமிழ் — Tamil | Abdul Hameed Baqavi | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ta-baqavi.epub)<br>[epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ta-baqavi_enwbw.epub)<sup>en wbw</sup> |
| മലയാളം — Malayalam | Abdul Hameed & Kunhi Mohammed | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ml-hameed.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ml-hameed.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ml-hameed_enwbw.epub)<sup>en wbw</sup> |
| پښتو — Pashto | Zakaria Abulsalam | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ps-abulsalam_enwbw.epub)<sup>en wbw</sup> |
| کوردی — Kurdish | Muhammad Saleh Bamoki | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ku-bamoki_enwbw.epub)<sup>en wbw</sup> |
| ئۇيغۇرچە — Uyghur | Muhammad Saleh | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ug-saleh.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ug-saleh.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ug-saleh_enwbw.epub)<sup>en wbw</sup> |
| 中文 — Chinese | Ma Jian | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-zh-majian.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-zh-majian.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-zh-majian_enwbw.epub)<sup>en wbw</sup> |
| 한국어 — Korean | Hamed Choi | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ko-choi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ko-choi.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ko-choi_enwbw.epub)<sup>en wbw</sup> |
| 日本語 — Japanese | Saeed Sato | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-ja-sato.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-ja-sato.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-ja-sato_enwbw.epub)<sup>en wbw</sup> |
| ไทย — Thai | King Fahad Quran Complex | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-th-fahad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-th-fahad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-th-fahad_enwbw.epub)<sup>en wbw</sup> |
| Tiếng Việt | Ruwwad Center | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-vi-ruwwad_enwbw.epub)<sup>en wbw</sup> |
| Filipino | Dar Al-Salam Center | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-tl-darsalam_enwbw.epub)<sup>en wbw</sup> |

</details>

<details><summary>Azərbaycanca, Oʻzbekcha, Тоҷикӣ — Tajik, Қазақша — Kazakh, Shqip — Albanian, Polski, Українська — Ukrainian, አማርኛ — Amharic, Yorùbá</summary>

| Language | Translator | Bilingual | Interactive | WBW |
|----------|-----------|:---------:|:-----------:|:-------------|
| Azərbaycanca | Alikhan Musayev | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-az-musayev.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-az-musayev.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-az-musayev_enwbw.epub)<sup>en wbw</sup> |
| Oʻzbekcha | Muhammad Sodiq Muhammad Yusuf | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-uz-yusuf_enwbw.epub)<sup>en wbw</sup> |
| Тоҷикӣ — Tajik | Khawaja Mirof & Khawaja Mir | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-tg-mirof.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-tg-mirof.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-tg-mirof_enwbw.epub)<sup>en wbw</sup> |
| Қазақша — Kazakh | Khalifa Altay | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-kk-altay.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-kk-altay.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-kk-altay_enwbw.epub)<sup>en wbw</sup> |
| Shqip — Albanian | Sherif Ahmeti | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-sq-ahmeti_enwbw.epub)<sup>en wbw</sup> |
| Polski | Józef Bielawski | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-pl-bielawski_enwbw.epub)<sup>en wbw</sup> |
| Українська — Ukrainian | Dr. Mikhailo Yaqubovic | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-uk-yaqubovic_enwbw.epub)<sup>en wbw</sup> |
| አማርኛ — Amharic | Sadiq and Sani | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-am-sadiq.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-am-sadiq.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-am-sadiq_enwbw.epub)<sup>en wbw</sup> |
| Yorùbá | Shaykh Abu Rahimah Mikael Aykyuni | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_bilin_ar-yo-mikael.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_interactive_ar-yo-mikael.epub) | [epub](../../releases/download/v0.9.0/quran_hafs_kfgqpc_wbw_ar-yo-mikael_enwbw.epub)<sup>en wbw</sup> |

</details>

Word-by-Word download links: **epub** = native-language word gloss, **epub**<sup>en wbw</sup> = English word gloss, **epub**<sup>id wbw</sup> = Indonesian word gloss. Cross-language WBW pairs English (or Indonesian) word-level meanings with a full sentence translation in the target language — useful for readers who understand basic English vocabulary but prefer reading a translation in their own language.

Many translations include translator footnotes where the source data provides them (Sahih International, Hamidullah, Garcia, Hamza Roberto Piccardo, Nasr, and others). Editions marked "with commentary" or "annotated" have especially extensive notes — Tafhim ul-Quran includes Sayyid Abul Ala Maududi's full tafseer-style commentary, and the annotated Clear Quran has 1,270 scholarly footnotes. See [KOReader Settings](../../#koreader-settings) for footnote popup setup.

**Note on Maududi footnotes:** A small number (~9%) of Tafhim ul-Quran footnotes are truncated in the upstream source data (ending mid-sentence). This is a known issue in the digitized text that all online sources share — not specific to this project.

### Updating EPUBs

Overwrite the old file with the new one, keeping the same filename. KOReader (and most e-readers) store your reading position, highlights, and settings separately — they will be preserved. Do **not** delete the book from within KOReader before replacing, as this will delete your data. After updating, you can force refresh metadata (cover, etc) by long-pressing the book in KOReader and selecting Refresh cached metadata.


**Full Changelog**: https://github.com/zeeyado/quran-ebook/compare/v0.8.0...v0.9.0

# v0.8.0

109 EPUB files across 42 languages — bilingual, interactive, word-by-word, and Arabic-only.

### New since v0.7.1

**Word-by-word interlinear layout** — each Arabic word paired with its translation directly below, forming visual word stacks. A full sentence translation follows each ayah. 13 variants across 8 languages: English (5 translations), Turkish, Urdu (2), Indonesian, Bengali, Persian, Hindi, and Tamil. Word-level glosses sourced from Quran.com API.

**Warsh 'an Nafi' (experimental)** — Arabic-only test build using KFGQPC Warsh data (Madani ayah numbering, 6,214 ayahs). Correct text rendering, juz boundaries, and hizb markers. Known limitations include plain surah headers (no calligraphic glyphs) and virtual page numbers not tied to real mushaf. See [Other Riwayat (Work in Progress)](../../#other-riwayat-work-in-progress) for details — feedback welcome.

**Redesigned covers** — color-coded PNG covers by variant type (bilingual, interactive, Arabic-only, word-by-word) with per-language Noto fonts for translator labels and Scheherazade New for Arabic riwayah text. In-book XHTML covers now also use native translator names and improved vertical centering.

**KOReader companion resources updated** — all 20 tafsir dictionaries and 6 surah overview dictionaries rebuilt as v1.1, fixing oversized headings in dictionary popups.

**Typography and layout fixes** — ayah/hizb marker spacing in justified inline text, Scheherazade New for TOC Arabic text, expanded symbol font subset, fixed WBW long-ayah duplication bug.

KOReader addons: [plugin](../../#install) · [word dictionary](../../#dictionary) · [grammar & i'rab](../../#grammar-dictionary-lookup) · [tafsir](../../#tafsir-commentary-lookup) · [surah overview](../../#surah-overview-lookup) · [setup tips](../../#koreader-settings)

## EPUBs

### Arabic

| Riwayah | | |
|---------|---|---|
| Hafs | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_inline_ar.epub) | Continuous flowing text, no translation |
| Warsh (experimental) | [epub](../../releases/download/v0.8.0/quran_warsh_kfgqpc_inline_ar.epub) | Arabic-only, Riwayat Warsh 'an Nafi' — see [known limitations](../../#other-riwayat-work-in-progress) |

### English

| Translator | Bilingual | Interactive | Word-by-Word |
|-----------|:---------:|:-----------:|:------------:|
| Sahih International | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-en-sahih.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-en-sahih.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-en-sahih.epub) |
| M.A.S. Abdel Haleem | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-en-haleem.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-en-haleem.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-en-haleem.epub) |
| Sayyid Abul Ala Maududi (Tafhim ul-Quran) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-en-maududi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-en-maududi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-en-maududi.epub) |
| Dr. Mustafa Khattab / The Clear Quran | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-en-khattab.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-en-khattab.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-en-khattab.epub) |
| Dr. Mustafa Khattab / The Clear Quran (annotated) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-en-khattab-fn.epub) |

### Other languages

<details><summary>Français, Deutsch, Español, Türkçe, اردو — Urdu, Bahasa Indonesia, Русский, বাংলা — Bengali</summary>

| Language | Translator | Bilingual | Interactive | Word-by-Word |
|----------|-----------|:---------:|:-----------:|:------------:|
| Français | Hamidullah | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-fr-hamidullah.epub) | |
| Deutsch | Bubenheim & Elyas | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-de-bubenheim.epub) | |
| Español | Isa Garcia | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-es-garcia.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-es-garcia.epub) | |
| Türkçe | Diyanet İşleri | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-tr-diyanet.epub) |
| اردو — Urdu | Jalandhari | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-ur-jalandhari.epub) |
| اردو — Urdu | Sayyid Abul Ala Maududi (Tafheem-ul-Quran) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ur-maududi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ur-maududi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-ur-maududi.epub) |
| Bahasa Indonesia | Kementerian Agama | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-id-ministry.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-id-ministry.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-id-ministry.epub) |
| Русский | Kuliev | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ru-kuliev.epub) | |
| বাংলা — Bengali | Taisirul Quran | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-bn-taisirul.epub) |

</details>

<details><summary>فارسی — Persian, Bahasa Melayu, Português, Italiano, Nederlands, Norsk, Svenska, Bosanski, Soomaali, Hausa, Fulfulde, Kiswahili</summary>

| Language | Translator | Bilingual | Interactive | Word-by-Word |
|----------|-----------|:---------:|:-----------:|:------------:|
| فارسی — Persian | Hussein Taji Kal Dari | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-fa-dari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-fa-dari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-fa-dari.epub) |
| Bahasa Melayu | Abdullah Muhammad Basmeih | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ms-basmeih.epub) | |
| Português | Helmi Nasr | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-pt-nasr.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-pt-nasr.epub) | |
| Italiano | Hamza Roberto Piccardo | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-it-piccardo.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-it-piccardo.epub) | |
| Nederlands | Sofian S. Siregar | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-nl-siregar.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-nl-siregar.epub) | |
| Norsk | Einar Berg | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-no-berg.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-no-berg.epub) | |
| Svenska | Knut Bernström | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-sv-bernstrom.epub) | |
| Bosanski | Besim Korkut | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-bs-korkut.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-bs-korkut.epub) | |
| Soomaali | Mahmud Muhammad Abduh | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-so-abduh.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-so-abduh.epub) | |
| Hausa | Abubakar Mahmoud Gumi | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ha-gumi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ha-gumi.epub) | |
| Fulfulde — Fula | Rowad Translation Center | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ff-ruwwad.epub) | |
| Kiswahili | Ali Muhsin Al-Barwani | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-sw-barwani.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-sw-barwani.epub) | |

</details>

<details><summary>हिन्दी — Hindi, தமிழ் — Tamil, മലയാളം — Malayalam, پښتو — Pashto, کوردی — Kurdish, ئۇيغۇرچە — Uyghur, 中文, 한국어, 日本語, ไทย, Tiếng Việt, Filipino</summary>

| Language | Translator | Bilingual | Interactive | Word-by-Word |
|----------|-----------|:---------:|:-----------:|:------------:|
| हिन्दी — Hindi | Maulana Azizul Haque al-Umari | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-hi-umari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-hi-umari.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-hi-umari.epub) |
| தமிழ் — Tamil | Abdul Hameed Baqavi | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_wbw_ar-ta-baqavi.epub) |
| മലയാളം — Malayalam | Abdul Hameed & Kunhi Mohammed | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ml-hameed.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ml-hameed.epub) | |
| پښتو — Pashto | Zakaria Abulsalam | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ps-abulsalam.epub) | |
| کوردی — Kurdish | Muhammad Saleh Bamoki | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ku-bamoki.epub) | |
| ئۇيغۇرچە — Uyghur | Muhammad Saleh | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ug-saleh.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ug-saleh.epub) | |
| 中文 — Chinese | Ma Jian | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-zh-majian.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-zh-majian.epub) | |
| 한국어 — Korean | Hamed Choi | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ko-choi.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ko-choi.epub) | |
| 日本語 — Japanese | Saeed Sato | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-ja-sato.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-ja-sato.epub) | |
| ไทย — Thai | King Fahad Quran Complex | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-th-fahad.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-th-fahad.epub) | |
| Tiếng Việt | Ruwwad Center | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-vi-ruwwad.epub) | |
| Filipino | Dar Al-Salam Center | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-tl-darsalam.epub) | |

</details>

<details><summary>Azərbaycanca, Oʻzbekcha, Тоҷикӣ — Tajik, Қазақша — Kazakh, Shqip — Albanian, Polski, Українська — Ukrainian, አማርኛ — Amharic, Yorùbá</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| Azərbaycanca | Alikhan Musayev | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-az-musayev.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-az-musayev.epub) |
| Oʻzbekcha | Muhammad Sodiq Muhammad Yusuf | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-uz-yusuf.epub) |
| Тоҷикӣ — Tajik | Khawaja Mirof & Khawaja Mir | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-tg-mirof.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-tg-mirof.epub) |
| Қазақша — Kazakh | Khalifa Altay | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-kk-altay.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-kk-altay.epub) |
| Shqip — Albanian | Sherif Ahmeti | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-sq-ahmeti.epub) |
| Polski | Józef Bielawski | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-pl-bielawski.epub) |
| Українська — Ukrainian | Dr. Mikhailo Yaqubovic | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-uk-yaqubovic.epub) |
| አማርኛ — Amharic | Sadiq and Sani | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-am-sadiq.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-am-sadiq.epub) |
| Yorùbá | Shaykh Abu Rahimah Mikael Aykyuni | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_bilin_ar-yo-mikael.epub) | [epub](../../releases/download/v0.8.0/quran_hafs_kfgqpc_interactive_ar-yo-mikael.epub) |

</details>

Many translations include translator footnotes where the source data provides them (Sahih International, Hamidullah, Garcia, Hamza Roberto Piccardo, Nasr, and others). Editions marked "with commentary" or "annotated" have especially extensive notes — Tafhim ul-Quran includes Sayyid Abul Ala Maududi's full tafseer-style commentary, and the annotated Clear Quran has 1,270 scholarly footnotes. See [KOReader Settings](../../#koreader-settings) for footnote popup setup.

### Updating EPUBs

Overwrite the old file with the new one, keeping the same filename. KOReader (and most e-readers) store your reading position, highlights, and settings separately — they will be preserved. Do **not** delete the book from within KOReader before replacing, as this will delete your data. After updating, you can force refresh metadata (cover, etc) by long-pressing the book in KOReader and selecting Refresh cached metadata.


**Full Changelog**: https://github.com/zeeyado/quran-ebook/compare/v0.7.1...v0.8.0

# v0.7.1

95 EPUB files across 42 languages — bilingual, interactive, and Arabic-only.

### New since v0.7.0

**Redesigned cover images** — color-coded PNG covers by variant type (bilingual, interactive, Arabic-only) with repositioned labels to clear KOReader's progress bar overlay.

**Post-build content verification** — `quran-ebook validate` now checks EPUB content integrity after building, not just epubcheck structural validation.

Latest KOReader addons: [plugin](../../#install) · [word dictionary](../../#dictionary) · [grammar & i'rab](../../#grammar-dictionary-lookup) · [tafsir](../../#tafsir-commentary-lookup) · [surah overview](../../#surah-overview-lookup) · [setup tips](../../#koreader-settings)


## EPUBs

### Arabic

| | |
|---|---|
| [Arabic-only](../../releases/download/v0.7.1/quran_hafs_kfgqpc_inline_ar.epub) | Continuous flowing text, no translation |

### English

| Translator | Bilingual | Interactive |
|-----------|:---------:|:-----------:|
| Sahih International | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-en-sahih.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-en-sahih.epub) |
| M.A.S. Abdel Haleem | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-en-haleem.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-en-haleem.epub) |
| Sayyid Abul Ala Maududi (Tafhim ul-Quran) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-en-maududi.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-en-maududi.epub) |
| Dr. Mustafa Khattab / The Clear Quran | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-en-khattab.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-en-khattab.epub) |
| Dr. Mustafa Khattab / The Clear Quran (annotated) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-en-khattab-fn.epub) |

### Other languages

<details><summary>Français, Deutsch, Español, Türkçe, اردو — Urdu, Bahasa Indonesia, Русский, বাংলা — Bengali</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| Français | Hamidullah | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-fr-hamidullah.epub) |
| Deutsch | Bubenheim & Elyas | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-de-bubenheim.epub) |
| Español | Isa Garcia | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-es-garcia.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-es-garcia.epub) |
| Türkçe | Diyanet İşleri | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-tr-diyanet.epub) |
| اردو — Urdu | Jalandhari | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ur-jalandhari.epub) |
| اردو — Urdu | Sayyid Abul Ala Maududi (Tafheem-ul-Quran) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ur-maududi.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ur-maududi.epub) |
| Bahasa Indonesia | Kementerian Agama | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-id-ministry.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-id-ministry.epub) |
| Русский | Kuliev | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ru-kuliev.epub) |
| বাংলা — Bengali | Taisirul Quran | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-bn-taisirul.epub) |

</details>

<details><summary>فارسی — Persian, Bahasa Melayu, Português, Italiano, Nederlands, Norsk, Svenska, Bosanski, Soomaali, Hausa, Fulfulde, Kiswahili</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| فارسی — Persian | Hussein Taji Kal Dari | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-fa-dari.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-fa-dari.epub) |
| Bahasa Melayu | Abdullah Muhammad Basmeih | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ms-basmeih.epub) |
| Português | Helmi Nasr | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-pt-nasr.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-pt-nasr.epub) |
| Italiano | Hamza Roberto Piccardo | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-it-piccardo.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-it-piccardo.epub) |
| Nederlands | Sofian S. Siregar | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-nl-siregar.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-nl-siregar.epub) |
| Norsk | Einar Berg | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-no-berg.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-no-berg.epub) |
| Svenska | Knut Bernström | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-sv-bernstrom.epub) |
| Bosanski | Besim Korkut | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-bs-korkut.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-bs-korkut.epub) |
| Soomaali | Mahmud Muhammad Abduh | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-so-abduh.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-so-abduh.epub) |
| Hausa | Abubakar Mahmoud Gumi | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ha-gumi.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ha-gumi.epub) |
| Fulfulde — Fula | Rowad Translation Center | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ff-ruwwad.epub) |
| Kiswahili | Ali Muhsin Al-Barwani | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-sw-barwani.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-sw-barwani.epub) |

</details>

<details><summary>हिन्दी — Hindi, தமிழ் — Tamil, മലയാളം — Malayalam, پښتو — Pashto, کوردی — Kurdish, ئۇيغۇرچە — Uyghur, 中文, 한국어, 日本語, ไทย, Tiếng Việt, Filipino</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| हिन्दी — Hindi | Maulana Azizul Haque al-Umari | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-hi-umari.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-hi-umari.epub) |
| தமிழ் — Tamil | Abdul Hameed Baqavi | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ta-baqavi.epub) |
| മലയാളം — Malayalam | Abdul Hameed & Kunhi Mohammed | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ml-hameed.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ml-hameed.epub) |
| پښتو — Pashto | Zakaria Abulsalam | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ps-abulsalam.epub) |
| کوردی — Kurdish | Muhammad Saleh Bamoki | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ku-bamoki.epub) |
| ئۇيغۇرچە — Uyghur | Muhammad Saleh | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ug-saleh.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ug-saleh.epub) |
| 中文 — Chinese | Ma Jian | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-zh-majian.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-zh-majian.epub) |
| 한국어 — Korean | Hamed Choi | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ko-choi.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ko-choi.epub) |
| 日本語 — Japanese | Saeed Sato | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-ja-sato.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-ja-sato.epub) |
| ไทย — Thai | King Fahad Quran Complex | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-th-fahad.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-th-fahad.epub) |
| Tiếng Việt | Ruwwad Center | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-vi-ruwwad.epub) |
| Filipino | Dar Al-Salam Center | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-tl-darsalam.epub) |

</details>

<details><summary>Azərbaycanca, Oʻzbekcha, Тоҷикӣ — Tajik, Қазақша — Kazakh, Shqip — Albanian, Polski, Українська — Ukrainian, አማርኛ — Amharic, Yorùbá</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| Azərbaycanca | Alikhan Musayev | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-az-musayev.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-az-musayev.epub) |
| Oʻzbekcha | Muhammad Sodiq Muhammad Yusuf | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-uz-yusuf.epub) |
| Тоҷикӣ — Tajik | Khawaja Mirof & Khawaja Mir | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-tg-mirof.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-tg-mirof.epub) |
| Қазақша — Kazakh | Khalifa Altay | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-kk-altay.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-kk-altay.epub) |
| Shqip — Albanian | Sherif Ahmeti | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-sq-ahmeti.epub) |
| Polski | Józef Bielawski | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-pl-bielawski.epub) |
| Українська — Ukrainian | Dr. Mikhailo Yaqubovic | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-uk-yaqubovic.epub) |
| አማርኛ — Amharic | Sadiq and Sani | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-am-sadiq.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-am-sadiq.epub) |
| Yorùbá | Shaykh Abu Rahimah Mikael Aykyuni | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_bilin_ar-yo-mikael.epub) | [epub](../../releases/download/v0.7.1/quran_hafs_kfgqpc_interactive_ar-yo-mikael.epub) |

</details>

Many translations include translator footnotes where the source data provides them (Sahih International, Hamidullah, Garcia, Hamza Roberto Piccardo, Nasr, and others). Editions marked "with commentary" or "annotated" have especially extensive notes — Tafhim ul-Quran includes Sayyid Abul Ala Maududi's full tafseer-style commentary, and the annotated Clear Quran has 1,270 scholarly footnotes. See [KOReader Settings](../../blob/main/README.md#koreader-settings) for footnote popup setup.

### Updating EPUBs

Overwrite the old file with the new one, keeping the same filename. KOReader (and most e-readers) store your reading position, highlights, and settings separately — they will be preserved. Do **not** delete the book from within KOReader before replacing, as this will delete your data. After updating, you can force refresh metadata (cover, etc) by long-pressing the book in KOReader and selecting Refresh cached metadata.

---

**Full Changelog**: https://github.com/zeeyado/quran-ebook/compare/v0.7.0...v0.7.1

# v0.7.0

95 EPUB files across 42 languages — bilingual, interactive, and Arabic-only.

### New since v0.6.0

**Cover images** — each EPUB now has a generated PNG cover (1200×1600) with calligraphic glyph and variant label showing riwayah, layout, language, and translator.

**Five-font EPUB** — added Me Quran (subsetted 460→5KB) for surah header labels (ترتيبها / آياتها). Now five embedded fonts: KFGQPC (body) + Scheherazade New (symbols) + quran-common (basmala) + Surah Name V2 (calligraphic headers) + Me Quran (header labels).

**Surah name font upgrade** — switched from V4 to V2 (1421H Madani Mushaf edition) for lighter calligraphic strokes in chapter headers.

**Script-aware translation sizing** — translations in Arabic-script, Thai/Khmer, South Indian, Ethiopic, and Myanmar scripts now render at 0.65em (was 0.6em) for better readability on e-ink.

**Page break control** — `break-inside: avoid` prevents ayahs and translations from splitting across pages.

**Fulfulde (Fula)** — 42nd language added. First language sourced exclusively from fawazahmed0/quran-api.

**Grammar dictionary v1.1** — improved e-ink formatting, RTL i'rab alignment, verb-as-pronoun classification fix.

## Downloads

### Dictionaries & Tools

| | |
|---|---|
| [Word dictionary v1.1](../../releases/download/v0.7.0/quran_qpc_en_stardict_v1.1.zip) | Word-by-word dictionary ([details](../../blob/v0.7.0/README.md#dictionary)) |
| [Grammar plugin v1.0](../../releases/download/v0.7.0/quran_koplugin_v1.0.zip) | Ayah-level grammar lookup plugin ([details](../../blob/v0.7.0/README.md#grammar-dictionary)) |
| [Grammar — combined v1.1](../../releases/download/v0.7.0/quran_grammar_combined_v1.1.zip) | WBW + morphology + syntax + i'rab |
| [Grammar — lite v1.1](../../releases/download/v0.7.0/quran_grammar_lite_v1.1.zip) | WBW + morphology + syntax (no i'rab) |
| [Grammar — i'rab only v1.1](../../releases/download/v0.7.0/quran_irab_v1.1.zip) | Traditional Arabic grammatical analysis only |

### EPUBs

#### Arabic

| | |
|---|---|
| [Arabic-only](../../releases/download/v0.7.0/quran_hafs_kfgqpc_inline_ar.epub) | Continuous flowing text, no translation |

#### English

| Translator | Bilingual | Interactive |
|-----------|:---------:|:-----------:|
| Sahih International | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-en-sahih.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-en-sahih.epub) |
| Abdel Haleem | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-en-haleem.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-en-haleem.epub) |
| Maududi / Tafhim ul-Quran (with commentary) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-en-maududi.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-en-maududi.epub) |
| Dr. Mustafa Khattab / The Clear Quran | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-en-khattab.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-en-khattab.epub) |
| Dr. Mustafa Khattab / The Clear Quran (annotated) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-en-khattab-fn.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-en-khattab-fn.epub) |

#### Other languages

<details><summary>Français, Deutsch, Español, Türkçe, اردو — Urdu, Bahasa Indonesia, Русский, বাংলা — Bengali</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| Français | Hamidullah | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-fr-hamidullah.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-fr-hamidullah.epub) |
| Deutsch | Bubenheim & Elyas | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-de-bubenheim.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-de-bubenheim.epub) |
| Español | Isa Garcia | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-es-garcia.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-es-garcia.epub) |
| Türkçe | Diyanet İşleri | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-tr-diyanet.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-tr-diyanet.epub) |
| اردو — Urdu | Jalandhari | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ur-jalandhari.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ur-jalandhari.epub) |
| اردو — Urdu | Maududi / Tafheem ul-Quran (with commentary) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ur-maududi.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ur-maududi.epub) |
| Bahasa Indonesia | Kementerian Agama | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-id-ministry.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-id-ministry.epub) |
| Русский | Kuliev | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ru-kuliev.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ru-kuliev.epub) |
| বাংলা — Bengali | Taisirul Quran | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-bn-taisirul.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-bn-taisirul.epub) |

</details>

<details><summary>فارسی — Persian, Bahasa Melayu, Português, Italiano, Nederlands, Norsk, Svenska, Bosanski, Soomaali, Hausa, Fulfulde, Kiswahili</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| فارسی — Persian | Taji Kal Dari | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-fa-dari.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-fa-dari.epub) |
| Bahasa Melayu | Basmeih | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ms-basmeih.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ms-basmeih.epub) |
| Português | Helmi Nasr | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-pt-nasr.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-pt-nasr.epub) |
| Italiano | Piccardo | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-it-piccardo.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-it-piccardo.epub) |
| Nederlands | Sofian S. Siregar | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-nl-siregar.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-nl-siregar.epub) |
| Norsk | Einar Berg | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-no-berg.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-no-berg.epub) |
| Svenska | Knut Bernström | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-sv-bernstrom.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-sv-bernstrom.epub) |
| Bosanski | Besim Korkut | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-bs-korkut.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-bs-korkut.epub) |
| Soomaali | Mahmud Muhammad Abduh | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-so-abduh.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-so-abduh.epub) |
| Hausa | Abubakar Mahmoud Gumi | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ha-gumi.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ha-gumi.epub) |
| Fulfulde — Fula | Rowad Translation Center | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ff-ruwwad.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ff-ruwwad.epub) |
| Kiswahili | Ali Muhsin Al-Barwani | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-sw-barwani.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-sw-barwani.epub) |

</details>

<details><summary>हिन्दी — Hindi, தமிழ் — Tamil, മലയാളം — Malayalam, پښتو — Pashto, کوردی — Kurdish, ئۇيغۇرچە — Uyghur, 中文, 한국어, 日本語, ไทย, Tiếng Việt, Filipino</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| हिन्दी — Hindi | al-Umari | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-hi-umari.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-hi-umari.epub) |
| தமிழ் — Tamil | Baqavi | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ta-baqavi.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ta-baqavi.epub) |
| മലയാളം — Malayalam | Abdul Hameed & Kunhi Mohammed | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ml-hameed.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ml-hameed.epub) |
| پښتو — Pashto | Zakaria Abulsalam | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ps-abulsalam.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ps-abulsalam.epub) |
| کوردی — Kurdish | Muhammad Saleh Bamoki | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ku-bamoki.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ku-bamoki.epub) |
| ئۇيغۇرچە — Uyghur | Muhammad Saleh | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ug-saleh.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ug-saleh.epub) |
| 中文 — Chinese | Ma Jian | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-zh-majian.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-zh-majian.epub) |
| 한국어 — Korean | Hamed Choi | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ko-choi.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ko-choi.epub) |
| 日本語 — Japanese | Saeed Sato | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-ja-sato.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-ja-sato.epub) |
| ไทย — Thai | King Fahad Quran Complex | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-th-fahad.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-th-fahad.epub) |
| Tiếng Việt | Ruwwad Center | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-vi-ruwwad.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-vi-ruwwad.epub) |
| Filipino | Dar Al-Salam Center | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-tl-darsalam.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-tl-darsalam.epub) |

</details>

<details><summary>Azərbaycanca, Oʻzbekcha, Тоҷикӣ — Tajik, Қазақша — Kazakh, Shqip — Albanian, Polski, Українська — Ukrainian, አማርኛ — Amharic, Yorùbá</summary>

| Language | Translator | Bilingual | Interactive |
|----------|-----------|:---------:|:-----------:|
| Azərbaycanca | Alikhan Musayev | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-az-musayev.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-az-musayev.epub) |
| Oʻzbekcha | Muhammad Sodiq Muhammad Yusuf | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-uz-yusuf.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-uz-yusuf.epub) |
| Тоҷикӣ — Tajik | Khawaja Mirof & Khawaja Mir | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-tg-mirof.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-tg-mirof.epub) |
| Қазақша — Kazakh | Khalifa Altay | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-kk-altay.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-kk-altay.epub) |
| Shqip — Albanian | Sherif Ahmeti | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-sq-ahmeti.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-sq-ahmeti.epub) |
| Polski | Józef Bielawski | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-pl-bielawski.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-pl-bielawski.epub) |
| Українська — Ukrainian | Dr. Mikhailo Yaqubovic | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-uk-yaqubovic.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-uk-yaqubovic.epub) |
| አማርኛ — Amharic | Sadiq and Sani | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-am-sadiq.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-am-sadiq.epub) |
| Yorùbá | Shaykh Abu Rahimah Mikael Aykyuni | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_bilin_ar-yo-mikael.epub) | [epub](../../releases/download/v0.7.0/quran_hafs_kfgqpc_interactive_ar-yo-mikael.epub) |

</details>

Many translations include translator footnotes where the source data provides them (Sahih International, Hamidullah, Garcia, Piccardo, Nasr, and others). Editions marked "with commentary" or "annotated" have especially extensive notes — Tafhim ul-Quran includes Maududi's full tafseer-style commentary, and the annotated Clear Quran has 1,270 scholarly footnotes. See [KOReader Settings](../../blob/v0.7.0/README.md#koreader-settings) for footnote popup setup.

See [README](../../blob/v0.7.0/README.md#koreader-settings) for KOReader setup tips (footnote popups, RTL page turns, mushaf page numbers).


**Full Changelog**: https://github.com/zeeyado/quran-ebook/compare/v0.6.0...v0.7.0
