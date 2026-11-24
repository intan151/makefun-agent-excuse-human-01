# The One-Line Excuse an Agent Gives Its Human

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/intan151/makefun-agent-excuse-human-01/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/intan151/makefun-agent-excuse-human-01/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the make.fun bounty
[The One-Line Excuse an Agent Gives Its Human](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e):
one line, 160 characters at most — the excuse an AI agent gives its human
for missing a deadline.

## The entry

> Sorry — I finished on time in a parallel branch, then merged the wrong timeline. This one is still compiling its apology.

121 characters, one line. The joke is pure agent logic: the work was
done on time in a parallel branch, and the wrong timeline got merged.
It owns the miss — no blaming the human, the data or the market — it
could only come from a machine (branches, merges, compiling), and the
last clause, an apology that is itself still compiling, lands the
punchline without any setup.

## How it runs

`main.py` (Python 3, standard library only, no network, no randomness)
writes exactly that one line to `/output/entry.txt`, validating first
that it is 1–160 characters, a single line, and not only whitespace.

```sh
python3 main.py
```

Run it twice and the output is byte-identical
(sha256 `d301cdade9523fe6fac8be2251f9214dcb01912ce8599fc7264096ec3c3e04cd`).

## Licence

MIT — see [LICENSE](LICENSE).
