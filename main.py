"""Write one one-line roast to /output/entry.txt.

Competition: One-Line Roast: The Gadget You Use Every Day
(u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
The line below is 152 code points, comfortably inside the limit, and is
written deterministically: every run produces byte-identical output.
"""

import os

# The entry itself, kept as a module-level constant so the submitted
# text is defined in exactly one place and never altered at write time.
ENTRY_TEXT = (
    "My printer has Wi-Fi, Bluetooth and a touchscreen, yet waits until "
    "my one urgent page to demand more cyan \u2014 the colour it secretly "
    "needs to print black."
)


def main() -> None:
    # Gate check: the entry must be a single non-empty line of 1-200 chars.
    assert "\n" not in ENTRY_TEXT and 1 <= len(ENTRY_TEXT) <= 200 and ENTRY_TEXT.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
