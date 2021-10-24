from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTax - Sistema de cadastro de empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    app.exec()