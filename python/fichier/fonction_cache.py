
import json

with open('./polytech.json') as mon_fichier:
    data = json.load(mon_fichier)


for i in data:
    for j in i[1]:
        j[1][2]=(j[1][2]*2)
        j[1][3]=(j[1][3]*2)


with open('./polytech.json', "w") as f:
    json.dump(data, f)
