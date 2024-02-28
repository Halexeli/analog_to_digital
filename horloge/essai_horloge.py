import math

import pygame


class Aiguille():
    def __init__(self,taille=80):
        self.goal_theta=0 #but
        self.current_theta=0 #position actuelle
        self.pas=1 #distance parcourue en une "visualisation"
        self.taille=taille #taille de l'aiguille

    def set_goal_theta(self,theta):
        self.goal_theta=theta%360 

    def set_current_theta(self):
        self.current_theta+=self.pas
        self.current_theta=self.current_theta%360

    def dessiner_aiguille(self, pos, screen):
        eps=self.goal_theta-self.current_theta #pour tester notre condition d'arrêt
        next_pas=self.pas # pour que l'arrêt soit fluide 
        if abs(eps)>=abs(self.pas):
            self.set_current_theta() #l'aiguille avance
        elif abs(eps)!=0:
            next_pas=self.pas #pour que l'aiguile s'arrête exactement a la bonne position
            self.pas=eps
            self.set_current_theta()
        pos1=(pos[0]+self.taille*math.cos(2*math.pi/360*self.current_theta),pos[1]+ self.taille*math.sin(2*math.pi/360*self.current_theta))
        pygame.draw.line(screen, "red", pos, pos1, 5 )
        self.pas=next_pas


    def set_pas(self,pas):
        self.pas=pas

class Horloge():
    def __init__(self, pos_0=(0,0), rayon=100, width=3):
        self.pos_0=pos_0
        self.aiguille_1=Aiguille(rayon*0.8)
        self.aiguille_2=Aiguille(rayon*0.8)
        self.rayon=rayon
        self.width=width

    def set_aiguille(self,theta_1,theta_2):
        self.aiguille_1.set_goal_theta(theta_1)
        self.aiguille_2.set_goal_theta(theta_2)

    def set_aig_pas(self,pas1,pas2):
        self.aiguille_1.set_pas(pas1)
        self.aiguille_2.set_pas(pas2)


    def dessiner(self, screen):
        pygame.draw.circle(screen, "black", self.pos_0, self.rayon,self.width)
        self.aiguille_1.dessiner_aiguille(self.pos_0,screen)
        self.aiguille_2.dessiner_aiguille(self.pos_0,screen)






