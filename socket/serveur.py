import pickle
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                try:
                    data_dict = pickle.loads(data)
                    if 'jack' in data_dict:
                        print(data_dict['jack'])
                    else:
                        print("No 'jack' in received data")
                except Exception as e:
                    print(f"Error while deserializing data: {e}")
            else:
                print("No data received")
            conn.sendall(data)