import math
import sys
from datetime import datetime

import numpy as np
import pygame
from Horloge import Horloge
from Aiguille import Aiguille

# pygame setup

hauteur=int (sys.argv[1])
largeur=int (sys.argv[2])
nbligne=int(sys.argv[3])
nbcolonne=int(sys.argv[4])

pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()
running = True
dt = 0
i=0
j=0
a=(largeur-20)/ nbcolonne
b=(hauteur-20) / nbligne
ray=min(a,b)*0.45
Liste_horloge=[]
for i in range(nbcolonne):
    Liste_horloge2=[]
    for j in range(nbligne):
        horloge=Horloge((i*a + a/2 +10,j*b + b/2 +10), ray)
        horloge.set_aiguille(45,90)
        horloge.set_aig_pas(1,0.5)
        Liste_horloge2.append(horloge)
    Liste_horloge.append(Liste_horloge2)

t=0
while running:
    now=datetime.now().time()

    t=t+1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    for i in range(nbcolonne):
        for j in range(nbligne):
            horloge=Liste_horloge[i][j]
            horloge.dessiner(screen)
            if(t%500==0):
                horloge.set_aiguille(horloge.aiguille_1.goal_theta-35,horloge.aiguille_2.goal_theta+45)
                horloge.aiguille_1.set_pas(horloge.aiguille_1.pas*-1)
            
    #print(player_pos)



   
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    

pygame.quit()