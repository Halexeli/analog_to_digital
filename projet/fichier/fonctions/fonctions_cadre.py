
from fonctions.fonctions import *

'''
ce fichier se compose de 3 fonctions qui permettent de créer un cadre autour des horloges
'''

'''
fonction_cadre_ligne: permet de créer un cadre autour des horloges avec des lignes
    -Liste : la liste des horloges
    -nbligne, nbcolonne : la taille de la matrice des horloges
    -transition_position : la liste des positions des horloges utilisées pour la transition
    -Matrice_horloge : la matrice des horloges
    -butee : la butée de la transition (si elle existe)
'''
def fonction_cadre_ligne(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
    for i in range(nbligne): 
        for j in range(nbcolonne):
            test=0 #test pour savoir si l'horloge est dans la transition
            for pos in transition_position: #on regarde si l'horloge est dans la transition
                if(pos[0][0]<=i and pos[1][0]>=i and pos[0][1]<= j and pos[1][1] >=j):
                    test=1 #si l'horloge est dans la transition, on met test à 1
            if(test==0):#si l'horloge n'est pas dans la transition
                sens=fonction_sens((i, j), (180, 0), (1, 1), Matrice_horloge, butee ) #on regarde le sens de l'horloge    
                #on ajoute l'horloge à la liste des horloges  
                Liste.append(((i, j), 180, 0, fonction_adaptation_au_tick(0.008), fonction_adaptation_au_tick(0.008), sens[0], sens[1])) 
                #on met à jour la matrice des horloges
                Matrice_horloge[i][j][0][0]=180
                Matrice_horloge[i][j][0][1]=0
                Matrice_horloge[i][j][1][0]=sens[0]
                Matrice_horloge[i][j][1][1]=sens[1]
    return Liste, Matrice_horloge

'''
fonction_cadre_cran: permet de créer un cadre autour des horloges avec des crans
'''
def fonction_cadre_cran(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
    for i in range(nbligne):
        for j in range(nbcolonne):
            test=0
            for pos in transition_position:
                if(pos[0][0]<=i and pos[1][0]>=i and pos[0][1]<= j and pos[1][1] >=j):
                    test=1
            if(test==0):
                sens=fonction_sens((i, j), (45, 135), (1, 1), Matrice_horloge, butee )     
                Liste.append(((i, j), 45, 135, fonction_adaptation_au_tick(0.008), fonction_adaptation_au_tick(0.008), sens[0], sens[1]))
                Matrice_horloge[i][j][0][0]=45
                Matrice_horloge[i][j][0][1]=135
                Matrice_horloge[i][j][1][0]=sens[0]
                Matrice_horloge[i][j][1][1]=sens[1]
    return Liste, Matrice_horloge

''' 
fonction_cadre_fleches: permet de créer un cadre autour des horloges avec des flèches'''
def fonction_cadre_fleches(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
    for i in range(nbligne):
        for j in range(nbcolonne):
            test=0
            for pos in transition_position:
                if(pos[0][0]<=i and pos[1][0]>=i and pos[0][1]<= j and pos[1][1] >=j):
                    test=1
            if(test==0):
                if(i==0):  
                    sens=fonction_sens((i, j), (45, 135), (1, 1), Matrice_horloge, butee )  
                    Liste.append(((i, j), 45, 135, fonction_adaptation_au_tick(0.008), fonction_adaptation_au_tick(0.008), sens[0], sens[1]))
                    Matrice_horloge[i][j][0][0]=45
                    Matrice_horloge[i][j][0][1]=135
                    Matrice_horloge[i][j][1][0]=sens[0]
                    Matrice_horloge[i][j][1][1]=sens[1]
                elif(i==nbligne-1):
                    sens=fonction_sens((i, j), (225,315), (1, 1), Matrice_horloge, butee )  
                    Liste.append(((i, j), 225, 315, fonction_adaptation_au_tick(0.008), fonction_adaptation_au_tick(0.008), sens[0], sens[1]))
                    Matrice_horloge[i][j][0][0]=225
                    Matrice_horloge[i][j][0][1]=315
                    Matrice_horloge[i][j][1][0]=sens[0]
                    Matrice_horloge[i][j][1][1]=sens[1]
                else:
                    sens=fonction_sens((i, j), (90,270), (1, 1), Matrice_horloge, butee )  
                    Liste.append(((i, j), 90,270, fonction_adaptation_au_tick(0.008), fonction_adaptation_au_tick(0.008), sens[0], sens[1]))
                    Matrice_horloge[i][j][0][0]=90
                    Matrice_horloge[i][j][0][1]=270
                    Matrice_horloge[i][j][1][0]=sens[0]
                    Matrice_horloge[i][j][1][1]=sens[1]
    return Liste, Matrice_horloge