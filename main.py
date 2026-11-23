#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes the chosen roast to /output/entry.txt (UTF-8, one line, 63 chars).
"""

import os

ROAST = "My agent thinks it's JARVIS. It's Clippy with a GitHub account."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
