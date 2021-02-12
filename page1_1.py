import sys
import os

from page1.page_main import *
from page1.page_main import Ui_Window1


class Window1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Window1()
        self.ui.setupUi(self)

        self.b=self.ui.pushButton_all
        self.n = self.ui.pushButton_new
        self.d = self.ui.pushButton_del
        self.g2 = self.ui.groupBox_2
        self.up=self.ui.pushButton_update
        self.ier=self.ui.pushButton_ierarx