from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import reg_uis as ui
import blockchain
import os, json

class regClass(QDialog, ui.Ui_Reg_Form):
	def __init__(self, parent):
		super(regClass, self).__init__(parent)
		self.setupUi(self)
		#connect
		self.reg_btn.clicked.connect(self.reg_block)
		self.close_btn.clicked.connect(self.close)


	def reg_block(self):
		result=[]
		path=blockchain.sorting_file(blockchain.people_directory)
		name = self.login.text()
		for i in path[1:]:
			f=open(blockchain.people_directory + str(i), encoding='utf-8')
			login=json.load(f)['name']
			if login == name:
				result.append(login)
				msgBox=QMessageBox()
				msgBox.setText('Логин уже существует')
				ret=msgBox.exec_()

		if result==[]:
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
		else:
			print('Error')

	