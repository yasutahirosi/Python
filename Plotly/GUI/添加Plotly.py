# -*- coding:UTF-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly as py
import plotly.graph_objs as go
import pandas as pd


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(1000, 1000)
        self.setWindowTitle("Powered By PyQt5")
        self.user_label = QLabel("Subjects", self)
        self.user_line = QLineEdit(self)
        self.pwd_label = QLabel("Rate", self)
        self.pwd_line = QLineEdit(self)
        self.log_btn=QPushButton("Save",self)
        self.sign_btn=QPushButton("Clear",self)
        self.view=QWebEngineView()
        self.view.setHtml(raw_html)
        self.cb=QComboBox(self)
        self.cb.addItem("X")
        self.cb.addItem("Y")





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


    #导入数据
    data=pd.read_csv("waterfall.csv")
    data.sort_values("LSPCHG",ascending=False,inplace=True)
    data.reset_index()
    y=data["LSPCHG"]
    z=data["LSRESP"]
    x=data["USUBJID"]

    #设置图像
    colors=["lightseagreen",]*54
    for i in range(len(data["DRUG"])):
        if data["DRUG"][i]=="Treatment B":
            colors[i]="steelblue"

    trace1=go.Bar(x=x,y=y,marker_color=colors
    ,text=z,textposition="outside",width=1,name="Treatment B")
    trace2=go.Bar(x=x,y=y,marker_color="lightseagreen"
    ,text=z,textposition="outside",width=1,name="Treatment A",visible="legendonly")
    image=[trace1,trace2]

    #设置图层
    #01 增加参考线
    shape1=dict(type="line",x0=-0.5,y0=-30,x1=54,y1=-30,line=dict(color="blue",width=2,dash="longdash"))
    shape2=dict(type="line",x0=-0.5,y0=30,x1=54,y1=30,line=dict(color="steelblue",width=2,dash="longdash"))
    shape=[shape1,shape2]
    #02 对坐标轴进行设置
    xaxis=dict(title="Subjects",titlefont_size=13)
    yaxis=dict(title="Best Percentage Change From Baseline",titlefont_size=13)
    #03 增加注释
    annotations = [go.layout.Annotation(dict(x =0,y = -70,xref="paper",
    text = "CR=COMPLETE RESPONSE<br>PR=PARTIAL RESPONSE<br>SD=STABLE DISEASE<br>PD=PROGRESSION DISEASE",
    align="left",font = dict(size=10),showarrow = False,bordercolor="forestgreen",borderwidth=2))]
    layout=go.Layout(showlegend=True,title="Waterfall Plot In oncology",shapes=shape,xaxis=xaxis,yaxis=yaxis,annotations=annotations)

    #整合图和图层
    fig=go.Figure(data=image,layout=layout)

    #QT
    raw_html = '<html><head><meta charset="utf-8" />'
    raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
    raw_html += '<body>'
    raw_html += py.offline.plot(fig, include_plotlyjs=False, output_type='div')
    raw_html += '</body></html>'

    demo = Demo()
    demo.show()
    status = app.exec_()
    sys.exit(status)
