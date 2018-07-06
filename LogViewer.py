import os
import re
import sys
import threading

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QWidget
from QCandyUi.CandyWindow import colorful

import color_util
import sshLogger
from ui_LogViewer import Ui_LogViewer

DEBUG = False


@colorful('blueGreen')
class LogViewer(QWidget):
    signal_response = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_LogViewer()
        self.ui.setupUi(self)
        self.__redirect_print()
        self.run_log_async()
        self.ui.textBrowser.setFocus()

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
        text = re.sub(r'(\([\w_]+\.java:\d+\))', color_util.colorize(color_util.underline('\\1'), 'red'), text)
        return text

    def closeEvent(self, e):
        sys.stdout = sys.__stdout__  # 归还print输出
        os._exit(0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.ui.textBrowser.clear()


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
