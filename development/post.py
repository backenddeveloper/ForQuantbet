import socket

#clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

class Post:

    def __init__(self , clientsocket , cookie , divisor):
        self.clientsocket = clientsocket
	self.cookie = str(cookie)
	self.divisor = str(divisor)

    def connect(self) :
	    packet = ("POST /submit HTTP/1.1 \n"
		      "Host: quantbet.com \n"
		      "Content-Length: 13 \n"
		      "Origin: http://quantbet.com \n"
		      "Content-Type: application/x-www-form-urlencoded \n"
		      "Referer: http://quantbet.com/quiz \n"
		      "Cookie:" + self.cookie + "\n\n"
		      "divisor=" + self.divisor)
	    self.clientsocket.connect(('quantbet.com', 80))
	    self.clientsocket.send(packet)
	    self.clientsocket.shutdown(1)
	    print "Divisor sent..."
	    data = []
	    while 1:
		reply = self.clientsocket.recv(8192)
		data.append(reply)
		if "</html>" in reply:
		    break
	    self.clientsocket.close()
	    return data

