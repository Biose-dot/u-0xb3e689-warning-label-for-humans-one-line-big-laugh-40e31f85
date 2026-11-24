#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

A label that reads like a real safety warning, with the laugh landing in the last clause: the danger is not the human, it is asking twice.
"""
import os

ENTRY = 'WARNING: This human runs on caffeine, spite, and four hours of sleep. Do not shake, do not update before coffee, and never ask twice if they are okay.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
