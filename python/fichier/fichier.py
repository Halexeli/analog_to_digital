# echo-client.py

import pickle
import socket
import sys
import time
from datetime import datetime

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
time.sleep(1)



import json

with open('transition1.json') as transition:
    transition = json.load(transition)
with open(transition["fichier_chiffre_name"]) as fichier_chiffre:
    chiffre = json.load(fichier_chiffre)
with open(transition["fichier_cadre_name"]) as fichier_cadre:
    cadre = json.load(fichier_cadre)
with open(transition["fichier_transition_minute"]) as fichier_transition_minute:
    transition_minute = json.load(fichier_transition_minute)
with open(transition["fichier_transition_heure"]) as fichier_transition_heure:
    transition_heure = json.load(fichier_transition_heure)
heure_dizaine_delta_ligne=transition["init_position_chiffre"][0]
heure_dizaine_delta_colonne=transition["init_position_chiffre"][1]
heure_unite_delta_ligne=transition["init_position_chiffre"][2]
heure_unite_delta_colonne=transition["init_position_chiffre"][3]
minute_dizaine_delta_ligne=transition["init_position_chiffre"][4]
minute_dizaine_delta_colonne=transition["init_position_chiffre"][5]
minute_unite_delta_ligne=transition["init_position_chiffre"][6]
minute_unite_delta_colonne=transition["init_position_chiffre"][7]

Liste_horloge=[]
last_time = datetime.fromtimestamp(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.setblocking(0)
    while(1):
        current_time = datetime.now()
        if(current_time.strftime("%H:%M")!=last_time.strftime("%H:%M")):
            current_time_str_heure=str(current_time.strftime("%H"))
            heure_dizaine=chiffre[current_time_str_heure[0]]
            heure_unite=chiffre[current_time_str_heure[1]]
            current_time_str_minute=str(current_time.strftime("%M"))
            minute_dizaine=chiffre[current_time_str_minute[0]]
            minute_unite=chiffre[current_time_str_minute[1]]
            if(current_time.strftime("%H")!=last_time.strftime("%H")):
                for step in transition_heure:
                    for element in step[1]:
                        for position in element[0]:
                            Liste_horloge.append(((position[0], position[1]),element[1][0],element[1][1],element[1][2],element[1][3]))
                    array_bytes = pickle.dumps(Liste_horloge)
                    Liste_horloge=[]
                    s.sendall(array_bytes)
                    time.sleep(step[0])
            else:
                for step in transition_minute:
                    for element in step[1]:
                        for position in element[0]:
                            Liste_horloge.append(((position[0], position[1]),element[1][0],element[1][1],element[1][2],element[1][3]))
                    array_bytes = pickle.dumps(Liste_horloge)
                    print(Liste_horloge)
                    Liste_horloge=[]
                    s.sendall(array_bytes)
                    time.sleep(step[0])
            for element in heure_dizaine:
                for position in element[0]:
                    Liste_horloge.append(((position[1]+heure_dizaine_delta_colonne, position[0]+heure_dizaine_delta_ligne),element[1][0],element[1][1],element[1][2],element[1][3]))
            for element in heure_unite:
                for position in element[0]:
                    Liste_horloge.append(((position[1]+heure_unite_delta_colonne, position[0]+heure_unite_delta_ligne),element[1][0],element[1][1],element[1][2],element[1][3]))
            for element in minute_dizaine:
                for position in element[0]:
                    Liste_horloge.append(((position[1]+minute_dizaine_delta_colonne, position[0]+minute_dizaine_delta_ligne),element[1][0],element[1][1],element[1][2],element[1][3]))
            for element in minute_unite:
                for position in element[0]:
                    Liste_horloge.append(((position[1]+minute_unite_delta_colonne, position[0]+minute_unite_delta_ligne),element[1][0],element[1][1],element[1][2],element[1][3]))
            for element in cadre:
                for position in element[0]:
                    Liste_horloge.append(((position[1], position[0]),element[1][0],element[1][1],element[1][2],element[1][3]))
            array_bytes = pickle.dumps(Liste_horloge)
            Liste_horloge=[]
            s.sendall(array_bytes)
            last_time=current_time
        try:
            data = s.recv(2048)
        except:
                # Gérer l'erreur de non-blocage
                pass


