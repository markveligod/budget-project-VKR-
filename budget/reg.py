from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import reg_uis as ui
import blockchain

class regClass(QDialog, ui.Ui_Reg_Form):
	def __init__(self, parent):
		super(regClass, self).__init__(parent)
		self.setupUi(self)
		#connect
		self.reg_btn.clicked.connect(self.reg_block)
		self.close_btn.clicked.connect(self.close)


	def reg_block(self):
		try:
			name = self.login.text()
			password = self.password.text()
			two_pass = self.rep_password.text()
			directory = blockchain.people_directory
			if password==two_pass:
				self.record_new_block=blockchain.reg_user(name=name, password=password, directory=directory)
				msgBox=QMessageBox()
				msgBox.setText('Данные внесены в новый блок.')
				ret=msgBox.exec_()
				self.close()
			else:
				msgBox=QMessageBox()
				msgBox.setText('Пароль не совпадает. Попробуйте еще раз.')
				ret=msgBox.exec_()
		except Exception as info:
			print(info)

	