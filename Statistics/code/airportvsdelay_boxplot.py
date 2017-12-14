import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# monthNames ={1:'Jan', 2:'Feb', 3:'Mar' , 4:'Apr',5:'May',6:'June', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}
delayThreshold = 30
# DelaysMonth = {}
dest_airport_delays = {}
year ='2014'
for eachmonth in range(1,13):
    data = pd.read_csv("DataSet/" + year +"/" + str(eachmonth) +"/" + str(eachmonth)+".csv")
    dest_airport = data[['DEST']].values
    dest_airport = np.nan_to_num(dest_airport)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)
    for i,j in zip(actualDelays, dest_airport):
        if j[0] not in dest_airport_delays.keys():
            dest_airport_delays[j[0]] = 0
        if i[0] >= delayThreshold:
            dest_airport_delays[j[0]] += 1
    # DelaysMonth[monthNames.get(eachmonth)] = count
plt.figure()
print dest_airport_delays
plt.boxplot(dest_airport_delays.values(), sym='.')
plt.show()