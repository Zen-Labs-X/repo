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

# v1.41.3

## [1.41.3](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.2...v1.41.3) (2026-08-26)


### Bug Fixes

* alias `@/types/constants` lnreader ([17cc35c](https://github.com/tachibana-shin/rakuyomi/commit/17cc35c270d359f9a47fd27818765c407da7ee84)), closes [#324](https://github.com/tachibana-shin/rakuyomi/issues/324)

# v1.41.2

## [1.41.2](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.1...v1.41.2) (2026-08-24)


### Bug Fixes

* rebuild focused backend fixes ([#314](https://github.com/tachibana-shin/rakuyomi/issues/314)) ([bd3cad5](https://github.com/tachibana-shin/rakuyomi/commit/bd3cad5e6a268afa4336398e9ab3d737711b7fcb))

# v1.41.1

## [1.41.1](https://github.com/tachibana-shin/rakuyomi/compare/v1.41.0...v1.41.1) (2026-08-23)


### Bug Fixes

* disable stream mode ([11e7d37](https://github.com/tachibana-shin/rakuyomi/commit/11e7d37613ce462e66ea4e8d72f8c5f465138e88))


### Reverts

* remove streaming reader from main (still in development on feat/stream-read) ([92bb8df](https://github.com/tachibana-shin/rakuyomi/commit/92bb8df93c6a3155758d77be003b59e0c0fb50c8))
