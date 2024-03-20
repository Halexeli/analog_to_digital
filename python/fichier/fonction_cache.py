
import json

with open('./dataretour.json') as mon_fichier:
    data = json.load(mon_fichier)


for i in data:
    for j in i[1]:
        for t in j[0]:
            a=t[0]
            t[0]=t[1]
            t[1]=a


with open('./dataretour.json', "w") as f:
    json.dump(data, f)
