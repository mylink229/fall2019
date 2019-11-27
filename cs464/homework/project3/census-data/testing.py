from sklearn.ensemble import RandomForestClassifier 
from sklearn import tree
from sklearn.impute import SimpleImputer
import numpy
import pandas as panda
from sklearn.model_selection import train_test_split

##########
# TASK 1 #
##########
column_names = ['age', 'workclass', 'education', 'marital-status', 
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 
            'capital-loss', 'hours-per-week', 'native-country', '50k']

trainDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_train.txt", header = None, na_values=" ?").copy()
testDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/adult_test.txt", header = None, na_values= " ?").copy()
featuresDataFrame = panda.read_csv("/home/chufu/Documents/fall2019/cs464/homework/project3/census-data/features.txt", sep = ":,|_", engine="python", header = None).copy()

trainDataFrame.columns = column_names
testDataFrame.columns = column_names

trainWorkclassMode = trainDataFrame["workclass"].mode()
trainOccupationMode = trainDataFrame["occupation"].mode()
trainNativeCountryMode = trainDataFrame["native-country"].mode()

trainDataFrame["workclass"].fillna(trainWorkclassMode, inplace = True)
trainDataFrame["occupation"].fillna(trainOccupationMode, inplace = True)
trainDataFrame["native-country"].fillna(trainNativeCountryMode, inplace = True)

/

##########
# TASK 2 #
##########
# column names are essentially the features
#feature_len = len(column_names)

new_feature_values = []
j = 0
for i in trainDataFrame["age"]:
    if trainDataFrame.at[j, "age"] == " ?":
        item = ["age", 0]
        new_feature_values.append(item)
    else:
        item = ["age", trainDataFrame.at[j, "age"]]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["workclass"]:
    if trainDataFrame.at[j, "workclass"] == " ?":
        item = ["workclass", 0]
        new_feature_values.append(item)
    else:
        item = ["workclass", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["education"]:
    if trainDataFrame.at[j, "education"] == " ?":
        item = ["education", 0]
        new_feature_values.append(item)
    else:
        item = ["education", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["marital-status"]:
    if trainDataFrame.at[j, "marital-status"] == " ?":
        item = ["marital-status", 0]
        new_feature_values.append(item)
    else:
        item = ["marital-status", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["occupation"]:
    if trainDataFrame.at[j, "occupation"] == " ?":
        item = ["occupation", 0]
        new_feature_values.append(item)
    else:
        item = ["occupation", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["relationship"]:
    if trainDataFrame.at[j, "relationship"] == " ?":
        item = ["relationship", 0]
        new_feature_values.append(item)
    else:
        item = ["relationship", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["race"]:
    if trainDataFrame.at[j, "race"] == " ?":
        item = ["race", 0]
        new_feature_values.append(item)
    else:
        item = ["race", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["sex"]:
    if trainDataFrame.at[j, "sex"] == " ?":
        item = ["sex", 0]
        new_feature_values.append(item)
    else:
        item = ["sex", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["capital-gain"]:
    if trainDataFrame.at[j, "capital-gain"] == " ?":
        item = ["capital-gain", trainDataFrame.at[j, "capital-gain"]]
        new_feature_values.append(item)
    else:
        item = ["capital-gain", trainDataFrame.at[j, "capital-gain"]]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["capital-loss"]:
    if trainDataFrame.at[j, "capital-loss"] == " ?":
        item = ["capital-loss", trainDataFrame.at[j, "capital-loss"]]
        new_feature_values.append(item)
    else:
        item = ["capital-loss", 1]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["hours-per-week"]:
    if trainDataFrame.at[j, "hours-per-week"] == " ?":
        item = ["hours-per-week", trainDataFrame.at[j, "hours-per-week"]]
        new_feature_values.append(item)
    else:
        item = ["hours-per-week", trainDataFrame.at[j, "hours-per-week"]]
        new_feature_values.append(item)
    j+=1

j = 0
for i in trainDataFrame["50k"]:
    if trainDataFrame.at[j, "50k"] == " ?":
        item = ["50k", trainDataFrame.at[j, "50k"]]
        new_feature_values.append(item)
    else:
        item = ["50k", trainDataFrame.at[j, "50k"]]
        new_feature_values.append(item)
    j+=1

    if i != trainDataFrame["age"][j].isnull():
        print(trainDataFrame["age"][j])


test = train_test_split(
    new_feature_values,
    trainDataFrame,
    train_size = 0.70,
    test_size = 0.30,
    random_state = 85
    )








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