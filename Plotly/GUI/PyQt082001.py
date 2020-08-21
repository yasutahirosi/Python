import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 设置窗口大小
        self.resize(300, 300)

        # 添加相应需要的控件
        self.username_label = QLabel("用户名", self)
        self.user_line = QLineEdit(self)
        self.pwd_label = QLabel("密码", self)
        self.pwd_line = QLineEdit(self)

        #对控件进行布局
        self.h_layout_0 = QHBoxLayout()
        self.h_layout_0.addWidget(self.username_label)
        self.h_layout_0.addWidget(self.user_line)

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_1.addWidget(self.pwd_label)
        self.h_layout_1.addWidget(self.pwd_line)

        #添加布局
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout_0)
        self.v_layout.addLayout(self.h_layout_1)
        self.setLayout(self.v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    status = app.exec_()
    sys.exit(status)
