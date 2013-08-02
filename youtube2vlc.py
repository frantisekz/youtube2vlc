#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui, QtCore

class Youtube2VLC(QtGui.QMainWindow):
    
    def __init__(self):
        super(Youtube2VLC, self).__init__()
        self.initUI()
        
    def initUI(self):      
        self.btn = QtGui.QPushButton('Enter URL', self)
        self.btn.move(40, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.btn = QtGui.QPushButton('Exit', self)
        self.btn.move(180, 20)
        self.btn.clicked.connect(QtGui.qApp.quit)

	lbl = QtGui.QLabel('Last URL:', self)
        lbl.move(10, 60)

	self.lurl = QtGui.QLineEdit(self)
        self.lurl.move(100, 60)

        self.setGeometry(100, 100, 290, 100)
        self.setWindowTitle('Youtube2VLC')
        self.show()
        
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Video URL', 
            'Enter video url:')
        
        if ok:
	 self.lurl.setText(str(text))
	 os.system("vlc "+ str(text))	

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Youtube2VLC()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
