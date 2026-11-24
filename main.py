#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes one funny single-line out-of-office auto-reply to /output/entry.txt
and prints the same line. Standard library only, fully deterministic.
"""

import os
import sys

ENTRY_LINE = (
    "Out until Monday. My inbox is being handled by my houseplant, "
    "which got promoted yesterday and has already missed two deadlines."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate the line the same way the competition gate does."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= 140):
        raise ValueError(
            f"entry must be 1-140 characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    lowered = line.lower()
    if "http://" in lowered or "https://" in lowered or "www." in lowered:
        raise ValueError("entry must not contain a link")
    line.encode("utf-8")  # raises UnicodeEncodeError on invalid text


def main() -> int:
    try:
        validate(ENTRY_LINE)
    except (ValueError, UnicodeEncodeError) as exc:
        print(f"error: invalid entry line: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE + "\n")

    print(ENTRY_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
