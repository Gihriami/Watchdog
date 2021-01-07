# import
import os
import json

with open('watchdog.conf') as json_file:
    data = json.load(json_file)


def getWithKey(key):
    b=[]
    for i in range(len(data)):
        #print(data[i][key])
        temp=data[i][key]
        #print(temp)
        b.append(temp)
    return b

#a=getWithKey("Name")

#for i in range(len(a)):
#    print(a[i])

def checkIfTrue():
    names=getWithKey("Name")
    enabled=getWithKey("enable")
    tab=[]
    for i in range(len(names)):
        if(enabled[i]=="true"):
            tab.append(names[i])
    return tab

tableau=checkIfTrue()

for i in range(len(tableau)):
    print(tableau[i])


json_file.close()
