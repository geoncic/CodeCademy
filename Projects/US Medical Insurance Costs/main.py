import argparse
import os.path
import csv
from collections import defaultdict


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'insurance.csv')


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        file = csv.DictReader(f)
        data = defaultdict(list)

        for row in file:
            data['age'].append(row['age'])
            data['sex'].append(row['sex'])
            data['bmi'].append(row['bmi'])
            data['children'].append(row['children'])
            data['smoker'].append(row['smoker'])
            data['region'].append(row['region'])
            data['charges'].append(row['charges'])
        return data


def main():
    data = read_file()
    print(data)


if __name__ == "__main__":
    raise SystemExit(main())
