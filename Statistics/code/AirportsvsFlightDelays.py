import matplotlib.pyplot as plt;
from collections import OrderedDict
from collections import defaultdict
import json
import operator
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

monthNames = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}

delayThreshold = 30
DelaysDest = defaultdict(lambda : 0)
year = '2015'
for eachmonth in range(1, 13):
    data = pd.read_csv("DataSet/" + year + "/" + str(eachmonth) + "/" + str(eachmonth) + ".csv")
    count = 0
    destination = data[['DEST']].values
    #destination = np.nan_to_num(destination)
    actualDelays = data[['ARR_DELAY_NEW']].values
    actualDelays = np.nan_to_num(actualDelays)
    delays = data[['ARR_DEL15']].values
    delays = np.nan_to_num(delays)

    if delayThreshold == 15:
        for i,dest in zip(delays,destination):
            if i == 1:
                DelaysDest[str(dest)] += 1
    else:
        for i,dest in zip(actualDelays,destination):
            if i >= delayThreshold:
                DelaysDest[str(dest)] += 1
    count = 0;


file = str(year)+"Airports" + str(delayThreshold) +"minutes"
with open(file, 'w') as file:
    file.write(json.dumps(DelaysDest))

newDelaysDest = dict(sorted(dict(DelaysDest).items(), key=operator.itemgetter(1), reverse=True)[:15])



plt.bar(range(len(newDelaysDest)), newDelaysDest.values(), align="center")
plt.xticks(range(len(newDelaysDest)), list(newDelaysDest.keys()))
plt.xlabel("Airports")
plt.ylabel("Number of delays above " + str(delayThreshold) + "minutes in the year:" + str(year))
plt.show()

