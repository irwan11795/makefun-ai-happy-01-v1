#!/usr/bin/env python3
"""Copy entry.png to the make.fun output directory, byte for byte.

Deterministic, standard library only, no network access.
"""
import os
import shutil
from pathlib import Path

# The image lives next to this script, so the copy works from any cwd.
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# make.fun sets MAKEFUN_OUTPUT_DIR; fall back to /output/entry.png.
# Byte-verified below, so a partial or corrupted copy can never pass silently.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    assert DEST.read_bytes() == SOURCE.read_bytes(), "byte verification failed: output differs from entry.png"
    print(f"Copied {SOURCE} -> {DEST} ({DEST.stat().st_size} bytes, byte-verified)")


if __name__ == "__main__":
    main()
