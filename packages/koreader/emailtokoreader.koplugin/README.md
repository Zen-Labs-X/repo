# Email to KOReader (Streaming Architecture Fork)

Automatically download EPUB files from your email directly to your KOReader device.

> **Note on this fork:** This version features a completely rebuilt, embedded-safe streaming IMAP parser designed specifically for low-memory e-ink devices like the Kindle Paperwhite. 

## 🚀 The Streaming Refactor
The original version of this plugin processed emails by loading the entire payload into memory and running heavy regex scans, which could cause watchdog freezes and crashes on 800MHz e-ink hardware when downloading large (5MB+) EPUBs. 

This fork introduces a **True Streaming Architecture**:
* **IMAP Literal Accounting:** Reads exact byte counts to prevent protocol strings from corrupting the EPUB ZIP structure.
* **Bounded Memory Usage:** Decodes Base64 payloads directly to disk in 8KB mathematically aligned chunks.
* **UI Yielding:** Cooperatively yields to the KOReader UI loop to prevent device watchdog lockups.
* **Strict RFC MIME Parsing:** Accurately isolates payloads and prevents random truncation from nested email boundaries.
* **Atomic Filesystem Writes:** Safely writes to `.tmp` files and renames them only upon successful verification.

## 📦 Installation
1. Download the latest version of this repository.
2. Place the `emailtokoreader.koplugin` folder into your KOReader `plugins` directory (usually `koreader/plugins/`).
3. Open `config.lua` and add your email credentials (use an App Password if using Gmail).
4. Restart KOReader.

## 📖 Usage & Filename Requirements
Because KOReader's internal library scanner relies on standard naming conventions to extract metadata, **your EPUB attachments must be named precisely**.

* **Format:** `Book Title - Author Name.epub`
* **Valid Example:** `The Martian - Andy Weir.epub`
* **Invalid Example:** `The-Martian-Andy-Weir.epub` *(Dashes instead of spaces will cause KOReader to fail to read the EPUB format!)*

To trigger a download, simply open KOReader's top menu, navigate to **Tools > Email to KOReader**, and tap **Check Inbox**.