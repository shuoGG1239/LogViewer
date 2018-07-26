from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget

from ui_searchForm import Ui_SearchForm


class SearchForm(QWidget):
    signal_key = pyqtSignal(int)

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

    def keyPressEvent(self, e):
        if (e.modifiers() == Qt.NoModifier) and (e.key() == Qt.Key_Return):
            self.signal_key.emit(Qt.Key_Return)
        elif (e.modifiers() == Qt.ShiftModifier) and (e.key() == Qt.Key_Return):
            self.signal_key.emit(Qt.Key_Return + Qt.ShiftModifier)
        elif (e.modifiers() == Qt.ControlModifier) and (e.key() == Qt.Key_F):
            self.ui.pushButtonClose.click()
        elif (e.modifiers() == Qt.NoModifier) and (e.key() == Qt.Key_Escape):
            self.ui.pushButtonClose.click()
