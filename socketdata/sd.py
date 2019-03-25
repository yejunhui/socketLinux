import socket

class SocketData :
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def opensocket(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.host,self.port))
        s.listen(5)
        return s

    def senddata(self,d):
        self.sk.send(d)

    def recvdata(self):
        self.sk.recv(1024)
