import json
import sys

ligne=int(sys.argv[1]) 
col = int(sys.argv[2]) 

def init(ligne,col):
    a=[]
    c=[]
    e=[]
    for i in range(ligne):
        for j in range(col):
            if(i==0):
                a.append([i,j])
            elif(i==col-1):
                c.append([i,j])
            else:
                e.append([i,j])
    res=[3,[
    [
        a,
        [0, 0, 0.007, 0.007, 1, -1]
    ],[
        c,
        [180, 180, 0.007, 0.007, 1, -1]
    ],[
        e,
        [135, 315, 0.007, 0.007, 1, -1]
    ]]
    ]
    return(res)

def pacman(ligne,col):
    a=[]
    b=[]
    c=[]
    d=[]
    for j in range(col):
        if j%2==0:
            a.append([0,j])
            c.append([ligne-1,j])
        else:
            b.append([0,j])
            d.append([ligne-1,j])
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
            [180,180,0.004,0.004, -1, 1]
        ]]
    ],[
        0.25,
        [[
            b,
            [45, 315, 0.004, 0.004, 1, -1]
        ],[
            c,
            [225,135,0.004,0.004, 1, -1]
        ]]
    ],[
        0.25,
        [[
            b,
            [0, 0, 0.004, 0.004, -1, 1]
        ],[
            c,
            [180,180,0.004,0.004, -1, 1]
        ]]
    ]]
    return(res)
    

data=[init(ligne,col)]
for j in range(7):
    res=pacman(ligne,col)
    data.append(res[0])
    data.append(res[1])
    data.append(res[2])
    data.append(res[3])

data_envoi={
    "taille": [ligne, col],
    "transition": data
}



with open('./pacman.json', "w") as f:
    json.dump(data_envoi, f)
