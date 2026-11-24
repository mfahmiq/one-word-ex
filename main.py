"""One Word From Your Ex — make.fun text bounty entry.

Writes exactly one word — the word an ex would use to describe the
entrant — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-24 characters, exactly one word with no spaces, not
whitespace-only. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = "overthinker"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-24 chars, exactly one word, not
    # whitespace-only. The gate counts the word itself (11 chars);
    # the trailing newline in the file is formatting, not content.
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"FAIL: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    if not 1 <= len(ENTRY) <= 24:
        print(f"FAIL: entry is {len(ENTRY)} chars, must be 1-24", file=sys.stderr)
        return 1

    if not ENTRY.strip():
        print("FAIL: entry must not be whitespace-only", file=sys.stderr)
        return 1

    if len(ENTRY.split()) != 1:
        print("FAIL: entry must be exactly one word", file=sys.stderr)
        return 1

    if any(ch.isspace() for ch in ENTRY):
        print("FAIL: entry must contain no whitespace", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Re-read and confirm the written file matches exactly.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        print("FAIL: written file does not match the entry", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
