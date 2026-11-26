#!/usr/bin/env python3
"""One fortune cookie message for a software engineer.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network, fully deterministic.

v1 line: a bug the engineer thought was dead comes back with a
career. It reads like a fortune (a prediction about the reader's
day), it is specific to an engineer's world (a fixed bug
returning), and the laugh lands at the end: the bug did not just
come back, it got promoted above the person who killed it.

Revision (v2, final): made the bug the reader's own ("The bug",
not "A bug") and the time concrete ("six months ago" instead of
"months ago") — a fortune names a specific past, and the definite
article turns a generic bug into the one the reader personally
killed, which makes the promotion sting harder. Same ending,
same punch word.
"""

import os

LINE = "The bug you fixed six months ago returns today, older, wiser, and promoted above you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
