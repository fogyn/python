from PyQt5 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.uic.properties import QtWidgets
from page1.page_main import *


from page1.page_ierarh import Ui_Window5

class Window5(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Window5()
        self.ui.setupUi(self)

        self.b = self.ui.pushButton_all
        self.n = self.ui.pushButton_new
        self.d = self.ui.pushButton_del
        self.up = self.ui.pushButton_update
        self.ier = self.ui.pushButton_ierarx

        self.tree = self.ui.treeWidget
        self.item=QtWidgets.QTreeWidgetItem

    def ierarhiy(self, result):

        self.tree.headerItem().setText(0, "Звено")

        self.tree.headerItem()
        self.tree.headerItem().setText(1, "Армия")

        self.tree.headerItem()
        self.tree.headerItem().setText(2, "Дивизия")

        self.tree.headerItem()
        self.tree.headerItem().setText(3, "Полк")

        self.tree.headerItem()
        self.tree.headerItem().setText(4, "Дивизион")

        self.tree.headerItem()
        self.tree.headerItem().setText(5, "Взвод")


        self.mask=[]
        for row in result:
            parent = row[1]
            if parent==None:
                #print(row)
                it = self.item(self.tree)
                it.setText(0, row[2])
                if row[4] == 0:
                    it.setBackground(2, QColor("red"))
                if row[4] == 1:
                    it.setBackground(2, QColor("yellow"))
                if row[4] == 2:
                    it.setBackground(2, QColor("green"))

                list = [row[0], row[2], row[4], 0, it]
                self.mask.append(list)
                result.remove(row)

        for row2 in self.mask:
            for row in result:
                if row[1]==row2[0]:
                    it = self.item(row2[4])
                    col = row2[3] + 1
                    it.setText(col, row[2])
                    if row[4] == 0:
                        it.setBackground(col, QColor("red"))
                    if row[4] == 1:
                        it.setBackground(col, QColor("yellow"))
                    if row[4] == 2:
                        it.setBackground(col, QColor("green"))


                    list = [row[0], row[2], row[4],col, it]
                    self.mask.append(list)
                    #result.remove(row)
                else:
                    continue

        self.ui.label_com.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.ui.label_com.setText("Иерархия данных из таблицы - построена!")


