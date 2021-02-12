import sys
import os

from page1.page_main import *
from page1.page_all import Ui_Window2
from page1.page_main import Ui_Window1
from page1.page_new import Ui_Window3
from page1.page_del import Ui_Window4

import base
import page5
import page6
import page1_1
import page2_1


class Window3(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Window3()
        self.ui.setupUi(self)

        self.b = self.ui.pushButton_all
        self.n = self.ui.pushButton_new
        self.d = self.ui.pushButton_del
        self.up = self.ui.pushButton_update
        self.ier = self.ui.pushButton_ierarx

        self.imagebtn = self.ui.selectImagebtn
        self.ok = self.ui.pushButton_newOk

        self.path=""

    def madeNew(self):
        chast=["Армия", "Дивизия", "Полк", "Дивизион", "Взвод"]
        s=self.ui.lineEdit_name.text()
        lst = s.split()
        param=0
        for namechast in chast:
            if namechast==lst[0]:
                #print(lst[0] + " = ура")
                param=1

        if param==1 and self.ui.lineEdit_idparent.text()==None or self.ui.lineEdit_idparent.text()=="":
            self.ui.label_com.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            self.ui.label_com.setText("Часть должна иметь родителя (Номер подчинения - id_parent).")

        else:
            if self.ui.lineEdit_state.text()==None or self.ui.lineEdit_state.text()=="":
                self.state=None
            else:
                self.state=self.ui.lineEdit_state.text()
            if self.ui.lineEdit_idparent.text()==None or self.ui.lineEdit_idparent.text()=="":
                self.parent=None
            else:
                self.parent=self.ui.lineEdit_idparent.text()

            if self.path =="" or self.path==None:

                m = [self.parent, self.ui.lineEdit_name.text(), None, self.state]
                base.new_element(base.db, base.table, m)
                self.ui.label_com.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
                self.ui.label_com.setText("Данные успешно добавлены.")
            else:
                m = [self.parent, self.ui.lineEdit_name.text(), base.image_binary(self.path),
                     self.state]
                base.new_element(base.db, base.table, m)
                self.ui.label_com.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
                self.ui.label_com.setText("Данные успешно добавлены.")





    def selectImage(self):

        filename, _=QtWidgets.QFileDialog.getOpenFileName(None,"Select Image", "", "Image File (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            pixmap=QtGui.QPixmap(filename)
            pixmap=pixmap.scaled(self.ui.lblImage.width(), self.ui.lblImage.width(), QtCore.Qt.KeepAspectRatio)
            self.ui.lblImage.setPixmap(pixmap)
            self.ui.lblImage.setAlignment(QtCore.Qt.AlignCenter)
            self.path = os.path.abspath(filename)