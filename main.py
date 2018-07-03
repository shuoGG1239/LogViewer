import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from QCandyUi import CandyWindow

from LogViewer import LogViewer


def run_with_titlebar():
    app = QApplication(sys.argv)
    w = CandyWindow.createWindow(LogViewer(),'blueGreen', 'Log Viewer', 'myicon.ico')
    w.show()
    sys.exit(app.exec_())


def run_dec():
    app = QApplication(sys.argv)
    w = LogViewer()
    w.setWindowTitle('Log Viewer')
    w.setWindowIcon(QIcon('myicon.ico'))
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_dec()
