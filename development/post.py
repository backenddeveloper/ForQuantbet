import socket

#clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

class Post:

    def __init__(self , clientsocket , cookie , divisor):
        self.clientsocket = clientsocket
	self.cookie = str(cookie)
	self.divisor = str(divisor)

    def connect(self) :
	    packet = "POST /submit HTTP/1.1\nHost: quantbet.com\nCookie:" + self.cookie + "\n\ndivisor:" + self.divisor
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
