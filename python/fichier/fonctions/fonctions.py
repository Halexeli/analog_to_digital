import pickle

tick_en_degres = 1/12

def fonction_sens(position, angle, sens,  Matrice_Horloge,butee):
    if(not butee): 
       return sens
    elem=[0,0]
    if(Matrice_Horloge[position[0]][position[1]][0][0]< angle[0]):
        if(Matrice_Horloge[position[0]][position[1]][0][0]==0):
            if(Matrice_Horloge[position[0]][position[1]][1][0]==-1):
                elem[0]=1
            else:
                elem[0]=-1
        else:
            elem[0]=1
    elif(angle[0]==0):
        elem[0]=sens[0]
    else:
        elem[0]=-1
    if(Matrice_Horloge[position[0]][position[1]][0][1]< angle[1]):
        if(Matrice_Horloge[position[0]][position[1]][0][1]==0):
            if(Matrice_Horloge[position[0]][position[1]][1][1]==-1):
                elem[1]=1
            else:
                elem[1]=-1
        else:
            elem[1]=1
    elif(angle[1]==0):
        elem[1]=sens[1]
    else:
        elem[1]=-1
    return elem


def fonction_adaptation_au_tick(temps):
    return temps*tick_en_degres

def envoi(Liste_horloge, s):
    s.sendall(pickle.dumps(Liste_horloge))