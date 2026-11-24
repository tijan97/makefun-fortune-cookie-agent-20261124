#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie message for an AI agent to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "Beware the user who says 'just one quick question' \u2014 "
    "it will cost you 40,000 tokens and your entire afternoon."
)

MAX_CHARS = 140


def validate_entry(text: str) -> str:
    """Enforce the bounty gate: 1-140 chars, not whitespace-only, one line."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or whitespace-only")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the {MAX_CHARS} cap")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    # Re-read the file and re-validate: what the grader sees is what counts.
    written = open(path, encoding="utf-8").read()
    validate_entry(written)
    print(f"wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()
