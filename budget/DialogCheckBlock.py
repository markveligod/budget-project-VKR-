from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from widgets import check_uis as ui
import os, json, blockchain


class checkClass(QDialog, ui.Ui_Form_check):
	def __init__(self, parent):
		super(checkClass, self).__init__(parent)
		self.setupUi(self)
		#connect's
		self.check_block_btn.clicked.connect(self.checkblock)
		self.close_btn.clicked.connect(self.close)

	def checkblock(self):
		self.list_blocks.clear()
		self.checking=blockchain.check_block(blockchain.statement_directory)
		checking=self.checking
		for i in checking:
			self.list_blocks.addItem('Блок: {} Статус: {}'.format(i['Block'], i['Status']))
			
			
