**Full Changelog**: https://github.com/stelzch/zotero.koplugin/compare/0.2.1...1.0.0-rc.1

* **Use SQLite3 to store item metadata** instead of dumping API responses into JSON file (issue #19). Feel free to delete `items.json` and `collections.json` after upgrading.
* **Support uploading annotations of PDF files via Zotero API** (issue #13). Limitations as outlined in the README apply (one-way sync, no updates/deletes)
* **Collections can now be marked as offline collection**. All attachments of offline-attachments are downloaded during synchronization, making them available without network connectivity.
* Show sync progress
* Support choosing from multiple attachments using tap-hold

This is a pre-release. Feedback and bug reports are highly appreciated before we can release it as final v1.0.