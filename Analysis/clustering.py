import pandas as pd
from sklearn.cluster import KMeans


#DEFINE VARIABLES
#Define Kmeans Analysis

kmeans = KMeans(init='k-means++',n_clusters=6,n_init=600)

#define Input/Output Files

infile='Redemption_Tots.csv'
outfile='Redemption_Tots_out.csv'

#Import file

df = pd.read_csv(infile)

#Set Index Field

df.set_index(['Guest_ID'], inplace=True)

#Fill Nulls/NaN

df.fillna(value=0, inplace=True)

# data fields

cols = df.columns.values.tolist()

data = df[cols].values

#Run kmeans on dataframe

kmeans.fit(df)

#Add resulting array to dataframe

df['kmeans6'] = kmeans.labels_

target = kmeans.labels_

#Output dataframe to csv

#df.to_csv(outfile)

