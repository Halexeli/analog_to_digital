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
import threading
import time
from datetime import datetime
from queue import Queue

from classes.Tableau import Tableau
from docopt import docopt


def get_name():
    while(1):
        name = input("Nom de fichier? ")
        butee = input("butee? ")
        name_queue.put([name,int(butee)]) 

if __name__=='__main__':
    arguments = docopt(__doc__, version='Simulateur 1.0')
    butee=int(arguments['<butee>'])
    nom_fichier="./parametres/"+str(arguments['<nom_fichier>'])

    HOST = "127.0.0.1"  
    PORT = 65432  
    time.sleep(1)

    tab=Tableau(nom_fichier, butee)

    last_time = datetime.fromtimestamp(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.setblocking(0)
        tab.envoi_nb_horloge(s)
        name_queue = Queue()
        input_thread = threading.Thread(target=get_name)
        input_thread.start()
        while(1):
            if not name_queue.empty():
                name = input_thread.name  # Get the name from the thread's name attribute
                name = name_queue.get()  # Reset the event for future use
                tab=Tableau("./parametres/"+name[0], name[1])
                last_time = datetime.fromtimestamp(0)
                tab.envoi_nb_horloge(s)
            current_time = datetime.now()
            if(current_time.strftime("%H:%M")!=tab.chiffres.current_time.strftime("%H:%M")):
                if(current_time.strftime("%H")!=tab.chiffres.current_time.strftime("%H")):
                    tab.execute_transition_heure(s)
                else:
                    tab.execute_transition_minute(s)
                tab.chiffres.set_heure(current_time) 
                tab.execute_chiffres(s)
            try:
                data = s.recv(2048)
            except:
                pass
