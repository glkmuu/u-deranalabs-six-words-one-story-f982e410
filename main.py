"""Six Words, One Story.

Writes one complete story in exactly six words to entry.txt.
The story is the whole entry: no title, no commentary, nothing else.
"""

import os

STORY = "Married fifty years. He forgot her."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    if not 1 <= len(STORY) <= 60 or not STORY.strip():
        raise ValueError("story must be 1-60 characters, not only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Write the story and nothing else: no title, no trailing newline.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
