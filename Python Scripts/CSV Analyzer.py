import matplotlib.pyplot as data
from collections import defaultdict
import csv
import sys
import os

print("------- Welcome to CSV Analyzer -------")
print("------------- Created by Harshit Aghera")
print("\n")

columns = defaultdict(list)             #define column to get column as list from .csv file

File = input("Give CSV File name :")
try :
    new = open(File +".csv",'r')
    add = csv.DictReader(new)
except :
    print("File not found")
    os.execl(sys.executable, sys.executable, *sys.argv)


for row in add :
    for (k,v) in row.items():           #to get column as list from .csv file
        columns[k].append(v)

Xaxis = input("Give X-axis Data : ")
Yaxis = input("Give Y-axis Data : ")

print("Do you want to set graph characteristics?")
temp = input("'Yes' or 'No' : ")

data.figure(1)

if temp == "Yes" :
    xl = input("Xaxis limit :")
    yl = input("Yaxis limit :")
    xlb = input("Xlable :")
    ylb = input("Ylable :")
    ttl = input("Graph title :")
    xl = xl.split(",")
    yl = yl.split(",")

    data.xlim(int(xl[0]),int(xl[1]))
    data.ylim(int(yl[0]),int(yl[1]))
    data.xlabel(xlb)
    data.ylabel(ylb)
    data.title(ttl)

data.plot(columns[Xaxis],columns[Yaxis],'b')
data.show()