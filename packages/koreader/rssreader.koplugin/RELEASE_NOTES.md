- Fix non-Latin titles (Cyrillic, etc.) being sanitized to underscores in filenames

    Filename sanitization used a whitelist of ASCII word chars, so any
    non-ASCII letter was stripped, turning archived titles into
    all-underscore filenames. Switch to a blacklist of characters actually
    illegal in filenames, and make title truncation UTF-8 boundary aware
    so it can't cut a multi-byte character in half.