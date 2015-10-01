import unittest
from lib.socketmock import SocketMock
from development.get import Get
from development.processResponse import ProcessResponse
from development.localmath import GCD

class TestGet(unittest.TestCase):

    def test_connects(self):
	mock = SocketMock()
	test = Get(mock)
	reply = test.connect()
	self.assertEquals(mock.connectCalled , ('quantbet.com', 80))
	self.assertEquals(reply , ["<html><div>" , "test" , "</div></html>"])
	self.assertEquals(mock.dataSent , "GET /quiz HTTP/1.1\nHost: quantbet.com\n\n")
	self.assertEquals(mock.closeCalled , 1)

class TestProcessResponse(unittest.TestCase):

    def test_finds_tags(self):
	mock = "<html><div><strong>17</strong><strong>101</strong></div></html>"
	test = ProcessResponse(mock)
	numbers = test.getNumbers()
	self.assertEquals(numbers , [17,101])

    def test_finds_cookie(self):
	mock = "\nHost:quantbet.com \nCookie:thisisa brokencookie string \nAccept:gzip"
	test = ProcessResponse(mock)
	cookie = test.getCookie()
	self.assertEquals(cookie , "thisisa brokencookie string ")

class TestMathGCD(unittest.TestCase):

    def test_returns_GCD(self):
	test = GCD(100 , 10)
	self.assertEquals(test.getGCD() , 10)
	test = GCD(13 , 17)
	self.assertEquals(test.getGCD() , 1)
	test = GCD(100 , 120)
	self.assertEquals(test.getGCD() , 20)

if __name__ == '__main__':
    unittest.main()
