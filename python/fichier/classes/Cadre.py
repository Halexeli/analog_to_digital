import importlib


class Cadre():
    def __init__(self, fonction):
        self.fonction=getattr(importlib.import_module("fonctions.fonctions_cadre"), fonction)
    
    def fonction_cadre(self,Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
        return self.fonction(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee)