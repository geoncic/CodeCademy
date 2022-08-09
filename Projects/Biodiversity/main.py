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
    # dup = observations[observations.duplicated(keep=False)]
    # dup = dup.sort_values(['scientific_name'])

    # print(observations.shape)
    observations = observations.drop_duplicates()
    # print(observations.shape)

    # check for records which have the same scientific_name and park_name (possibly conflicting observation counts)

    # dup2 = observations[observations.duplicated(subset=['scientific_name', 'park_name'], keep=False)]
    # dup2 = dup2.sort_values(['scientific_name', 'park_name'])
    # print(dup2)

    # check shape of duplicate dataset
    # print(dup2.shape)

    # drop duplicates by using the mean of the observations to represent the approximate number
    # of observations for duplicate records

    # print(observations.groupby(['scientific_name', 'park_name'], as_index = False).mean())

    observations_cleaned = observations.groupby(['scientific_name', 'park_name'], as_index=False).mean()
    observations_cleaned = observations_cleaned.sort_values(['scientific_name', 'park_name'])

    # check for records which have the same category and scientific_name
    # dup3 = species_info[species_info.duplicated(subset=['category', 'scientific_name'], keep=False)]
    # dup3 = dup3.sort_values(['category', 'scientific_name'])

    # drop duplicates and keep the first record
    species_info_cleaned = species_info.drop_duplicates(subset=['category', 'scientific_name'])

    # Merge Dataframes

    df = observations_cleaned.merge(species_info_cleaned, how='left')
    # print(df.head())

    # check for N/A values
    # print(df.isna().sum())

    # get an overview of the quantitative column data
    # print(df['observations'].describe())

    # select only categorical columns
    # cat_columns = df.select_dtypes(include='object')

    # get an overview of the categorical columns

    # print(cat_columns.describe())

    species_info.fillna('No Intervention', inplace=True)
    # cons_category = species_info[
    # species_info['conservation_status']
    # != "No Intervention"].groupby("conservation_status").size()

    # create list of animal categories
    # categories = df.category.unique()

    # set custom color palette
    category_palette = {'Vascular Plant': '#66c2a5', 'Mammal': '#fc8d62', 'Fish': '#a6cee3', 'Amphibian': '#e78ac3',
                        'Nonvascular Plant': '#a6d854', 'Reptile': '#ffd92f', 'Bird': '#e5c494'}

    # create a sorted dataframe of number of scientific_name by categories
    species_by_category = df.groupby(['category'])
    species_by_category = species_by_category['scientific_name'].nunique().reset_index(name='species_cnt')
    species_by_category = species_by_category.sort_values('species_cnt', ascending=False).reset_index(drop=True)
    print(species_by_category)

    # create a bar chart of the number of species grouped by category
    fig1, ax1 = plt.subplots(figsize=(14, 10))

    # plot data
    ax = sns.barplot(x='species_cnt', y='category', data=species_by_category, palette=category_palette, ax=ax1)
    ax.set_title("The Number of Species Grouped by Categories", pad=20)
    ax.set_xlabel("Number of Species")
    ax.set_ylabel("Categories")
    # plt.show()
    plt.close()

    # create a sorted dataframe of number of scientific_name by park_name
    species_by_park = df.groupby(['park_name'])
    species_by_park = species_by_park['scientific_name'].nunique().reset_index(name='species_cnt')
    species_by_park = species_by_park.sort_values('species_cnt', ascending=False).reset_index(drop=True)

    print(species_by_park)

    # create a bar chart of the number of species grouped by categories in each park
    species_count_at_park = df.groupby(['park_name', 'category'])
    species_count_at_park = species_count_at_park['scientific_name'].count().reset_index()
    print(species_count_at_park)

    # create a figure
    fig2, ax2 = plt.subplots()

    # plot data
    ax2 = sns.barplot(x='park_name', y='scientific_name', hue='category',
                      data=species_count_at_park, palette=category_palette, ax=ax2)
    ax2.set_title("The Number of Species Grouped by Categories", fontsize='x-large', pad=20)
    ax2.set_xlabel("National Park")
    ax2.legend(loc="upper left", bbox_to_anchor=[1, 1])
    ax2.set_xticklabels(['Bryce', 'Great Smoky Mountains', 'Yellowstone', 'Yosemite'], rotation=20)
    ax2.set_ylabel("Number of Species")
    plt.show()
    plt.close()

    # ToDo: Define goals and analyze the data

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
