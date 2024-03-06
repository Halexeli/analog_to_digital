# echo-client.py

import pickle
import socket
import sys
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
time.sleep(10)


nbligne=int(sys.argv[1])
nbcolonne=int(sys.argv[2])
Matrice_horloge=[]
for i in range(nbcolonne):
    Liste_horloge=[]
    for j in range(nbligne):
        Liste_horloge.append({"theta_1":0, "theta_2":0, "pas1":1, "pas2":1})
    Matrice_horloge.append(Liste_horloge)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i=0
    while(1):
        for i in range(nbcolonne):
            for j in range (nbligne):
                if (j%2==0):
                    if(i==nbcolonne-1):
                        Matrice_horloge[i][j]={"theta_1":45, "theta_2":120, "pas1":1, "pas2":-1}
                    else:
                        Matrice_horloge[i][j]={"theta_1":45, "theta_2":315, "pas1":1, "pas2":1}
                else:
                    if(i==0):
                        Matrice_horloge[i][j]={"theta_1":45, "theta_2":120, "pas1":1, "pas2":1}
                    else:
                        Matrice_horloge[i][j]={"theta_1":210, "theta_2":135, "pas1":1, "pas2":1}
       
        # Encodage de l'array en bytes avec pickle
        array_bytes = pickle.dumps(Matrice_horloge)
        time.sleep(3)
        # Envoi des données encodées
        s.sendall(array_bytes)
        i=i+1
        var=str(i).encode()
        #s.sendall(b"test")
        data = s.recv(1024)
        print(f"Received {data!r}")

