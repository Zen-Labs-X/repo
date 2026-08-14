- add: optional "Web Search" button in the text selection popup

    Adds a Web Search button next to Search and Wikipedia in the reader
    highlight menu, so a selection can be searched without opening the
    browser dialog and retyping the query.
    
    - tap searches the selection with the currently selected engine
    - hold opens the search dialog prefilled with the selection
    - selection is cleaned up, whitespace collapsed and capped at 300 chars
      on a word boundary before it is sent to the engine
    - off by default, enabled with search_highlighted_text = true
 