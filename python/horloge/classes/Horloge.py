import pygame
from classes.Aiguille import Aiguille

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
    def __init__(self, pos_0=(0,0), rayon=100, butee=0,width=3):
        self.__pos_0=pos_0
        self.__aiguille_1=Aiguille(rayon*0.8)
        self.__aiguille_2=Aiguille(rayon*0.8)
        self.__rayon=rayon
        self.__width=width
        self.__butee=butee
    """
    Méthode set_aiguille :
    Permet de changer l'angle but des aiguilles
    - theta_1 : angle but de la première aiguille
    - theta_2 : angle but de la deuxième aiguille
    """
    def set_aiguille(self,theta_1,theta_2):
        if(self.__butee==1):
            self.__aiguille_1.set_aiguille(theta_1,1)
            self.__aiguille_2.set_aiguille(theta_2,1)
        else:
            self.__aiguille_1.set_aiguille(theta_1,0)
            self.__aiguille_2.set_aiguille(theta_2,0)

    """
    Méthode set_aig_tps :
    Permet de changer le tps des aiguilles
    - tps1 : tps de la première aiguille
    - tps2 : tps de la deuxième aiguille
    """
    def set_aig_tps(self,tps1,tps2):
        self.__aiguille_1.tps=tps1
        self.__aiguille_2.tps=tps2

    def set_aig_sens(self,s1,s2):
        self.__aiguille_1.sens=s1
        self.__aiguille_2.sens=s2

    """
    Méthode dessiner :
    Permet de dessiner l'horloge
    - screen : écran de la simulation
    """

    def dessiner(self, screen,couleur):
        pygame.draw.circle(screen, "black", self.__pos_0, self.__rayon,self.__width)
        self.__aiguille_1.dessiner_aiguille(self.__pos_0,screen,couleur)
        self.__aiguille_2.dessiner_aiguille(self.__pos_0,screen,couleur)