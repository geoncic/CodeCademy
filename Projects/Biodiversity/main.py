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
    cons_category = species_info[species_info['conservation_status'] != "No Intervention"].groupby("conservation_status").size()

    print(cons_category)
    print(cons_category.index)

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    # ax1 = plt.pie(cons_category, labels = cons_category.index, colors=sns.color_palette('pastel'), autopct='%.0f%%')
    # plt.show()
    # plt.clf()
    ax2 = sns.countplot(data = species_info, x = 'conservation_status', ax = ax2)

    plt.show()
    plt.interactive(False)

if __name__ == "__main__":
    raise SystemExit(main())
