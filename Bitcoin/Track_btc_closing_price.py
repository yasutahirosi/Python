#Module----------------------------------------------------------------
import requests
import yfinance as yf
import MySQLdb
from sqlalchemy import create_engine
import pandas as pd
# Get Bitcoin data-----------------------------------------------------
data = yf.download(tickers='BTC-USD',
                   period='max',
                   # use "period" instead of start/end
                   # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                   # (optional, default is '1mo')interval = '1d')
                   interval='1d'
                   # fetch data by interval (including intraday if period < 60 days)
                   # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                   # (optional, default is '1d'）
)
# Insert data to Mysql--------------------------------------------------
#Set up connect
db = 'Crypto'
user = 'root'
password = 'ly113216'
engine = create_engine('mysql+pymysql://{}:{}@localhost/{}'.format(user,password,db))

#To database
data.to_sql(name='btc_1d',con=engine,if_exists='append',index=False)

# Count pct_change
data['close_change'] = data.Close.pct_change()
data=data.iloc[1:,:]
correction=data[data['close_change']<=-0.1]
correction.index=pd.to_datetime(correction.index)
