import math
from datetime import datetime

import pygame

from essai_horloge import Horloge

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
i=0
j=0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2= (player_pos[0], player_pos[1]-80)
horloge=Horloge(player_pos)
horloge.set_aiguille(45,90)
horloge.set_aig_pas(1,0.5)


while running:
    i=i+0.5
    j=j+1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    horloge.dessiner(screen)
    print(player_pos)



   
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    

pygame.quit()