#!/usr/bin/python2
#coding:utf8
import sys
from PyQt4 import QtGui

app=QtGui.QApplication(sys.argv)

widget=QtGui.QWidget()
# widget.resize(250,150)
widget.setWindowTitle("cb's")
widget.show()
sys.exit(app.exec_())