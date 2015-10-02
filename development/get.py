import socket

#clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

class Get:

    def __init__(self , clientsocket):
        self.clientsocket = clientsocket

    def connect(self) :
	    packet = "GET /quiz HTTP/1.1\nHost: quantbet.com\n\n"
	    self.clientsocket.connect(('quantbet.com', 80))
	    self.clientsocket.send(packet)
	    data = []
	    while 1:
		reply = self.clientsocket.recv(8192)
		data.append(reply)
		if "</html>" in reply:
		    break
	    self.clientsocket.close()
	    return data
