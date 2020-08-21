import sys
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 设置窗口大小
        self.resize(300, 300)

        # 添加相应需要的控件
        self.label_test = QLabel(" 你猜？",self)
        self.btn=QPushButton("索尼倒闭了吗",self)
        self.btn.clicked.connect(lambda :self.change_text("倒闭了"))
        self.btn.clicked.connect(self.change_size)



        #对控件进行布局
        self.v_layout=QVBoxLayout()
        self.v_layout.addWidget(self.label_test)
        self.v_layout.addWidget(self.btn)
        self.setLayout(self.v_layout)

    def change_text(self,text):
        self.label_test.setText(text)
        print(text)
    def change_size(self):
        self.resize(1000,1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    app.processEvents()
    status = app.exec_()
    sys.exit(status)
