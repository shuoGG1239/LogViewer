import os
import re
import sys
import threading

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtGui import QCursor, QTextDocument
from PyQt5.QtWidgets import QWidget, QMenu, QAction
from QCandyUi.CandyWindow import colorful

import color_util
import sshLogger
from ui_LogViewer import Ui_LogViewer
from SearchForm import SearchForm

DEBUG = False


@colorful('blueGreen')
class LogViewer(QWidget):
    signal_response = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_LogViewer()
        self.ui.setupUi(self)
        self.__init_searchForm()
        self.__redirect_print()
        self.__init_menu()
        self.run_log_async()

    def __init_searchForm(self):
        self.searchForm = SearchForm()
        self.searchForm.setParent(self)
        self.searchForm.hide()
        self.searchForm.ui.pushButtonForward.clicked.connect(self.__slot_find_forward)
        self.searchForm.ui.pushButtonBackward.clicked.connect(self.__slot_find_backward)
        self.searchForm.ui.pushButtonClose.clicked.connect(self.__slot_searchForm_close)

    def __slot_searchForm_close(self):
        self.ui.textBrowser.setFocus()

    def __slot_find_forward(self):
        self.ui.textBrowser.find(self.searchForm.ui.lineEdit.text())

    def __slot_find_backward(self):
        self.ui.textBrowser.find(self.searchForm.ui.lineEdit.text(), QTextDocument.FindBackward)

    def run_log_async(self):
        """
        异步跑ssh的logging任务
        :return:
        """
        t = threading.Thread(target=sshLogger.run_conn_log)
        t.setDaemon(True)
        t.start()

    def __redirect_print(self):
        """
        重定向sys.out,使print(text)定向到__refunc(text)
        :return:
        """
        mystream = MyOutStream()
        mystream.textWritten.connect(self.__refunc)
        sys.stdout = mystream

    @pyqtSlot(str)
    def __refunc(self, text):
        useful_text = text.strip()
        if useful_text != '':
            self.ui.textBrowser.append(self.colorize(useful_text))

    def colorize(self, text):
        """
        对单行进行着色
        :param text:
        :return:
        """
        text = re.sub(r'(admin\d?\.log)', color_util.bold(color_util.colorize('\\1', 'orange')), text)
        text = re.sub(r'\s:\s(.+)', color_util.colorize(' : \\1', 'blue'), text)
        text = text.replace('INFO', color_util.colorize('INFO', color_util.LIGHT_BLUE))
        text = text.replace('ERROR', color_util.colorize('ERROR', 'red'))
        text = text.replace('WARN', color_util.colorize('WARN', 'orange'))
        text = re.sub(r'(\w+Exception)', color_util.colorize('\\1', 'red'), text)
        text = re.sub(r'(\([\w_]+\.java:\d+\))', color_util.colorize(color_util.underline('\\1'), 'red'), text)
        return text

    def closeEvent(self, e):
        sys.stdout = sys.__stdout__  # 归还print输出
        os._exit(0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.ui.textBrowser.clear()
        if (e.modifiers() == Qt.ControlModifier) and (e.key() == Qt.Key_F):
            if self.searchForm.isHidden():
                self.searchForm.setGeometry(self.width() - self.searchForm.width(), 0, self.searchForm.width(),
                                            self.searchForm.height())
                self.searchForm.show()
            else:
                self.searchForm.hide()
                self.ui.textBrowser.setFocus()

    def __init_menu(self):
        # 先将TextBrowser的右键菜单剔除, 不然其优先级会高于browserMenu
        self.ui.textBrowser.setContextMenuPolicy(Qt.NoContextMenu)
        self.browserMenu = QMenu()
        self.actionClear = QAction('Clear (esc)', self.browserMenu)
        self.actionCopy = QAction('Copy (ctrl+c)', self.browserMenu)
        self.actionSelectAll = QAction('Select All (ctrl+a)', self.browserMenu)
        self.browserMenu.addAction(self.actionClear)
        self.browserMenu.addAction(self.actionCopy)
        self.browserMenu.addAction(self.actionSelectAll)
        self.actionClear.triggered.connect(self.__slot_clear)
        self.actionCopy.triggered.connect(self.__slot_copy)
        self.actionSelectAll.triggered.connect(self.__slot_select_all)

    def __slot_clear(self):
        self.ui.textBrowser.clear()

    def __slot_copy(self):
        self.ui.textBrowser.copy()

    def __slot_select_all(self):
        self.ui.textBrowser.selectAll()

    def contextMenuEvent(self, event):
        self.browserMenu.exec(QCursor.pos())


# 用于重定向sys.out的类, 只要带write flush方法即可(非重写,是duckType)
class MyOutStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        # pyInstaller选择-w模式时, sys.__stdout__.write会直接阻塞
        if DEBUG:
            sys.__stdout__.write(str(text))  # 依旧打印到控制台, 调试时用

    def flush(self):
        if DEBUG:
            sys.__stdout__.flush()
