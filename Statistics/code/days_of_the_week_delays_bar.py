import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# monthNames ={1:'Jan', 2:'Feb', 3:'Mar' , 4:'Apr',5:'May',6:'June', 7:'July', 8:'Aug', 9:'Sept', 10:'Oct', 11:'Nov', 12:'Dec'}
delayThreshold = 30
# DelaysMonth = {}
day_of_week_delays = {}
year ='2015'
month_delays = []
for eachmonth in range(1,13):
    data = pd.read_csv("DataSet/" + year +"/" + str(eachmonth) +"/" + str(eachmonth)+".csv")
    day_of_week = data[['DAY_OF_WEEK']].values
    day_of_week = np.nan_to_num(day_of_week)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)
    for i,j in zip(actualDelays, day_of_week):
        j[0] = int(j[0])
        if j[0] not in day_of_week_delays.keys():
            day_of_week_delays[j[0]] = 0
        if i[0] >= delayThreshold:
            day_of_week_delays[j[0]] += 1
    month_delays.append(day_of_week_delays)
    day_of_week_delays = {}

    # DelaysMonth[monthNames.get(eachmonth)] = count
print month_delays