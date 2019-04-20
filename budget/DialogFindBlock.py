from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from widgets import Finder_uis as ui
import os, json, blockchain


class finderClass(QDialog, ui.Ui_FormFinder):
	def __init__(self, parent):
		super(finderClass, self).__init__(parent)
		self.setupUi(self)
		self.update()
		#connect's
		self.find_btn.clicked.connect(self.findblock)
		self.close_btn.clicked.connect(self.close)
		self.grb_box.currentIndexChanged.connect(self.update)

	def update(self):
		self.groupBox_2.setVisible(self.grb_box.currentIndex()==1)
		self.groupBox_3.setVisible(self.grb_box.currentIndex()==2)

	def findblock(self):
		self.listWidget.clear()
		if self.grb_box.currentIndex() == 1:
			data_find='name_main'
			w=str(self.spisok_grb_box.currentText())
			self.finded=blockchain.find_file(blockchain.statement_directory, w, data_find)
			finded=self.finded
			if finded != ['Запрашиваемые данные отсутствуют. Введите корректные данные.']:
				for i in finded:
					self.listWidget.addItem('Дата: {} \nГлавный распорядитель бюджетных средств: {} \nРаздел: {} \nПодраздел: {} \nПрограмма: {} \nПодпрограмма: {} \nМероприятие: {} \nВид расхода: {} \nСумма бюджетных средств: {} \nКод бюджетной классификации: {}'.format(i['data_time'], i['name_main'], i['name_section'], i['name_subsection'], i['name_pr'], i['name_pod'], i['name_event'], i['name_view'], i['value'], i['kbk']))
			elif finded == ['Запрашиваемые данные отсутствуют. Введите корректные данные.']:
				self.listWidget.addItem(finded[0])
		elif self.grb_box.currentIndex() == 2:
			data_find='name_section'
			w=str(self.spisok_sub_box.currentText())
			self.finded=blockchain.find_file(blockchain.statement_directory, w, data_find)
			finded=self.finded
			if finded != ['Запрашиваемые данные отсутствуют. Введите корректные данные.']:
				for i in finded:
					self.listWidget.addItem('Дата: {} \nГлавный распорядитель бюджетных средств: {} \nРаздел: {} \nПодраздел: {} \nПрограмма: {} \nПодпрограмма: {} \nМероприятие: {} \nВид расхода: {} \nСумма бюджетных средств: {} \nКод бюджетной классификации: {}'.format(i['data_time'], i['name_main'], i['name_section'], i['name_subsection'], i['name_pr'], i['name_pod'], i['name_event'], i['name_view'], i['value'], i['kbk']))
			elif finded == ['Запрашиваемые данные отсутствуют. Введите корректные данные.']:
				self.listWidget.addItem(finded[0])