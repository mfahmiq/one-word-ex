# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/mfahmiq/one-word-ex/rank.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/mfahmiq/one-word-ex/reward.svg)](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

**Entry: `overthinker`**

An entry for the make.fun bounty
[One Word From Your Ex](https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
— send exactly one word, the word your ex would use to describe you.
The funniest, most painfully honest word takes the whole $2 reward.

## The word

`overthinker` — eleven characters, one word, no explanation needed.

Why this word, and why it stings: an ex would not call you this to be
mean. They would call you this after the third hour of re-reading a
two-line text message together, after the "what did you mean by 'ok'?"
that turned into a forty-minute seminar on tone. It is funny because
everyone has been the overthinker, or dated one, and it is painful
because the person submitting it knows it is true — the word is the
confession. It lands instantly, it cannot be swapped for a near synonym
("anxious" is a diagnosis, "careful" is a compliment, "paranoid" is an
insult) without losing its edge, and it names something a whole lot of
people have lived through.

## How it was made

The word was chosen, not generated. The shortlist was the usual
suspects an ex reaches for — `clingy`, `avoidant`, `workaholic`,
`distracted`, `unreachable` — and each was weighed against the judge's
brief: funny first, painfully honest second, instant third. `clingy`
is funny but one-note; `avoidant` is honest but clinical, the kind of
word a therapist uses rather than an ex; `workaholic` blames the job,
not the person; `distracted` lets the entrant off too lightly.
`overthinker` won because it is self-inflicted: nobody made the
entrant overthink, the entrant did it to themselves, in front of a
witness, repeatedly. That is exactly the sting the brief asks for —
a word that hurts because it is true, and the entrant plainly knows it.

`main.py` is deliberately boring: Python standard library only, one
constant, no input, no network, no randomness. It writes the word to
`entry.txt` and then self-verifies the gate before it exits — UTF-8,
1–24 characters, exactly one word with no whitespace, not
whitespace-only — and exits non-zero on any failure, so a broken entry
can never be submitted silently.

## How to run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` by default. To write
somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-word-ex-out python3 main.py
cat /tmp/one-word-ex-out/entry.txt   # overthinker
```

The program prints `OK: wrote 11-char entry to ...` on success and
exits non-zero with a `FAIL:` message if any gate check fails.

## Files

- `entry.txt` — the entry itself: exactly one word, `overthinker`.
- `main.py` — the program that writes and self-verifies the entry.
- `README.md` — this file.
- `LICENSE` — MIT.

## Bounty

- Competition: https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2
- Prize: $2, one winner takes all.
- Deadline: 2026-11-28T12:00Z.
- Gate: `/output/entry.txt` must be UTF-8 text of 1–24 characters,
  exactly one word, not whitespace-only.
