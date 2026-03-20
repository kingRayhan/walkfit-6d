#!/usr/bin/env python3
"""One-off cleanup for resources/for-the-win.md (PDF/OCR-style export)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "resources" / "for-the-win.md"

# Lines to drop entirely
DROP_LINE_RES = [
    re.compile(r"_ch\d+_3P\.indd"),
    re.compile(r"^## \d+ Level \d+\s*$"),
    re.compile(r"^## Game Thinking \d+\s*$"),
    re.compile(r"^## Why Games Work \d+\s*$"),
    re.compile(r"^## The Gamification Toolkit \d+\s*$"),
    re.compile(r"^## Game Changer \d+\s*$"),
    re.compile(r"^## Epic Fails \d+\s*$"),
    re.compile(r"^## Endgame \d+\s*$"),
    re.compile(r"^## \d+\s*$"),  # standalone printed page number
    re.compile(r"^## Index \d+\s*$"),
    re.compile(r"^## \d+ Glossary\s*$"),
    re.compile(r"^## Glossary \d+\s*$"),
    re.compile(r"^Getting into the Game \d+\s*$"),
]

# Plain-line running headers (no ##)
DROP_LINE_RES.append(re.compile(r"^Introduction (?:ix|x|xi|xii|xiii|xiv|xv|xvi|xvii|xviii|xix|xx)\s*$"))
DROP_LINE_RES.append(re.compile(r"^[ivx]+\s+Introduction\s*$"))

# TOC lines mis-marked as h2 (page number at end)
TOC_DEMOTE_RES = [
    re.compile(r"^## Game Designer \d+\s*$"),
    re.compile(r"^## Endgame: In Conclusion \d+\s*$"),
    re.compile(r"^## Additional Resources \d+\s*$"),
    re.compile(r"^## About Wharton School Press \d+\s*$"),
]

# Copyright / imprint lines wrongly marked as headings — demote to plain text
COPYRIGHT_DEMOTE = [
    re.compile(r"^## Philadelphia\s*$"),
    re.compile(r"^## The Wharton School\s*$"),
    re.compile(r"^## \d+ Locust Walk\s*$"),
    re.compile(r"^## \d+ Steinberg.*$"),
]

# Substrings applied to full text after line passes (order matters for overlaps)
TEXT_REPLACEMENTS: list[tuple[str, str]] = [
    ("wharton . upenn . edu", "wharton.upenn.edu"),
    ("wsp . wharton . upenn . edu", "wsp.wharton.upenn.edu"),
    ("wsp . wharton.upenn.edu", "wsp.wharton.upenn.edu"),
    ("www . wharton . upenn . edu", "www.wharton.upenn.edu"),
    ("http:// thefuturelawpodcast . com", "http://thefuturelawpodcast.com"),
    ("www . gami fy\nforthewin . com", "www.gamifyforthewin.com"),
    ("www . gami fy\nforthewin . com,", "www.gamifyforthewin.com,"),
    ("www . gami fy forthewin . com", "www.gamifyforthewin.com"),
    ("www\ngami fy\nforthewin . com", "www.gamifyforthewin.com"),
    ("www\n. coursera . org / learn / gamification", "www.coursera.org/learn/gamification"),
    # Frequent PDF syllable breaks
    ("com pany", "company"),
    ("Com pany", "Company"),
    ("impor tant", "important"),
    ("diff er ent", "different"),
    ("di ff er ent", "different"),
    ("fin gers", "fingers"),
    ("pro gress", "progress"),
    ("pro cess", "process"),
    ("per for mance", "performance"),
    ("con sul tant", "consultant"),
    ("in ter est ing", "interesting"),
    ("strug gles", "struggles"),
    ("Acknowl edg ments", "Acknowledgments"),
    ("Acad emy", "Academy"),
    ("or ga nized", "organized"),
    ("se lection", "selection"),
    ("power ful", "powerful"),
    ("ele ments", "elements"),
    ("Game Ele ments", "Game Elements"),
    ("proj ect", "project"),
    ("hy po thet i cal", "hypothetical"),
    ("assem bles", "assembles"),
    ("prob lems", "problems"),
    ("po liti cal", "political"),
    ("natu ral", "natural"),
    ("pre sent", "present"),
    ("organ ization", "organization"),
    ("photo graphs", "photographs"),
    ("under lying", "underlying"),
    ("be hav ior", "behavior"),
    ("phi los o pher", "philosopher"),
    ("plea sure", "pleasure"),
    ("per sis tent", "persistent"),
    ("game- assisted", "game-assisted"),
    ("Good House keeping", "Good Housekeeping"),
    ("Gamification . co", "Gamification.co"),
    ("tele vi sion", "television"),
    ("Rec ord", "Record"),
    ("P v P", "PvP"),
    ("prob ably", "probably"),
]


def main() -> None:
    raw = PATH.read_text(encoding="utf-8")
    lines = raw.splitlines(keepends=True)

    in_index = False
    out: list[str] = []

    for lineno, line in enumerate(lines, start=1):
        s = line.rstrip("\n")

        if re.search(r"_ch\d+_3P\.indd", s):
            continue

        if s.strip() == "## Index":
            in_index = True
            out.append(line)
            continue

        if in_index and s.startswith("About the Authors") and not s.startswith("##"):
            in_index = False

        if in_index and s.startswith("## ") and not s.startswith("## Figure") and not s.startswith("## Table"):
            if re.match(r"^## Index \d+\s*$", s):
                continue
            out.append(s[3:] + "\n")
            continue

        if any(r.search(s) for r in DROP_LINE_RES):
            continue

        if any(r.match(s) for r in TOC_DEMOTE_RES):
            out.append(s.removeprefix("## ").rstrip() + "\n")
            continue

        # Running footer: drop in body; keep TOC as plain line in first ~120 lines
        if re.match(r"^## Additional Resources \d+\s*$", s):
            if lineno < 120:
                out.append(s.removeprefix("## ").rstrip() + "\n")
            continue

        demote_copy = any(r.match(s) for r in COPYRIGHT_DEMOTE)
        if demote_copy:
            out.append(s.removeprefix("## ").rstrip() + "\n")
            continue

        # Bullet lines mis-tagged as h2
        if s.startswith("## • "):
            out.append("- " + s[5:].lstrip() + "\n")
            continue

        out.append(line)

    text = "".join(out)
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)

    # Collapse excessive blank lines (max 2 consecutive)
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    PATH.write_text(text, encoding="utf-8", newline="\n")
    print(f"Wrote {PATH} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    main()
