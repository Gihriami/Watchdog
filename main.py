# import
import os
import json
import subprocess

with open('watchdog.conf') as json_file:
    data = json.load(json_file)


def getWithKey(key):
    b = []
    for i in range(len(data)):
        temp = data[i][key]
        b.append(temp)
    return b


def checkIfTrue():
    names = getWithKey("Name")
    enabled = getWithKey("enable")
    tab = []
    for i in range(len(names)):
        if enabled[i] == "true":
            tab.append(names[i])
    return tab

if __name__ == "__main__":
    tabletrue = checkIfTrue()
    # recuperation des process
    ps = subprocess.check_output(['ps', 'eaxco', 'command'], text=True)

    # mise en place des process dans une liste
    process = ps.split('\n')

    # compare les valeurs pour resortir
    for pro in process:
        for valeur in tabletrue:
            if valeur == pro:
                tabletrue.remove(valeur)

    
    json_file.close()
