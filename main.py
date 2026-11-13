"""Copy the committed letter image to the output directory, byte for byte."""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / IMAGE_NAME)


if __name__ == "__main__":
    main()
