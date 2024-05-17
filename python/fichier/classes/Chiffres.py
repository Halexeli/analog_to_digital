import json
from datetime import datetime

from classes.Cadre import Cadre
from classes.Chiffre import Chiffre
from fonctions.fonctions import *


class Chiffres():
    def __init__(self, data, fichier, cadre_fonction):
        with open(fichier) as recup:
            recup= json.load(recup)
        self.dico=recup["dico"]
        self.taille=recup["taille"]
        self.dizaine_heure= Chiffre(data[0])
        self.unite_heure= Chiffre(data[1])
        self.dizaine_minute= Chiffre(data[2])
        self.unite_minute= Chiffre(data[3])
        self.cadre=Cadre(cadre_fonction)
        self.current_time = datetime.fromtimestamp(0)

    def set_heure(self, heure):
        self.current_time=heure
        heure_chiffre=str(self.current_time.strftime("%H"))
        self.dizaine_heure.chiffre=heure_chiffre[0]
        self.unite_heure.chiffre=heure_chiffre[1]
        minute_chiffre=str(self.current_time.strftime("%M"))
        self.dizaine_minute.chiffre=minute_chiffre[0]
        self.unite_minute.chiffre=minute_chiffre[1]


    def mise_en_liste(self):
        return [[self.dizaine_heure.haut,(self.dizaine_heure.haut[0]+self.taille[0]-1, self.dizaine_heure.haut[1]+self.taille[1]-1)],[self.unite_heure.haut,(self.unite_heure.haut[0]+self.taille[0]-1, self.unite_heure.haut[1]+self.taille[1]-1)], [self.dizaine_minute.haut,(self.dizaine_minute.haut[0]+self.taille[0]-1, self.dizaine_minute.haut[1]+self.taille[1]-1)], [self.unite_minute.haut,(self.unite_minute.haut[0]+self.taille[0]-1, self.unite_minute.haut[1]+self.taille[1]-1)]]


    def execute_chiffres(self, s, Matrice_horloge, butee, nb_ligne, nb_colonne):
        Liste_horloge=[]
        Liste_horloge, Matrice_horloge =self.dizaine_heure.execute_chiffre(self.dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.unite_heure.execute_chiffre(self.dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.dizaine_minute.execute_chiffre(self.dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.unite_minute.execute_chiffre(self.dico, Liste_horloge ,Matrice_horloge, butee)
        if self.cadre !=0:
                Liste_horloge, Matrice_horloge=self.cadre.fonction_cadre(Liste_horloge,nb_ligne,nb_colonne, self.mise_en_liste(), Matrice_horloge, butee) 
        envoi(Liste_horloge, s)
        return Matrice_horloge
