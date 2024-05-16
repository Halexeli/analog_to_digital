"""Testeur de transitions; !!! faire marcher /horloge/simulateur.py avant.

Usage: 
  test_transition.py 
  test_transition.py [-h | --help]


Options:
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import socket
import time

from fonctions_cadre import *
import json
if __name__=='__main__':
    
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server
    time.sleep(1)

    Liste_horloge=[]


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(0)
        while(1):
            print("Quelle transition ?")
            m=input()
            with open(m) as fichier_transition:
                transition = json.load(fichier_transition)
            for step in transition:
                for element in step[1]:
                    for position in element[0]:
                        Liste_horloge.append(((position[0], position[1]),element[1][0],element[1][1],element[1][2],element[1][3]))
                array_bytes = pickle.dumps(Liste_horloge)
                Liste_horloge=[]
                s.sendall(array_bytes)
                time.sleep(step[0])
        try:
            data = s.recv(2048)
        except:
                # Gérer l'erreur de non-blocage
                pass
