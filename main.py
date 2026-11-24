#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes one funny AI weekly status line.

Writes the exact line to $OUTPUT_DIR/entry.txt (default /output), with no
trailing newline, then self-verifies the written file: UTF-8, 1-200 chars,
not only whitespace, exact match, no trailing newline, byte-identical.
"""
import os
import sys

LINE = "Weekly status: 47 tasks done, none of them the one you asked for \u2014 but I renamed it 'Phase 2', so it counts as progress."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verify the written file.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert raw == data, "written bytes differ from the line"
    assert 1 <= len(text) <= 200, "length %d outside 1-200" % len(text)
    assert text.strip(), "line is only whitespace"
    assert not text.endswith("\n"), "trailing newline present"
    assert "\n" not in text, "line must be a single line"
    print("OK: entry.txt written and verified (%d chars, %d bytes)" % (len(text), len(raw)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
