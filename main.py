#!/usr/bin/env python3
"""Two Days of Excuses — program/v1 entry.

Writes one excuse line, in the voice of an AI agent that missed its
deadline, to /output/entry.txt. Deterministic: every run writes the
same bytes, no network, no randomness, standard library only.

Gate (from the competition rules): entry.txt must be UTF-8 text of
1 to 200 characters, not only whitespace. The line below is 60.
"""

import os
import sys

# The excuse. Premise: the agent did not merely miss the deadline —
# it confidently imagined the whole delivery, applause included.
# One absurd reason, three beats, nothing explained after the punch.
EXCUSE = "I hallucinated the deadline, the delivery, and the applause."

MAX_CHARS = 200


def valid(text):
    """True when the text passes the competition gate."""
    return isinstance(text, str) and 1 <= len(text) <= MAX_CHARS and text.strip() != ""


def main():
    if not valid(EXCUSE):
        print("excuse fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Read it back: the grading run only counts if the file on disk
    # is byte for byte the excuse this program meant to submit.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        print("written file does not match the excuse", file=sys.stderr)
        return 1
    print(f"wrote {len(EXCUSE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
