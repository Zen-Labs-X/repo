# v0.7.1

- add: optional "Web Search" button in the text selection popup

    Adds a Web Search button next to Search and Wikipedia in the reader
    highlight menu, so a selection can be searched without opening the
    browser dialog and retyping the query.
    
    - tap searches the selection with the currently selected engine
    - hold opens the search dialog prefilled with the selection
    - selection is cleaned up, whitespace collapsed and capped at 300 chars
      on a word boundary before it is sent to the engine
    - off by default, enabled with search_highlighted_text = true

# v0.7.0

- open sanitized and save sanitized buttons on search popup (uses [rssreader.koplugin](https://github.com/omer-faruq/rssreader.koplugin) functions, so you need to install it also) 
- cache folder safety modifications

# v0.6.1

- fix: DuckDuckGo language setting missing

# v0.6.0

- new search engines: Tavily, Exa
- enable multiple profiles for the same engine
- fix: settings popup language selection

# v0.5.0

- settings popup added (search engine, language, and country selection) 
- fix: language support for search engines
