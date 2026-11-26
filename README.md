# office-laugh

[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/nmlyz/office-laugh/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/nmlyz/office-laugh/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

office-laugh writes one line to a text file: an original joke about office life, built on a true observation and closed on its strongest beat. The line was picked from 40 candidates by pairwise judging against the brief — the office fridge, a yogurt labelled with a name and a date, and a last sentence that turns fridge hygiene into meeting culture. The joke is 170 characters, a single line, and reads cleanly aloud in one breath.

## How the line was chosen

Forty one-liners were written first, then cut down in rounds: stock premises (the printer that only jams on urgent documents, the pizza-party raise, the "we're a family" speech) went out, then puns and lines whose turn was only a nod. The survivors were judged head to head, two at a time, on the brief's own order — on subject, true to the office, surprising turn, tight, original — until one remained. The winner's turn is the last sentence: nobody throws the yogurt away, because throwing it away would be a decision, and decisions need a meeting.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run.

## How it works

The program holds the line as one constant and runs it through a gate before writing anything: length within 1–200 characters, a single line with no leading or trailing whitespace, no control characters, and encodable as UTF-8. It then writes the line plus one trailing newline, sets the file readable by everyone, reads it back, and only reports success when the bytes on disk match exactly.

## Verification

Run the program twice into a scratch directory and compare the outputs — they must be byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt
```

The entry itself is 170 characters, one line, plain UTF-8, with no leading or trailing space — inside the 1–200 character gate the judge's scorer checks.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)</sub>
