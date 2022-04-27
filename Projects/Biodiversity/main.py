import argparse
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set to display dataframe rows without truncating
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', None)

# set fontsize for all plots
plt.rcParams['font.size'] = 14


def read_file(filename):
    input_txt = os.path.join(os.path.dirname(__file__), filename)
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=input_txt)
    args = parser.parse_args()

    print(args.data_file)

    re = pd.read_csv(args.data_file)

    return re


def main():

    # Import data
    observations = read_file('observations.csv')
    species_info = read_file('species_info.csv')

    # check the construction of the observation data
    # print(observations.info())
    # print(observations.head())
    #
    # print(species_info.info())
    # print(species_info.head())

    # check for duplicate records
    dup = observations[observations.duplicated(keep = False)]
    dup = dup.sort_values(['scientific_name'])

    # print(observations.shape)
    observations = observations.drop_duplicates()
    # print(observations.shape)

    # check for records which have the same scientific_name and park_name (possibly conflicting observation counts)

    dup2 = observations[observations.duplicated(subset=['scientific_name', 'park_name'], keep = False)]
    dup2 = dup2.sort_values(['scientific_name', 'park_name'])
    # print(dup2)

    # check shape of duplicate dataset
    # print(dup2.shape)

    # drop duplicates by using the mean of the observations to represent the approximate number of observations for duplicate records

    # print(observations.groupby(['scientific_name', 'park_name'], as_index = False).mean())

    observations_cleaned = observations.groupby(['scientific_name', 'park_name'], as_index = False).mean()
    observations_cleaned = observations_cleaned.sort_values(['scientific_name', 'park_name'])

    # check for records which have the same category and scientific_name
    dup3 = species_info[species_info.duplicated(subset =['category', 'scientific_name'], keep = False)]
    dup3 = dup3.sort_values(['category', 'scientific_name'])


    # drop duplicates and keep the first record
    species_info_cleaned = species_info.drop_duplicates(subset=['category', 'scientific_name'])

    # Merge Dataframes

    df = observations_cleaned.merge(species_info_cleaned, how = 'left')
    print(df.head())

    # check for N/A values
    print(df.isna().sum())

    # get an overview of the quantitative column data
    print(df['observations'].describe())

    # select only categorical columns
    cat_columns = df.select_dtypes(include='object')

    # get an overview of the categorical columns

    print(cat_columns.describe())

    species_info.fillna('No Intervention', inplace=True)
    cons_category = species_info[species_info['conservation_status'] != "No Intervention"].groupby("conservation_status").size()



    ## ToDo: Define goals and analyze the data





    # print(cons_category)
    # print(cons_category.index)

    # fig1, ax1 = plt.subplots()
    # fig2, ax2 = plt.subplots()

    # print(species_info.columns)

    # ax1 = plt.pie(cons_category, labels = cons_category.index, colors=sns.color_palette('pastel'), autopct='%.0f%%')
    # plt.show()
    # plt.clf()
    # ax2 = sns.countplot(data = species_info, x = 'conservation_status', ax = ax2)

    plt.show()
    plt.interactive(False)

if __name__ == "__main__":
    raise SystemExit(main())
