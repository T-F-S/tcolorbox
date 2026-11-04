#!/usr/bin/env python3
"""Check rendered marker colors, including within split paragraphs.

Requires pdfplumber. From the repository root, for example:
  TEXINPUTS="$PWD/tex/latex/tcolorbox//:" xelatex -output-directory=/tmp \
    -interaction=nonstopmode -halt-on-error tests/breakable-color-stack.tex
  python3 tests/check-breakable-colors.py /tmp/breakable-color-stack.pdf

The same fixture runs with pdflatex, lualatex, or lualatex with
  '\\def\\WithLuaColor{1}\\input{tests/breakable-color-stack.tex}'.
Use --expect-loss with an unpatched XeLaTeX PDF to check reproduction.
"""
import argparse
import re
from collections import Counter

import pdfplumber

EXPECTED = {
    "BLUE": (0, 0, 1), "RED": (1, 0, 0), "GREEN": (0, 1, 0),
    "BLACK": (0,), "GRAY": (0.5,), "CYAN": (1, 0, 0, 0),
    "YELLOW": (1, 1, 0),
}
PATTERN = re.compile("|".join(EXPECTED))


def same_color(actual, expected):
    if actual == (0, 0, 0) and expected == (0,):
        return True
    return len(actual) == len(expected) and all(
        abs(a - e) < 0.0001 for a, e in zip(actual, expected)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf")
    parser.add_argument("--expect-loss", action="store_true")
    args = parser.parse_args()
    counts = Counter()
    failures = []
    with pdfplumber.open(args.pdf) as pdf:
        if len(pdf.pages) < 3:
            raise SystemExit("Fixture did not exercise repeated page breaks")
        for page_number, page in enumerate(pdf.pages, 1):
            # Use character order, not word extraction: adjacent words can be
            # merged by PDF extraction, especially in justified box text.
            chars = page.chars
            text = "".join(char["text"] for char in chars)
            # All fixture markers are ASCII, so string and char offsets agree.
            assert all(len(char["text"]) == 1 for char in chars)
            for match in PATTERN.finditer(text):
                marker = match.group()
                counts[marker] += 1
                colors = [tuple(char["non_stroking_color"])
                          for char in chars[match.start():match.end()]]
                if any(not same_color(color, EXPECTED[marker]) for color in colors):
                    failures.append((page_number, marker, colors))
    if sum(counts.values()) < 1500 or set(counts) != set(EXPECTED):
        raise SystemExit(f"Incomplete fixture: {dict(counts)}")
    print(f"Checked {sum(counts.values())} markers: {dict(counts)}")
    print(f"Wrong colors: {len(failures)}")
    if args.expect_loss:
        if not failures:
            raise SystemExit("Expected the unpatched XeLaTeX failure")
    elif failures:
        for failure in failures[:10]:
            print(failure)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
