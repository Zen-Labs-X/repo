# v1.4.0

- show popup on bulk download process
- name downloads after the article title, without the bookmark id 
- add author, excerpt, cover and chapters to downloaded articles

# v1.3.3

- fix: don't crash on non-http(s) image URLs
  Articles can contain `<img src="file://...">` or other non-web schemes
  (leftover from broken exports); socket.http has no handler for these
  and throws uncaught, crashing the reader. Reject unsupported schemes
  in resolveUrl and wrap http.request in pcall as a backstop.

# v1.3.2

- fill author field for HTML and epub output file

# v1.3.1

- fix: rendering of article listing

# v1.3.0

- "add to Instapaper" button in link popup
- fix: safety controls for the custom cache folder
