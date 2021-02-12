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
import page4_1

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Window1()
        self.ui.setupUi(self)




    def show_new(self):
        self.w3 = page3_1.Window3()

        self.w3.b.clicked.connect(self.show_all)
        self.w3.b.clicked.connect(self.w3.close)
        self.w3.imagebtn.clicked.connect(self.w3.selectImage)
        self.w3.ok.clicked.connect(self.w3.madeNew)

        self.w3.n.clicked.connect(self.show_new)
        self.w3.n.clicked.connect(self.w3.close)

        self.w3.d.clicked.connect(self.show_del)
        self.w3.d.clicked.connect(self.w3.close)

        self.w3.up.clicked.connect(self.show_up)
        self.w3.up.clicked.connect(self.w3.close)

        self.w3.ier.clicked.connect(self.show_ier)
        self.w3.ier.clicked.connect(self.w3.close)

        self.w3.show()


    def show_all(self):
        self.w2 = page2_1.Window2()

        self.w2.n.clicked.connect(self.show_new)
        self.w2.n.clicked.connect(self.w2.delImage)
        self.w2.n.clicked.connect(self.w2.close)

        self.w2.b.clicked.connect(self.show_all)
        self.w2.b.clicked.connect(self.w2.close)

        self.w2.d.clicked.connect(self.show_del)
        self.w2.d.clicked.connect(self.w2.close)

        self.w2.up.clicked.connect(self.show_up)
        self.w2.up.clicked.connect(self.w2.close)

        self.w2.ier.clicked.connect(self.show_ier)
        self.w2.ier.clicked.connect(self.w2.close)


        result = base.element_all(base.db,base.table)
        self.w2.blue(result)

        self.w2.show()

    def show_del(self):
        self.w4 = page4_1.Window4()
        result = base.element_all_id(base.db, base.table)

        self.w4.all_id(result)

        self.w4.b.clicked.connect(self.show_all)
        self.w4.b.clicked.connect(self.w4.close)

        self.w4.n.clicked.connect(self.show_new)
        self.w4.n.clicked.connect(self.w4.close)

        self.w4.d.clicked.connect(self.show_del)
        self.w4.d.clicked.connect(self.w4.close)

        self.w4.up.clicked.connect(self.show_up)
        self.w4.up.clicked.connect(self.w4.close)

        self.w4.ier.clicked.connect(self.show_ier)
        self.w4.ier.clicked.connect(self.w4.close)

        self.w4.btndel.clicked.connect(self.w4.del_id)

        self.w4.show()

    def show_ier(self):
        self.w5=page5.Window5()
        result = base.element_all(base.db, base.table)
        self.w5.ierarhiy(result)


        self.w5.b.clicked.connect(self.show_all)
        self.w5.b.clicked.connect(self.w5.close)

        self.w5.n.clicked.connect(self.show_new)
        self.w5.n.clicked.connect(self.w5.close)

        self.w5.d.clicked.connect(self.show_del)
        self.w5.d.clicked.connect(self.w5.close)

        self.w5.ier.clicked.connect(self.show_ier)
        self.w5.ier.clicked.connect(self.w5.close)

        self.w5.up.clicked.connect(self.show_up)
        self.w5.up.clicked.connect(self.w5.close)

        self.w5.show()

    def show_up(self):
        self.w6=page6.Window6()
        result = base.element_all_id(base.db, base.table)
        self.w6.all_id(result)

        self.w6.b.clicked.connect(self.show_all)
        self.w6.b.clicked.connect(self.w6.close)

        self.w6.n.clicked.connect(self.show_new)
        self.w6.n.clicked.connect(self.w6.close)

        self.w6.d.clicked.connect(self.show_del)
        self.w6.d.clicked.connect(self.w6.close)

        self.w6.ier.clicked.connect(self.show_ier)
        self.w6.ier.clicked.connect(self.w6.close)

        self.w6.up.clicked.connect(self.show_up)
        self.w6.up.clicked.connect(self.w6.close)

        self.w6.btn_select.clicked.connect(self.w6.select_id)
        self.w6.imagebtn.clicked.connect(self.w6.selectImage)
        self.w6.btn_update.clicked.connect(self.w6.made_update)

        self.w6.show()


    def show_main(self):
        self.w1 = page1_1.Window1()

        self.w1.b.clicked.connect(self.show_all)
        self.w1.b.clicked.connect(self.w1.close)

        self.w1.n.clicked.connect(self.show_new)
        self.w1.n.clicked.connect(self.w1.close)

        self.w1.d.clicked.connect(self.show_del)
        self.w1.d.clicked.connect(self.w1.close)

        self.w1.up.clicked.connect(self.show_up)
        self.w1.up.clicked.connect(self.w1.close)

        self.w1.ier.clicked.connect(self.show_ier)
        self.w1.ier.clicked.connect(self.w1.close)

        self.w1.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    #myapp.show()
    myapp.show_main()
    sys.exit(app.exec_())



