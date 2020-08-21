import sys
import plotly as py
import plotly.graph_objs as go
import pandas as pd
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import *

def show_qt(fig):
    raw_html = '<html><head><meta charset="utf-8" />'
    raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
    raw_html += '<body>'
    raw_html += py.offline.plot(fig, include_plotlyjs=False, output_type='div')
    raw_html += '</body></html>'
    fig_view = QWebEngineView()
    fig_view.setHtml(raw_html)
    fig_view.show()
    fig_view.raise_()
    return fig_view


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    data=pd.read_csv("waterfall.csv")
    data.sort_values("LSPCHG",ascending=False,inplace=True)
    data.reset_index()
    y=data["LSPCHG"]
    z=data["LSRESP"]
    x=data["USUBJID"]
    colors=["lightseagreen",]*54
    for i in range(len(data["DRUG"])):
        if data["DRUG"][i]=="Treatment B":
            colors[i]="steelblue"
    trace1=go.Bar(x=x,y=y,marker_color=colors
    ,text=z,textposition="outside",width=1,name="Treatment B")
    trace2=go.Bar(x=x,y=y,marker_color="lightseagreen" 
    ,text=z,textposition="outside",width=1,name="Treatment A",visible="legendonly")
    image=[trace1,trace2]
    shape1=dict(type="line",x0=-0.5,y0=-30,x1=54,y1=-30,line=dict(color="blue",width=2,dash="longdash"))
    shape2=dict(type="line",x0=-0.5,y0=30,x1=54,y1=30,line=dict(color="steelblue",width=2,dash="longdash"))
    shape=[shape1,shape2]
    xaxis=dict(title="Subjects",titlefont_size=13)
    yaxis=dict(title="Best Percentage Change From Baseline",titlefont_size=13)
    annotations = [go.layout.Annotation(dict(x =0,y = -70,xref="paper",
    text = "CR=COMPLETE RESPONSE<br>PR=PARTIAL RESPONSE<br>SD=STABLE DISEASE<br>PD=PROGRESSION DISEASE",
    align="left",font = dict(size=10),showarrow = False,bordercolor="forestgreen",borderwidth=2))]
    layout=go.Layout(showlegend=True,title="Waterfall Plot In oncology",shapes=shape,xaxis=xaxis,yaxis=yaxis,annotations=annotations)
    fig = go.Figure(data=image,layout=layout)
    fig_view = show_qt(fig)
    sys.exit(app.exec_())

    Hermes: connect kernel