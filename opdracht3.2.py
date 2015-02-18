#!/usr/bin/env python

from country2 import *


def getCountry():
	""" Haalt de landen namen op uit het bestand landennamen.txt """
	#Landen namen uit bestand halen
	landen = []
	with open('landennamen.txt', 'r') as in_f:
		for line in in_f:
			landobject = Country()
			landenInfo = (line, landobject)
			landen.append(landenInfo)
			
	print(landen)

	
	
def main():
	app = QtGui.QApplication(sys.argv)
	Landennaam = getCountry()
	
	
if __name__ == '__main__':
	main()
