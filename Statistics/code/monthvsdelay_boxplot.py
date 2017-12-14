import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# monthNames ={1:'Jan', 2:'Feb', 3:'Mar' , 4:'Apr',5:'May',6:'June', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}
delayThreshold = 30
# DelaysMonth = {}

year ='2014'
monthly_delay_count = []
for eachmonth in range(1,13):
    data = pd.read_csv("DataSet/" + year +"/" + str(eachmonth) +"/" + str(eachmonth)+".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)
    delays = data[['ARR_DEL15']].values
    delays = np.nan_to_num(delays)
    for i in actualDelays:
        if i >= delayThreshold:
            count += 1
    # DelaysMonth[monthNames.get(eachmonth)] = count
    monthly_delay_count.append(count)
    count =0;
plt.figure()
plt.boxplot(monthly_delay_count, sym='.')
print monthly_delay_count
plt.show()