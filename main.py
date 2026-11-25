"""Funniest One-Line Out-of-Office Reply - entry program.

Writes a single out-of-office email auto-reply, one line long, to
/output/entry.txt.
The line: I'm away until Monday. My goldfish is now in charge of my inbox
and has already eaten two deadlines.
"""

import os

LINE = ("I'm away until Monday. My goldfish is now in charge of my inbox "
        "and has already eaten two deadlines.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 160:
        raise ValueError("entry must be 1-160 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
