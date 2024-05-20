from fonctions.fonctions import *

'''
cette classe se compose:
    -de la position de l'horloge la plus à gauche et la plus haute des horloges composant le chiffre
    -du chiffre à afficher en string afin de retrouver les instructions nécessaires à son affichage dans le fichier json des chiffres
'''
class Chiffre():
    '''
    Constructeur de la classe Chiffre
    data : la position de l'horloge la plus à gauche et la plus haute des horloges composant le chiffre
    '''
    def __init__(self, data):
        self.haut=data
        self.chiffre="0"

    '''
    Méthode qui permet de choisir le chiffre à afficher
    dico : le dictionnaire des chiffres
    Liste_horloge : la liste des horloges
    Matrice_horloge : la matrice des horloges
    butee : la butée de la transition
    @return : la liste des horloges et la matrice des horloges
    '''
    def execute_chiffre(self, dico, Liste_horloge ,Matrice_horloge, butee):
        l=dico[self.chiffre]
        for element in l:
            for position in element[0]:
                sens=fonction_sens((position[0]+ self.haut[0], position[1]+self.haut[1]), (element[1][0],element[1][1]), (element[1][4],element[1][5]), Matrice_horloge, butee )
                Liste_horloge.append((( position[0]+self.haut[0], position[1]+self.haut[1]),element[1][0],element[1][1],fonction_adaptation_au_tick(element[1][2]),fonction_adaptation_au_tick(element[1][3]),sens[0],sens[1]))
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][0][0]=element[1][0]
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][0][1]=element[1][1]
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][1][0]=sens[0]
                Matrice_horloge[position[0]+self.haut[0]][position[1]+self.haut[1]][1][1]=sens[1]
        return Liste_horloge, Matrice_horloge