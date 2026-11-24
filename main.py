#!/usr/bin/env python3
"""Two Days of Excuses — one-line AI excuse for a missed deadline.

Writes the entry to /output/entry.txt (no trailing newline, so the file
is exactly one line of 1-200 characters). Python 3.13 stdlib only,
no network, no randomness: the output is deterministic.
"""

import os
import sys

ENTRY = "I was 99.9% sure I'd meet the deadline. Unfortunately, this timeline was the 0.1%."


def main() -> int:
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
