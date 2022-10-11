import argparse
import os.path
import csv
from collections import defaultdict
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

INPUT_TEXT = os.path.join(os.path.dirname(__file__), 'data/developer_dataset.csv')


def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TEXT)
    args = parser.parse_args()
    
    # print(args.data_file)
    re = pd.read_csv(args.data_file)

    return re


def main():
    data = read_file()
    print(data.columns)
    print(data.count())
    print(data.describe())
    maxRows = data['RespondentID'].count()
    print('% Missing Data:')
    print((1 - data.count() / maxRows) * 100)

    data.drop(['NEWJobHunt', 'NEWJobHuntResearch', 'NEWLearn'],
            axis=1,
            inplace=True)

    data[['RespondentID', 'Country']].groupby('Country').count()

    missingData = data[['Employment', 'DevType']].isnull().groupby(data['Country']).sum().reset_index()

    #A = sns.catplot(data=missingData, kind="bar",
    #        x="Country", y="Employment",
    #        height = 6, aspect = 2)
    #B = sns.catplot(data=missingData, kind="bar",
    #        x="Country", y="DevType",
    #        height = 6, aspect = 2)

    #plt.show()
    #plt.close()

    data.dropna(subset = ['Employment', 'DevType'],
            inplace = True,
            how = 'any')

#    empfig = sns.catplot(x="Country", col="Employment",
#           data=data, kind="count",
#           height=7, aspect=1.6);

#    devdf = data[['Country', 'DevType']]
#    devdf.loc[devdf['DevType'].str.contains('back-end'), 'BackEnd'] = True
#    devdf.loc[devdf['DevType'].str.contains('front-end'), 'FrontEnd'] = True
#    devdf.loc[devdf['DevType'].str.contains('full-stack'), 'FullStack'] = True
#    devdf.loc[devdf['DevType'].str.contains('mobile'), 'Mobile'] = True
#    devdf.loc[devdf['DevType'].str.contains('administrator'), 'Admin'] = True

#    devdf = devdf.melt(id_vars=['Country'],
#        value_vars=['BackEnd', 'FrontEnd', 'FullStack', 'Mobile', 'Admin'],
#        var_name='DevCat',
#        value_name='DevFlag')

#    devdf.dropna(how='any', inplace=True)

    #devFig = sns.catplot(x="Country", col="DevCat",
    #    data=devdf, kind="count",
    #    height=6, aspect=1.5);

    #plt.show()
    #plt.close()

    missingUndergrad = data['UndergradMajor'].isnull().groupby(data['Year']).sum().reset_index()
    #sns.catplot(x="Year", y="UndergradMajor",
    #        data=missingUndergrad, kind="bar",
    #        height=4, aspect=1);

    # plt.show()
    # plt.close()

    data = data.sort_values(['RespondentID', 'Year'])
    data['UndergradMajor'].bfill(axis=0, inplace=True)

    majors = ['social science', 'natural science', 'computer science', 'development', 'another engineering', 'never declared']
    
    edudf = data[['Year', 'UndergradMajor']].copy(deep=True)
    edudf.dropna(how='any', inplace=True)
    print(data[['Year','UndergradMajor']])
    print(edudf)


    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)social science'), 'SocialScience'] = True
    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)natural science'), 'NaturalScience'] = True
    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)computer science'), 'ComSci'] = True
    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)development'), 'ComSci'] = True
    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)another engineering'), 'OtherEng'] = True
    edudf.loc[edudf['UndergradMajor'].str.contains('(?i)never declared'), 'NoMajor'] = True

    edudf = edudf.melt(id_vars=['Year'],
        value_vars=['SocialScience','NaturalScience','ComSci','OtherEng','NoMajor'],
        var_name='EduCat',
        value_name='EduFlag')

    edudf.dropna(how='any', inplace=True)
    
    edudf = edudf.groupby(['Year','EduCat']).count().reset_index()
    
#    eduFig = sns.catplot(x="Year", y="EduFlag", col="EduCat",
#        data=edudf, kind="bar",
#        height=6, aspect=1.5);

#    plt.show()
#    plt.close()

    compFields = data[['Year', 'YearsCodePro', 'ConvertedComp']].copy(deep=True)

#    D = sns.boxplot(x='Year', y='YearsCodePro',
#            data=compFields)

#    E = sns.boxplot(x='Year', y='ConvertedComp',
#            data=compFields)


#    plt.show()
#    plt.close()

    imputedf = data[['YearsCodePro', 'ConvertedComp']].copy(deep=True)

    traindf, testdf = train_test_split(imputedf, train_size=0.1)

    # Create the IterativeImputer model to predict missing values
    imp = IterativeImputer(max_iter=20, random_state=0)
    
    # Fit the model to the test dataset
    imp.fit(imputedf)

    # Transform the model on the entire dataset
    compdf = pd.DataFrame(np.round(imp.transform(imputedf),0), columns=['YearsCodePro','ConvertedComp'])

    compPlotdf = compdf.loc[compdf['ConvertedComp'] <=150000].copy(deep=True)
    compPlotdf['CodeYearBins'] = pd.qcut(compPlotdf['YearsCodePro'], q=5)

    sns.boxplot(x='CodeYearBins', y='ConvertedComp',
            data=compPlotdf)

    plt.show()
    plt.close()

if __name__ == "__main__":
    raise SystemExit(main())
