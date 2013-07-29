#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore


class Youtube2VLC(QtGui.QWidget):
    
    def __init__(self):
        super(Youtube2VLC, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Another URL', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.setGeometry(100, 100, 290, 100)
        self.setWindowTitle('Youtube2VLC')
        self.show()
	self.showDialog()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Video URL', 
            'Enter video url:')
        
        if ok:
         self.setWindowTitle('Youtube2VLC')
	os.system("vlc "+ str(text))	
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Youtube2VLC()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
