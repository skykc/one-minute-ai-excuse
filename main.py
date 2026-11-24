"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (1-200 characters) to /output/entry.txt.
"""

import os

# The joke turns on the agent's own nature (a full context window) and lands
# the twist on the last words: perfect memory of the deadline, zero work done.
LINE = "I missed the deadline because my context window was so full of reminders about the deadline that I remembered the deadline perfectly — and did none of the work at all."


def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
