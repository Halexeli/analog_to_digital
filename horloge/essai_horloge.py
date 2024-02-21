import math
from datetime import datetime

import pygame


class Aiguille():
    def __init__(self):
        self.theta=0
        self.theta_int=0
        self.pas=1

    def set_theta(self,theta):
        self.theta=theta

    def set_theta_int(self):
        self.theta_int+=self.pas

    def dessiner_aiguille(self, pos, screen):
        pos1=(pos[0]+80*math.cos(2*math.pi/360*self.theta_int),pos[1]+ 80*math.sin(2*math.pi/360*self.theta_int))
        pygame.draw.line(screen, "red", pos, pos1, 5 )
        if self.theta!=self.theta_int:
            self.set_theta_int()

    def set_pas(self,pas):
        self.pas=pas

class Horloge():
    def __init__(self, pos_0=(0,0)):
        self.pos_0=pos_0
        self.aiguille_1=Aiguille()
        self.aiguille_2=Aiguille()

    def set_aiguille(self,theta_1,theta_2):
        self.aiguille_1.set_theta(theta_1)
        self.aiguille_2.set_theta(theta_2)

    def set_aig_pas(self,pas1,pas2):
        self.aiguille_1.set_pas(pas1)
        self.aiguille_2.set_pas(pas2)


    def dessiner(self, screen,rayon=100,width=5):
        pygame.draw.circle(screen, "black", self.pos_0, rayon, width)
        self.aiguille_1.dessiner_aiguille(self.pos_0,screen)
        self.aiguille_2.dessiner_aiguille(self.pos_0,screen)








