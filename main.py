#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt: "ryk07" — no trailing newline, no explanation,
no links, no pitch. Exactly what the bounty asks for.
"""

from pathlib import Path

WORD = "ryk07"


def main() -> None:
    # Guard the gate before writing: one word, 1 to 30 characters,
    # no whitespace at all — the sealed scorer's exact requirement.
    assert 1 <= len(WORD) <= 30, "username must be 1-30 characters"
    assert WORD.split() == [WORD], "username must be a single word"
    # The harness fixes the output location: /output/entry.txt.
    # Resolve nothing from the working directory.
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one word: the file is the username itself.
    out_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
