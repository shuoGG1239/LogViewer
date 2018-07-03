import sys

from PyQt5.QtWidgets import QApplication
from QCandyUi import CandyWindow

from LogViewer import LogViewer


def run_with_titlebar():
    app = QApplication(sys.argv)
    w = CandyWindow.createWindow(LogViewer(), 'Log Viewer', 'myicon.ico', 'blue')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_with_titlebar()
