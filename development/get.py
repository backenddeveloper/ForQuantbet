import socket

#clientsocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

class Get:

    def __init__(self , clientsocket):
        self.clientsocket = clientsocket

    def connect(self) :
	    packet = "GET /quiz HTTP/1.1\nHost: quantbet.com\nCookie:laravel_session=eyJpdiI6InRwNHJmZm9ZK0dreUxxUjVEN3Q3VlE9PSIsInZhbHVlIjoiQ3Y5a1lPaEN2UWFBVm0xTW9nMDkra3pwT2dUVHZLV1ltN09yNERQb3RVNWQrZzlBSHl2V3F5aVZqakFNWHA0YmU4ZG04Y0pTd1haeVwvZmFoQnNPeWRBPT0iLCJtYWMiOiJiY2I4M2U0ODkyNTI5MjZmY2I5NThlM2YwY2IxYjcyNTJiNGVkZjViMDU2ZjMzNzQ1ODM2NGExZjA1NWY0NjI4In0%3D\n\n"
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
