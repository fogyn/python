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

class Window2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Window2()
        self.ui.setupUi(self)

        self.n = self.ui.pushButton_new
        self.b = self.ui.pushButton_all
        self.d = self.ui.pushButton_del
        self.up = self.ui.pushButton_update
        self.ier = self.ui.pushButton_ierarx

        self.area = self.ui.scrollArea
        self.bluebtn = self.ui.pushButton_update



    def delImage(self):
        path="./outimage/"

        filelist = [f for f in os.listdir(path) if f.endswith(".png")]
        for f in filelist:
            os.remove(os.path.join(path, f))

    def getImage(self, name):
        path = "./outimage/" + str(name) + ".png"
        #print(path)
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(self.lblimage.width(), self.lblimage.width(), QtCore.Qt.KeepAspectRatio)
        self.lblimage.setPixmap(pixmap)
        self.lblimage.setAlignment(QtCore.Qt.AlignCenter)


    def blue(self,result):
        self.font = QtGui.QFont()
        self.font.setBold(True)

        for row in result:
            id = row[0]
            id_parent = row[1]
            name = row[2]
            state = row[4]

            self.g = QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents)
            self.g.setMinimumSize(QtCore.QSize(651, 91))
            self.g.setMaximumSize(QtCore.QSize(651, 91))
            self.g.setTitle("")
            self.g.setObjectName("gb_x")
            self.h = QtWidgets.QHBoxLayout(self.g)
            self.h.setContentsMargins(0, -1, 0, -1)
            self.h.setObjectName("horizontalLayout_x")

            self.l1 = QtWidgets.QLabel(self.g)
            self.l1.setLineWidth(3)
            self.l1.setObjectName("label_id_x")
            self.l1.setText("id")
            self.l1.setFont(self.font)
            self.h.addWidget(self.l1)
            self.line1 = QtWidgets.QLineEdit(self.g)
            self.line1.setObjectName("lineEdit_id_x")
            self.line1.setText(str(id))
            self.h.addWidget(self.line1)

            self.l2 = QtWidgets.QLabel(self.g)
            self.l2.setObjectName("label_parent_x")
            self.l2.setText("id_parent")
            self.l2.setFont(self.font)
            self.h.addWidget(self.l2)
            self.line2 = QtWidgets.QLineEdit(self.g)
            self.line2.setObjectName("lineEdit_parent_x")
            self.line2.setText(str(id_parent))
            self.h.addWidget(self.line2)

            self.l3 = QtWidgets.QLabel(self.g)
            self.l3.setObjectName("label_name_x")
            self.l3.setText("name")
            self.l3.setFont(self.font)
            self.h.addWidget(self.l3)
            self.line3 = QtWidgets.QLineEdit(self.g)
            self.line3.setObjectName("lineEdit_name_x")
            self.line3.setText(name)

            if state==0:
                self.line3.setStyleSheet("background:rgb(255, 0, 0)")
            if state==1:
                self.line3.setStyleSheet("background:rgb(255, 255, 0)")
            if state==2:
                self.line3.setStyleSheet("background:rgb(0, 255, 0)")
            self.h.addWidget(self.line3)

            self.l4 = QtWidgets.QLabel(self.g)
            self.l4.setObjectName("label_image_x")
            self.l4.setText("image")
            self.l4.setFont(self.font)
            self.h.addWidget(self.l4)
            self.lblimage = QtWidgets.QLabel(self.g)
            self.lblimage.setFrameShape(QtWidgets.QFrame.Box)
            self.lblimage.setObjectName("lblimage_x")

            if row[3] != None:
                self.delImage()
                base.image_db_image(row[3], id)
                self.getImage(id)
            else:
                image="Фото нет"
                self.lblimage.setText(image)
            #self.lblimage.setText("TextLabel")
            self.h.addWidget(self.lblimage)

            self.l5 = QtWidgets.QLabel(self.g)
            self.l5.setObjectName("label_state_x")
            self.l5.setText("state")
            self.l5.setFont(self.font)
            self.h.addWidget(self.l5)
            self.line5 = QtWidgets.QLineEdit(self.g)
            self.line5.setObjectName("lineEdit_state_x")
            self.line5.setText(str(state))
            self.h.addWidget(self.line5)

            self.ui.verticalLayout.addWidget(self.g)
            self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents)

        self.ui.label_com.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.ui.label_com.setText("Все записи успешно извлечены!")