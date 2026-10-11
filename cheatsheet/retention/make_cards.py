"""
Build the flashcard deck from verified problem records.

  python3 make_cards.py <records_dir>

<records_dir> holds one folder per problem with record.final.json (or record.verified.json).
Writes, next to this script:
  cards.json        cards for review.py
  anki_cards.csv    Anki import file (Front, Back, Tags; fields contain HTML)
Only NeetCode 150 and Blind 75 problems become cards.
"""
import csv
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP_CATEGORIES = {"Practice set", "Practice list extra"}


def load(folder):
    for name in ("record.final.json", "record.verified.json"):
        path = os.path.join(folder, name)
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
    return None


def slug_from_title(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def build(records_dir):
    cards = []
    for d in sorted(os.listdir(records_dir)):
        r = load(os.path.join(records_dir, d))
        if not r or r.get("category") in SKIP_CATEGORIES or not r.get("lc"):
            continue
        category = r["category"]
        if category.startswith("Blind 75 extra"):
            category = "Blind 75 extra"
        constraints = r.get("constraints", [])[:4]
        ladder = [f'{a["name"]}: {a["time"]} time, {a["space"]} space' + ("" if a.get("fits_constraints") else " (too slow)")
                  for a in r.get("approaches", [])]
        cards.append({
            "id": f'LC{r["lc"]}',
            "title": r["title"],
            "lc": r["lc"],
            "category": category,
            "difficulty": r.get("difficulty", ""),
            "statement": r.get("statement", ""),
            "constraints": constraints,
            "follow_up": r.get("follow_up", ""),
            "signals": r.get("recognition_signals", [])[:4],
            "techniques": r.get("techniques", []),
            "memory_hook": r.get("memory_hook", ""),
            "approach": r.get("intuitive_approach", ""),
            "rebuild_steps": r.get("rebuild_steps", []),
            "key_insight": r.get("key_insight", ""),
            "optimal_note": r.get("optimal_note", ""),
            "ladder": ladder,
            "pitfalls": r.get("pitfalls", [])[:3],
            "solution": r.get("intuitive_solution_code") or r.get("solution_code", ""),
        })
    cards.sort(key=lambda c: c["lc"])
    return cards


def esc(text):
    return html.escape(text).replace("\n", "<br>")


def anki_rows(cards):
    for c in cards:
        front = (f"<b>{esc(c['title'])}</b> ({esc(c['category'])}, {esc(c['difficulty'])})<br><br>"
                 f"{esc(c['statement'])}<br><br><i>Constraints:</i><br>" + "<br>".join(esc(x) for x in c["constraints"]) +
                 (f"<br><i>Follow-up:</i> {esc(c['follow_up'])}" if c["follow_up"] else "") +
                 "<br><br><b>Name the technique and the memory hook. Then rebuild the solution.</b>")
        back = (f"<b>Hook:</b> {esc(c['memory_hook'])}<br><b>Techniques:</b> {esc(', '.join(c['techniques']))}<br><br>"
                f"<b>Approach:</b> {esc(c['approach'])}<br><br><b>Rebuild:</b><ol>" +
                "".join(f"<li>{esc(s)}</li>" for s in c["rebuild_steps"]) + "</ol>"
                f"<b>Signals:</b><ul>" + "".join(f"<li>{esc(s)}</li>" for s in c["signals"]) + "</ul>"
                f"<b>Key insight:</b> {esc(c['key_insight'])}<br>" +
                (f"<b>Optimal:</b> {esc(c['optimal_note'])}<br>" if c["optimal_note"] else "") +
                "<b>Approaches:</b><ul>" + "".join(f"<li>{esc(s)}</li>" for s in c["ladder"]) + "</ul>"
                f"<pre>{esc(c['solution'])}</pre>")
        tags = " ".join([slug_from_title(c["category"])] + [t.replace(" ", "-") for t in c["techniques"]])
        yield front, back, tags


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cards = build(sys.argv[1])
    with open(os.path.join(HERE, "cards.json"), "w") as f:
        json.dump(cards, f, indent=1)
    with open(os.path.join(HERE, "anki_cards.csv"), "w", newline="") as f:
        w = csv.writer(f)
        for row in anki_rows(cards):
            w.writerow(row)
    print(f"{len(cards)} cards -> cards.json, anki_cards.csv")


if __name__ == "__main__":
    main()
