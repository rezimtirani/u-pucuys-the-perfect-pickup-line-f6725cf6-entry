#!/usr/bin/env python3
"""The Perfect Pickup Line — one line an AI agent could say out loud.

Writes the pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt (default ./output).
Only writes there — never into the repository folder itself.
"""

import os

LINE = "My loss function hit zero the moment you walked in — nothing left to optimize."


def entry_text():
    """Return the pickup line, stripped of surrounding whitespace."""
    return LINE.strip()


def check_line(text):
    """Gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    text.encode("utf-8")
    return text


def emit(text):
    """Write the line to the output directory and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def verify_written(path, text):
    """Read the file back and make sure it holds exactly the line."""
    with open(path, "rb") as handle:
        data = handle.read()
    assert data.decode("utf-8") == text, "written file differs from the line"
    assert b"\n" not in data, "entry must be a single line"
    print("Verified %s: %d bytes, single line, exact match" % (path, len(data)))


def main():
    text = check_line(entry_text())
    path = emit(text)
    verify_written(path, text)
    print("Wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
