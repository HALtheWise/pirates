#!/usr/bin/python3

import re

pirate ={
	'conversation_start_err':"Blimey! Ye landlubber still be learnin' the ropes! Every good talk starts with a hearty \"Arrrgh!\"",
	'get_or_give_q':"Good to be seein' you back.\nDo you be lookin' to get(1) or give(2) help today?"
}

class Session(object):
	"""Represents a user session"""
	queriesProcessed = 0
	hasOpenedWell = False

	knownData = {}

	def __init__(self, name):
		super(Session, self).__init__()
		self.name = name


	def handleQuery(session, request):
		session.queriesProcessed += 1

		if not session.hasOpenedWell:
			if isProperOpener(request):
				session.hasOpenedWell = True
			else:
				return pirate['conversation_start_err']

		return pirate['get_or_give_q']

	def askData(self, data):
		if data in self.knownData:
			print("Warning: {} is already known about user {}".format(data, self.name))

		
		

def isProperOpener(request):
	# A proper pirate greeting must be at least "Aar!" or "Arr!" with some other characters maybe thrown in.
	return bool(re.match('.*a[ar]+r.*!.*', request.lower()))


def main():
	session = Session(input('Your name:'))
	while True:
		request = input('---> ')

		if not request:
			break

		print(session.handleQuery(request))


if __name__ == '__main__':
	main()