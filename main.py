import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qss_ui_theme import green_theme
from qss_ui_theme import qss_setting
from qss_ui_theme import window_titlebar

import LogViewer


def scan_icon(ico_name):
    """
    扫描ico并返回Qicon
    :param ico_name:
    :return: Qicon
    """
    if os.path.isfile(window_titlebar.imageroot + ico_name):
        return QIcon(window_titlebar.imageroot + ico_name)
    else:
        return QIcon(ico_name)


def run_with_titlebar():
    app = QApplication(sys.argv)
    keywidget = LogViewer.LogViewer()
    mainWindow = window_titlebar.WindowWithTitleBar(keywidget, qss_setting.DARKBLUEGREEN, 0)
    mainWindow.setWindowTitle('Log Viewer')
    mainWindow.setWindowIcon(scan_icon('myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())


def run_only_greentheme():
    app = QApplication(sys.argv)
    mainWindow = LogViewer.LogViewer()
    mainWindow.setWindowTitle('Log Viewer')
    mainWindow.setWindowIcon(scan_icon('myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())


def run():
    app = QApplication(sys.argv)
    mainWindow = LogViewer.LogViewer()
    mainWindow.setWindowTitle('Log Viewer')
    mainWindow.setWindowIcon(scan_icon('myicon.ico'))
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_only_greentheme()
