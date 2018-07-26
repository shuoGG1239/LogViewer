from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from ui_searchForm import Ui_SearchForm


class SearchForm(QWidget):
    signal_response = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self)

    def on_pushButtonClose_clicked(self):
        self.hide()

    def on_pushButtonForward_clicked(self):
        pass

    def on_pushButtonBackward_clicked(self):
        pass
