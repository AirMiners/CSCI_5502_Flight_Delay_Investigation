import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

######################## Training Logistic Regression Model############################

train_month =1
for year in range (2012, 2013):
    train_data = pd.read_csv("DataSet/" + str(year) +"/" + str(train_month) +"/" + str(train_month)+".csv")
    if year == 2012:
        x_train = train_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID']].values
        y_train = train_data[['ARR_DELAY_NEW']].values
    else:
        x = train_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID' ]].values
        y = train_data[['ARR_DELAY_NEW']].values
        x_train = np.append(x_train, x, axis=0)
        y_train = np.append(y_train, y, axis=0)

print(len(x_train))
print(len(y_train))
indices = np.logical_not(np.logical_or(np.isnan(x_train), np.isnan(y_train)))
x_train = x_train[indices]
y_train = y_train[indices[:,0]]

X_train = x_train.reshape(-1, 5)

y_train= np.where(y_train < 30, 0, 1)
Y_train = y_train.reshape(-1, 1)


LogReg = LogisticRegression()
LogReg.fit(X_train, Y_train)

###################################### Testing ##########################################
test_month = "1"
test_year = "2015"
test_data = pd.read_csv("DataSet/" + str(test_year) +"/" + str(test_month) +"/" + str(test_month)+".csv")
x_test = test_data[['DEST_AIRPORT_ID', 'MONTH', 'DAY_OF_MONTH', 'AIRLINE_ID', 'ORIGIN_AIRPORT_ID']].values
y_actual = test_data[['ARR_DELAY_NEW']].values

indices = np.logical_not(np.logical_or(np.isnan(x_test), np.isnan(y_actual)))

x_test = x_test[indices]
y_actual = y_actual[indices[:,0]]
y_actual= np.where(y_actual < 30, 0, 1)

X_test = x_test.reshape(-1, 5)
Y_actual = y_actual.reshape(-1, 1)

######predict################
Y_pred = LogReg.predict(X_test)

confusion_matrix = confusion_matrix(Y_actual, Y_pred)
print(confusion_matrix)