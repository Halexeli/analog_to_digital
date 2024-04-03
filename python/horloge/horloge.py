import math

import pygame
from Aiguille import Aiguille

""" 
    Classe Horloge :
    Permet de créer une horloge
    """
class Horloge():
    """Constructeur:
        - pos_0 : position du centre de l'horloge
        - rayon : rayon de l'horloge
        - width : largeur de l'horloge
    """
    def __init__(self, pos_0=(0,0), rayon=100, width=3):
        self.pos_0=pos_0
        self.aiguille_1=Aiguille(rayon*0.8)
        self.aiguille_2=Aiguille(rayon*0.8)
        self.rayon=rayon
        self.width=width
    """
    Méthode set_aiguille :
    Permet de changer l'angle but des aiguilles
    - theta_1 : angle but de la première aiguille
    - theta_2 : angle but de la deuxième aiguille
    """
    def set_aiguille(self,theta_1,theta_2):
        self.aiguille_1.goal_theta=theta_1%360
        self.aiguille_2.goal_theta=theta_2%360

    """
    Méthode set_aig_tps :
    Permet de changer le tps des aiguilles
    - tps1 : tps de la première aiguille
    - tps2 : tps de la deuxième aiguille
    """
    def set_aig_tps(self,tps1,tps2):
        self.aiguille_1.tps=tps1
        self.aiguille_2.tps=tps2
    """
    Méthode dessiner :
    Permet de dessiner l'horloge
    - screen : écran de la simulation
    """

    def dessiner(self, screen,couleur):
        pygame.draw.circle(screen, "black", self.pos_0, self.rayon,self.width)
        self.aiguille_1.dessiner_aiguille(self.pos_0,screen,couleur)
        self.aiguille_2.dessiner_aiguille(self.pos_0,screen,couleur)