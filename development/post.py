import socket

#clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

class Post:

    def __init__(self , clientsocket , cookie , divisor):
        self.clientsocket = clientsocket
	self.cookie = str(cookie)
	self.divisor = str(divisor)

    def connect(self) :
	    packet = '''POST /submit HTTP/1.1
Host: quantbet.com
Content-Length: 13
Origin: http://quantbet.com
Content-Type: application/x-www-form-urlencoded
Referer: http://quantbet.com/quiz\n\n
divisor=''' + self.divisor
	    self.clientsocket.connect(('quantbet.com', 80))
	    self.clientsocket.send(packet)
	    print "Divisor sent..."
	    data = []
	    while 1:
		reply = self.clientsocket.recv(8192)
		data.append(reply)
		if "</html>" in reply:
		    break
	    self.clientsocket.close()
	    return data

#'''Cookie:''' + self.cookie + '''\n'''
