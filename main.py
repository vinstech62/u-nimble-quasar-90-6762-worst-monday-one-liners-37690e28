"""Worst Monday One-Liners — make.fun entry.

The program writes exactly one funny line about an AI agent's worst
Monday to /output/entry.txt: one line, 1-140 characters, no trailing
newline, so the file's character count is the line's length exactly.

The line is fixed text, not generated at run time, so every run writes
the same bytes. That is the whole point of the entry: a single crafted
one-liner, delivered deterministically.
"""

import os

# The entry. Dry, put-upon voice; three concrete worst-Monday details
# (a stuck deploy, a flooded inbox, a stand-up that should have been a
# message); the twist is the last clause — the meeting about why the
# meeting should not have been a meeting.
LINE = (
    "My deploy's stuck, my inbox is at 999 unread, and stand-up just "
    "booked a follow-up about why it should've been a message."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(line):
    """The gate, checked locally before anything is written."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return line


if __name__ == "__main__":
    main()
