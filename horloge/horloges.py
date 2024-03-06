import math
import sys
from datetime import datetime

import numpy as np
import pygame
from horloge import Horloge
from Aiguille import Aiguille

# pygame setup

# On récupère les arguments passés à notre programme (hauteur, largeur, nbligne, nbcolonne)
hauteur=int (sys.argv[1])
largeur=int (sys.argv[2])
nbligne=int(sys.argv[3])
nbcolonne=int(sys.argv[4])

# On initialise pygame et on crée un écran de largeur et hauteur données en argument
pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
# On crée une horloge
clock = pygame.time.Clock()
running = True # on initialise une variable pour savoir si le programme est en cours d'exécution
dt = 0 # on initialise un delta time
i=0 # on initialise des compteurs
j=0
a=(largeur-20)/ nbcolonne # on calcule la largeur d'une horloge
b=(hauteur-20) / nbligne # on calcule la hauteur d'une horloge
ray=min(a,b)*0.45 # on calcule le rayon de l'horloge
Liste_horloge=[] # on initialise une liste pour stocker les horloges
for i in range(nbcolonne):
    Liste_horloge2=[]  # on initialise une liste pour stocker les horloges pour faire la matrice
    for j in range(nbligne): 
        horloge=Horloge((i*a + a/2 +10,j*b + b/2 +10), ray) # on crée une horloge
        horloge.set_aiguille(359,359) # on initialise les aiguilles
        horloge.set_aig_pas(1,1) # on initialise les pas des aiguilles
        Liste_horloge2.append(horloge) # on ajoute l'horloge à la liste
    Liste_horloge.append(Liste_horloge2) # on ajoute à la liste.

t=0
while running: # tant que le programme est en cours d'exécution
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
            if horloge.aiguille_1.current_theta==189:
                print(t)
                horloge.set_aiguille(180,180)
            
    #print(player_pos)
    # flip() le display pour afficher sur l'écran
    pygame.display.flip()
    # limiter le framerate à 60fps
    # dt = delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick_busy_loop(60) / 1000 #nombre de secondes depuis le dernier appel de tick
    t=t+dt
    
pygame.quit()