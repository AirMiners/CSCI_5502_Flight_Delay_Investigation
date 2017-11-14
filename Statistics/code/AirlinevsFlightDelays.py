import matplotlib.pyplot as plt;
from collections import OrderedDict
from collections import defaultdict
import json
import operator
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

delayThreshold = 30
DelaysAirline = defaultdict(lambda : 0)
airlineOperations = defaultdict(lambda :0)
year = '2015'
airlineValues =[]
airlineActualValues =[]
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")

    airlines = data[['CARRIER']].values
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)

    for i,airline in zip(actualDelays,airlines):
        airlineOperations[str(airline)] += 1
        if i >= delayThreshold:
            DelaysAirline[str(airline)] += 1

file = str(year)+"Airlines" + str(delayThreshold) +"minutes"
with open(file, 'w') as file:
    file.write(json.dumps(DelaysAirline))

#Ordering the display in Bar Graph
airlinesSorted = sorted(DelaysAirline)
for key in airlinesSorted:
    airlineValues.append((DelaysAirline[key]))

for key in airlinesSorted:
    airlineActualValues.append(airlineOperations[key])

print(airlineValues)
plt.bar(np.arange(len(DelaysAirline)), airlineActualValues, align="center", width=0.2, color='g')
plt.bar(np.arange(len(DelaysAirline)) -0.2, airlineValues, align="center", width=0.2, color='r')
plt.legend(('Total Flights', 'Delayed Flights'))
plt.xticks(np.arange(len(DelaysAirline)), airlinesSorted)
plt.xlabel("Airlines")
plt.ylabel("Number of delays above " + str(delayThreshold) + "minutes in the year:" + str(year))
plt.show()

