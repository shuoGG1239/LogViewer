# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_LogViewer.ui'
#
# Created: Thu Jun 28 10:13:06 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogViewer(object):
    def setupUi(self, LogViewer):
        LogViewer.setObjectName("LogViewer")
        LogViewer.resize(1090, 648)
        LogViewer.setLayoutDirection(QtCore.Qt.LeftToRight)
        LogViewer.setAutoFillBackground(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LogViewer)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(LogViewer)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.retranslateUi(LogViewer)
        QtCore.QMetaObject.connectSlotsByName(LogViewer)

    def retranslateUi(self, LogViewer):
        _translate = QtCore.QCoreApplication.translate
        LogViewer.setWindowTitle(_translate("LogViewer", "Form"))

