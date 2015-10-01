class ProcessResponse:

    def __init__(self , responseString):
	self.string = responseString

    def getNumbers(self):
	firstNumber  = int(self.string.split('<strong>')[1].split('</strong>')[0])
	secondNumber = int(self.string.split('<strong>')[2].split('</strong>')[0])
	return [firstNumber , secondNumber]

    def getCookie(self):
	cookie = self.string.split("Cookie:")[1].split("\n")[0]
	return cookie
