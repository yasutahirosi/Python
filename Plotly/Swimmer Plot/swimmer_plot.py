#导入所需模块
import plotly.graph_objs as go
import plotly.offline as py 
import pandas as pd
import numpy as np
import random

#创建样本数据
CR=pd.Series(np.random.randint(low=1,high=30,size=30))
PR=pd.Series(np.random.randint(low=1,high=30,size=30))
PD=pd.Series(np.random.randint(low=1,high=30,size=30))
LB=["Ongoing","Died"]*15
random.shuffle(LB)
data=pd.DataFrame({"CR":CR,"PR":PR,"PD":PD,"LB":LB})
data["SUM"]=data["CR"]+data["PR"]+data["PD"]
order=["CR","PR","PD","SUM","LB"]
data=data[order]
data.reset_index(inplace=True)
data.rename(columns={"index":"SB"},inplace=True)
data.sort_values("SUM",ascending=True,inplace=True)
data.reset_index(drop=True,inplace=True)
y=["A"+str(i) for i in data["SB"]]
data.to_csv("swimmer.csv")

#Setting Trace details
# 01 trace1_color
trace1_color=[]
for i in data["LB"]:
    if i=="Ongoing":
        trace1_color.append("lightseagreen")
    else:
        trace1_color.append("steelblue")
# dot symbol
marker2=dict(color="peru",size=10)
marker3=dict(color="khaki",size=10,symbol="diamond-dot")
marker4=dict(color="lavenderblush",size=10,symbol="hexagon-dot")

#arrow for Ongoing stage
trace_5=[]
for j in range(len(data["LB"])):
    if data["LB"][j]=="Ongoing":
        trace_5.append(data["SUM"][j]+2)
    else:
        trace_5.append(" ")        
marker5=dict(color="red",size=10,symbol=208)

#Trace
trace1=go.Bar(x=data["SUM"],y=y,orientation="h",showlegend=False,marker=dict(color=trace1_color),text=data["SUM"],textposition="outside")
trace2=go.Scatter(x=data["CR"],y=y,orientation="h",mode="markers",marker=marker2,name="Compeletely Response")
trace3=go.Scatter(x=data["PR"],y=y,orientation="h",mode="markers",marker=marker3,name="Partial Response")
trace4=go.Scatter(x=data["PD"],y=y,orientation="h",mode="markers",marker=marker4,name="Progressive Disease")
trace5=go.Scatter(x=trace_5,y=y,orientation="h",mode="markers",marker=marker5,name="Ongoing")
trace=[trace1,trace2,trace3,trace4,trace5]

#Layout
layout=go.Layout(title="Swimmer plot by Python")
fig=go.Figure(data=trace,layout=layout)

#Setting layout details
xaxis=dict(title="Weeks")
yaxis=dict(title="Subjets",)
fig.layout.update(xaxis=xaxis,yaxis=yaxis)
py.plot(fig)









