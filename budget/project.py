from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import MainMenu_uis as ui
import os
import json
import DialogGetBlock, DialogCheckBlock, Auto, DialogFindBlock

class projectClass(QMainWindow, ui.Ui_MainWindow):
	def __init__(self):
		super(projectClass, self).__init__()
		self.setupUi(self)
		#connect's
		self.createblock_btn.clicked.connect(self.openDialogGetBlock)
		self.check_btn.clicked.connect(self.openDialogCheckBlock)
		self.find_btn.clicked.connect(self.openDialogFindBlock)
		#start func
		self.openDialogAuthorization()

	def openDialogAuthorization(self):
		self.dial=Auto.authorizationClass(self)
		if self.dial.exec_():
			print ('Authorization')

	def openDialogGetBlock(self):
		self.dial=DialogGetBlock.GetBlockClass(self)
		if self.dial.exec_():
			print ('CREATY in BLOCK')


	def openDialogCheckBlock(self):
		self.dial=DialogCheckBlock.checkClass(self)
		if self.dial.exec_():
			print ('CHECK in BLOCK')

	def openDialogFindBlock(self):
		self.dial=DialogFindBlock.finderClass(self)
		if self.dial.exec_():
			print ('FIND a BLOCK')


if __name__ == '__main__':
	app=QApplication([])
	w=projectClass()
	w.show()
	app.exec_()