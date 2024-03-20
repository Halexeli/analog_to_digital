import threading

class MonThread(threading.Thread):
    def __init__(self, clientsocket):
        self.clientsocket=clientsocket
    
    def run(self):
        data=self.clientsocket.recv(2048)
        return data


    