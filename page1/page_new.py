# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3-new.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window3(object):
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")
        Window3.resize(805, 607)
        Window3.setMinimumSize(QtCore.QSize(805, 607))
        Window3.setMaximumSize(QtCore.QSize(805, 607))
        Window3.setLocale(QtCore.QLocale(QtCore.QLocale.Samburu, QtCore.QLocale.Kenya))
        self.centralwidget = QtWidgets.QWidget(Window3)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 90, 21, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 801, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(270, 20, 241, 41))
        self.label.setLineWidth(5)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 90, 651, 491))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_idparent = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_idparent.setGeometry(QtCore.QRect(160, 110, 171, 20))
        self.lineEdit_idparent.setObjectName("lineEdit_idparent")
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_name.setGeometry(QtCore.QRect(160, 220, 171, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_state = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_state.setGeometry(QtCore.QRect(160, 340, 171, 20))
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 141, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 131, 81))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 101, 61))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 621, 91))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(440, 310, 181, 61))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 430, 131, 41))
        self.label_10.setObjectName("label_10")
        self.label_com = QtWidgets.QLabel(self.groupBox_2)
        self.label_com.setGeometry(QtCore.QRect(140, 440, 491, 21))
        self.label_com.setObjectName("label_com")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(0, 420, 651, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lblImage = QtWidgets.QLabel(self.groupBox_2)
        self.lblImage.setGeometry(QtCore.QRect(360, 130, 281, 181))
        self.lblImage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImage.setText("")
        self.lblImage.setObjectName("lblImage")
        self.selectImagebtn = QtWidgets.QPushButton(self.groupBox_2)
        self.selectImagebtn.setGeometry(QtCore.QRect(360, 320, 75, 23))
        self.selectImagebtn.setObjectName("selectImagebtn")
        self.pushButton_newOk = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_newOk.setGeometry(QtCore.QRect(210, 380, 221, 41))
        self.pushButton_newOk.setObjectName("pushButton_newOk")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 90, 151, 491))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_new = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_new.setGeometry(QtCore.QRect(30, 40, 91, 23))
        self.pushButton_new.setObjectName("pushButton_new")
        self.pushButton_all = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_all.setGeometry(QtCore.QRect(30, 70, 91, 23))
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_update.setGeometry(QtCore.QRect(30, 100, 91, 23))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_del = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_del.setGeometry(QtCore.QRect(30, 160, 91, 23))
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_ierarx = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_ierarx.setGeometry(QtCore.QRect(30, 130, 91, 23))
        self.pushButton_ierarx.setObjectName("pushButton_ierarx")
        Window3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        Window3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window3)
        self.statusbar.setObjectName("statusbar")
        Window3.setStatusBar(self.statusbar)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "Новая запись"))
        self.label.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Тестовое задание</span></p></body></html>"))
        self.label_2.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Номер родителя</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">(id_parent)</span></p></body></html>"))
        self.label_3.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Название </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">подразделения</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">(name)</span></p></body></html>"))
        self.label_4.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Состояние</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">(state)</span></p></body></html>"))
        self.label_7.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Заполните строки, </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">для формирования новой записи.</span></p></body></html>"))
        self.label_8.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Эмблема подразделения</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">(если есть)</span></p></body></html>"))
        self.label_10.setText(_translate("Window3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Комментарий: </span></p></body></html>"))
        self.label_com.setText(_translate("Window3", "<html><head/><body><p><br/></p></body></html>"))
        self.selectImagebtn.setText(_translate("Window3", "selectImage"))
        self.pushButton_newOk.setText(_translate("Window3", "Внести данные"))
        self.pushButton_new.setText(_translate("Window3", "Новая запись"))
        self.pushButton_all.setText(_translate("Window3", "Вывести всех"))
        self.pushButton_update.setText(_translate("Window3", "Редактировать"))
        self.pushButton_del.setText(_translate("Window3", "Удалить"))
        self.pushButton_ierarx.setText(_translate("Window3", "Иерархия"))
