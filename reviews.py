import pandas as pd
import zipfile

df = pd.read_csv('data\winemag-data-130k-v2.csv.zip', compression='zip')

#review_df = df[['country', 'count', 'points']]
print(df.columns)
#data_summary = review_df.groupby('country').agg(count=('points', 'count'), points=('points', 'mean'))

#data_summary['points'] = data_summary['points'].round(1)

#data_summary = data_summary.sort_values(by='count', ascending=False)

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

#data_summary.to_csv('data/reviews-per-country.csv')



