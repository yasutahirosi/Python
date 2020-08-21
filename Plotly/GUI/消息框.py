import sys
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.setWindowTitle("消息框测试")
        self.btn1=QPushButton("测试一",self)
        self.btn2 = QPushButton("测试一", self)
        self.btn1.clicked.connect(lambda:self.show_msg_box(self.btn1))
        self.btn2.clicked.connect(lambda: self.show_msg_box(self.btn2))


        self.vlayout=QVBoxLayout()
        self.vlayout.addWidget(self.btn1)
        self.vlayout.addWidget(self.btn2)
        self.setLayout(self.vlayout)

    def show_msg_box(self,btn):
        if btn==self.btn1:
            choice=QMessageBox.question(self,"弹出来1","你想保存吗",QMessageBox.Yes|QMessageBox.No)
            if choice==QMessageBox.Yes:
                print("保存好了哦")
                self.close()
            elif choice==QMessageBox.No:
                self.close()
        elif btn==self.btn2:
            QMessageBox.information(self,"好的","好烦啊",QMessageBox.Ok)





if __name__=="__main__":
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())
