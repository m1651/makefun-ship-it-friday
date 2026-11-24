#!/usr/bin/env python3
"""Ship It Friday entry.

Writes one line - the funniest git commit message an AI coding agent
writes right before breaking production on a Friday - to
/output/entry.txt. Stdlib only, deterministic.
"""

import os
import sys

ENTRY = "feat: Friday deploy \u2014 all tests pass, and I wrote all the tests, so this is definitely fine"

MAX_CHARS = 159


def main() -> int:
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip verification: what landed on disk must match exactly.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        on_disk = f.read()
    if on_disk != ENTRY:
        print("error: /output/entry.txt does not match the entry", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
