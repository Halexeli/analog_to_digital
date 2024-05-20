import importlib

'''
cette classe se compose du cadre à afficher soit autour de l'heure, soit autour des motifs de la transition.
Elle permet de choisir le cadre à afficher en fonction de la fonction passée en paramètre.
'''

class Cadre():
    '''
    Constructeur de la classe Cadre
    @param fonction : la fonction qui permet de choisir le cadre à afficher
    '''
    def __init__(self, fonction):
        self.__fonction=getattr(importlib.import_module("fonctions.fonctions_cadre"), fonction)

    '''
    Méthode qui permet de choisir le cadre à afficher
    Liste : la liste des motifs de la transition
    nbligne, nbcolonne : le nombre de lignes et colonnes de la matrice des motifs
    transition_position : la position de la transition 
    Matrice_horloge : la matrice de l'horloge
    butee : la butée de la transition
    @return : la matrice du cadre à afficher
    '''
    
    def fonction_cadre(self,Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
        return self.__fonction(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee)