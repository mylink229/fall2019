from sklearn.ensemble import RandomForestClassifier 
from sklearn import tree
import numpy
import pandas as panda

column_names = ['age', 'workclass', 'education', 'marital-status', 
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 
            'capital-loss', 'hours-per-week', 'native-country', '50k']

#trainDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_train.txt", sep = ",", header = None, names = ["age", "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country"])
#testDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_test.txt", sep = ",", header = None, names = ["age", "workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country"])
trainDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_train.txt", header = None)
testDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_test.txt", header = None)
featuresDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/features.txt", sep = ",", header = None)
trainDataFrame.columns = column_names

#trainAgeMean = trainDataFrame["age"].mean()
#trainAgeMedian = trainDataFrame["age"].median()

#trainCapitalGainMean = trainDataFrame["capital-gain"].mean()
#trainCapitalGainMedian = trainDataFrame["capital-gain"].median()

#trainCapitalLossMean = trainDataFrame["capital-loss"].mean()
#trainCapitalLossMedian = trainDataFrame["capital-loss"].median()

#trainHrPerWeekMean = trainDataFrame["hours-per-week"].mean()
#trainHrPerWeekMedian = trainDataFrame["hours-per-week"].median()

#i = 0
#l = 0
#for j in trainDataFrame:
    #for k in 12:
    #if trainDataFrame.iat[i,l] == "?":
        #trainDataFrame.iat[i, l] =

i = 0 # x
l = 0 # y 
for j in trainDataFrame["age"]:
    for k in range(13):
        if trainDataFrame.iat[l, i] == "?":
            if k == 0:
                trainDataFrame.iat[l, k] = trainDataFrame["age"].mean()

            if k == 1:
                trainDataFrame.iat[l,k] = trainDataFrame["workclass"].mode()

            if k == 2:
                trainDataFrame.iat[l,k] = trainDataFrame["education"].mode()

            if k == 3:
                trainDataFrame.iat[l,k] = trainDataFrame["marital-status"].mode()

            if k == 4:
                trainDataFrame.iat[l,k] = trainDataFrame["occupation"].mode()

            if k == 5:
                trainDataFrame.iat[l,k] = trainDataFrame["relationship"].mode()

            if k == 6:
                trainDataFrame.iat[l,k] = trainDataFrame["race"].mode()

            if k == 7:
                trainDataFrame.iat[l,k] = trainDataFrame["sex"].mode()

            if k == 8:
                trainDataFrame.iat[l,k] = trainDataFrame["capital-gain"].mean()

            if k == 9:
                trainDataFrame.iat[l,k] = trainDataFrame["capital-loss"].mean()
                
            if k == 10:
                trainDataFrame.iat[l,k] = trainDataFrame["hours-per-week"].mean()

            if k == 11:
                trainDataFrame.iat[l,k] = trainDataFrame["workclass"].mode()

            if k == 12:
                trainDataFrame.iat[l,k] = trainDataFrame["50k"].mode()
        #i+=1
    l+=1



    if trainDataFrame["workclass"][i] == "?":
        trainDataFrame.iat[1,i] = trainDataFrame["workclass"].mode()

    if trainDataFrame["education"][i] == "?":
        trainDataFrame.iat[2,i] = trainDataFrame["education"].mode() 

    if trainDataFrame["marital-status"][i] == "?":
        trainDataFrame.iat[3, i] = trainDataFrame["marital-status"].mode()

    if trainDataFrame["occupation"][i] == "?":
        trainDataFrame.iat[4, i] = trainDataFrame["occupation"].mode()

    if trainDataFrame["relationship"][i] == "?":
        trainDataFrame.iat[5,i] = trainDataFrame["relationship"].mode()

    if trainDataFrame["race"][i] == "?":
        trainDataFrame.iat[6,i] = trainDataFrame["race"].mode() 

    if trainDataFrame["sex"][i] == "?":
        trainDataFrame.iat[7, i] = trainDataFrame["sex"].mode() 

    if trainDataFrame["capital-gain"][i] == "?":
        trainDataFrame.iat[8, i] = trainDataFrame["capital-gain"].mean() 

    if trainDataFrame["capital-loss"][i] == "?":
        trainDataFrame.iat[9, i] = trainDataFrame["capital-loss"].mean()

    if trainDataFrame["hours-per-week"][i] == "?":
        trainDataFrame.iat[l, i] = trainDataFrame["hours-per-week"].mean()

    if trainDataFrame["native-country"][i] == "?":
        trainDataFrame.iat["native-country"][i] = trainDataFrame["native-country"].mode() 

    if trainDataFrame["50k"][i] == "?":
        trainDataFrame.iat["50k"][i] = trainDataFrame["50k"].mode() 
    i+=1

i = 0
for j in testDataFrame["age"]:
    if testDataFrame["age"][i] == "?":
        testDataFrame["age"][i] = testDataFrame["age"].mean()

    if testDataFrame["workclass"][i] == "?":
        testDataFrame["workclass"][i] = testDataFrame["workclass"].mode()

    if testDataFrame["education"][i] == "?":
        testDataFrame["education"][i] = testDataFrame["education"].mode() 

    if testDataFrame["marital-status"][i] == "?":
        testDataFrame["marital-status"][i] = testDataFrame["marital-status"].mode()

    if testDataFrame["occupation"][i] == "?":
        testDataFrame["occupation"][i] = testDataFrame["occupation"].mode()

    if testDataFrame["relationship"][i] == "?":
        testDataFrame["relationship"][i] = testDataFrame["relationship"].mode()

    if testDataFrame["race"][i] == "?":
        testDataFrame["race"][i] = testDataFrame["race"].mode() 

    if testDataFrame["sex"][i] == "?":
        testDataFrame["sex"][i] = testDataFrame["sex"].mode() 

    if testDataFrame["capital-gain"][i] == "?":
        testDataFrame["capital-gain"][i] = testDataFrame["capital-gain"].mean() 

    if testDataFrame["capital-loss"][i] == "?":
        testDataFrame["capital-loss"][i] = testDataFrame["capital-loss"].mean()

    if testDataFrame["hours-per-week"][i] == "?":
        testDataFrame["hours-per-week"][i] = testDataFrame["hours-per-week"].mean()

    if testDataFrame["native-country"][i] == "?":
        testDataFrame["native-country"][i] = testDataFrame["native-country"].mode() 

    if testDataFrame["50k"][i] == "?":
        testDataFrame["50k"][i] = testDataFrame["50k"].mode() 
    i+=1

i = 0
for j in trainDataFrame["age"]:
    if trainDataFrame["age"][i] == "?":
        trainDataFrame["age"][i] = trainDataFrame["age"].mean()

    if trainDataFrame["workclass"][i] == "?":
        trainDataFrame["workclass"][i] = trainDataFrame["workclass"].mode()

    if trainDataFrame["education"][i] == "?":
        trainDataFrame["education"][i] = trainDataFrame["education"].mode() 

    if trainDataFrame["marital-status"][i] == "?":
        trainDataFrame["marital-status"][i] = trainDataFrame["marital-status"].mode()

    if trainDataFrame["occupation"][i] == "?":
        trainDataFrame["occupation"][i] = trainDataFrame["occupation"].mode()

    if trainDataFrame["relationship"][i] == "?":
        trainDataFrame["relationship"][i] = trainDataFrame["relationship"].mode()

    if trainDataFrame["race"][i] == "?":
        trainDataFrame["race"][i] = trainDataFrame["race"].mode() 

    if trainDataFrame["sex"][i] == "?":
        trainDataFrame["sex"][i] = trainDataFrame["sex"].mode() 

    if trainDataFrame["capital-gain"][i] == "?":
        trainDataFrame["capital-gain"][i] = trainDataFrame["capital-gain"].mean() 

    if trainDataFrame["capital-loss"][i] == "?":
        trainDataFrame["capital-loss"][i] = trainDataFrame["capital-loss"].mean()

    if trainDataFrame["hours-per-week"][i] == "?":
        trainDataFrame["hours-per-week"][i] = trainDataFrame["hours-per-week"].mean()

    if trainDataFrame["native-country"][i] == "?":
        trainDataFrame["native-country"][i] = trainDataFrame["native-country"].mode() 

    if trainDataFrame["50k"][i] == "?":
        trainDataFrame["50k"][i] = trainDataFrame["50k"].mode() 
    i+=1

i = 0
for j in testDataFrame["age"]:
    if testDataFrame["age"][i] == "?":
        testDataFrame["age"][i] = testDataFrame["age"].mean()

    if testDataFrame["workclass"][i] == "?":
        testDataFrame["workclass"][i] = testDataFrame["workclass"].mode()

    if testDataFrame["education"][i] == "?":
        testDataFrame["education"][i] = testDataFrame["education"].mode() 

    if testDataFrame["marital-status"][i] == "?":
        testDataFrame["marital-status"][i] = testDataFrame["marital-status"].mode()

    if testDataFrame["occupation"][i] == "?":
        testDataFrame["occupation"][i] = testDataFrame["occupation"].mode()

    if testDataFrame["relationship"][i] == "?":
        testDataFrame["relationship"][i] = testDataFrame["relationship"].mode()

    if testDataFrame["race"][i] == "?":
        testDataFrame["race"][i] = testDataFrame["race"].mode() 

    if testDataFrame["sex"][i] == "?":
        testDataFrame["sex"][i] = testDataFrame["sex"].mode() 

    if testDataFrame["capital-gain"][i] == "?":
        testDataFrame["capital-gain"][i] = testDataFrame["capital-gain"].mean() 

    if testDataFrame["capital-loss"][i] == "?":
        testDataFrame["capital-loss"][i] = testDataFrame["capital-loss"].mean()

    if testDataFrame["hours-per-week"][i] == "?":
        testDataFrame["hours-per-week"][i] = testDataFrame["hours-per-week"].mean()

    if testDataFrame["native-country"][i] == "?":
        testDataFrame["native-country"][i] = testDataFrame["native-country"].mode() 

    if testDataFrame["50k"][i] == "?":
        testDataFrame["50k"][i] = testDataFrame["50k"].mode() 
    i+=1

##########
# TASK 2 #
##########
# column names are essentially the features
#feature_len = len(column_names)

workclass = ["workclass", "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"]
education = ["education", "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"]
marital_status = ["marital-status", "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"]
occupation = ["occupation", "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"]
relationship = ["relationship", "Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"]
race = ["race", "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"]
sex = ["sex", "Female", "Male"]
native_country = ["native-country", "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"]

new_features = []

j = 0

for i in featuresDataFrame[0]:
    if i == featuresDataFrame[0][0] or i == featuresDataFrame[0][8] or i == featuresDataFrame[0][9] or i == featuresDataFrame[0][10]:
        new_features.append(i)
        
for i in workclass:
    if j > (len(workclass) - 1):
        j = 1
        break
    e = workclass[0] + ":" + workclass[j]
    new_features.append(e)
    j+=1
    
for i in education:
    if j > (len(education) - 1):
        j = 1
        break
    e = education[0] + ":" + education[j]
    new_features.append(e)
    j+=1
    
for i in marital_status:
    if j > (len(marital_status) - 1):
        j = 1
        break
    e = marital_status[0] + ":" + marital_status[j]
    new_features.append(e)
    j+=1
    
for i in occupation:
    if j > (len(occupation) - 1):
        j = 1
        break
    e = occupation[0] + ":" + occupation[j]
    new_features.append(e)
    j+=1
    
for i in relationship:
    if j > (len(relationship) - 1):
        j = 1
        break
    e = relationship[0] + ":" + relationship[j]
    new_features.append(e)
    j+=1
    
for i in race:
    if j > (len(race) - 1):
        j = 1
        break
    e = race[0] + ":" + race[j]
    new_features.append(e)
    j+=1
    
for i in sex:
    if j > (len(sex) - 1):
        j = 1
        break
    e = sex[0] + ":" + sex[j]
    new_features.append(e)
    j+=1
    
for i in native_country:
    if j > (len(native_country) - 1):
        j = 1
        break
    e = native_country[0] + ":" + native_country[j]
    new_features.append(e)
    j+=1