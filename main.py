# import
import time
import os
import json


# creation de fonction
def ask(answer):
    response = os.system('grep ' + answer + ' watchdog.conf | cut -d \\" -f 4')
    return response


def getsize():
    os.system('grep Name watchdog.conf | cut -d \\" -f 4 | wc -l')


if __name__ == "__main__":
    # recuperation des process
    # os.system('ps eaxco command')
    # lecture du fichier conf voir qui est true ou false
    # controle = ask("'enable'")
    # if controle ==
    controleName = ask("'Name'")
    controleValue = ask("'enable'")
    sizelist = getsize()

    # 1e étape
    liste1 = []
    liste2 = []

    # 2e étape
    for i in range(2):
        liste1.append(controleName)

    # 3e étape
    print("Your first list : ", liste1)

    # def myfunc(a, b):
    #   return a + b

#  print(liste1)
# print(liste2)

# x = map(myfunc, liste1, liste2)

# print(x)

# convert the map into a list, for readability:
# print(list(x))
