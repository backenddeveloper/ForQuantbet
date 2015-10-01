import unittest
from socketmock import SocketMock
from get import Get

class TestGet(unittest.TestCase):

    def test_connects(self):
	mock = SocketMock()
	test = Get(mock)
	reply = test.connect()
	self.assertEquals(mock.connectCalled , ('quantbet.com', 80))
	self.assertEquals(reply , ["<html><div>" , "test" , "</div></html>"])
	self.assertEquals(mock.dataSent , "GET /quiz HTTP/1.1\nHost: quantbet.com\n\n")
	self.assertEquals(mock.closeCalled , 1)

if __name__ == '__main__':
    unittest.main()
