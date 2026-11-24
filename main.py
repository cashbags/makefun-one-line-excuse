#!/usr/bin/env python3
"""One-line excuse entry for make.fun.

The competition asks for a single line: the excuse an AI agent hands its
human after missing a deadline. The judge reads entries two at a time and
picks the funnier, fresher one, checking first that the line really is an
agent's excuse, then that it is funny, fresh, agent-voiced and tight.

Why this line won our own ten-candidate tournament: the joke is built from
a failure mode only an agent can have. A person cannot hallucinate a
software library into existence, install the hallucination, and then burn
a deadline debugging it. The line escalates in three beats -- hallucinate,
install, debug -- so the punchline ("a library that never existed") lands
on a scene the reader has already watched unfold, instead of leaning on a
generic apology or a reheated human excuse in robot drag. It is first
person, it names one concrete agent situation, and it never explains the
joke. At 105 characters it sits inside the 1-160 gate with room to spare.

The program itself is deliberately boring: one constant, one write, one
guard. Determinism is the whole point -- the sealed scorer replays the
program and the output must be byte-identical every time, so there is no
randomness, no clock, no network, and no input to vary.
"""

import sys
from pathlib import Path

# The chosen line (105 characters, ASCII, single line, no trailing space).
LINE = "I hallucinated a dependency, installed it, and spent the deadline debugging a library that never existed."

# The competition's gate: /output/entry.txt must hold 1-160 characters.
MAX_CHARS = 160


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(f"entry line is {len(LINE)} chars, outside the 1-160 gate")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
