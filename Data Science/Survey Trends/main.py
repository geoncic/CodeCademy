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
    survey_data = read_file("developer_dataset.csv")

    df = pd.DataFrame(survey_data)
    # print(df.columns)
    # print(df.count())
    # print(df.describe())



    df.drop(['NEWJobHunt', 'NEWJobHuntResearch', 'NEWLearn'],
            axis=1,
            inplace=True)

    maxRows = df['RespondentID'].count()
    print('% Missing Data:')
    print((1 - df.count() / maxRows) * 100)

    df[['RespondentID', 'Country']].groupby('Country').count()

    missing_data = df[['Employment', 'DevType']].isnull().groupby(df['Country']).sum().reset_index()

    # fig1, ax1 = plt.subplots(figsize=(14, 10))
    #
    # A=sns.barplot(
    #     data=missing_data,
    #     x="Country", y="Employment", ax=ax1)
    #
    #
    # fig2, ax2 = plt.subplots(figsize=(14, 10))
    #
    # B=sns.barplot(
    #     data=missing_data,
    #     x="Country", y="DevType", ax=ax2)
    #
    # plt.show()

    df.dropna(subset= ['Employment', 'DevType'],
        inplace = True,
        how = 'any')

if __name__ == "__main__":
    # raise SystemExit(main())
    main()