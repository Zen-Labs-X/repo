# v0.3

UX upgrades all around thanks to community feedback

- **Automatic plugin updating**: checks latest release version on Github, and prompts the user for an update with patch note information (suggested by [kelmi3D](https://www.reddit.com/user/kelmi3D/))
- **Show book covers in search**: optionally show book covers alongside books in search results. Better formatted book information using a custom menu (suggested by [2211mg](https://www.reddit.com/user/2211mg/)). Note that book cover downloads can be hit or miss on older Kindles so there is a toggle for it in settings.
- **Tap book cover to expand to full screen** (suggested by [IbnRami](https://www.reddit.com/user/IbnRami/))
- **Simplify download prompt**: only have path + download buttons, and tap outside to close (suggested by [IbnRami](https://www.reddit.com/user/IbnRami/))
- **Extend search caches**: search caches now expire after 2 weeks and have max 1000 entries
- **Prompt updates**: plugin and curl updates will prompt the user first rather than being triggered automatically

# v0.2

Big update this one

- **Caching**: Caches search results (72 hours), mirror URLs (7 days), and book covers (for length of search) to minimise network requests and improve performance
- **Preferences**: Filter results by preferred languages, file types, and book types
- **Book Cover Previews**: Display cover images in download previews
- **Background Downloads**: Downloads run in the background using curl, with non-blocking UI updates
- **Automatic Curl Updates**: Ensures a compatible curl version (8.17.0+) is available
- **Automatic Retry Logic**: Fallback to other available urls if connection fails
- **Safe File Handling**: Automatic filename sanitisation and directory management

# v0.1

**Initial release** - it works, but don't expect much else. And don't expect it to always work.
