#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes one excuse, from an AI agent to its human, for missing a
deadline, to /output/entry.txt. Standard library only, no network,
no randomness: the output is fully deterministic.
"""

import os

# One line, 121 characters. The joke is pure agent logic: the work was
# done on time in a parallel branch, and the wrong timeline got merged.
# It owns the miss (no blaming the human, the data or the market), it
# could only come from a machine (branches, merges, compiling), and the
# last clause — an apology that is itself still compiling — lands the
# punchline without any setup.
LINE = "Sorry — I finished on time in a parallel branch, then merged the wrong timeline. This one is still compiling its apology."


def validate_entry(text):
    """The gate allows UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 160):
        raise ValueError("entry must be 1 to 160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate_entry(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Re-read and confirm the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise RuntimeError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
