# office-laugh

[![make.fun · u-alfasurya91-make-the-ai-judge-laugh-6ed40225](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/nmlyz/office-laugh/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/nmlyz/office-laugh/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

office-laugh writes one line to a text file: an original joke about office life, built on a true observation and closed on its strongest beat. The line was picked from 56 candidates by pairwise judging against the brief — a calendar block called "Focus Time", booked over by a meeting named after the very thing it destroys. The joke is 115 characters, a single line, and reads cleanly aloud in one breath.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The program holds the line as one constant and checks it against the entry gate (length, single line, no leading or trailing space) before writing it, then reads the file back to confirm the bytes match.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)</sub>
