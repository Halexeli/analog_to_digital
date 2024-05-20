import json
from datetime import datetime

from classes.Cadre import Cadre
from classes.Chiffre import Chiffre
from fonctions.fonctions import *

'''
cette classe se compose:
 -du fichier json des chiffres
 -de la taille d'un chiffre
 -de 4 objets Chiffre qui composent l'heure et les minutes
 -de l'objet Cadre pour créer un cadre autour de l'heure affichée et de l'heure à afficher
'''

class Chiffres():
    '''
    Constructeur de la classe Chiffres
    data : la liste des positions de l'horloge la plus à gauche et la plus haute des horloges composant l'heure
    fichier : le fichier json des chiffres
    cadre_fonction : la fonction qui permet de choisir le cadre à afficher
    '''
    def __init__(self, data, fichier, cadre_fonction):
        with open(fichier) as recup:
            recup= json.load(recup)
        self.__dico=recup["dico"]
        self.__taille=recup["taille"]
        self.__dizaine_heure= Chiffre(data[0])
        self.__unite_heure= Chiffre(data[1])
        self.__dizaine_minute= Chiffre(data[2])
        self.__unite_minute= Chiffre(data[3])
        self.cadre=Cadre(cadre_fonction)
        self.current_time = datetime.fromtimestamp(0)
    '''
    Méthode qui permet de choisir l'heure à afficher
    heure : l'heure à afficher
    '''

    def set_heure(self, heure):
        self.current_time=heure
        heure_chiffre=str(self.current_time.strftime("%H"))
        self.__dizaine_heure.chiffre=heure_chiffre[0]
        self.__unite_heure.chiffre=heure_chiffre[1]
        minute_chiffre=str(self.current_time.strftime("%M"))
        self.__dizaine_minute.chiffre=minute_chiffre[0]
        self.__unite_minute.chiffre=minute_chiffre[1]

    '''
    Méthode qui permet de mettre en liste les horloges composant l'heure
    @return : la liste des horloges composant l'heure
    '''

    def mise_en_liste(self):
        return [[self.__dizaine_heure.haut,(self.__dizaine_heure.haut[0]+self.__taille[0]-1, self.__dizaine_heure.haut[1]+self.__taille[1]-1)],[self.__unite_heure.haut,(self.__unite_heure.haut[0]+self.__taille[0]-1, self.__unite_heure.haut[1]+self.__taille[1]-1)], [self.__dizaine_minute.haut,(self.__dizaine_minute.haut[0]+self.__taille[0]-1, self.__dizaine_minute.haut[1]+self.__taille[1]-1)], [self.__unite_minute.haut,(self.__unite_minute.haut[0]+self.__taille[0]-1, self.__unite_minute.haut[1]+self.__taille[1]-1)]]

    '''
    Méthode qui permet d'afficher l'heure
    s : la socket
    Matrice_horloge : la matrice de l'horloge
    butee : la butée de la transition
    nb_ligne, nb_colonne : le nombre de lignes et colonnes de la matrice des motifs
    @return : la matrice de l'horloge
    '''

    def execute_chiffres(self, s, Matrice_horloge, butee, nb_ligne, nb_colonne):
        Liste_horloge=[]
        Liste_horloge, Matrice_horloge =self.__dizaine_heure.execute_chiffre(self.__dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.__unite_heure.execute_chiffre(self.__dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.__dizaine_minute.execute_chiffre(self.__dico, Liste_horloge ,Matrice_horloge, butee)
        Liste_horloge, Matrice_horloge =self.__unite_minute.execute_chiffre(self.__dico, Liste_horloge ,Matrice_horloge, butee)
        if self.cadre !=0:
                Liste_horloge, Matrice_horloge=self.cadre.fonction_cadre(Liste_horloge,nb_ligne,nb_colonne, self.mise_en_liste(), Matrice_horloge, butee) 
        envoi(Liste_horloge, s)
        return Matrice_horloge
