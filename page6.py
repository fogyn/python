import os

from PyQt5.QtCore import Qt
from PyQt5.uic.properties import QtWidgets
import base
from page1.page_main import *

from page1.page_update import Ui_Window6

class Window6(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Window6()
        self.ui.setupUi(self)

        self.b = self.ui.pushButton_all
        self.n = self.ui.pushButton_new
        self.d = self.ui.pushButton_del
        self.ier = self.ui.pushButton_ierarx
        self.up = self.ui.pushButton_update

        self.btn_select = self.ui.pushButton_select_ok
        self.imagebtn = self.ui.selectImagebtn
        self.btn_update=self.ui.pushButton_newOk_2

        self.x = 0
    def made_update(self):

        if self.ui.lineEdit_idparent.text()=="" or self.ui.lineEdit_idparent.text()==None:
            id_parent=self.parent
        else:
            id_parent = self.ui.lineEdit_idparent.text()

        if self.ui.lineEdit_name.text()=="" or self.ui.lineEdit_name.text()==None:
            name=self.name
        else:
            name = self.ui.lineEdit_name.text()

        if self.ui.lineEdit_state.text()=="" or self.ui.lineEdit_state.text()==None:
            state=self.state
        else:
            state = self.ui.lineEdit_state.text()
#

        if self.x==0:

            if self.image=="есть":

                pth = "./outimage/"+str(self.id2)+".png"
                self.m = (id_parent, name, base.image_binary(pth), state, self.id2)
            else:

                self.m = (id_parent, name, None, state, self.id2)

        else:

            self.m = (id_parent, name, base.image_binary(self.path2), state, self.id2)


        base.element_update(base.db, base.table, self.m)

        self.ui.label_com.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.ui.label_com.setText("Данные упешно отредактированы.")

    def delImage(self):
        path="./outimage/"

        filelist = [f for f in os.listdir(path) if f.endswith(".png")]
        for f in filelist:
            os.remove(os.path.join(path, f))

    def getImage(self, name):
        path = "./outimage/" + str(name) + ".png"
        #print(path)
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(self.ui.lblImage_2.width(), self.ui.lblImage_2.width(), QtCore.Qt.KeepAspectRatio)
        #print("!!!")
        self.ui.lblImage_2.setPixmap(pixmap)
        self.ui.lblImage_2.setAlignment(QtCore.Qt.AlignCenter)

    def select_id(self):
        id = self.ui.lineEdit_id.text()
        self.id2=id
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
            result2 =base.element_select_param(base.db, base.table, 'id', id)
            for row in result2:
                self.parent = row[1]
                self.name = row[2]
                self.state = row[4]

                self.ui.label_parent_2.setText(str(self.parent))
                self.ui.label_parent_2.setAlignment(Qt.AlignCenter)
                self.ui.label_name_2.setText(self.name)
                self.ui.label_name_2.setAlignment(Qt.AlignCenter)
                self.ui.label_state_2.setText(str(self.state))
                self.ui.label_state_2.setAlignment(Qt.AlignCenter)
                if row[3] != None:
                    self.image ="есть"
                    self.delImage()
                    base.image_db_image(row[3], id)
                    self.getImage(id)
                else:
                    self.image = "Фото нет"
                    self.ui.lblImage_2.setText(self.image)





            self.ui.label_com.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
            self.ui.label_com.setText("Данные выведены")

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
        self.ui.label_com.setText("Выберите из представленных номеров, тот который требуется отобразить!")

    def selectImage(self):

        filename, _=QtWidgets.QFileDialog.getOpenFileName(None,"Select Image", "", "Image File (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            pixmap=QtGui.QPixmap(filename)
            pixmap=pixmap.scaled(self.ui.lblImage.width(), self.ui.lblImage.width(), QtCore.Qt.KeepAspectRatio)
            self.ui.lblImage.setPixmap(pixmap)
            self.ui.lblImage.setAlignment(QtCore.Qt.AlignCenter)
            self.path2 = os.path.abspath(filename)
            self.x=1
            #print(self.path2)