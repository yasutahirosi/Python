# Module----------------------------------------------------------------
import yfinance as yf

import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots


# Get Bitcoin data-----------------------------------------------------
data = yf.download(tickers='BTC-USD',
                   period='max',
                   # use "period" instead of start/end
                   # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                   # (optional, default is '1mo')interval = '1d')
                   interval='1m'
                   # fetch data by interval (including intraday if period < 60 days)
                   # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                   # (optional, default is '1d'）
                   )

# Count pct_change
data['close_change'] = data.Close.pct_change()
data = data.iloc[1:, :]
correction = data[data['close_change'] <= -0.1]
correction.reset_index(inplace=True)
correction['date_range'] = correction.Date.diff().dt.days
correction.fillna(0, inplace=True)


# Plot

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(
        x=correction['Date'],
        y=correction['Close'],
        mode='lines+markers'),
    secondary_y=True)


fig.add_trace(
    go.Scatter(x=data.index,
               y=data.Close,
               mode='lines'),
    secondary_y=True)

fig.update_yaxes(type="log")

plot(fig)
