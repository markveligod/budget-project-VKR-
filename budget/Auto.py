from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from widgets import Authorization_uis as ui
import os, json
import basa_password

class authorizationClass(QDialog, ui.Ui_AuthorizationDialog):
	def __init__(self, parent):
		super(authorizationClass, self).__init__(parent)
		self.setupUi(self)
		#connect's
		self.ok_btn.clicked.connect(self.ok)

	def ok(self):
		login=str(self.name_line.text())
		password=str(self.password_line.text())
		data_find=basa_password.basa_pass
		try:
			if data_find[login]==password:
				msgBox=QMessageBox()
				msgBox.setText('Добро пожаловать, {}'.format(login))
				ret=msgBox.exec_()
				self.close()
			elif data_find[login]!=password:
				msgBox=QMessageBox()
				msgBox.setText('Неправильный логин или пароль. Попробуйте ещё раз.')
				ret=msgBox.exec_()

		except Exception as info:
			msgBox=QMessageBox()
			msgBox.setText('Неправильный логин или пароль. Попробуйте ещё раз.')
			ret=msgBox.exec_()