# readeck.koplugin

A [KOReader](https://koreader.rocks/) plugin to add integration with your
[Readeck](https://readeck.org/en/) instance's API.

> [!WARNING]  
> THIS IS STILL IN EARLY DEVELOPMENT, AND MAY NOT FUNCTION AS EXPECTED SOMETIMES.  
> Early progress tracked in [TODO.md](./TODO.md)

## Installation

Simply put this repo in your KOReader's plugin folder (koreader/plugins).

*No need to also copy the koreader git submodule (`./koreader`), as it's only
there for better Lua development integration.*

## Usage

#TODO

- Browse bookmarks  
	You can browse your bookmarks and collections in `🔎 > Readeck bookmarks` (will likely be on the second page of the `🔎` menu).
- Save links  
	You can click on links while reading to add them as a bookmark to Readeck.

## Configuration

Settings can be changed within KOReader in `🔎 > Settings > Readeck Settings`.

### Server and credentials

You **must** set the Server URL and either:
- Username and Password, and click on "Sign in";
- or the API Token, and click on "Save".

If you don't want your password being stored in plaintext on your device, you
can manually create your API token at `http(s)://[yourreadeckserver]/profile/tokens`.
Don't forget to set both the "Bookmarks: Read Only" and "Bookmarks: Write Only"
roles.

### Misc.

- New bookmark settings:
	- Default labels: Comma-separated list of labels to add by default when
		creating new bookmarks from links.

You can also configure it by changing the `readeck.lua` file in your
`koreader/settings` folder:

```koreader/settings/readeck.lua
return {
  data_dir = nil -- default: require("datastorage"):getDataDir() .. "/readeck",
  server_url = "http(s)://[yourreadeckserver]/", -- mandatory
  username = nil, -- Needed to generate the API token automatically
  password = nil, -- Needed to generate the API token automatically
  api_token = nil, -- Generated automatically if username and password are given,
                   -- but can also be set manually.
  default_labels = { }, -- string list
}
```

