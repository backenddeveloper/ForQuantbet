#Copyright Graham Turner 2015 released for use under GNU/GPLv3. This is not suitable for production use.

class SocketMock:

    connectCalled = 0
    dataSent = 0
    closeCalled = 1
    recvIndex = -1
    recvData = ["<html><div>" , "test" , "</div></html>"]

    def connect(self , url):
	self.connectCalled = url

    def send(self , data):
	self.dataSent = data

    def recv(self , data):
	self.recvIndex += 1
	return self.recvData[self.recvIndex]

    def close(self):
	self.closeCalled = 1
