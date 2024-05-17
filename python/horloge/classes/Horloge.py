import math

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
        self.pos_0=pos_0
        self.aiguille_1=Aiguille(rayon*0.8)
        self.aiguille_2=Aiguille(rayon*0.8)
        self.rayon=rayon
        self.width=width
        self.butee=butee
    """
    Méthode set_aiguille :
    Permet de changer l'angle but des aiguilles
    - theta_1 : angle but de la première aiguille
    - theta_2 : angle but de la deuxième aiguille
    """
    def set_aiguille(self,theta_1,theta_2):
        if(self.butee==1):
            if (self.aiguille_1.sens==1):
                if(self.aiguille_1.butee_flag==1):
                    self.aiguille_1.goal_theta=0
                    self.aiguille_1.butee_flag=1
                else:
                    if(self.aiguille_1.goal_theta< theta_1%360):
                        if(theta_1==0):
                            self.aiguille_1.goal_theta=0
                            self.aiguille_1.butee_flag=1
                        else:
                            self.aiguille_1.goal_theta=theta_1%360
                            self.aiguille_1.butee_flag=0
                    elif(self.aiguille_1.goal_theta== theta_1%360):
                        self.aiguille_1.goal_theta=self.aiguille_1.goal_theta
                        self.aiguille_1.butee_flag=self.aiguille_1.butee_flag
                    else:
                        self.aiguille_1.goal_theta=0
                        self.aiguille_1.butee_flag=1
            else:
                if(self.aiguille_1.butee_flag==-1):
                    self.aiguille_1.goal_theta=0
                    self.aiguille_1.butee_flag=-1
                else:
                    if(self.aiguille_1.goal_theta>theta_1%360):
                        if(theta_1==0):
                            self.aiguille_1.goal_theta=0
                            self.aiguille_1.butee_flag=-1
                        else:
                            self.aiguille_1.goal_theta=theta_1%360
                            self.aiguille_1.butee_flag=0
                    elif(self.aiguille_1.goal_theta== theta_1%360):
                        self.aiguille_1.goal_theta=self.aiguille_1.goal_theta
                        self.aiguille_1.butee_flag=self.aiguille_1.butee_flag
                    else:
                        self.aiguille_1.goal_theta=0
                        self.aiguille_1.butee_flag=-1
            if (self.aiguille_2.sens==1):
                if(self.aiguille_2.butee_flag==1):
                    self.aiguille_2.goal_theta=0
                    self.aiguille_2.butee_flag=1
                else:
                    if(self.aiguille_2.goal_theta< theta_2%360):
                        if(theta_2==0):
                            self.aiguille_2.goal_theta=0
                            self.aiguille_2.butee_flag=1
                        else:
                            self.aiguille_2.goal_theta=theta_2%360
                            self.aiguille_2.butee_flag=0
                    elif(self.aiguille_2.goal_theta== theta_2%360):
                        self.aiguille_2.goal_theta=self.aiguille_2.goal_theta
                        self.aiguille_2.butee_flag=self.aiguille_2.butee_flag
                    else:
                        self.aiguille_2.goal_theta=0
                        self.aiguille_2.butee_flag=1
            else:
                if(self.aiguille_2.butee_flag==-1):
                    self.aiguille_2.goal_theta=0
                    self.aiguille_2.butee_flag=-1
                else:
                    if(self.aiguille_2.goal_theta>theta_2%360):
                        if(theta_2==0):
                            self.aiguille_2.goal_theta=0
                            self.aiguille_2.butee_flag=-1
                        else:
                            self.aiguille_2.goal_theta=theta_2%360
                            self.aiguille_2.butee_flag=0
                    elif(self.aiguille_2.goal_theta== theta_2%360):
                        self.aiguille_2.goal_theta=self.aiguille_2.goal_theta
                        self.aiguille_2.butee_flag=self.aiguille_2.butee_flag
                    else:
                        self.aiguille_2.goal_theta=0
                        self.aiguille_2.butee_flag=-1
        else:
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

    def set_aig_sens(self,s1,s2):
        self.aiguille_1.sens=s1
        self.aiguille_2.sens=s2

    """
    Méthode dessiner :
    Permet de dessiner l'horloge
    - screen : écran de la simulation
    """

    def dessiner(self, screen,couleur):
        pygame.draw.circle(screen, "black", self.pos_0, self.rayon,self.width)
        self.aiguille_1.dessiner_aiguille(self.pos_0,screen,couleur)
        self.aiguille_2.dessiner_aiguille(self.pos_0,screen,couleur)