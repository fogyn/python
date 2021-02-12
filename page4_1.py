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
import page3_1


class Window4(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Window4()
        self.ui.setupUi(self)

        self.b=self.ui.pushButton_all
        self.n = self.ui.pushButton_new
        self.d = self.ui.pushButton_del
        self.up = self.ui.pushButton_update
        self.ier = self.ui.pushButton_ierarx

        self.btndel = self.ui.pushButton_del_ok



    def del_id(self):
        id = self.ui.lineEdit_id.text()
        #idd = "("+id+",)"
        bull = False
        #print(id)
        #print(idd)
        for row in self.rez:
            rowitem = row[0]
            if str(rowitem)==id:
                bull = True

        if bull == False:
            self.ui.label_com.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
            self.ui.label_com.setText("Выбранное число не подходит. Нет в базе")
        else:
            base.element_del(base.db, base.table, 'id', id)
            self.ui.label_com.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
            self.ui.label_com.setText("Данные удалены")


    def all_id(self, result):
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.rez=result
        for row in result:
            rowitem=row[0]
            self.g = QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents)
            self.g.setMinimumSize(QtCore.QSize(120, 40))
            self.g.setMaximumSize(QtCore.QSize(120, 40))
            self.g.setTitle("")
            self.g.setObjectName("gb_x")
            self.h = QtWidgets.QHBoxLayout(self.g)
            self.h.setContentsMargins(0, -1, 0, -1)
            self.h.setObjectName("horizontalLayout_x")

            self.l1 = QtWidgets.QLabel(self.g)
            self.l1.setLineWidth(10)
            self.l1.setObjectName("label_id_xx")
            self.l1.setText("id")
            self.l1.setFont(self.font)
            self.h.addWidget(self.l1)

            self.line1 = QtWidgets.QLineEdit(self.g)
            self.line1.setObjectName("lineEdit_id_x")
            self.line1.setText(str(rowitem))
            self.h.addWidget(self.line1)


            self.ui.verticalLayout.addWidget(self.g)
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)

        self.ui.label_com.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.ui.label_com.setText("Выберите из представленных номеров, тот который требуется удалить!")