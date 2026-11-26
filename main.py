"""One-Liner Laughs entry: write one funny single-line joke to /output/entry.txt.

Deterministic: the joke is a fixed string. No randomness, no clock, no
network, no input other than this file, so two runs write identical bytes.
Python 3.13, standard library only.

Draft: "I asked my smart fridge to stop judging my midnight snacks, so now
it just sighs and opens the salad drawer instead."
Revision (final): tightened the setup, cut the sigh/salad detour, and landed
the twist on "we both eat in the dark" — the fridge is dark too.
"""

import os

JOKE = "My smart fridge kept judging my midnight snacks, so I unplugged it. Now we both eat in the dark."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(JOKE)}")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
