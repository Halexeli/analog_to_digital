import math
import pickle
import socket
import subprocess
import sys
import time
from threads import MonThread
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

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
# pygame setup



# On initialise pygame et on crée un écran de largeur et hauteur données en argument
pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
# On crée une horloge pour pygame
clock = pygame.time.Clock()
running = True # on initialise une variable pour savoir si le programme est en cours d'exécution
dt = 0 # on initialise un delta time

a=(largeur-20)/ nbcolonne #on calcule la largeur possible
b=(hauteur-20)/nbligne # on calcule la hauteur possible d'une horloge
if a>b:
    lar=0 #si la largeur est plus grande que la hauteur
else:
    lar=1 #inverse
ray=min(a,b)*0.45 # on calcule le rayon de l'horloge

#pour la matrice d'horloges
Liste_horloge=[] # on initialise une liste pour stocker les horloges
for i in range(nbcolonne):
    Liste_horloge2=[]  # on initialise une liste pour stocker les horloges pour faire la matrice
    for j in range(nbligne): 
        if lar:
            horloge=Horloge((i*a + a/2 +10,j*a + a/2 +10+(b-a)/2*nbligne), ray) # on crée une horloge centré avec le meme espace entre elles
        else:
            horloge=Horloge((i*b + b/2 +10+(a-b)/2*nbcolonne,j*b + b/2 +10), ray) # on crée une horloge
        Liste_horloge2.append(horloge) # on ajoute l'horloge à la liste
    Liste_horloge.append(Liste_horloge2) # on ajoute à j=0 la liste.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    conn.setblocking(0)
    with conn:
        while running: # tant que le programme est en cours d'exécution
            try:
                data = conn.recv(4096)
                if data:
                    # Si des données ont été reçues, les traiter
                    print("ok")
                    datarecup=pickle.loads(data)
                    print(datarecup)
                    for i in datarecup:
                            pos,t1,t2,p1,p2=i
                            print(t1)
                            print(t2)
                            colonne,ligne=pos
                            (Liste_horloge[colonne][ligne]).set_aiguille(t1, t2)
                            (Liste_horloge[colonne][ligne]).set_aig_tps(p1, p2)
                            #print(Liste_horloge[colonne][ligne])
                    conn.sendall(b'1')
            except:
                # Gérer l'erreur de non-blocage
                pass

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
                    horloge.dessiner(screen,couleur="blue")

            pygame.display.flip()
            # limiter le framerate à 60fps
            # dt = delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick_busy_loop(60) / 1000 #nombre de secondes depuis le dernier appel de tick

    
pygame.quit()