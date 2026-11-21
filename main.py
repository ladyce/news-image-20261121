#!/usr/bin/env python3
"""Entry program for news-image-20261121 (Saturday 21 November 2026).

The finished front page lives in this repository as entry.png
(1024x1024 PNG). Running this file copies those exact bytes to
entry.png inside the output directory (/output in the grader,
MAKEFUN_OUTPUT_DIR locally). Standard library only, no network,
so every run produces the same output.
"""

import os
import shutil
import sys


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(repo_dir, "entry.png")
    if not os.path.exists(image_path):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target_path = os.path.join(output_dir, "entry.png")
    shutil.copyfile(image_path, target_path)
    # Sanity check: the copy must be byte-identical in size to the source,
    # which keeps the two grader runs deterministic by construction.
    if os.path.getsize(target_path) != os.path.getsize(image_path):
        print("copied image size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
