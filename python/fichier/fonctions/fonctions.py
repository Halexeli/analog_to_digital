import pickle


def fonction_sens(position, angle, sens,  Matrice_Horloge,butee):
    if(not butee): 
       return sens
    elem=[0,0]
    if(Matrice_Horloge[position[0]][position[1]][0]< angle[0]):
        elem[0]=1
    else:
        elem[0]=-1
    if(Matrice_Horloge[position[0]][position[1]][1]< angle[1]):
        elem[1]=1
    else:
        elem[1]=-1
    return elem


def envoi(Liste_horloge, s):
    s.sendall(pickle.dumps(Liste_horloge))