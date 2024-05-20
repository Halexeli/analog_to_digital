import json

from classes.Chiffres import Chiffres
from classes.Transition import Transition
from fonctions.fonctions import *

'''
cette classe se compose:
    -du nombre de lignes et de colonnes de la matrice des horloges
    -de l'objet Chiffres
    -de l'objet Transition pour les heures
    -de l'objet Transition pour les minutes
    -de la matrice des horloges (comprenant les angles du dernier affichage des aiguilles de chaque horloge)
    -de la butée de la transition (si elle existe)
'''

class Tableau():
    '''
    Constructeur de la classe Tableau
    fichier : le fichier json du tableau
    butee : la butée de la transition
    '''
    def __init__(self, fichier, butee):
        with open(fichier) as data:
            data = json.load(data)
        self.nb_ligne=data["nb_ligne"]
        self.nb_colonne=data["nb_colonne"]
        self.chiffres=Chiffres(data["init_position_chiffre"], data["fichier_chiffre_name"], data["fonction_cadre_chiffre_name"])
        self.__transition_heure=Transition(data["init_position_transition_heure"], data["fichier_transition_name_heure"],  data["fonction_cadre_transition_heure_name"], self.nb_ligne, self.nb_colonne)
        self.__transition_minute=Transition(data["init_position_transition_minute"], data["fichier_transition_name_minute"], data["fonction_cadre_transition_minute_name"], self.nb_ligne, self.nb_colonne)
        self.__Matrice_horloge=[[[[180, 180],[1,1]] for _ in range(data["nb_colonne"])] for _ in range(data["nb_ligne"])]
        self.__butee=butee

    def execute_transition_heure(self, s):
        self.__Matrice_horloge=self.__transition_heure.execute_transition(s,self.__Matrice_horloge, self.__butee, self.nb_ligne, self.nb_colonne)
    def execute_transition_minute(self, s):
        self.__Matrice_horloge=self.__transition_minute.execute_transition(s,self.__Matrice_horloge, self.__butee, self.nb_ligne, self.nb_colonne)
    def execute_chiffres(self, s):
        self.__Matrice_horloge=self.chiffres.execute_chiffres(s,self.__Matrice_horloge, self.__butee, self.nb_ligne, self.nb_colonne)
    def envoi_nb_horloge(self, s):
        envoi((self.nb_ligne, self.nb_colonne, self.__butee), s)

        

