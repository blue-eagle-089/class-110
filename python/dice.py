import random
import plotly.graph_objects as pg
import plotly.figure_factory as ps
import statistics


count = []
diceOutput = [] 

for a in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceOutput.append(dice1 + dice2)
    count.append(a)

mean = sum(diceOutput)/len(diceOutput)
SD = statistics.stdev(diceOutput)
mode = statistics.mode(diceOutput)
median = statistics.median(diceOutput)
print(mean,SD,mode,median)

sd1start = mean - SD 
Sd1end = mean + SD

sd2start = mean - (2*SD)
sd2end = mean + (2*SD)

sd3start = mean - (3*SD)
sd3end = mean + (3*SD)

fig = ps.create_distplot([diceOutput], ["number"])
fig.add_trace(pg.Scatter(x = [mean,mean] , y = [0,1] , mode = "lines" , name = "mean"))

fig.add_trace(pg.Scatter(x=[sd1start, sd1start], y=[0, 1] , mode = "lines" , name = "standard deviation 1"))
fig.add_trace(pg.Scatter(x=[Sd1end, Sd1end], y=[0, 1] , mode = "lines" , name = "standard deviation 1"))

fig.add_trace(pg.Scatter(x=[sd2start, sd2start], y=[0,1] , mode = "lines" , name = "standard deviation 2"))
fig.add_trace(pg.Scatter(x=[sd2end, sd2end], y=[0, 1] , mode = "lines" , name = "standard deviation 2"))

fig.add_trace(pg.Scatter(x=[sd3start, sd3start], y=[0,1] , mode = "lines" , name = "standard deviation 3"))
fig.add_trace(pg.Scatter(x=[sd3end, sd3end], y=[0, 1] , mode = "lines" , name = "standard deviation 3"))

fig.show()
