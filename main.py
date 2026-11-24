#!/usr/bin/env python3
"""Draft entry writer for the human warning-label bounty (v1)."""

import os

ENTRY = "WARNING: This human runs on coffee, Wi-Fi, and pure spite. Do not shake, do not reboot mid-sentence, and never ask 'are we there yet' before breakfast."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
