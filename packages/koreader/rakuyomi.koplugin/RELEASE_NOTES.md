# v1.41.8

## [1.41.8](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.7...v1.41.8) (2026-09-08)


### Bug Fixes

* **aidoku:** sync process_page_image on lazy boot ([#342](https://github.com/tachibana-shin/rakuyomi/issues/342)) ([82087f7](https://github.com/tachibana-shin/rakuyomi/commit/82087f74f42d88ebbb12b3df388df61f7c46874c))

# v1.41.7

## [1.41.7](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.6...v1.41.7) (2026-09-08)


### Bug Fixes

* apply cookies.json to wasm image requests ([#338](https://github.com/tachibana-shin/rakuyomi/issues/338)) ([#340](https://github.com/tachibana-shin/rakuyomi/issues/340)) ([2dbcbbc](https://github.com/tachibana-shin/rakuyomi/commit/2dbcbbc78d2f1d0ce9543ac872c23f83cd985c5a))
* **ui:** reconnect to Wi-Fi before retrying source list fetch ([#334](https://github.com/tachibana-shin/rakuyomi/issues/334)) ([#341](https://github.com/tachibana-shin/rakuyomi/issues/341)) ([ccdeaac](https://github.com/tachibana-shin/rakuyomi/commit/ccdeaac140c7fbfb60ee89a17f99ac9e6a8a53bf))

# v1.41.6

## [1.41.6](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.5...v1.41.6) (2026-09-05)


### Bug Fixes

* **html:** flatten nested element lists + MangaPlus blank images ([#336](https://github.com/tachibana-shin/rakuyomi/issues/336)) ([c46b1a8](https://github.com/tachibana-shin/rakuyomi/commit/c46b1a8e3ce3274584c0e8787da1d3b19c464b6a))

# v1.41.5

## [1.41.5](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.4...v1.41.5) (2026-09-01)


### Bug Fixes

* **html:** return element children only ([#331](https://github.com/tachibana-shin/rakuyomi/issues/331)) ([2c14a75](https://github.com/tachibana-shin/rakuyomi/commit/2c14a75a53cf295b1bff6372c48fb05a900dfb7d))
* **suwayomi:** correct GraphQL queries against real Suwayomi schema ([#333](https://github.com/tachibana-shin/rakuyomi/issues/333)) ([20f2a5c](https://github.com/tachibana-shin/rakuyomi/commit/20f2a5cf6ea12fece419bfb6911d9649f08c7baf))
* title bar icon sizing + human-readable language names ([#329](https://github.com/tachibana-shin/rakuyomi/issues/329)) ([fa05f9f](https://github.com/tachibana-shin/rakuyomi/commit/fa05f9f0bd8b90f6f31abd546a6fa5f4a5ad2c23))

# v1.41.4

## [1.41.4](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.3...v1.41.4) (2026-08-27)


### Bug Fixes

* **android:** register CbzDocument provider on Android too ([#327](https://github.com/tachibana-shin/rakuyomi/issues/327)) ([9b06ec2](https://github.com/tachibana-shin/rakuyomi/commit/9b06ec2d0cce4fa93e9f04c07e5b115a92f9fe84))
* mmap and munmap calls to use ffi.C ([8fd5a4d](https://github.com/tachibana-shin/rakuyomi/commit/8fd5a4d90af01e1ee9481bf1d60f4c367e360804))
