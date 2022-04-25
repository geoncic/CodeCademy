import argparse
import os.path
# import csv
# from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

    all_data.rename(columns={'Life expectancy at birth (years)': 'life_expectancy'}, inplace=True)

    print(all_data.head())
    print(all_data.columns)
    print(all_data.info())
    print(all_data['Country'].unique())
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ((ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(nrows = 3, ncols = 2, figsize = (14, 10))
    fig4, ax9 = plt.subplots()

    plt.subplots_adjust(hspace = 0.5, right = 0.9, left = 0.1, top = 0.9, bottom = 0.1)


    sns.violinplot(data = all_data, x='Country', y='life_expectancy', ax=ax1)
    sns.lineplot(data = all_data, x = "Year", y = "GDP", hue = 'Country', ax = ax2)

    # plt.show(block=True)
    # plt.interactive(False)


    sns.regplot(data = all_data[all_data['Country'] == "Chile"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax3)
    ax3.set_title("Chile")
    sns.regplot(data = all_data[all_data['Country'] == "China"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax4)
    ax4.set_title("China")
    sns.regplot(data = all_data[all_data['Country'] == "Germany"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax5)
    ax5.set_title("Germany")
    sns.regplot(data = all_data[all_data['Country'] == "Mexico"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax6)
    ax6.set_title("Mexico")
    sns.regplot(data = all_data[all_data['Country'] == "United States of America"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax7)
    ax7.set_title("USA")
    sns.regplot(data = all_data[all_data['Country'] == "Zimbabwe"], x = "GDP", y = "life_expectancy", scatter = True, fit_reg = True, ax = ax8)
    ax8.set_title("Zimbabwe")

    sns.barplot(data = all_data, x = "Country", y = "GDP")
    plt.xticks(rotation = 90)

    # plt.show(block=True)
    plt.show()
    plt.interactive(False)



    # plt.show(block=True)
    # plt.interactive(False)


if __name__ == "__main__":
    raise SystemExit(main())