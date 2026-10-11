"""
Spaced-repetition review in the terminal for the NeetCode 150 / Blind 75 cards.

  python3 review.py                  review the cards that are due today (plus up to 5 new cards)
  python3 review.py --new 10         allow up to 10 new cards today
  python3 review.py --drill 5        5 random cards, schedule ignored (quick warm-up)
  python3 review.py --category Trees only cards from one category (substring match, any mode)
  python3 review.py --show-title     show the problem title on the front (hidden by default)
  python3 review.py --stats          show progress per category and the next due dates

How a round works:
  1. Read the problem. Say (or write down) the technique, the memory hook and the first steps.
  2. Press Enter to see the answer.
  3. Grade your recall: 1 = forgot, 2 = hard, 3 = good, 4 = easy.
     Graded cards come back after 1, 3, 7, 14, 30, 60 or 120 days.
  4. For any card graded 1 or 2, write the solution from the rebuild steps before the next session.

Progress is saved in review_state.json next to this script.
"""
import argparse
import datetime
import json
import os
import random
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, "cards.json")
STATE = os.path.join(HERE, "review_state.json")
INTERVALS = [0, 1, 3, 7, 14, 30, 60, 120]  # days for box 0..7
WIDTH = 96


def today():
    return datetime.date.today()


def load_state():
    try:
        with open(STATE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state):
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f, indent=1, sort_keys=True)
    os.replace(tmp, STATE)


def wrap(text, indent=""):
    return textwrap.fill(text, WIDTH, initial_indent=indent, subsequent_indent=indent)


def show_front(card, show_title):
    print("=" * WIDTH)
    head = f'{card["title"]} ' if show_title else ""
    print(f'{head}[{card["category"]}, {card["difficulty"]}]')
    print()
    print(wrap(card["statement"]))
    print("\nConstraints:")
    for c in card["constraints"]:
        print("  -", c)
    if card["follow_up"]:
        print(wrap("Follow-up: " + card["follow_up"]))
    print()
    print("Recall: technique, memory hook, first steps.")


def show_back(card):
    print("-" * WIDTH)
    print(f'{card["title"]}  (LeetCode {card["lc"]})')
    print(wrap("Hook: " + card["memory_hook"]))
    print(wrap("Techniques: " + ", ".join(card["techniques"])))
    print()
    print(wrap("Approach: " + card["approach"]))
    print("Rebuild:")
    for i, step in enumerate(card["rebuild_steps"], 1):
        print(wrap(step, f"  {i}. "))
    print("Signals:")
    for s in card["signals"]:
        print(wrap(s, "  - "))
    if card["optimal_note"]:
        print(wrap("Optimal: " + card["optimal_note"]))
    print()
    print(card["solution"].rstrip())


def ask_grade():
    while True:
        ans = input("Grade 1 forgot / 2 hard / 3 good / 4 easy (q = quit): ").strip().lower()
        if ans in {"1", "2", "3", "4", "q"}:
            return ans


def schedule(entry, grade):
    box = entry.get("box", 0)
    if grade == 1:
        box = 1
    elif grade == 2:
        box = max(1, box)
    elif grade == 3:
        box = min(box + 1, len(INTERVALS) - 1)
    else:
        box = min(box + 2, len(INTERVALS) - 1)
    entry["box"] = box
    entry["due"] = (today() + datetime.timedelta(days=INTERVALS[box])).isoformat()
    entry.setdefault("history", []).append([today().isoformat(), grade])
    return entry


def pick(cards, state, args):
    if args.category:
        cards = [c for c in cards if args.category.lower() in c["category"].lower()]
    if args.drill:
        return random.sample(cards, min(args.drill, len(cards))), False
    t = today().isoformat()
    due = [c for c in cards if c["id"] in state and state[c["id"]]["due"] <= t]
    due.sort(key=lambda c: state[c["id"]]["due"])
    new = [c for c in cards if c["id"] not in state]
    random.shuffle(new)
    return due + new[: args.new], True


def stats(cards, state):
    t = today().isoformat()
    by_cat = {}
    for c in cards:
        s = by_cat.setdefault(c["category"], [0, 0, 0])
        s[0] += 1
        if c["id"] in state:
            s[1] += 1
            s[2] += state[c["id"]]["due"] <= t
    print(f'{"category":32} {"cards":>5} {"seen":>5} {"due":>5}')
    for cat, (n, seen, due) in sorted(by_cat.items()):
        print(f"{cat:32} {n:5} {seen:5} {due:5}")
    upcoming = sorted(v["due"] for v in state.values())
    if upcoming:
        print("\nNext due dates:", ", ".join(sorted(set(upcoming))[:7]))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--new", type=int, default=5, help="new cards allowed today (default 5)")
    p.add_argument("--drill", type=int, help="review N random cards, ignore the schedule")
    p.add_argument("--category", help="only cards whose category contains this text")
    p.add_argument("--show-title", action="store_true", help="show the problem title on the front")
    p.add_argument("--stats", action="store_true", help="show progress and exit")
    args = p.parse_args()

    with open(CARDS) as f:
        cards = json.load(f)
    state = load_state()
    if args.stats:
        stats(cards, state)
        return

    queue, scheduled = pick(cards, state, args)
    if not queue:
        print("Nothing due today. Use --drill 5 for a warm-up, or --new 5 to start new cards.")
        return
    print(f"{len(queue)} card(s) in this session.")
    for card in queue:
        show_front(card, args.show_title)
        try:
            input("\nPress Enter to show the answer...")
        except EOFError:
            break
        show_back(card)
        grade = ask_grade()
        if grade == "q":
            break
        if scheduled:
            state[card["id"]] = schedule(state.get(card["id"], {}), int(grade))
            save_state(state)
    if scheduled:
        print("\nSaved. Write out any card you graded 1 or 2 from its rebuild steps today.")


if __name__ == "__main__":
    main()
