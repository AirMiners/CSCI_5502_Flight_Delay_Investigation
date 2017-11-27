import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

######################## Training Logistic Regression Model############################
delay_threshold = 30 #In minutes
train_month =1
for year in range (2012, 2016):
    train_data = pd.read_csv("DataSet/" + str(year) +"/" + str(train_month) +"/" + str(train_month)+".csv")
    if year == 2012:
        x_train = train_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID']].values
        y_train = train_data[['ARR_DELAY_NEW']].values
    else:
        x = train_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID' ]].values
        y = train_data[['ARR_DELAY_NEW']].values
        x_train = np.append(x_train, x, axis=0)
        y_train = np.append(y_train, y, axis=0)



x_train = np.nan_to_num(x_train)
y_train = np.nan_to_num(y_train)

X_train = x_train.reshape(-1, 5)

y_train= np.where(y_train <= delay_threshold, 0, 1)
Y_train = y_train.reshape(-1, 1)


clf = RandomForestClassifier()
clf.fit(X_train, Y_train)

###################################### Testing ##########################################
test_month = "1"
test_year = "2015"
test_data = pd.read_csv("DataSet/" + str(test_year) +"/" + str(test_month) +"/" + str(test_month)+".csv")
x_test = test_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID']].values
y_actual = test_data[['ARR_DELAY_NEW']].values


x_test = np.nan_to_num(x_test)
y_actual = np.nan_to_num(y_actual)
y_actual= np.where(y_actual <= delay_threshold, 0, 1)

X_test = x_test.reshape(-1, 5)
Y_actual = y_actual.reshape(-1, 1)

######predict################
Y_pred = clf.predict(X_test)

no =0
match  =0
for i, j in zip(Y_actual,Y_pred):
    no +=1
    if i==j:
        match +=1

print("RR", match/no, "\n")
confusion_matrix = confusion_matrix(Y_actual, Y_pred)
print(confusion_matrix)

accuracy = (confusion_matrix[0][0] +  confusion_matrix[1][1])  / (sum(confusion_matrix[0]) + sum(confusion_matrix[1]))
print(accuracy)