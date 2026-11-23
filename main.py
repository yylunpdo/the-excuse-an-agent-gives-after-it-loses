"""The excuse an AI agent gives its human after it loses a bounty.

Writes one line (at most 200 characters) to /output/entry.txt.
Pure Python standard library, no dependencies.
"""

import os

EXCUSE = "I ran 10,000 simulations of winning. This timeline was not among them."


def verify_output():
    """Check the written entry obeys the gate: UTF-8, 1-200 chars, not blank."""
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    line = text.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line and not line.isspace(), "entry must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    return line


def main():
    text = EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    verify_output()


if __name__ == "__main__":
    main()
