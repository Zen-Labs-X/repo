# SmartDeck

AI-powered flashcard plugin for KOReader.

Select a word or phrase from the book (via the highlight menu) or from the
dictionary popup, and SmartDeck will store the card into an SQLite database.
When an internet connection is available, the plugin will use an AI provider
to enrich every card with:

* Pronunciation / phonetics
* Word type (part of speech)
* Meaning in your preferred target language
* Up to three example sentences
* The surrounding context (X words around the selection) that was sent to the AI

Cards can be reviewed in a study screen similar to PhraseDeck, with a
configurable **front** and **back** (choose which fields are shown on each side,
similar to the AnkiViewer plugin). Editing and deleting cards are both
supported; after editing the phrase you can decide whether to keep the current
content, clear it for a later refetch, or refetch immediately.

## Configuration

Copy `smartdeck_configuration.sample.lua` to `smartdeck_configuration.lua` and
fill in the API key(s) for your provider. Multiple named providers are
supported (e.g. `openai`, `openai_grok`, `anthropic`, `gemini`) – name-based
dispatch selects the handler (the part before the first `_`) in exactly the
same way as the AI Assistant plugin does.

### Supported providers

* **OpenAI-compatible** (`openai` handler): OpenAI, Groq, xAI Grok, DeepSeek,
  Mistral, OpenRouter, Azure OpenAI, local Ollama servers using the
  `/v1/chat/completions` endpoint, and any other provider that implements the
  OpenAI chat completions format.
* **Anthropic** (`anthropic` handler): Claude models via the Messages API.
* **Google Gemini** (`gemini` handler): Gemini models via the native
  `generateContent` endpoint.
* **Ollama** (`ollama` handler): Ollama's native `/api/chat` endpoint for local
  models.

See `smartdeck_configuration.sample.lua` for configuration examples.

## Main menu

* **Study** — open the spaced-repetition review screen.
* **Cards for this book** / **All cards** — browse, edit, or delete cards.
  Each list includes a **Filter** button in the bottom toolbar for quick
  case-insensitive search across phrase, meaning, note, word type,
  pronunciation, and sentence fields. Filter is session-only (cleared when
  reopening the list).
* **Fetch missing info** — cancellable bulk enrichment of cards that don't
  yet have AI data. Failed requests are automatically retried up to 3 times
  with exponential backoff (1.5s, 3s) to handle transient network errors and
  rate limits. Tap outside the progress popup to cancel.
* **Import from Vocabulary Builder** — imports words collected by the built-in
  Vocabulary Builder into the current book's deck.
* **Settings** — provider selection, target language, context-word counts,
  auto-fetch toggle, example count, front/back field selection, daily new
  card limit, randomization, etc.

## Highlight menu & dictionary popup

* A "SmartDeck" button is injected into the highlight menu while reading.
* A "SmartDeck" button is injected into the dictionary popup; tap it to send
  the looked-up word directly to the deck.

**Note**: In newer KOReader versions (2026.05+), dictionary popup buttons can be
customized via **Dictionary settings → Customize buttons → Max buttons in row**.
Increase this value to display multiple plugin buttons on the same row.

## Credits
This project was created with assistance from Windsurf (AI).