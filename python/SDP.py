import csv
import math 

with open('data.csv', newline='')as f:
    reader = csv.reader(f)
    datalist = list(reader)

data = datalist[0]

def mean(data):
    length = len(data)
    total = 0

    for i in data:
        total = total+int(i)
    
    mean = total/length
    return mean

squares = []

for a in data:
    meandif = int(a)-mean(data)
    meandif = meandif**2
    squares.append(meandif)

meansum = 0

for b in squares:
    meansum = meansum + b

ans = meansum/(len(data)-1)
SD = math.sqrt(ans)
print(SD)