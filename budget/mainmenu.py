from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import MainMenu_uis as ui
import os
import json
import DialogGetBlock, DialogCheckBlock, DialogFindBlock
import datetime
from icons import icons_rcs


class projectClass(QWidget, ui.Ui_Menu_Form):
	def __init__(self, ):
		super(projectClass, self).__init__()
		self.setupUi(self)
		self.anytime()
		self.user()
		#ui
		self.setWindowIcon(QIcon(':/monitor.png'))
		pix=QPixmap(':/ava.png')
		self.image.setPixmap(pix)
		#connect's
		self.getblock_btn.clicked.connect(self.openDialogGet)
		self.check_btn.clicked.connect(self.openDialogCheck)
		self.find_info.clicked.connect(self.openDialogFind)
		self.close_btn.clicked.connect(self.close)


	def openDialogGet(self):
		self.dial=DialogGetBlock.GetBlockClass(self)
		if self.dial.exec_():
			print ('CREATY in BLOCK')


	def openDialogCheck(self):
		self.dial=DialogCheckBlock.checkClass(self)
		if self.dial.exec_():
			print ('CHECK in BLOCK')

	def openDialogFind(self):
		self.dial=DialogFindBlock.finderClass(self)
		if self.dial.exec_():
			print ('FIND BLOCK')

	def anytime(self):
		data_time=str(datetime.date.today().strftime("%d/%m/%Y"))
		self.time.setText(data_time)

	def user(self):
		with open('logs.py') as f:
			users=f.read()
			self.welcome.setText('Добро пожаловать, {}'.format(users))
