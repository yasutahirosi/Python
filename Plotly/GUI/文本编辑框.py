import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.resize(700,700)
		self.setWindowTitle('QtextEdit Test')
		self.text_edit=QTextEdit(self)
		self.text_edit.setText("Life is beautiful")
		self.text_edit.setPlaceholderText("Please edit your text here")
		self.text_edit.textChanged.connect(lambda:print("text changed"))
		self.save_button=QPushButton("save",self)
		self.clear_button=QPushButton("Clear",self)
		self.view=QWebEngineView()

		self.h_layout=QHBoxLayout()
		self.h_layout.addWidget(self.save_button)
		self.h_layout.addWidget(self.clear_button)

		self.v_layout=QVBoxLayout()
		self.v_layout.addWidget(self.text_edit)
		self.v_layout.addLayout(self.h_layout)
		self.v_layout.addWidget(self.view)

		self.setLayout(self.v_layout)

	def btn_slot(self,btn):
		if btn==self.save_button:
			with open("abc.txt","w") as f:
				f.write(self.text_edit.toPlainText())
		elif btn==self.clear_button:
			self.text_edit.clear()

if __name__=="__main__":
	app=QApplication(sys.argv)
	demo=Demo()
	demo.show()
	sys.exit(app.exec_())







