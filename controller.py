import socket
import time

from development.get import Get
from development.post import Post
from development.localmath import GCD
from development.processResponse import ProcessResponse

start_time = time.time()

print "Sending request..."

soc = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

request = Get(soc)

reply = request.connect()

print "Processing response..."

data = ProcessResponse(reply)

cookie = data.getCookie()

numbers = data.getNumbers()

p =  "recieved: " + str(numbers[0]) + " , " + str(numbers[1])

print p

math = GCD(numbers[0] , numbers[1])

divisor = math.getGCD()

print "Divisor = " + str(divisor)

print "Sending divisor..."

soc = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

request = Post(soc , cookie , divisor)

profit = request.connect()

print "Divisor sent..."

print profit

print "Total time: " + str(time.time() - start_time)
