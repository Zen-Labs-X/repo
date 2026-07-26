#!/usr/bin/env python3
"""Serve this repository locally for ZenPM development."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PORT = 8000


def main() -> None:
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(
        *args, directory=REPOSITORY_ROOT, **kwargs
    )
    server = ThreadingHTTPServer(("0.0.0.0", PORT), handler)
    print(f"Serving manifest at http://localhost:{PORT}/manifest.json")
    print("Press Ctrl-C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
