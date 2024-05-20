import pickle

tick_en_degres = 1/12

''' 
fonction_sens: permet de déterminer le sens de rotation de l'aiguille
    position : position de l'horloge
    angle : angle de l'aiguille
    sens : sens de l'horloge
    Matrice_Horloge : matrice des horloges
    butee : butée de la transition
'''
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


'''
fonction_adaptation_au_tick: permet d'adapter le temps en fonction du tick
    temps : temps
'''
def fonction_adaptation_au_tick(temps):
    return temps*tick_en_degres

'''
envoi: permet d'envoyer la liste des horloges
    Liste_horloge : liste des horloges
    s : socket
'''
def envoi(Liste_horloge, s):
    s.sendall(pickle.dumps(Liste_horloge))