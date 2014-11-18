# Load Packages

from sklearn import tree

import pandas as pd

from os import system

#import Data

infile = 'Redemption_Tots_out.csv'

df = pd.read_csv(infile)

df.set_index(['Guest_ID'], inplace=True)

df.fillna(value=0, inplace=True)

data_cols= ['PR8230','PR8231','PR7766','PR8180','PR8181','PR9599','PR9600']

# Define Response

Y = df['kmeans3']

# Define Predictors

X = df[data_cols]

#Specify Tree Classifier 

dtree = tree.DecisionTreeClassifier(criterion = "gini", min_samples_leaf = 1, compute_importances = True)

dtree = dtree.fit(X,Y)

# Print Variable Importance

print(pd.DataFrame(dtree.feature_importances_,columns = ['Imp'], index = X.columns).sort(['Imp'],ascending = False))