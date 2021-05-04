import plotly.figure_factory as ps
import pandas as pd
import csv
import random
import statistics

data = pd.read_csv("data.csv")
list = data["temp"].tolist()

# population data

population_mean = statistics.mean(list)
population_SD = statistics.stdev(list)
print(population_mean,population_SD)

# sample data

def sample_data(counted):
    dataPoints = []
    
    for a in range(0,counted):
        index = random.randint(0, len(list)-1)
        randomData = list[index]
        dataPoints.append(randomData)

    sample_mean = statistics.mean(dataPoints)
    sample_SD = statistics.stdev(dataPoints)

# multi sample data

multiSamplePoints = []

for b in range(0,1000):
    call = sample_data(100)
    multiSamplePoints.append(call)

multiSample_mean = statistics.mean(multiSamplePoints)
multiSample_SD = statistics.stdev(multiSamplePoints)
print(multiSample_mean,multiSample_SD)

#fig = ps.create_distplot([data["temp"].tolist()], ["room temprature"])
#fig.show()

