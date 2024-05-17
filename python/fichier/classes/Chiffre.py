from fonctions.fonctions import *


class Chiffre():
    def __init__(self, data):
        self.haut=data
        self.chiffre="0"

    def execute_chiffre(self, dico, Liste_horloge ,Matrice_horloge, butee):
        l=dico[self.chiffre]
        for element in l:
            for position in element[0]:
                sens=fonction_sens((position[0]+ self.haut[0], position[1]+self.haut[1]), (element[1][0],element[1][1]), (element[1][4],element[1][5]), Matrice_horloge, butee )
                Liste_horloge.append((( position[0]+self.haut[0], position[1]+self.haut[1]),element[1][0],element[1][1],element[1][2],element[1][3],sens[0],sens[1]))
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][0]=element[1][0]
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][1]=element[1][1]
        return Liste_horloge, Matrice_horloge