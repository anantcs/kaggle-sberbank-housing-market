#IMPORTING REQUIRED HEADERS
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import RidgeCV
import collections

#READING IN THE DATA
data = pd.read_csv("../data/train.csv")
#print list(data.dtypes)
counter = collections.Counter(list(data.dtypes))
print(counter)

#oho = [o for o in list(data.columns) if data.dtypes[o] == 'O']
#print oho
#raw_input()
#data = data.dropna(axis=1)
data = data.fillna(data.mean())
print data.shape

#DIVIDING TEST, TRAIN DATA
train, test = train_test_split(data, test_size=0.2)
cols = [c for c in list(data.columns) if c not in ['price_doc'] and data.dtypes[c] != 'O']
xtrain = train[cols]
print 'xtrain.shape', xtrain.shape
train_columns = list(xtrain.columns)
ytrain = train['price_doc']
xtest = test[cols]
ytest = test['price_doc']

#MODELING DATA
regr = linear_model.RidgeCV()
regr.fit(xtrain, ytrain)
#print(regr.coef_)
print(np.mean((regr.predict(xtest)-ytest)**2))
print regr.score(xtest, ytest)

#SUBMISSION
outfile = open("../output/submission1.csv","w")
test_data = pd.read_csv("../data/test.csv")
#test_data = test_data.dropna(axis=1)
test_data = test_data.fillna(test_data.mean())
print data.shape
print test_data.shape

cols = [c for c in list(test_data.columns) if c not in ['price_doc','product_type'] and test_data.dtypes[c] != 'O']
test_x = test_data[cols]
test_columns = list(test_x.columns)
difference = list(set(train_columns).difference(test_columns))
print difference
print 'test_x.shape',test_x.shape
outfile.write("id,price_doc\n")
print regr.predict(test_x).shape
preds = regr.predict(test_x)
for i in range(len(preds)):
    outfile.write(str(test_x['id'][i])+','+str(preds[i])+'\n')

