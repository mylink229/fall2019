from sklearn.ensemble import RandomForestClassifier 
from sklearn import tree
import numpy
import pandas as panda

column_names = ['age', 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', '50k']
#trainDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_train.txt", sep = ",", header = None, names = ["age", "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country"])
#testDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_test.txt", sep = ",", header = None, names = ["age", "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country"])
trainDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_train.txt", header = None)
testDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_test.txt", header = None)
featuresDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/features.txt", sep = ",", header = None)
trainDataFrame.columns = column_names
trainAgeMean = trainDataFrame["age"].mean()
trainAgeMedian = trainDataFrame["age"].median()

trainCapitalGainMean = trainDataFrame["capital-gain"].mean()
trainCapitalGainMedian = trainDataFrame["capital-gain"].median()

trainCapitalLossMean = trainDataFrame["capital-loss"].mean()
trainCapitalLossMedian = trainDataFrame["capital-loss"].median()

trainHrPerWeekMean = trainDataFrame["hours-per-week"].mean()
trainHrPerWeekMedian = trainDataFrame["hours-per-week"].median()

feature_len = len(column_names)
new_features = []

for i in column_names:
    if i == age 