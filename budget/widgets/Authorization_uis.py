# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\markveligod\Desktop\budget\widgets\Authorization.ui',
# licensing of 'C:\Users\markveligod\Desktop\budget\widgets\Authorization.ui' applies.
#
# Created: Sat Apr 20 17:41:52 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AuthorizationDialog(object):
    def setupUi(self, AuthorizationDialog):
        AuthorizationDialog.setObjectName("AuthorizationDialog")
        AuthorizationDialog.resize(242, 134)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(AuthorizationDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(AuthorizationDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_laybol = QtWidgets.QLabel(self.groupBox)
        self.name_laybol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_laybol.setObjectName("name_laybol")
        self.horizontalLayout.addWidget(self.name_laybol)
        self.name_line = QtWidgets.QLineEdit(self.groupBox)
        self.name_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_laybol = QtWidgets.QLabel(self.groupBox)
        self.password_laybol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_laybol.setObjectName("password_laybol")
        self.horizontalLayout_2.addWidget(self.password_laybol)
        self.password_line = QtWidgets.QLineEdit(self.groupBox)
        self.password_line.setObjectName("password_line")
        self.horizontalLayout_2.addWidget(self.password_line)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ok_btn = QtWidgets.QPushButton(self.groupBox)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_3.addWidget(self.ok_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(AuthorizationDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationDialog)

    def retranslateUi(self, AuthorizationDialog):
        AuthorizationDialog.setWindowTitle(QtWidgets.QApplication.translate("AuthorizationDialog", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("AuthorizationDialog", "authorization", None, -1))
        self.name_laybol.setText(QtWidgets.QApplication.translate("AuthorizationDialog", "name", None, -1))
        self.password_laybol.setText(QtWidgets.QApplication.translate("AuthorizationDialog", "password", None, -1))
        self.ok_btn.setText(QtWidgets.QApplication.translate("AuthorizationDialog", "ОК", None, -1))

