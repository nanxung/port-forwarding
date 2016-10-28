#!/usr/bin/python2
#coding:utf8
import sys
from PyQt4 import QtGui,QtCore
'''app=QtGui.QApplication(sys.argv)
widget=QtGui.QWidget()
widget.resize(250,150)
widget.setWindowTitle('cb')
widget.show()
sys.exit(app.exec_())'''

'''class QuiButton(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit button')

        quit=QtGui.QPushButton('Close',self)
        quit.setGeometry(10,10,64,35)
        self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))
        self.setWindowIcon(QtGui.QIcon('icons/web.jpg'))'''
class MessageBox(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('message box')
    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message','Are you sure to quit?'
                                         ,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
app=QtGui.QApplication(sys.argv)
qb=MessageBox()
qb.show()
sys.exit(app.exec_())
