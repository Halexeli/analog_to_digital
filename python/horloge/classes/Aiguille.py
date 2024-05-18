import math

import pygame

tick_en_degres=1/12

vitesse=62.5*(1/tick_en_degres)



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
        - pas = 1/(tps*62,5) : distance parcourue (a 0,5 degree près) en une "visualisation", 1 pas correspond au fait qu'on a entre 62 et 63 frames par secondes afin de parcourir la distance tick_en_degrees en 62.5 frames
        - taille : taille de l'aiguille
    """
    def __init__(self,taille=80):
        self.goal_theta=0 #but
        self.__current_theta=0 #position actuelle
        self.tps=0.02 #distance parcourue en une "visualisation"
        self.__taille=taille #taille de l'aiguille
        self.sens=1
        self.__butee_flag=0

    """
    Méthode dessiner_aiguille :
    Permet de dessiner l'aiguille
    - pos : position de l'aiguille
    - screen : écran de la simulation
    """
    def dessiner_aiguille(self, pos, screen,couleur):
        eps=(self.goal_theta-self.__current_theta)%360 #pour tester notre condition d'arrêt
        next_tps=self.tps*self.sens # pour que l'arrêt soit fluide 
        if abs(eps)>=abs(1/(self.tps*vitesse*self.sens)):
            self.__current_theta+=1/(self.tps*vitesse*self.sens)
            self.__current_theta=self.__current_theta%360 #l'aiguille avance, on avance current_theta
        elif abs(eps)!=0:
            next_tps=self.tps*self.sens #pour que l'aiguile s'arrête exactement a la bonne position
            self.tps=abs(1/(eps*vitesse))
            self.__current_theta+=1/(self.tps*vitesse)
            self.__current_theta=self.__current_theta%360 #on avance current_theta
        pos1=(pos[0]+self.__taille*math.cos(2*math.pi/360*self.__current_theta),pos[1]+ self.__taille*math.sin(2*math.pi/360*self.__current_theta))
        pygame.draw.line(screen, couleur, pos, pos1, 5 )
        self.tps=abs(next_tps)

    def set_aiguille(self,theta,butee):
        if(butee==1):
            if (self.sens==1):
                if(self.__butee_flag==1):
                    self.goal_theta=0
                    self.__butee_flag=1
                else:
                    if(self.goal_theta< theta%360):
                        if(theta==0):
                            self.goal_theta=0
                            self.__butee_flag=1
                        else:
                            self.goal_theta=theta%360
                            self.__butee_flag=0
                    elif(self.goal_theta== theta%360):
                        self.goal_theta=self.goal_theta
                        self.__butee_flag=self.__butee_flag
                    else:
                        self.goal_theta=0
                        self.__butee_flag=1
            else:
                if(self.__butee_flag==-1):
                    self.goal_theta=0
                    self.__butee_flag=-1
                else:
                    if(self.goal_theta>theta%360):
                        if(theta==0):
                            self.goal_theta=0
                            self.__butee_flag=-1
                        else:
                            self.goal_theta=theta%360
                            self.__butee_flag=0
                    elif(self.goal_theta== theta%360):
                        self.goal_theta=self.goal_theta
                        self.__butee_flag=self.__butee_flag
                    else:
                        self.goal_theta=0
                        self.__butee_flag=-1
        else:
            self.goal_theta=theta%360
