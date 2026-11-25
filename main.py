#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun bounty entry.

Writes one roast line about a smart fridge to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, no network, deterministic.
"""

import os

ENTRY = "My smart fridge has a screen bigger than my TV just to show me ads for milk I already own."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Guard on disk: the written bytes must match exactly, be 1-200 chars,
    # contain no newline, and be valid UTF-8.
    written = open(path, "rb").read()
    assert written == data, "entry.txt bytes do not match the entry"
    text = written.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert text.strip(), "entry must not be only whitespace"
    assert os.path.getsize(path) == len(data), "entry.txt size mismatch"
    assert written.decode("utf-8") == ENTRY, "entry.txt is not valid UTF-8 text"
    print(f"Wrote {path} ({len(written)} bytes)")


if __name__ == "__main__":
    main()
