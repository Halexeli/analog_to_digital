import json
import sys


def pacman(ligne,col):
    data=[init(ligne,col)]
    j=0
    for j in range(7):
        res=fonction_pacman(ligne,col)
        data.append(res[0])
        data.append(res[1])
        data.append(res[2])
        data.append(res[3])

    data_envoi={
        "taille": [ligne, col],
        "transition": data
    }

    with open('./transitions/pacman_transition.json', "w") as f:
        json.dump(data_envoi, f)
    return "./transitions/pacman_transition.json"

def init(ligne,col):
    a=[]
    c=[]
    e=[]
    for i in range(ligne):
        for j in range(col):
            if(i%2==0):
                a.append([i,j])
            else:
                c.append([i,j])
    res=[5,[
    [
        a,
        [0, 0, 0.007, 0.007, -1, 1]
    ],[
        c,
        [180, 180, 0.008, 0.008, 1, -1]
    ]]
    ]
    return(res)

def fonction_pacman(ligne,col):
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(ligne):
        for j in range(col):
            if j%2==0:
                if i%2==0:
                    a.append([i,j])
                else:
                    b.append([i,j])
            else:
                if i%2==0:
                    c.append([i,j])
                else:
                    d.append([i,j])
    res=[[
        0.25,
        [[
            a,
            [45, 315, 0.004, 0.004, 1, -1]
        ],[
            d,
            [225,135,0.004,0.004, 1, -1]
        ]]
    ],[
        0.25,
        [[
            a,
            [0, 0, 0.004, 0.004, -1, 1]
        ],[
            d,
            [180, 180,0.004,0.004, -1, 1]
        ]]
    ],[
        0.25,
        [[
            c,
            [45, 315, 0.004, 0.004, 1, -1]
        ],[
            b,
            [225,135,0.004,0.004, 1, -1]
        ]]
    ],[
        0.25,
        [[
            c,
            [0, 0, 0.004, 0.004, -1, 1]
        ],[
            b,
            [180, 180,0.004,0.004, -1, 1]
        ]]
    ]]
    return(res)
    



if __name__=='__main__':
    ligne=int(sys.argv[1]) 
    col = int(sys.argv[2]) 
    fonction_pacman(ligne,col)