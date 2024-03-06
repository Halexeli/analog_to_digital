import math
import pickle
import socket
import subprocess
import sys
import time
from datetime import datetime

import numpy as np
import pygame
from Aiguille import Aiguille

from horloge import Horloge

# On récupère les arguments passés à notre programme (hauteur, largeur, nbligne, nbcolonne)
hauteur=int (sys.argv[1])
largeur=int (sys.argv[2])
nbligne=int(sys.argv[3])
nbcolonne=int(sys.argv[4])
url="./horloge/main.py"
subprocess.Popen(["/opt/homebrew/bin/python3",url, str(nbligne), str(nbcolonne)]) 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
# pygame setup



# On initialise pygame et on crée un écran de largeur et hauteur données en argument
pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
# On crée une horloge
clock = pygame.time.Clock()
running = True # on initialise une variable pour savoir si le programme est en cours d'exécution
dt = 0 # on initialise un delta time
i=0 # on initialise des compteurs
j=0
a=(largeur-20)/ nbcolonne #on calcule la largeur possible
b=(hauteur-20)/nbligne # on calcule la hauteur possible d'une horloge
if a>b:
    lar=0 #si la largeur est plus grande que la hauteur
else:
    lar=1 #inverse
ray=min(a,b)*0.45 # on calcule le rayon de l'horloge
Liste_horloge=[] # on initialise une liste pour stocker les horloges
for i in range(nbcolonne):
    Liste_horloge2=[]  # on initialise une liste pour stocker les horloges pour faire la matrice
    for j in range(nbligne): 
        if lar:
            horloge=Horloge((i*a + a/2 +10,j*a + a/2 +10+(b-a)/2*nbligne), ray) # on crée une horloge centré avec le meme espace entre elles
        else:
            horloge=Horloge((i*b + b/2 +10+(a-b)/2*nbcolonne,j*b + b/2 +10), ray) # on crée une horloge
        horloge.set_aiguille(359,359) # on initialise les aiguilles
        horloge.set_aig_pas(1,1) # on initialise les pas des aiguilles
        Liste_horloge2.append(horloge) # on ajoute l'horloge à la liste
    Liste_horloge.append(Liste_horloge2) # on ajoute à la liste.

t=0





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    conn.setblocking(0)
    with conn:
        while running: # tant que le programme est en cours d'exécution
            try:
                data = conn.recv(1024)
                if data:
                    # Si des données ont été reçues, les traiter
                    print("Données reçues :", pickle.loads(data))
                    datarecup=pickle.loads(data)
                    for i in range(nbcolonne):
                        for j in range(nbligne):
                            print("on est avant for\n")
                            (Liste_horloge[i][j]).set_aiguille(datarecup[i][j]["theta_1"], datarecup[i][j]["theta_2"])
                            (Liste_horloge[i][j]).set_aig_pas(datarecup[i][j]["pas1"], datarecup[i][j]["pas2"])
                            print("on est dans for\n")
                    conn.sendall(b'1')
                else:
                    # Si aucune donnée n'a été reçue
                    print("Aucune donnée disponible pour le moment")
                
            except:
                # Gérer l'erreur de non-blocage
                pass
            now=datetime.now().time() # on récupère l'heure actuelle

            # on parcourt tous les événements qui ont eu lieu
            # pygame.QUIT = l'utilisateur a cliqué sur X pour fermer la fenêtre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # fill l'ecran avec une couleur pour effacer les frames précédents
            screen.fill("white")
            for i in range(nbcolonne):
                for j in range(nbligne):
                    horloge=Liste_horloge[i][j] # on récupère l'horloge
                    horloge.dessiner(screen) # on dessine l'horloge
                    
            #print(player_pos)
            # flip() le display pour afficher sur l'écran
            pygame.display.flip()
            # limiter le framerate à 60fps
            # dt = delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick_busy_loop(60) / 1000 #nombre de secondes depuis le dernier appel de tick
            t=t+dt
    
pygame.quit()