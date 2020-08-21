# -*- coding:UTF-8 -*-
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
        self.btn.clicked.connect(self.change_text)

        #对控件进行布局
        self.v_layout=QVBoxLayout()
        self.v_layout.addWidget(self.label_test)
        self.v_layout.addWidget(self.btn)
        self.setLayout(self.v_layout)

    def change_text(self):
        self.label_test.setText("倒闭了")
        print("why")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    status = app.exec_()
    sys.exit(status)
