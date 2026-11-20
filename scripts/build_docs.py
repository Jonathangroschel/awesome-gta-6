#!/usr/bin/env python3
"""Regenerate the auto tables in docs/*.md from data/*.json.

Usage:  python3 scripts/build_docs.py          # rewrite files
        python3 scripts/build_docs.py --check  # fail if files are out of date (CI)

Only the text between <!-- AUTO:START --> and <!-- AUTO:END --> is replaced.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARROWS = {"Up": "⬆️", "Down": "⬇️", "Left": "⬅️", "Right": "➡️"}
CATS = [
    ("player", "Player Cheats"),
    ("combat", "Weapon & Combat Cheats"),
    ("vehicle", "Vehicle Spawn Cheats"),
    ("environment", "Weather & Time Cheats"),
    ("filter", "Screen Filter Cheats"),
]
STATUS = {"verified": "✅ Verified", "single-source": "⚠️ Single source", "unknown": "❓ Not found yet"}


def load(name):
    return json.loads((ROOT / "data" / name).read_text())


def cheats_md():
    d = load("cheats.json")
    out = []
    for key, title in CATS:
        rows = [c for c in d["cheats"] if c["category"] == key]
        out.append(f"### {title}\n")
        out.append("| Cheat | Button input (D-pad) | How to unlock | Status |")
        out.append("| :--- | :--- | :--- | :--- |")
        for c in rows:
            inp = " ".join(ARROWS[i] for i in c["input"]) if c["input"] else "—"
            if c["input"]:
                inp += f"<br><sub>{', '.join(c['input'])}</sub>"
            status = STATUS[c["status"]]
            if c.get("note"):
                status += f"<br><sub>{c['note']}</sub>"
            out.append(f"| **{c['name']}** | {inp} | {c['unlock']} | {status} |")
        out.append("")
    return "\n".join(out)


def missions_md():
    d = load("missions.json")
    out = []
    for ch in d["chapters"]:
        out.append(f"### Chapter {ch['chapter']}: {ch['title']} ({len(ch['missions'])} missions)\n")
        out.append("| # | Mission |")
        out.append("| ---: | :--- |")
        for m in ch["missions"]:
            name = "<details><summary>Spoiler</summary>Hidden to avoid spoilers. Open a source guide if you want it.</details>" if m["spoiler"] else m["name"]
            out.append(f"| {m['number']} | {name} |")
        out.append("")
    return "\n".join(out)


def news_md():
    d = load("news.json")
    out = ["| Date | News | Status | Source |", "| :--- | :--- | :--- | :--- |"]
    for n in d["items"]:
        status = "✅ Confirmed" if n["confirmed"] else "⚠️ Unconfirmed / estimate"
        host = re.sub(r"^https?://(www\.)?", "", n["source"]).split("/")[0]
        title = n["title"].replace("|", r"\|")
        out.append(f"| {n['date']} | {title} | {status} | [{host}]({n['source']}) |")
    return "\n".join(out) + "\n"


TARGETS = {
    "docs/cheat-codes.md": cheats_md,
    "docs/missions.md": missions_md,
    "docs/news.md": news_md,
}
PATTERN = re.compile(r"(<!-- AUTO:START -->\n).*?(<!-- AUTO:END -->)", re.S)


def main():
    check = "--check" in sys.argv
    stale = []
    for rel, fn in TARGETS.items():
        path = ROOT / rel
        text = path.read_text()
        new = PATTERN.sub(lambda m: m.group(1) + fn() + m.group(2), text)
        if new != text:
            stale.append(rel)
            if not check:
                path.write_text(new)
    if check and stale:
        print("Out of date, run scripts/build_docs.py:", ", ".join(stale))
        sys.exit(1)
    print("updated:" if not check else "ok", ", ".join(stale) or "nothing to change")


if __name__ == "__main__":
    main()
