# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchForm.ui'
#
# Created: Thu Jul 26 21:56:45 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(330, 50)
        SearchForm.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit = QtWidgets.QLineEdit(SearchForm)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonBackward = QtWidgets.QPushButton(SearchForm)
        self.pushButtonBackward.setGeometry(QtCore.QRect(243, 15, 21, 21))
        self.pushButtonBackward.setObjectName("pushButtonBackward")
        self.pushButtonForward = QtWidgets.QPushButton(SearchForm)
        self.pushButtonForward.setGeometry(QtCore.QRect(267, 15, 21, 21))
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.pushButtonClose = QtWidgets.QPushButton(SearchForm)
        self.pushButtonClose.setGeometry(QtCore.QRect(292, 15, 21, 21))
        self.pushButtonClose.setObjectName("pushButtonClose")

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "Form"))
        self.pushButtonBackward.setText(_translate("SearchForm", "<"))
        self.pushButtonForward.setText(_translate("SearchForm", ">"))
        self.pushButtonClose.setText(_translate("SearchForm", "×"))

