#!/usr/bin/env python
#country.py
#Daphne Groot

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from opdracht3_2 import *
from random import *

class Country(QtGui.QWidget):
    def __init__(self):
        super(Country, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        """ Maakt de combobox en voegt de gegevens eraan toe.
        Ook worden de connecties gemaakt naar de methode om de gegevens te updaten"""
        
        landen = self.getCountry()
        
        #Combobox "landennaam"
        self.comboboxLand = QtGui.QComboBox(self)
        self.comboboxLand.addItems(landen)
        self.comboboxLand.adjustSize()
        self.comboboxLand.move(40, 30)
        
        #Connecties voor aanpassen aan nieuwe gegevens
        self.connect(self.comboboxLand,SIGNAL("currentIndexChanged(int)"), self.updateUi)


        #################################################################################
        self.col = QtGui.QColor(0, 0, 0)

        # self.comboboxLand.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 120, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())
        
        
    def getCountry(self):
        """ Haalt de landen namen op uit het bestand landennamen.txt """
        #Landen namen uit bestand halen
        self.landen = []
        with open('landennamen.txt', 'r') as in_f:
            for line in in_f:
                self.landen.append(line[:-1])
                
        return self.landen


    def updateUi(self):
        """ Zorgt ervoor dat de gegevens in de combobox geupdate zijn """
        #Aanpassen aan nieuwe gegevens
        landnaam = str(self.comboboxLand.currentText())

        
        self.col.setRed(randrange(0, 256))
        self.col.setGreen(randrange(0, 256))
        self.col.setBlue(randrange(0, 256)) 
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  

    
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    Landennaam = Country()
    Landennaam.setWindowTitle('Landennaam')
    Landennaam.setGeometry(400, 400, 500, 300)
    Landennaam.show()
    sys.exit(app.exec_())

    
    
if __name__ == '__main__':
    main()

