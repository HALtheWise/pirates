#!/usr/bin/python3

import re

questions = {
	'is_pirate':"Blimey! Ye landlubber still be learnin' the ropes! Every good talk starts with a hearty \"Arrrgh!\"",
	'which_side':"Good to be seein' you back.\nDo you be lookin' to give(1) or get(2) help today?"
}

responses = {
	'is_pirate':(
			('a[ar]+r', True), # A proper pirate responds "Arrrgh!" or some variation thereof
			('.*', None),
		),
	'which_side':(
			('give','pirate'),
			('1', 	'pirate'),
			('get', 'victim'),
			('2', 	'victim'),
			('recieve', 'victim'),
		),
}

class Session(object):
	"""Represents a user session"""
	queriesProcessed = 0
	hasOpenedWell = False

	knownData = {}

	activeQuestion = 'is_pirate'

	def __init__(self, name):
		super(Session, self).__init__()
		self.name = name


	def handleQuery(self, request):
		self.queriesProcessed += 1

		if self.activeQuestion:
			trans = self.interpretResponse(request)
			if trans == None:
				# We couldn't (or refused to) parse the response
				return self.askData(self.activeQuestion)

		if 'is_pirate' not in self.knownData:
			return self.askData('is_pirate')

		if 'which_side' not in self.knownData:
			return self.askData('which_side')

		return "This be the end of the demo, you {}.".format(self.knownData['which_side'])

	def interpretResponse(self, request):
		l = responses[self.activeQuestion]
		for patt, val in l:
			if re.search(patt, request.lower()):

				if val is not None:
					print('learned {}:{}'.format(self.activeQuestion, val))

					self.knownData[self.activeQuestion] = val
					self.activeQuestion = None

				return val
		return None

	def askData(self, data):
		if data in self.knownData:
			print("Warning: {} is already known about user {}".format(data, self.name))
		self.activeQuestion = data

		return questions[data]

		

def main():
	session = Session('testuser')
	while True:
		request = input('---> ')

		if not request:
			break

		response = session.handleQuery(request)

		if response:
			print("\n"+response)
		else:
			return


if __name__ == '__main__':
	main()