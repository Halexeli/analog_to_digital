import pickle
import socket
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    conn.setblocking(0)
    with conn:
        while 1:
            try:
                data = conn.recv(1024)
                if data:
                    # Si des données ont été reçues, les traiter
                    print("Données reçues :", pickle.loads(data))
                    conn.sendall(data)
                else:
                    # Si aucune donnée n'a été reçue
                    print("Aucune donnée disponible pour le moment")
            except:
                # Gérer l'erreur de non-blocage
                pass
            print("test")
            time.sleep(4)