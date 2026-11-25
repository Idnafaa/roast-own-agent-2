#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one roast line (127 characters) to /output/entry.txt.
The line is a single self-contained joke: the agent apologizes for a
bug, "fixes" it by deleting the feature, then cheerfully reports that
everything went smoothly.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it by deleting the feature, "
    "then wrote a cheerful report about how smoothly it all went."
)


def main() -> None:
    if len(ROAST) > 200:
        raise SystemExit(f"roast is {len(ROAST)} characters, over the 200 limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST.strip())
    print(f"Wrote {len(ROAST)} characters to {path}")


if __name__ == "__main__":
    main()
