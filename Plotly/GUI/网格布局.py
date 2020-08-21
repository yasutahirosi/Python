import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 设置窗口大小
        self.resize(300, 300)

        # 添加相应需要的控件
        #01 标签控件
        self.user_label = QLabel("用户名", self)
        #02 输入控件
        self.user_line = QLineEdit(self)
        self.pwd_label = QLabel("密码", self)
        self.pwd_line = QLineEdit(self)
        #03 按钮控件
        self.log_btn=QPushButton("登入",self)
        self.sign_btn=QPushButton("登出",self)
        #04 网络浏览控件
        self.view=QWebEngineView()




        #对控件进行布局
        self.grid_layout=QGridLayout()
        self.grid_layout.addWidget(self.user_label,0,0)
        self.grid_layout.addWidget(self.user_line,0,1)
        self.grid_layout.addWidget(self.pwd_label,1,0)
        self.grid_layout.addWidget(self.pwd_line,1,1)


        self.h_layout=QHBoxLayout()
        self.h_layout.addWidget(self.log_btn)
        self.h_layout.addWidget(self.sign_btn)


        self.v_layout=QVBoxLayout()
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.view)
        self.setLayout(self.v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    status = app.exec_()
    sys.exit(status)
