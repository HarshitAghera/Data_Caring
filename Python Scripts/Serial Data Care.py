import serial
import csv
import time
import os
import sys

print("----- Welcome to Serial Data Care -----")
print("------------- Created by Harshit Aghera")
print("\n")

port = input('Data Port = ')
timeout = float(input('Timeout = '))         #set timeout as required
try:
    DataSerial = serial.Serial(port,timeout=timeout)
except:
    print("Port not available")
    os.execl(sys.executable, sys.executable, *sys.argv)

print(DataSerial)
DataSerial.flush()

if DataSerial :
    print("Success")
    print("Do you want to name your file?")
    temp = input("'Yes' or 'No' : ")

    if temp == "Yes" :
        tm = input("Give CSV file name : ")
        DataFileName = tm + ".csv"
    else :
        tm = time.strftime("%d %b %Y_%H-%M", time.localtime())
        DataFileName = tm + "_Data.csv"



print("Give titles of value in sequence :")
FieldNames = []
for i in range(int(input("Number of values :"))) :
    FieldNames.append(input("Value " + str(i) + " :"))

print("Value list : " + str(FieldNames))

ignore = int(input("Give Number of first bytes to ignore :"))
Dataline = []
DataList = []

try :
    while (DataSerial.isOpen()) :           #read lines from serial port
        line = str(DataSerial.readline(),'utf-8')
        print(line)
        Dataline.append(line)

except :
    print("Disconnected")
    DataSerial.close()

    lines = open(str(DataFileName),'w')     #create .csv file
    Data = csv.DictWriter(lines ,delimiter=',',fieldnames=FieldNames,lineterminator='\n')
    Data.writeheader()


    Data = csv.writer(lines ,delimiter=',',lineterminator='\n')
    for item in Dataline :
        Data_line = str(item[ignore:-1])                 #remove first five and last '\n'
        DataList = str(Data_line).split(",")
        print(DataList)
        Data.writerow(DataList)      #write .csv file





