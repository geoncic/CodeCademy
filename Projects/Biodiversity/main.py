import argparse
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_file(filename):
    input_txt = os.path.join(os.path.dirname(__file__), filename)
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=input_txt)
    args = parser.parse_args()

    print(args.data_file)

    re = pd.read_csv(args.data_file)

    return re


def main():
    observations = read_file('observations.csv')
    species_info = read_file('species_info.csv')
    print(observations.info())
    print(species_info.info())
    print(observations.head())
    print(species_info.head())

    species_info.fillna('No Intervention', inplace=True)
    print(species_info.groupby("conservation_status").size())


if __name__ == "__main__":
    raise SystemExit(main())
