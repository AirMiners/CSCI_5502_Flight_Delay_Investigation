import matplotlib.pyplot as plt;
from collections import OrderedDict

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

monthNames = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}
delayThreshold = 30
DelaysMonth2012 = OrderedDict({})
DelaysMonth2013 = OrderedDict({})
DelaysMonth2014 = OrderedDict({})
DelaysMonth2015 = OrderedDict({})


year ="2012"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)


    for i in actualDelays:
        if i >= delayThreshold:
            count += 1
    DelaysMonth2012[monthNames.get(eachmonth)] = count
    count = 0;


year ="2013"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i in actualDelays:
        if i >= delayThreshold:
            count += 1
    DelaysMonth2013[monthNames.get(eachmonth)] = count
    count = 0;


year ="2014"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i in actualDelays:
        if i >= delayThreshold:
            count += 1
    DelaysMonth2014[monthNames.get(eachmonth)] = count
    count = 0;

year ="2015"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    month = data[['MONTH']].values
    month = np.nan_to_num(month)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i in actualDelays:
        if i >= delayThreshold:
            count += 1
    DelaysMonth2015[monthNames.get(eachmonth)] = count
    count = 0;



plt.bar(np.arange(len(DelaysMonth2015)), DelaysMonth2015.values(), align="center", width=0.2, color='g')
plt.bar(np.arange(len(DelaysMonth2014)) -0.2, DelaysMonth2014.values(), align="center", width=0.2, color='r')
plt.bar(np.arange(len(DelaysMonth2013)) -0.4, DelaysMonth2013.values(), align="center", width=0.2, color='b')
plt.bar(np.arange(len(DelaysMonth2012)) -0.6, DelaysMonth2012.values(), align="center", width=0.2, color='y')
plt.legend(('2015','2014', '2013','2012'))
plt.xticks(range(len(DelaysMonth2015)), list(DelaysMonth2015.keys()))
plt.xlabel("Months of the Year")
plt.ylabel("Number of delays above " + str(delayThreshold) + "minutes")
plt.show()

