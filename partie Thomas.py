# import
import time
import os
import json
import subprocess

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

