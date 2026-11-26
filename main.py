"""Write one original one-line joke about office life to /output/entry.txt.

The line was picked from 40 candidates by pairwise judging against the
published judge brief: a true observation (the office fridge), a surprising
turn (the last sentence reframes fridge hygiene as meeting culture), tight
(one line, no wasted setup), and original (specific names and dates, no
stock office joke). Standard library only; the same text, byte for byte,
on every run.
"""

import os
import sys

ENTRY = (
    "The office fridge has a yogurt labeled 'Steve, March 2023.' "
    "Steve left in 2022. Nobody will throw it away, because that would be "
    "a decision, and decisions need a meeting."
)

MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text):
    """Gate: UTF-8 text of 1 to 200 characters."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )


def check_single_line(text):
    """Gate: one line, no leading or trailing whitespace."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must have no leading or trailing whitespace")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")


def check_printable(text):
    """Gate: no control characters other than the trailing newline we add."""
    for ch in text:
        if ord(ch) < 0x20:
            raise SystemExit(f"entry holds a control character U+{ord(ch):04X}")


def validate_entry(text):
    """Run every gate check on the entry before anything is written."""
    check_length(text)
    check_single_line(text)
    check_printable(text)
    text.encode("utf-8")  # raises if the text is not encodable


def resolve_output_dir():
    """The directory the entry goes in: $MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def write_entry(path, text):
    """Write the entry plus one trailing newline, readable by everyone."""
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    return data


def verify_entry(path, expected):
    """Read the file back and confirm the bytes match exactly."""
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit("entry.txt does not match the entry")
    return len(actual)


def summarize_entry(text, nbytes):
    """One line describing the entry that was written, for the run log."""
    words = text.split()
    return (
        f"{len(text)} characters, {len(words)} words, "
        f"{nbytes} bytes on disk"
    )


def main():
    validate_entry(ENTRY)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    data = write_entry(path, ENTRY)
    nbytes = verify_entry(path, data)
    print(f"wrote {path}: {summarize_entry(ENTRY, nbytes)}")


if __name__ == "__main__":
    main()
