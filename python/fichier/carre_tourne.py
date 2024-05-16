import json
import sys

col=int(sys.argv[1])
ligne = int(sys.argv[2])

a=[]
b=[]
c=[]
d=[]

for i in range(ligne):
    for j in range(col):
        if(i%2==0):
            if(j%2==0):
                a.append([j,i])
            else:
                b.append([j,i])
        else:
            if(j%2==0):
                c.append([j,i])
            else:
                d.append([j,i])

data=[
    [3.5,
     [
         [
             a,
             [0, 90, 0.008, 0.008]
         ],
         [
             b,
             [180, 90, -0.008, -0.008] 
         ],
         [
             c,
             [0, 270, 0.008, -0.008]
         ],
         [
             d,
             [180, 270, 0.008, -0.008]
         ]
     ]],
    [1,
     [
         [
             a,
             [270, 180, 0.008, -0.008]
         ],
         [
             b,
             [270, 0, -0.008, 0.008]
         ],
         [
             c,
             [90, 180, -0.008, 0.008]
         ],
         [
             d,
             [90, 0, 0.008, -0.008]
         ]
     ]
    ],
    [3,
     [
         [
            a,
            [0, 90, 0.008, -0.008]
         ],
         [
            b,
            [180, 90, -0.008, 0.008]
         ],
         [
             c,
             [0, 270, -0.008, 0.008]
         ],
         [
             d,
             [180, 270, 0.008, -0.008]
         ]
     ]]
]




with open('./carre_tourne.json', "w") as f:
    json.dump(data, f)
