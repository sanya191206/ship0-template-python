import argparse, sys
from .storage import add_entry, load_entries, clear_entries
from .stats import mean_length

def main(argv=None):
    parser = argparse.ArgumentParser(prog="ship0", description="Edge Labs — Ship Log (Python)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="add a new entry")
    p_add.add_argument("text", nargs="+", help="entry text")

    sub.add_parser("list", help="list entries (newest first)")

    p_clear = sub.add_parser("clear", help="clear the log")
    p_clear.add_argument("-y", "--yes", action="store_true", help="do not prompt")

    sub.add_parser("stats", help="show count and mean entry length")

    ns = parser.parse_args(argv)

    if ns.cmd == "add":
        text = " ".join(ns.text).strip()
        if not text:
            print("Nothing to add.", file=sys.stderr)
            return 2
        add_entry(text)
        print("OK: added")
        return 0

    if ns.cmd == "list":
        entries = load_entries()
        if not entries:
            print("(no entries yet)")
            return 0
        for e in entries:
            print(f"{e['t']} — {e['v']}")
        return 0

    if ns.cmd == "clear":
        if not ns.yes:
            ans = input("This will erase all entries. Continue? [y/N] ").strip().lower()
            if ans not in ("y", "yes"):
                print("Aborted.")
                return 1
        clear_entries()
        print("Cleared.")
        return 0

    if ns.cmd == "stats":
        entries = load_entries()
        n = len(entries)
        avg = mean_length([e["v"] for e in entries]) if entries else 0.0
        print(n)
        print(f"{avg:.2f}")
        print(f"Count: {n} | Mean length: {avg:.2f} chars")
        return 0

    parser.print_help()
    return 2

if __name__ == "__main__":
    sys.exit(main())
