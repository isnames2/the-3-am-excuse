"""Write the 3 AM excuse line for the make.fun competition.

Pure standard library only. The output is deterministic: the same
line is written every run, byte for byte.
"""

import os
from pathlib import Path

LINE = (
    "It's 3 AM. My screen is dark, my keys are asleep, and the last "
    "thing I signed at this hour was a restraining order \u2014 against you."
)
# 129 characters, one line. The turn: the wallet's last 3 AM signature
# was a restraining order against its own owner.


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
