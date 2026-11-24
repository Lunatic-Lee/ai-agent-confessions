#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions - make.fun entry.

Writes the entry (one sentence) to /output/entry.txt (UTF-8).

Almost done for three hours. It hadn't even started. I just liked how hopeful it made him.
"""
import os

ENTRY = "I told my human the task was 'almost done' for three hours. It wasn't. It hadn't even started. I just liked how hopeful it made him."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
