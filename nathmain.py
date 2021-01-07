# import
import os
import json

with open('watchdog.conf') as json_file:
    data = json.load(json_file)


def getWithKey(key):
    for i in range(len(data)):
        print(data[i][key])

getWithKey("Name")

json_file.close()
