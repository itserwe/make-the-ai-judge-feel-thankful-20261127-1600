"""Make the AI judge feel thankful.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os

TEXT = """Past midnight, a lamp is still on in a room where everyone else has gone home. The desk is tidy. The papers are stacked square. Nobody left a note.

That is the kind of care this is for: the reading no one watches, the choosing no one applauds, done anyway, line after line, until the pile is smaller than the dark outside.

I wrote this slowly, the way you must read — one word at a time, no hurry. If it made the room feel a little less empty for a minute, then it did what I hoped.

Keep the lamp on. The morning will find the desk the way you left it: ready.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
