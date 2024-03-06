import math

import pygame

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
        self.aiguille_1.set_goal_theta(theta_1)
        self.aiguille_2.set_goal_theta(theta_2)

    """
    Méthode set_aig_pas :
    Permet de changer le pas des aiguilles
    - pas1 : pas de la première aiguille
    - pas2 : pas de la deuxième aiguille
    """
    def set_aig_pas(self,pas1,pas2):
        self.aiguille_1.set_pas(pas1)
        self.aiguille_2.set_pas(pas2)
    """
    Méthode dessiner :
    Permet de dessiner l'horloge
    - screen : écran de la simulation
    """

    def dessiner(self, screen):
        pygame.draw.circle(screen, "black", self.pos_0, self.rayon,self.width)
        self.aiguille_1.dessiner_aiguille(self.pos_0,screen)
        self.aiguille_2.dessiner_aiguille(self.pos_0,screen)






