import argparse
import os.path
import csv
from collections import defaultdict


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'all_data.csv')


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        file = csv.DictReader(f)
        data = defaultdict(list)

        for row in file:
            print(row)

        return data


def main():
    data = read_file()
    print(data)


if __name__ == "__main__":
    raise SystemExit(main())