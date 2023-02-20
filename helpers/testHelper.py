def parseRawCommand(command: str):
	return command.split(" ")

def getRandomChoiceMock(i: int):
	return lambda choices: choices[i]