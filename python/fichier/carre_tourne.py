import json
import sys

col=int(sys.argv[1])
ligne = int(sys.argv[2])

a=[]
b=[]
c=[]
d=[]





with open('./pacman.json', "w") as f:
    json.dump(data, f)
