#!/usr/bin/env python
#country.py
#Daphne Groot
#Hennie Veldthuis

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from random import *

class Flagcolor(QtGui.QColor):
    def __init__(self):
        super(Flagcolor, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        """ Maakt een combinatie van willkeurige RGB waarden"""

        self.kleur = QtGui.QColor(0, 0, 0)
        
        self.kleur.setRed(randrange(0, 256))
        self.kleur.setGreen(randrange(0, 256))
        self.kleur.setBlue(randrange(0, 256))
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    Landennaam = Flagcolor()
    sys.exit(app.exec_())

    
    
if __name__ == '__main__':
    main()



