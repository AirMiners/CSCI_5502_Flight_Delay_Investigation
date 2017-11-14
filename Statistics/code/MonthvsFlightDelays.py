import matplotlib.pyplot as plt;
from collections import OrderedDict
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

monthNames ={1:'Jan', 2:'Feb', 3:'Mar' , 4:'Apr',5:'May',6:'June', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}
delayThreshold = 30
DelaysMonth =OrderedDict({})
year ='2015'
for eachmonth in range(1,13):
    data = pd.read_csv("DataSet/" + year +"/" + str(eachmonth) +"/" + str(eachmonth)+".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)
    delays = data[['ARR_DEL15']].values
    delays = np.nan_to_num(delays)
    
    if delayThreshold == 15:
        for i in delays:
            if i == 1:
                count +=1
    else:
        for i in actualDelays:
            if i >= delayThreshold:
                count += 1
    DelaysMonth[monthNames.get(eachmonth)] = count
    count =0;


plt.bar(range(len(DelaysMonth)), DelaysMonth.values(), align="center")
plt.xticks(range(len(DelaysMonth)), list(DelaysMonth.keys()))
plt.xlabel("Months of the Year:" + str(year))
plt.ylabel("Number of delays above " + str(delayThreshold)+ "minutes")
plt.show()
