import json

from classes.Chiffres import Chiffres
from classes.Transition import Transition


class Tableau():
    def __init__(self, fichier, butee):
        with open(fichier) as data:
            data = json.load(data)
        self.nb_ligne=data["nb_ligne"]
        self.nb_colonne=data["nb_colonne"]
        self.chiffres=Chiffres(data["init_position_chiffre"], data["fichier_chiffre_name"], data["fonction_cadre_chiffre_name"])
        self.transition_heure=Transition(data["init_position_transition_heure"], data["fichier_transition_name_heure"],  data["fonction_cadre_transition_heure_name"])
        self.transition_minute=Transition(data["init_position_transition_minute"], data["fichier_transition_name_minute"], data["fonction_cadre_transition_minute_name"])
        self.Matrice_horloge=[[[0, 0] for _ in range(data["nb_colonne"])] for _ in range(data["nb_ligne"])]
        self.butee=butee

    def execute_transition_heure(self, s):
        self.Matrice_horloge=self.transition_heure.execute_transition(s,self.Matrice_horloge, self.butee, self.nb_ligne, self.nb_colonne)
    def execute_transition_minute(self, s):
        self.Matrice_horloge=self.transition_minute.execute_transition(s,self.Matrice_horloge, self.butee, self.nb_ligne, self.nb_colonne)
    def execute_chiffres(self, s):
        self.Matrice_horloge=self.chiffres.execute_chiffres(s,self.Matrice_horloge, self.butee, self.nb_ligne, self.nb_colonne)

