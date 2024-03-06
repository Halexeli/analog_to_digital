import math

import pygame

"""
Classe Aiguille  : 
    Permet de créer une aiguille pour une horloge
"""
class Aiguille():
    """
        Constructeur : 
        - goal_theta : angle but de l'aiguille
        - current_theta : angle actuel de l'aiguille
        - pas : distance parcourue en une "visualisation", 1 pas correspond a entre 62 et 63 degrées par secondes
        - taille : taille de l'aiguille
    """
    def __init__(self,taille=80):
        self.goal_theta=0 #but
        self.current_theta=0 #position actuelle
        self.pas=1 #distance parcourue en une "visualisation"
        self.taille=taille #taille de l'aiguille

    """
    Méthode dessiner_aiguille :
    Permet de dessiner l'aiguille
    - pos : position de l'aiguille
    - screen : écran de la simulat            if(t%500==0): # on change l'angle des aiguilles toutes les 500 frames
                # on change l'angle des aiguilles
                horloge.set_aiguille(horloge.aiguille_1.goal_theta-35,horloge.aiguille_2.goal_theta+45)
                # on change le pas des aiguilles
                horloge.aiguille_1.set_pas(horloge.aiguille_1.pas*-1)ion
    """
    def dessiner_aiguille(self, pos, screen):
        eps=self.goal_theta-self.current_theta #pour tester notre condition d'arrêt
        next_pas=self.pas # pour que l'arrêt soit fluide 
        if abs(eps)>=abs(self.pas):
            self.current_theta+=self.pas
            self.current_theta=self.current_theta%360 #l'aiguille avance, on avance current_theta
        elif abs(eps)!=0:
            next_pas=self.pas #pour que l'aiguile s'arrête exactement a la bonne position
            self.pas=eps
            self.current_theta+=self.pas
            self.current_theta=self.current_theta%360 #on avance current_theta
        pos1=(pos[0]+self.taille*math.cos(2*math.pi/360*self.current_theta),pos[1]+ self.taille*math.sin(2*math.pi/360*self.current_theta))
        pygame.draw.line(screen, "red", pos, pos1, 5 )
        self.pas=next_pas
