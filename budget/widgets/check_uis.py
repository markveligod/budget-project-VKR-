# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\budget\widgets\check.ui',
# licensing of 'C:\Users\markveligod\Desktop\budget\widgets\check.ui' applies.
#
# Created: Sun Apr 21 20:47:17 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_check(object):
    def setupUi(self, Form_check):
        Form_check.setObjectName("Form_check")
        Form_check.resize(590, 297)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form_check)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form_check)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_block_btn = QtWidgets.QPushButton(self.groupBox)
        self.check_block_btn.setObjectName("check_block_btn")
        self.verticalLayout.addWidget(self.check_block_btn)
        self.list_blocks = QtWidgets.QListWidget(self.groupBox)
        self.list_blocks.setObjectName("list_blocks")
        self.verticalLayout.addWidget(self.list_blocks)
        self.close_btn = QtWidgets.QPushButton(self.groupBox)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)

        self.retranslateUi(Form_check)
        QtCore.QMetaObject.connectSlotsByName(Form_check)

    def retranslateUi(self, Form_check):
        Form_check.setWindowTitle(QtWidgets.QApplication.translate("Form_check", "Blockchain Федерального бюджета", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Form_check", "состояние блоков", None, -1))
        self.check_block_btn.setText(QtWidgets.QApplication.translate("Form_check", "проверить", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("Form_check", "закрыть", None, -1))

