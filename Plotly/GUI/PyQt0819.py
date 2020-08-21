import sys
from PyQt5.QtWidgets import QApplication,QLabel,Qwidget,QPushButton

class Demo(Qwidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.label=QLabel("Label",self)





app=QApplication(sys.argv)
label1=QLabel("Hello PyQt5")
label1.show()
sys.exit(app.exec_())
