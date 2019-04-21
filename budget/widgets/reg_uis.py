# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\budget\widgets\reg.ui',
# licensing of 'C:\Users\markveligod\Desktop\budget\widgets\reg.ui' applies.
#
# Created: Sun Apr 21 20:47:24 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Reg_Form(object):
    def setupUi(self, Reg_Form):
        Reg_Form.setObjectName("Reg_Form")
        Reg_Form.resize(398, 186)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Reg_Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(Reg_Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(69, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.login = QtWidgets.QLineEdit(self.groupBox)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(52, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.rep_password = QtWidgets.QLineEdit(self.groupBox)
        self.rep_password.setObjectName("rep_password")
        self.horizontalLayout_3.addWidget(self.rep_password)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reg_btn = QtWidgets.QPushButton(self.groupBox)
        self.reg_btn.setObjectName("reg_btn")
        self.horizontalLayout_4.addWidget(self.reg_btn)
        self.close_btn = QtWidgets.QPushButton(self.groupBox)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addWidget(self.groupBox)

        self.retranslateUi(Reg_Form)
        QtCore.QMetaObject.connectSlotsByName(Reg_Form)

    def retranslateUi(self, Reg_Form):
        Reg_Form.setWindowTitle(QtWidgets.QApplication.translate("Reg_Form", "Blockchain Федерального бюджета", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Reg_Form", "Регистрация", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Reg_Form", "Введите имя", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Reg_Form", "Введите пароль", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Reg_Form", "Повторно введите пароль", None, -1))
        self.reg_btn.setText(QtWidgets.QApplication.translate("Reg_Form", "Зарегистрироваться", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("Reg_Form", "Закрыть", None, -1))

