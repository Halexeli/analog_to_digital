import json
import sys

'''
cette fonction génère un fichier json de transition pour les oiseaux
'''
def oiseau(ligne, col):
    a=[]
    b=[]
    for i in range(ligne):
        for j in range(col):
            if((i+j)%2==0):
                a.append([i,j])
            else:
                b.append([i,j])

    data=[
        [3.5,
        [
            [
                a,
                [225, 315, 0.008, 0.008, 1, -1]
            ],
            [
                b,
                [135, 45, 0.008, 0.008, 1, -1] 
            ]
        ]],
        [0.75,
        [
            [
                a,
                [135, 45, 0.008, 0.008, -1, 1]
            ],
            [
                b,
                [225, 315, 0.008, 0.008, 1, -1]
            ]
        ]
        ],
        [0.75,
        [
            [
                a,
                [225, 315, 0.008, 0.008, 1, -1]
            ],
            [
                b,
                [135, 45, 0.008, 0.008, -1, 1]
            ]
        ]],
        [0.75,
        [
            [
                a,
                [135, 45, 0.008, 0.008, -1, 1]
            ],
            [
                b,
                [225, 315, 0.008, 0.008, 1, -1]
            ]
        ]
        ],
        [0.75,
        [
            [
                a,
                [225, 315, 0.008, 0.008, 1, -1]
            ],
            [
                b,
                [135, 45, 0.008, 0.008, -1, 1]
            ]
        ]]
    ]

    data_envoi={
        "taille": [ligne, col],
        "transition": data
    }


    with open('./transitions/oiseau_transition.json', "w") as f:
        json.dump(data_envoi, f)
    return "./transitions/oiseau_transition.json"

if __name__=='__main__':
    ligne=int(sys.argv[1])
    col = int(sys.argv[2])
    oiseau(ligne, col)
