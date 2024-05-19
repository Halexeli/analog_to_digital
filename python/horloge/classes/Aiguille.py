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
    def __init__(self,taille=80,couleur="blue"):
        self.__couleur=couleur
        self.goal_theta=180 #but
        self.__current_theta=180 #position actuelle
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
    def dessiner_aiguille2(self, pos, screen):
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
        pygame.draw.line(screen, self.__couleur, pos, pos1, 5 )
        self.tps=abs(next_tps)

    '''
    Méthode set_aiguille2 :

    Permet de définir l'angle de l'aiguille
    - theta : angle de l'aiguille
    - butee : butee de l'aiguille
    '''
    def set_aiguille2(self,theta,butee):
        if(butee==1): #si il y a une butee
            if (self.sens==1): #si le sens est positif
                if(self.__butee_flag==1): #si on est sur la butee
                    self.goal_theta=0
                    self.__butee_flag=1
                else: 
                    if(self.__current_theta%360< theta%360):#si l'angle actuel est inferieur a l'angle but
                        self.goal_theta=theta%360
                        self.__butee_flag=0
                    elif(self.__current_theta%360== theta%360):#si l'angle actuel est egal a l'angle but
                        if(theta%360==0):
                            self.goal_theta=theta%360
                            self.__butee_flag=1
                        else:
                            self.goal_theta=theta%360
                    else:#si l'angle actuel est superieur a l'angle but
                        self.goal_theta=0
                        self.__butee_flag=1
            else: #si le sens est negatif
                if(self.__butee_flag==-1): #si on est sur la butee
                    self.goal_theta=0
                    self.__butee_flag=-1
                else:
                    if(self.__current_theta%360>theta%360): #si l'angle actuel est superieur a l'angle but
                        if(theta==0):
                            self.goal_theta=0
                            self.__butee_flag=-1
                        else:
                            self.goal_theta=theta%360
                            self.__butee_flag=0
                    elif(self.__current_theta== theta%360): #si l'angle actuel est egal a l'angle but
                        if(theta%360==0):
                            self.goal_theta=theta%360
                            self.__butee_flag=-1
                        else:
                            self.goal_theta=theta%360
                    else: #si l'angle actuel est inferieur a l'angle but
                        self.goal_theta=0
                        self.__butee_flag=-1
        else: #si il n'y a pas de butee
            self.goal_theta=theta%360

    def __test_dessiner(self):
        if(self.__current_theta%360!=self.goal_theta%360 and self.tps!=0):
            next_pos=(self.__current_theta%360+(1/(self.tps*vitesse)*self.sens)) #on calcule la prochaine position
            if(next_pos>=360): #si on depasse le 0 (ou egal a 0) aves sens==1
                if(self.__current_theta%360<=self.goal_theta%360<=next_pos):  
                    self.__current_theta=self.goal_theta%360
                    self.tps=0
                elif(self.__current_theta%360<=self.goal_theta%360+360<=next_pos):
                    self.__current_theta=self.goal_theta%360
                    self.tps=0
                else:
                    self.__current_theta=next_pos%360
            elif(next_pos<=0): #si on depasse le 0 (ou egal a 0) avec le sens==-1
                if(self.__current_theta%360>=self.goal_theta%360>=next_pos):
                    self.__current_theta=self.goal_theta
                elif(self.__current_theta%360>=self.goal_theta%360-360>=next_pos):
                    self.__current_theta=self.goal_theta%360
                else:
                    self.__current_theta=next_pos%360
            elif(self.goal_theta%360==0):#si on ne depasse pas le zero
                self.__current_theta=next_pos%360
            elif(self.sens==1): #cas simple sens==1
                if(self.__current_theta%360<=self.goal_theta%360<=next_pos%360):
                    self.__current_theta=self.goal_theta%360
                else:
                    self.__current_theta=next_pos%360
            elif(self.sens==-1): #cas simple si sens==-1
                if(self.__current_theta%360>=self.goal_theta%360>=next_pos%360):
                    self.__current_theta=self.goal_theta%360
                else:
                    self.__current_theta=next_pos%360


    def dessiner_aiguille_butee(self, pos, screen,couleur):
        if(self.tps!=0):
            next_pos=(self.__current_theta%360+(1/(self.tps*vitesse*self.sens))) #on calcule la prochaine position
            if(self.__current_theta!=0): #pas de butee atteint
                if (next_pos>=360 or next_pos<=0): #on atteint la butee au prochain tour
                    self.__current_theta=0
                    self.__butee_flag=self.sens
                else:
                    self.__test_dessiner()
            else:
                if(self.sens*self.__butee_flag==-1): #on est sur la butee
                    if(self.goal_theta==0):
                        self.__current_theta+=next_pos%360
                    else:
                        self.__test_dessiner()
        pos1=(pos[0]+self.__taille*math.cos(2*math.pi/360*self.__current_theta),pos[1]+ self.__taille*math.sin(2*math.pi/360*self.__current_theta))
        pygame.draw.line(screen, couleur, pos, pos1, 5 )


    '''
    Méthode dessiner_aiguille :
    Permet de dessiner l'aiguille 
    '''
    def dessiner_aiguille(self, pos, screen,couleur):
        self.__test_dessiner()
        pos1=(pos[0]+self.__taille*math.cos(2*math.pi/360*self.__current_theta),pos[1]+ self.__taille*math.sin(2*math.pi/360*self.__current_theta))
        pygame.draw.line(screen, couleur, pos, pos1, 5 )


    def set_aiguille(self,theta):
        self.goal_theta=theta%360
