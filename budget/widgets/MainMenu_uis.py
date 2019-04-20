# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\budget\widgets\MainMenu.ui',
# licensing of 'C:\Users\markveligod\Desktop\budget\widgets\MainMenu.ui' applies.
#
# Created: Wed Apr 17 20:29:49 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 156)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.check_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.check_btn.setFont(font)
        self.check_btn.setObjectName("check_btn")
        self.find_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.find_btn.setFont(font)
        self.find_btn.setObjectName("find_btn")
        self.createblock_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.createblock_btn.setFont(font)
        self.createblock_btn.setObjectName("createblock_btn")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate("MainWindow", "проверить состояние блоков", None, -1))
        self.find_btn.setText(QtWidgets.QApplication.translate("MainWindow", "поиск данных", None, -1))
        self.createblock_btn.setText(QtWidgets.QApplication.translate("MainWindow", "создать новый блок", None, -1))

