# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\budget\widgets\MainMenu.ui',
# licensing of 'C:\Users\markveligod\Desktop\budget\widgets\MainMenu.ui' applies.
#
# Created: Sun Apr 21 20:50:47 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Menu_Form(object):
    def setupUi(self, Menu_Form):
        Menu_Form.setObjectName("Menu_Form")
        Menu_Form.resize(298, 207)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Menu_Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Menu_Form)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 121, 111))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image = QtWidgets.QLabel(self.groupBox_2)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.welcome = QtWidgets.QLabel(self.groupBox)
        self.welcome.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.welcome.setObjectName("welcome")
        self.time = QtWidgets.QLabel(self.groupBox)
        self.time.setGeometry(QtCore.QRect(200, 20, 71, 20))
        self.time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time.setObjectName("time")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 170, 101, 16))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(164, 40, 111, 112))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getblock_btn = QtWidgets.QPushButton(self.widget)
        self.getblock_btn.setObjectName("getblock_btn")
        self.verticalLayout.addWidget(self.getblock_btn)
        self.check_btn = QtWidgets.QPushButton(self.widget)
        self.check_btn.setObjectName("check_btn")
        self.verticalLayout.addWidget(self.check_btn)
        self.find_info = QtWidgets.QPushButton(self.widget)
        self.find_info.setObjectName("find_info")
        self.verticalLayout.addWidget(self.find_info)
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Menu_Form)
        QtCore.QMetaObject.connectSlotsByName(Menu_Form)

    def retranslateUi(self, Menu_Form):
        Menu_Form.setWindowTitle(QtWidgets.QApplication.translate("Menu_Form", "Blockchain Федерального бюджета", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Menu_Form", "Пользователь", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Menu_Form", "Аватарка", None, -1))
        self.image.setText(QtWidgets.QApplication.translate("Menu_Form", "аватарка", None, -1))
        self.welcome.setText(QtWidgets.QApplication.translate("Menu_Form", "приветствие", None, -1))
        self.time.setText(QtWidgets.QApplication.translate("Menu_Form", "время", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Menu_Form", "by MARK VELIGOD", None, -1))
        self.getblock_btn.setText(QtWidgets.QApplication.translate("Menu_Form", "Добавить блок", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate("Menu_Form", "Проверка блоков", None, -1))
        self.find_info.setText(QtWidgets.QApplication.translate("Menu_Form", "Поиск информации", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("Menu_Form", "Выход", None, -1))

