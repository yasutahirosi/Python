import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

# Create random data with numpy
data=pd.read_sas(r"C:\Users\luoz14\OneDrive - Pfizer\Test Data\adpc_f001.sas7bdat",
                 encoding='latin1')

data=data.drop_duplicates(['_X','TRTA'])

fig = go.Figure()

trt1=data.query("TRTA=='60 mg IR'")
trt2=data.query("TRTA=='60 mg MR1'")
trt3=data.query("TRTA=='60 mg MR1, fed'")
# Add traces
fig.add_trace(go.Scatter(x=trt1._X, y=trt1.AVAL,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=trt2._X, y=trt2.AVAL,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=trt3._X, y=trt3.AVAL,
                    mode='lines+markers',
                    name='lines+markers'))



plot(fig)