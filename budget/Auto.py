from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import mainmenu
from widgets import Authorization_uis as ui
import os, json
import blockchain
from icons import icons_rcs
import reg


login_global=[]
class authorizationClass(QWidget, ui.Ui_AuthorizationDialog):
	def __init__(self):
		super(authorizationClass, self).__init__()
		self.setupUi(self)
		#ui
		pix=QPixmap(':/login.png').scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
		self.image.setPixmap(pix)
		self.setWindowIcon(QIcon(':/monitor.png'))
		# self.setWindowFlags(Qt.WindowStaysOnTopHint)
		#connect's
		self.ok_btn.clicked.connect(self.ok)
		self.reg_btn.clicked.connect(self.reg_user)


	def reg_user(self):
		self.dial=reg.regClass(self)
		if self.dial.exec_():
			print('REG')

	def start(self):
		self.dial=mainmenu.projectClass()
		self.dial.show()


	def ok(self):
		login=str(self.name_line.text())
		password=str(self.password_line.text())
		files=blockchain.sorting_file(blockchain.people_directory)
		for file in files[1:]:
			f=open(blockchain.people_directory + str(file), encoding='UTF-8')
			info=json.load(f)
			if login == info['name'] and password == info['password']:
				login_global.append(login)
				with open('logs.py', 'w') as f:
					f.write(login)
			else:
				print('не нашел')

		if login_global != []:
			print(login_global)
			msgBox=QMessageBox()
			msgBox.setText('Добро пожаловать, {}'.format(login))
			ret=msgBox.exec_()
			self.close()
			self.start()
		else:
			msgBox=QMessageBox()
			msgBox.setText('Неправильный логин или пароль. Попробуйте ещё раз.')
			ret=msgBox.exec_()
		# try:
		# 	if data_find[login]==password:
		# 		login_global.append(login)
		# 		msgBox=QMessageBox()
		# 		msgBox.setText('Добро пожаловать, {}'.format(login))
		# 		ret=msgBox.exec_()
		# 		self.close()
		# 		self.start()
				
		# 	elif data_find[login]!=password:
		# 		msgBox=QMessageBox()
		# 		msgBox.setText('Неправильный логин или пароль. Попробуйте ещё раз.')
		# 		ret=msgBox.exec_()

		# except Exception as info:
		# 	msgBox=QMessageBox()
		# 	msgBox.setText('Неправильный логин или пароль. Попробуйте ещё раз.')
		# 	print(info)
		# 	ret=msgBox.exec_()





if __name__ == '__main__':
	app=QApplication([])
	w=authorizationClass()
	w.show()
	app.exec_()