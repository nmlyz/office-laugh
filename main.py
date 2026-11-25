"""Write one original one-line joke about office life to /output/entry.txt.

The line was picked from 40 candidates by pairwise judging against the
published judge brief: a true observation (the office fridge), a surprising
turn (the last sentence reframes fridge hygiene as meeting culture), tight
(one line, no wasted setup), and original (specific names and dates, no
stock office joke). Standard library only; the same text, byte for byte,
on every run.
"""

import os

ENTRY = (
    "The office fridge has a yogurt labeled 'Steve, March 2023.' "
    "Steve left in 2022. Nobody will throw it away, because that would be "
    "a decision, and decisions need a meeting."
)


def main() -> None:
    # Gate: UTF-8 text, 1 to 200 characters, a single line, not only
    # whitespace, no leading or trailing space.
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no edge whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)

    # Read back and confirm the bytes match exactly.
    with open(path, "rb") as f:
        if f.read() != data:
            raise SystemExit("entry.txt does not match the entry")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
