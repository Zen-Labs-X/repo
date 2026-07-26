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