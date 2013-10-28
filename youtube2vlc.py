#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
from PyQt4 import QtGui, QtCore

def play():
    os.system("vlc "+ (str(yturledit.text())) + " --play-and-exit")
    yturledit.clear()

app = QtGui.QApplication(sys.argv)
mainWindow = QtGui.QMainWindow()
mainWindow.setWindowTitle("Youtube2VLC")
mainWidget=QtGui.QWidget(mainWindow)
mainWindow.setCentralWidget(mainWidget)
layout=QtGui.QGridLayout(mainWidget)
mainWindow.move(300,300)

headerLabel=QtGui.QLabel(u"<h1>Youtube2VLC</h1>",mainWidget)
headerLabel.setAlignment(QtCore.Qt.AlignHCenter)

yturl=QtGui.QLabel("Youtube video URL:",mainWidget)
yturledit=QtGui.QLineEdit(mainWidget)

showPushButton=QtGui.QPushButton(u"Play",mainWidget)
closePushButton=QtGui.QPushButton(u"Close",mainWidget)

layout.addWidget(headerLabel,0,0,1,2)
layout.addWidget(yturl,1,0)
layout.addWidget(yturledit,1,1)
layout.addWidget(showPushButton,3,0)
layout.addWidget(closePushButton,3,1)

app.connect(closePushButton,QtCore.SIGNAL("clicked ()"),mainWindow.close)
app.connect(showPushButton,QtCore.SIGNAL("clicked ()"),play)

mainWindow.show()
sys.exit(app.exec_())