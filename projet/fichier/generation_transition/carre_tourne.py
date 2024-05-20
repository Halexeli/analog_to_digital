import json
import sys

'''
cette fonction génère un fichier json de transition pour les carrés tournant
'''
def carre_tourne(ligne, col):
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(ligne):
        for j in range(col):
            if(i%2==0):
                if(j%2==0):
                    a.append([i,j])
                else:
                    b.append([i,j])
            else:
                if(j%2==0):
                    c.append([i,j])
                else:
                    d.append([i,j])

    data=[
        [3.5,
        [
            [
                a,
                [0, 90, 0.008, 0.008, 1, 1]
            ],
            [
                b,
                [180, 90, 0.008, 0.008, -1, -1] 
            ],
            [
                c,
                [0, 270, 0.008, 0.008, 1, -1]
            ],
            [
                d,
                [180, 270, 0.008, 0.008, 1, -1]
            ]
        ]],
        [1,
        [
            [
                a,
                [270, 180, 0.008, 0.008, 1, -1]
            ],
            [
                b,
                [270, 0, 0.008, 0.008, -1, 1]
            ],
            [
                c,
                [90, 180, 0.008, 0.008, -1, 1]
            ],
            [
                d,
                [90, 0, 0.008, 0.008, 1, -1]
            ]
        ]
        ],
        [3,
        [
            [
                a,
                [0, 90, 0.008, 0.008, 1, -1]
            ],
            [
                b,
                [180, 90, 0.008, 0.008, -1, 1]
            ],
            [
                c,
                [0, 270, 0.008, 0.008, -1, 1]
            ],
            [
                d,
                [180, 270, 0.008, 0.008, 1, -1]
            ]
        ]]
    ]

    data_envoi={
        "taille": [ligne, col],
        "transition": data
    }


    with open('./transitions/carre_transition.json', "w") as f:
        json.dump(data_envoi, f)
    return "./transitions/carre_transition.json"

if __name__=='__main__':
    ligne=int(sys.argv[1])
    col = int(sys.argv[2])
    carre_tourne(ligne, col)
