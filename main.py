# import
import os
import json
import subprocess
import time


#Retourne sous forme d'un tableau toutes les valeurs associé à la clé en parametre
def getValueWithKey(key):
    value=[]

    #Parcours le tableau data chargé depuis le main
    for i in range(len(wd)):
        #Ajoute au tableau la valeur de la donnée entrée en paramètre
        temp=wd[i][key]
        value.append(temp)
    return value



#Retourne sous forme d'un tableau les valeurs associé à la clé, mais uniquement celles dont la
#valeur "enable" est à "true"
def getValueEnable(key):
    # chargement des tableaux dont un avec toutes les valeurs
    # de cles specifié et l'autre avec toutes les valeurs de "enable", tous deux ordonées
    names=getValueWithKey(key)
    enabled=getValueWithKey("enable")
    tabNameEnable=[]

    for i in range(len(names)):
        #Ajoute au tableau le valeur de la cles si le valeur du meme indice dans le
        # tableau enabled est "true"
        if(enabled[i]=="true"):
            tabNameEnable.append(names[i])
    return tabNameEnable




#launchprocess lance le processus en prennant en parametre son nom et le mot de passe sudo
# de l'utilisateur, il relancera le binary du processus qu'il retrouvera grace à son nom
def launchprocess(process, mdp):

    #Chargement de deux tableaux, l'un avec les noms et l'autre avec les "binary" du watchdog.conf
    tabWithName=getValueWithKey("Name")
    tabWithBin=getValueWithKey("binary")
    bin="null"

    for i in range (len(tabWithBin)):
        if tabWithName[i]==process:
            bin=tabWithBin[i]

    #Execute la commande bin en temps que sudo
    cmd= "echo "+ mdp +" |  sudo -S " + bin + " start"
    os.system(cmd)





# Demande le mot de passe sudo de l'utilisateur
def askPasswd():

    print("Veuillez entrer le mot de passe sudo : ")
    passwd=input()
    return passwd




#restartAllProcess parcours le tableau de tout les process qui doivent etre
# lancé et le compare avec le tableau des processus en cours d'excution,
# s'ils ne sont pas lancé, il les execute.
def restartAllProcess(tps,mdp):

    #Chargement respectif d'un taleau avec le nom des processus à surveiller,
    # des processus non lancé et du watchtime respectif de tout les processus à surveiller
    processToMonitor = getValueEnable("Name")
    tableTrue= getProcessDisable()
    allWatchtime= getValueEnable("watchtime")


    for i in range(len(processToMonitor)):

        for j in range(len(tableTrue)):

            regarderTemps= int(allWatchtime[i]) #convertion du la velaur du tableau allWatchtime en int
            tempo=int(tps) % regarderTemps #le modulo permet mettre a 0 le compteur toutes les x secondes du wathtime

            #Si le processus apparait dans le tableau de processus non lancé et que "tempo" et
            # à 0, il le relance
            if (tableTrue[j]==processToMonitor[i] and tempo==0):
                launchprocess(processToMonitor[i],mdp)
                tableTrue=getProcessDisable() #Actualisation du Tableau des processus non lancé




# removePos retourne sous forme d'un tableau tous les processus qui ne sont pas executé
def getProcessDisable():

    tabProcessTrue = getValueEnable("Name")
    # recuperation des processus
    ps = subprocess.check_output(['ps', 'eaxco', 'command'], text=True)
    # mise en place des process dans une liste
    process = ps.split('\n')

    # compare les valeurs pour resortir un tableau des processus non lancé
    for i in process:
        for j in tabProcessTrue:
            if j == i:
                tabProcessTrue.remove(j)

    return tabProcessTrue



#main
if __name__ == "__main__":
    #Chargement du Watchdog.conf sous forme d'un tableau data
    with open('watchdog.conf') as json_file:
        wd = json.load(json_file)

    #Récuperation du mot de passe sudo de l'utilisateur et initialisation du compteur
    passwd=askPasswd()
    cpt=0

    while True:
        cpt+=1  #Incrementation du compteur
        time.sleep(1) #Stop la boucle une seconde
        restartAllProcess(cpt, passwd) #Relance le processus si celui-ci n'est pas déjà éxécuté

    #fermeture du fichier Watchdog.conf
    json_file.close()
