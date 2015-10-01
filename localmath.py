import math

class GCD:

    def __init__(self , firstNumber , secondNumber):
	try:
		self.firstNumber = int(firstNumber)
		self.secondNumber = int(secondNumber)
	except ValueError:
	    raise Error('A non integer value was collected.')

    def getGCD(self):
	x = self.firstNumber
	y = self.secondNumber
	
	while y:
	    x , y = y , x%y
	return x
