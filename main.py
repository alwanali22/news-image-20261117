#!/usr/bin/env python3
"""news-image-20261117 entry: copy the front-page image to the output dir.

The image is drawn at build time by draw_entry.py (Python PIL, kept in the
build workdir) and shipped in this repository as entry.png; this program
only copies it, so both graded runs write byte-identical output with no
network and no clock. v2 (18 Nov 2026): 27 stories, ALSO ON briefs,
numbered map dots, one pictogram per grid story.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a truncated copy: the gate rejects a partial image.
    # v2 entry.png: 1024x1024, 146802 bytes, sha256 0e3acea6…
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
