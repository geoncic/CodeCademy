import argparse
import os.path
# import csv
# from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




INPUT_TXT = os.path.join(os.path.dirname(__file__), 'all_data.csv')


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(args.data_file)

    re = pd.read_csv(args.data_file)

    return re


    # with open(args.data_file) as f:
    #     file = csv.DictReader(f)
    #     data = defaultdict(list)
    #
    #     for row in file:
    #         print(row)
    #
    #     return data


def main():
    all_data = read_file()
    print(all_data.head())
    print(all_data.columns)
    print(all_data.info())
    print(all_data['Country'].unique())

    # plt.subplots()
    # plt.show()

    plt.show(block=True)
    plt.interactive(False)


if __name__ == "__main__":
    raise SystemExit(main())