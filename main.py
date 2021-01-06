# import
import time
import os
import json

# creation de fonction
def ask(answer):
    os.system('grep '+answer+' watchdog.conf | cut -d \\" -f 4')

def tab():


if __name__ == "__main__":
    # recuperation des process
    #os.system('ps eaxco command')
    # lecture du fichier conf voir qui est true ou false
    controle = ask("'enable'")
    #if controle ==

