# v1.40.1

## [1.40.1](https://github.com/tachibana-shin/rakuyomi/compare/v1.40.0...v1.40.1) (2026-08-18)


### Bug Fixes

* condition for android build key in build-all.sh ([6e6e736](https://github.com/tachibana-shin/rakuyomi/commit/6e6e7369bf05638e09a3fc7decf2e488768d0c05))

# v1.40.0

# [1.40.0](https://github.com/tachibana-shin/rakuyomi/compare/v1.39.6...v1.40.0) (2026-08-18)


### Bug Fixes

* crash on tracking OAuth sign-in: Size.span.vertical_small does not exist ([#295](https://github.com/tachibana-shin/rakuyomi/issues/295)) ([5fcd0ee](https://github.com/tachibana-shin/rakuyomi/commit/5fcd0ee0e82ce7a1da14697fc1c08514c0631754))
* fetch CBZ metadata from the server instead of executing a binary ([#300](https://github.com/tachibana-shin/rakuyomi/issues/300)) ([35d4c35](https://github.com/tachibana-shin/rakuyomi/commit/35d4c358e3b030fc87aca5ace128156e8b798e11)), closes [#287](https://github.com/tachibana-shin/rakuyomi/issues/287)
* fix mangabaka tracking via API Key and OAuth2 ([#286](https://github.com/tachibana-shin/rakuyomi/issues/286)) ([0ad505e](https://github.com/tachibana-shin/rakuyomi/commit/0ad505ef83bc271a6502957fc87ee168c050fbb2))
* reconnect to Wi-Fi before retrying a failed chapter download ([#299](https://github.com/tachibana-shin/rakuyomi/issues/299)) ([97afb7c](https://github.com/tachibana-shin/rakuyomi/commit/97afb7cdd89534141a68e5397d0e87c33a9eb4a1)), closes [#277](https://github.com/tachibana-shin/rakuyomi/issues/277)
* **tracking:** include NSFW entries in MyAnimeList search ([#298](https://github.com/tachibana-shin/rakuyomi/issues/298)) ([212b082](https://github.com/tachibana-shin/rakuyomi/commit/212b08249f8e5f31ba42cb38c941b1145f46b0e3))


### Features

* support extension LNReader, Mangayomi (js, dart), Tachiyomi/Mihon ([#296](https://github.com/tachibana-shin/rakuyomi/issues/296)) ([a2d95f1](https://github.com/tachibana-shin/rakuyomi/commit/a2d95f1fb0184e90412f38c21a1e70cd04ab5656))

# v1.37.2

## [1.37.2](https://github.com/tachibana-shin/rakuyomi/compare/v1.37.1...v1.37.2) (2026-07-14)


### Performance Improvements

* add test cases to rust ([#248](https://github.com/tachibana-shin/rakuyomi/issues/248)) ([cecd3be](https://github.com/tachibana-shin/rakuyomi/commit/cecd3be2f65237cea0319f2ad54aa72038cde0a7))

# v1.37.1

## [1.37.1](https://github.com/tachibana-shin/rakuyomi/compare/v1.37.0...v1.37.1) (2026-07-14)


### Bug Fixes

* **tls:** use owned ClientConfig for use_preconfigured_tls and route … ([#246](https://github.com/tachibana-shin/rakuyomi/issues/246)) ([ac8c74a](https://github.com/tachibana-shin/rakuyomi/commit/ac8c74a0559feb3163203d90de5883e732491271))

# v1.37.0

# [1.37.0](https://github.com/tachibana-shin/rakuyomi/compare/v1.36.11...v1.37.0) (2026-07-13)


### Features

* add new js apis from aidoku-rs SDK ([#238](https://github.com/tachibana-shin/rakuyomi/issues/238)) ([09a972d](https://github.com/tachibana-shin/rakuyomi/commit/09a972d6c6942249b35a01c474580d22a774ff2e))
* implement Telegram bot for cookie management ([#233](https://github.com/tachibana-shin/rakuyomi/issues/233)) ([148a069](https://github.com/tachibana-shin/rakuyomi/commit/148a06930b1eb72476c07d830ac4f1f5ce82ed2a))
* **manga:** add per-manga viewer preference ([#241](https://github.com/tachibana-shin/rakuyomi/issues/241)) ([2553704](https://github.com/tachibana-shin/rakuyomi/commit/2553704bbc8bfbca868ecf9f2684e6091d463515))
* **proxy:** add global proxy support ([#239](https://github.com/tachibana-shin/rakuyomi/issues/239)) ([21a73ae](https://github.com/tachibana-shin/rakuyomi/commit/21a73aef5a65235f12f2a23839761fd1d380ab14))


### Performance Improvements

* **unix:** replace fork with posix_spawn ([#242](https://github.com/tachibana-shin/rakuyomi/issues/242)) ([cef20bc](https://github.com/tachibana-shin/rakuyomi/commit/cef20bc1af2b14af645b33dce301696788975ec0))
