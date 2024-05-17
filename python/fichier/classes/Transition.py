import json
import time

from classes.Cadre import Cadre
from fonctions.fonctions import *


class Transition():
    def __init__(self, data, fichier, cadre_fonction):
        with open(fichier) as recup:
            recup= json.load(recup)
        self.transition=recup["transition"]
        taille=recup["taille"]
        transition_position=[]
        for el in data:
            transition_position.append([el,(el[0]+taille[0]-1,el[1]+taille[1]-1)])
        self.transition_position=transition_position

        if cadre_fonction !=0:
            self.cadre=Cadre(cadre_fonction)
        else:
            self.cadre=0
    


    def execute_transition(self, s, Matrice_horloge, butee, nb_ligne, nb_colonne):
        for step in self.transition:
            Liste_horloge=[]
            for element in step[1]:
                for position in element[0]:
                    for motif in self.transition_position:
                        sens=fonction_sens((position[0]+motif[0][0], position[1]+motif[0][1]), (element[1][0],element[1][1]), (element[1][4],element[1][5]), Matrice_horloge, butee)
                        Liste_horloge.append(((position[0]+motif[0][0], position[1]+motif[0][1]),element[1][0],element[1][1],element[1][2],element[1][3], sens[0],sens[1]))
                        Matrice_horloge[position[0]+motif[0][0]][position[1]+motif[0][1]][0]=element[1][0]
                        Matrice_horloge[position[0]+motif[0][0]][position[1]+motif[0][1]][1]=element[1][1]
            if self.cadre !=0:
                Liste_horloge, Matrice_horloge=self.cadre.fonction_cadre(Liste_horloge,nb_ligne,nb_colonne, self.transition_position, Matrice_horloge, butee) 
            envoi(Liste_horloge, s)
            time.sleep(step[0])
        return Matrice_horloge

