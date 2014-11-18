import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics

# DEFINE VARIABLES


#define Input/Output Files

infile = 'Issuances_Tots.csv'
outfile = 'Issuances_Tots_out.csv'

#Import file

df = pd.read_csv(infile)

#Set Index Field

df.set_index(['Guest_ID'], inplace=True)

#Fill Nulls/NaN

df.fillna(value=0, inplace=True)

# define data columns

cols = df.columns.values.tolist()

data = df[cols]

data_array = data.values

print("Data Imported and Defined")

for i in range(2, 11):
    #Define Kmeans Analysis

    kmeans_calc = KMeans(init='k-means++', n_clusters=i, n_init=600)

    #Run kmeans on dataframe

    kmeans_calc.fit(df)

    #Add resulting array to dataframe

    df['kmeans_group' + str(i)] = kmeans_calc.labels_

    # define target

    target = df['kmeans_group' + str(i)]

    target_array = target.values

    # Run Silhouette Score

    df['sil' + str(i)] = metrics.silhouette_score(data_array, target_array, sample_size=1000)

    print("finished " + str(i) + " cluster groups")

#Output dataframe to csv

df.to_csv(outfile)

