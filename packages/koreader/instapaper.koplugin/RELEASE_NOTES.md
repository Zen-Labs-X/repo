- fix: don't crash on non-http(s) image URLs
  Articles can contain `<img src="file://...">` or other non-web schemes
  (leftover from broken exports); socket.http has no handler for these
  and throws uncaught, crashing the reader. Reject unsupported schemes
  in resolveUrl and wrap http.request in pcall as a backstop.