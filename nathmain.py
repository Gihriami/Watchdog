# import
import os
import json
import subprocess
import time

def getWithKey(key):
    b=[]
    for i in range(len(data)):
        temp=data[i][key]
        b.append(temp)
    return b

def checkIfTrue():
    names=getWithKey("Name")
    enabled=getWithKey("enable")
    tab=[]
    for i in range(len(names)):
        if(enabled[i]=="true"):
            tab.append(names[i])
    return tab

def getAllWatchtimeFromTrue():
    names = getWithKey("watchtime")
    enabled = getWithKey("enable")
    tab = []
    for i in range(len(names)):
        if (enabled[i] == "true"):
            tab.append(names[i])
    return tab

#launchprocess
def launchprocess(procss, mdp):

    tabName=getWithKey("Name")
    tabBin=getWithKey("binary")

    bin="null"
    for i in range (len(tabBin)):
        if tabName[i]==procss:
            bin=tabBin[i]

    cmd= "echo "+ mdp +" |  sudo -S " + bin + " start"
    os.system(cmd)

def askPasswd():
    print("Veuiilez entrer le mot de passe root : ")
    mdp=input()
    return mdp


def relanceAllProcess(tps,mdp):
    aRelancer = checkIfTrue()
    tabletTrue=removePros()
    allWatchtime=getAllWatchtimeFromTrue()
    temps="{:.0f}".format(tps)

    for i in range(len(aRelancer)):

        for j in range(len(tabletTrue)):
            regarderTemps= int(allWatchtime[i])
            tempo=int(temps) % regarderTemps
            if (tabletTrue[j]==aRelancer[i] and tempo==0):
                launchprocess(aRelancer[i],mdp)



def removePros():
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

    return tabletrue


if __name__ == "__main__":
    with open('watchdog.conf') as json_file:
        data = json.load(json_file)

    mdp=askPasswd()

    toc = time.perf_counter() % 3600
    while True:
        tic = time.perf_counter() % 3600 - toc + 1
        time.sleep(1)
        print("{:.0f}".format(tic))
        relanceAllProcess(tic, mdp)

    json_file.close()
