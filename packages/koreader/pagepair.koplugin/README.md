# PagePair

PagePair is a KOReader plugin that synchronizes page turns between two Kindles, allowing them to be used together as a two-page reading setup.

Use your normal Wi-Fi at home, or connect the Kindles directly with Travel Mode when no router is available.

> **Status:** Pre-release. PagePair has currently been tested on Kindle Basic 10th generation devices. Wider Kindle compatibility testing is still in progress.

## What PagePair does

One Kindle acts as the **Controller** and the other as the **Follower**.

When you turn a page on the Controller, PagePair moves the Follower to the corresponding page.

PagePair supports two connection modes:

### Home Wi-Fi

Both Kindles connect through your normal Wi-Fi network.

PagePair's **Home Wi-Fi setup** tells each Kindle where to find the other one.

### Travel Mode

The Kindles create a direct wireless connection to each other.

No router or internet connection is required.

While Travel Mode is active, normal Wi-Fi and internet access are unavailable on the Kindles.

## Requirements

For the currently tested configuration:

- Two compatible Kindles
- KOReader installed on both Kindles
- PagePair installed on both Kindles
- The same document available on both Kindles

Initial development and testing has been performed on Kindle Basic 10th generation devices.

Other Kindle models may work but have not yet been validated.

## Installation

1. Download the latest PagePair release.
2. Extract `pagepair.koplugin` into the KOReader plugins directory:

   `koreader/plugins/`

3. Restart KOReader.
4. Install PagePair on both Kindles.

## First-time setup

On one Kindle:

**PagePair → Role → Controller**

On the other:

**PagePair → Role → Follower**

Then choose:

**PagePair → Pair Kindles**

on both devices.

PagePair temporarily creates a direct connection between the Kindles and displays a six-digit verification code.

Confirm pairing only if the same code appears on both Kindles.

Pairing is normally required only once.

After pairing, PagePair can communicate using either Home Wi-Fi or Travel Mode.

## Page syncing

Pairing establishes trust between the two Kindles. Page syncing itself can be switched on or off separately using:

**PagePair → Page syncing**

## Home Wi-Fi setup

When both Kindles are connected to the same normal Wi-Fi network, open:

**PagePair → Home Wi-Fi setup**

Enter the other Kindle's Wi-Fi address.

On ordinary home networks, PagePair can usually use only the final number of the address.

## Travel Mode

Choose:

**PagePair → Travel Mode**

on both Kindles.

Travel Mode connects the Kindles directly and does not require a router.

Turn Travel Mode off to restore normal Wi-Fi and internet access.

## Updating

Replace the existing `pagepair.koplugin` directory with the version from the new release and restart KOReader.

Your PagePair pairing and settings are stored separately from the plugin directory.

## Security

PagePair creates a unique SSH identity for each Kindle during pairing.

The Kindles exchange public keys and random pairing data, then independently derive a six-digit verification code.

Confirm pairing only when the codes displayed on both Kindles match.

The installed PagePair SSH keys are restricted to the PagePair receiver rather than providing unrestricted shell access.

## Compatibility

| Device | Home Wi-Fi | Travel Mode | Status |
|---|---:|---:|---|
| Kindle Basic 10th gen | ✅ | ✅ | Tested |

More devices will be added as they are tested.

## Support PagePair

PagePair is free and open source.

If you find it useful and would like to support continued development:

**Buy Me a Coffee:** `buymeacoffee.com/pagepair`

## Bugs and feedback

Please use GitHub Issues to report bugs, compatibility results, or feature requests.

When reporting a problem, please include:

- Kindle model
- Kindle firmware version
- KOReader version
- PagePair version
- Controller and Follower models
- Whether you were using Home Wi-Fi or Travel Mode
- What happened
- What you expected to happen

## License

PagePair is licensed under the GNU Affero General Public License v3.0 only.

The bundled `pp-keygen` helper is built using the Go standard library.
See `THIRD_PARTY_NOTICES.md` for third-party licensing information.
