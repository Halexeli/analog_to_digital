"""ficher d horloges.

Usage: 
  fichier.py <nom_fichier> <butee> 
  fichier.py [-h | --help]
  fichier.py --version


Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import socket
import time
from datetime import datetime

from classes.Tableau import Tableau
from docopt import docopt

if __name__=='__main__':
    arguments = docopt(__doc__, version='Simulateur 1.0')
    butee=int(arguments['<butee>'])
    nom_fichier="./parametres/"+str(arguments['<nom_fichier>'])
    HOST = "127.0.0.1"  
    PORT = 65432  
    time.sleep(1)

    #on crée le tableau
    tab=Tableau(nom_fichier, butee)

    #on initialise le temps
    last_time = datetime.fromtimestamp(0)

    #on se connecte au serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(0)
        while(1): 
            current_time = datetime.now()
            if(current_time.strftime("%H:%M")!=tab.chiffres.current_time.strftime("%H:%M")): #si l'heure a changé
                if(current_time.strftime("%H")!=tab.chiffres.current_time.strftime("%H")):
                    tab.execute_transition_heure(s)#on execute la transition d'heure
                else:
                    tab.execute_transition_minute(s)#on execute la transition de minute sinon
                tab.chiffres.set_heure(current_time) #on met à jour l'heure
                tab.execute_chiffres(s)#on execute les chiffres
            try:
                data = s.recv(2048) #on reçoit les données
            except:
                pass #si on a rien reçu, on ne fait rien
