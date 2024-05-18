
from fonctions.fonctions import *


def fonction_cadre_ligne(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
    for i in range(nbligne):
        for j in range(nbcolonne):
            test=0
            for pos in transition_position:
                if(pos[0][0]<=i and pos[1][0]>=i and pos[0][1]<= j and pos[1][1] >=j):
                    test=1
            if(test==0):
                sens=fonction_sens((i, j), (180, 0), (1, 1), Matrice_horloge, butee )      
                Liste.append(((i, j), 180, 0, 0.008, 0.008, sens[0], sens[1]))
                Matrice_horloge[i][j][0]=180
                Matrice_horloge[i][j][1]=0
    return Liste, Matrice_horloge

def fonction_cadre_cran(Liste, nbligne, nbcolonne, transition_position, Matrice_horloge, butee):
    for i in range(nbligne):
        for j in range(nbcolonne):
            test=0
            for pos in transition_position:
                if(pos[0][0]<=i and pos[1][0]>=i and pos[0][1]<= j and pos[1][1] >=j):
                    test=1
            if(test==0):
                sens=fonction_sens((i, j), (45, 135), (1, 1), Matrice_horloge, butee )     
                Liste.append(((i, j), 45, 135, 0.008, 0.008, sens[0], sens[1]))
                Matrice_horloge[i][j][0]=45
                Matrice_horloge[i][j][1]=135
    return Liste, Matrice_horloge