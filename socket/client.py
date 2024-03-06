# echo-client.py

import pickle
import socket
import time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i=0
    while(1):
        my_array = {'jack': 4098, 'sape': 4139}

        # Encodage de l'array en bytes avec pickle
        array_bytes = pickle.dumps(my_array)
        time.sleep(30)
        # Envoi des données encodées
        s.sendall(array_bytes)
        i=i+1
        var=str(i).encode()
        #s.sendall(b"test")
        data = s.recv(1024)
        print(pickle.loads(data))

