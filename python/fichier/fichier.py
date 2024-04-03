# echo-client.py

import pickle
import socket
import sys
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
time.sleep(1)



import json

with open('python\\fichier\\etoile.json') as mon_fichier:
    texte = json.load(mon_fichier)


nbligne=int(sys.argv[1])
Liste_horloge=[]
nbcolonne=int(sys.argv[2])
a=0


 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(0)
    while(1):
        if a<len(texte):
            i=texte[a]
            for j in i[1]:
                for t in j[0]:
                        Liste_horloge.append(((t[0],t[1]),j[1][0],j[1][1],j[1][2],j[1][3]))
            # Encodage de l'array en bytes avec pickle
            array_bytes = pickle.dumps(Liste_horloge)
            Liste_horloge=[]
            a=a+1
        # Envoi des données encodées
        s.sendall(array_bytes)
        time.sleep(i[0])
        try:
            data = s.recv(2048)
            print(f"Received {data!r}")
        except:
                # Gérer l'erreur de non-blocage
                pass
