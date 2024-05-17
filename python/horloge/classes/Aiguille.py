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
        - tps : temps d'attente entre chaque pas du moteur
        - pas = 1/(tps*62,5) : distance parcourue (a 0,5 degree près) en une "visualisation", 1 pas correspond a entre 62 et 63 degrées par secondes
        - taille : taille de l'aiguille
    """
    def __init__(self,taille=80):
        self.goal_theta=0 #but
        self.current_theta=0 #position actuelle
        self.tps=0.02 #distance parcourue en une "visualisation"
        self.taille=taille #taille de l'aiguille
        self.sens=1
        self.butee_flag=0

    """
    Méthode dessiner_aiguille :
    Permet de dessiner l'aiguille
    - pos : position de l'aiguille
    - screen : écran de la simulation
    """
    def dessiner_aiguille(self, pos, screen,couleur):
        eps=self.goal_theta-self.current_theta #pour tester notre condition d'arrêt
        next_tps=self.tps*self.sens # pour que l'arrêt soit fluide 
        if abs(eps)>=abs(1/(self.tps*62.5*self.sens)):
            self.current_theta+=1/(self.tps*62.5*self.sens)
            self.current_theta=self.current_theta%360 #l'aiguille avance, on avance current_theta
        elif abs(eps)!=0:
            next_tps=self.tps*self.sens #pour que l'aiguile s'arrête exactement a la bonne position
            self.tps=abs(1/(eps*62.5))
            self.current_theta+=1/(self.tps*62.5)
            self.current_theta=self.current_theta%360 #on avance current_theta
        pos1=(pos[0]+self.taille*math.cos(2*math.pi/360*self.current_theta),pos[1]+ self.taille*math.sin(2*math.pi/360*self.current_theta))
        pygame.draw.line(screen, couleur, pos, pos1, 5 )
        self.tps=abs(next_tps)
