#!/usr/bin/env python3

import argparse
import time


def timer(minutes, label):
    seconds = minutes * 60

    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            print(f"\r{label}: {mins:02}:{secs:02}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
    except KeyboardInterrupt:
        print("\ncancelled")
        raise SystemExit(0)

    print(f"\r{label}: 00:00")
    print("\a", end="", flush=True)


def main():
    parser = argparse.ArgumentParser(description="A minimal Pomodoro timer")
    parser.add_argument(
        "minutes",
        type=int,
        nargs="?",
        default=25,
        help="work duration in minutes (default: 25)",
    )
    parser.add_argument(
        "-b",
        "--break",
        dest="break_minutes",
        type=int,
        default=5,
        help="break duration in minutes (default: 5)",
    )

    args = parser.parse_args()

    while True:
        timer(args.minutes, "work")
        input("press enter for break...")
        timer(args.break_minutes, "break")
        input("press enter to work...")


if __name__ == "__main__":
    main()
