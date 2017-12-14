import matplotlib.pyplot as plt;
from collections import OrderedDict

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

destNames = {1: 'LGA', 2: 'PHX', 3: 'SFO', 4: 'LAS', 5: 'IAH', 6: 'LAX', 7: 'DFW', 8: 'DEN', 9: 'EWR', 10: 'ATL',
              11: 'ORD', 12: 'DTW'}
delayThreshold = 30
DelaysMonth2012 = OrderedDict({})
DelaysMonth2013 = OrderedDict({})
DelaysMonth2014 = OrderedDict({})
DelaysMonth2015 = OrderedDict({})


year ="2012"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    destination = data[['DEST']].values
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i,dest in zip(actualDelays, destination):
        if i >= delayThreshold:
            if (dest) in destNames.values():
                if str(dest) in DelaysMonth2012.keys():
                    DelaysMonth2012[str(dest)] += 1
                else:
                    DelaysMonth2012[str(dest)] = 1

year = "2013"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    destination = data[['DEST']].values
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i, dest in zip(actualDelays, destination):
        if i >= delayThreshold:
            if (dest) in destNames.values():
                if str(dest) in DelaysMonth2013.keys():
                    DelaysMonth2013[str(dest)] += 1
                else:
                    DelaysMonth2013[str(dest)] = 1

year ="2014"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    destination = data[['DEST']].values
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i,dest in zip(actualDelays, destination):
        if i >= delayThreshold:
            if (dest) in destNames.values():
                if str(dest) in DelaysMonth2014.keys():
                    DelaysMonth2014[str(dest)] += 1
                else:
                    DelaysMonth2014[str(dest)] = 1

year = "2015"
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    destination = data[['DEST']].values
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i, dest in zip(actualDelays, destination):
        if i >= delayThreshold:
            if (dest) in destNames.values():
                if str(dest) in DelaysMonth2015.keys():
                    DelaysMonth2015[str(dest)] += 1
                else:
                    DelaysMonth2015[str(dest)] = 1



plt.bar(np.arange(len(DelaysMonth2015)), DelaysMonth2015.values(), align="center", width=0.2, color='g')
plt.bar(np.arange(len(DelaysMonth2014)) -0.2, DelaysMonth2014.values(), align="center", width=0.2, color='r')
plt.bar(np.arange(len(DelaysMonth2013)) -0.4, DelaysMonth2013.values(), align="center", width=0.2, color='b')
plt.bar(np.arange(len(DelaysMonth2012)) -0.6, DelaysMonth2012.values(), align="center", width=0.2, color='y')
plt.legend(('2015','2014', '2013','2012'))
plt.xticks(range(len(DelaysMonth2012)), list(DelaysMonth2012.keys()))
plt.xlabel("Months of the Year")
plt.ylabel("Number of delays above " + str(delayThreshold) + "minutes")
plt.show()

