"""Convert UNIX timestamp to a readable date."""

import argparse
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("timestamp", type=float)
    args = parser.parse_args()

    dt = datetime.fromtimestamp(args.timestamp)
    print(dt.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()