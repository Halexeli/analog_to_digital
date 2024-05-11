import json
import sys

col=int(sys.argv[1])
ligne = int(sys.argv[2])
with open('./polytech.json') as mon_fichier:
    data = json.load(mon_fichier)

def init(ligne,col):
    a=[]
    c=[]
    e=[]
    for i in range(ligne):
        for j in range(col):
            if(j==0):
                a.append([i,j])
            elif(j==col-1):
                c.append([i,j])
            else:
                e.append([i,j])
    res=[3,[
    [
        a,
        [0, 0, 0.008, -0.008]
    ],[
        c,
        [180, 180, 0.008, -0.008]
    ],[
        e,
        [135, 315, 0.008, -0.008]
    ]]
    ]
    return(res)

def pacman(ligne,col):
    a=[]
    b=[]
    c=[]
    d=[]
    for j in range(ligne):
        if j%2==0:
            a.append([j,0])
            c.append([j,col-1])
        else:
            b.append([j,0])
            d.append([j,col-1])
    res=[[
        0.25,
        [[
            a,
            [45, 315, 0.004, -0.004]
        ],[
            d,
            [225,135,0.004,-0.004]
        ]]
    ],[
        0.25,
        [[
            a,
            [0, 0, -0.004, 0.004]
        ],[
            d,
            [180,180,-0.004,0.004]
        ]]
    ],[
        0.25,
        [[
            b,
            [45, 315, 0.004, -0.004]
        ],[
            c,
            [225,135,0.004,-0.004]
        ]]
    ],[
        0.25,
        [[
            b,
            [0, 0, -0.004, 0.004]
        ],[
            c,
            [180,180,-0.004,0.004]
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




with open('./pacman.json', "w") as f:
    json.dump(data, f)
