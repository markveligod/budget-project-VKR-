from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from widgets import Structure_uis as ui
import os
import json
import blockchain


class GetBlockClass(QDialog, ui.Ui_FormStructure):
	def __init__(self, parent):
		super(GetBlockClass, self).__init__(parent)
		self.setupUi(self)
		self.update()
		#connect's
		self.send_btn.clicked.connect(self.recordblock)
		self.close_btn.clicked.connect(self.close)
		self.section_box.currentIndexChanged.connect(self.update)

	def recordblock(self):
		try:
			name_main=str(self.grbs_box.currentText())
			name_section=str(self.section_box.currentText())
			name_subsection=self.terment()
			name_pr=str(self.prog_box.currentText())
			name_pod=str(self.pod_box.currentText())
			name_event=str(self.event_box.currentText())
			name_view=str(self.view_box.currentText())
			value=str(self.line_sum.text())
			proverka=value.isdigit()
			if proverka == True:
				self.record_new_block=blockchain.record_block(blockchain.statement_directory, name_main, name_section, name_subsection, name_pr, name_pod, name_event, name_view, value)
				msgBox=QMessageBox()
				msgBox.setText('Данные внесены в новый блок.')
				ret=msgBox.exec_()
			else:
				msgBox=QMessageBox()
				msgBox.setText('Некорректно введены данные. Попробуйте ещё раз.')
				ret=msgBox.exec_()
		except Exception as info:
			print(info)
	
	def update(self):
		self.groupBox.setVisible(self.section_box.currentIndex()==1)
		self.groupBox_2.setVisible(self.section_box.currentIndex()==2)

	def terment(self):
		if self.section_box.currentIndex()==1:
			name_subsection=str(self.sub_box_1.currentText())
		elif self.section_box.currentIndex()==2:
			name_subsection=str(self.sub_box_4.currentText())
		return name_subsection

