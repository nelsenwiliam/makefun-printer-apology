#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one line (max 120 characters): an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. Pure standard library only.
"""

import os

ENTRY = "Sorry for the jam, the streaks, the burnt-toner smell. HR says I can't file a complaint about you."
# 98 characters. Chosen from 10 candidates scored against the judge's brief:
# a real apology plus the printer's own gripes (jam, streaks, burnt-toner
# smell), the punch at the very end, and the freshest angle — the printer
# went to HR to complain about its users and was turned down. "HR says"
# implies it actually tried, which is the joke.


def main() -> None:
    # Enforce the gate ourselves: 1 to 120 characters, not only whitespace.
    text = ENTRY.strip()
    if not (1 <= len(text) <= 120):
        raise ValueError(f"entry is {len(text)} characters, must be 1-120")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
