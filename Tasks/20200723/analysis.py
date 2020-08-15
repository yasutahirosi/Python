import pandas as pd
import numpy as np

#==========================Clean Frame========================
data=pd.read_excel('data of dissertation.xlsx',
                   sheet_name='Sheet1')

data['class']=data.iloc[:,0].map(lambda x:x.split()[0])
data['time']=data.iloc[:,0].map(lambda x:x.split()[2])

def trans(x):
    if '一季' in x:
        x=x.replace('一季','0331')
    elif '中报' in x:
        x=x.replace('中报','0630')
    elif '三季' in x:
        x=x.replace('三季','0930')
    else:
        x=x.replace('年报','1231')
    return x

data['time']=data['time'].map(trans)



data=data.iloc[:,1:]
data1=data.set_index(['class','time'])
data2=data1.unstack().T
data3=data2.reset_index()

data3.columns=['证券代码', '时间', '一年内到期的非流动负债', '以公允价值计量且其变动计入当期损益的金融负债',
       '企业自由现金流量FCFF', '净利润', '固定资产净额', '存货净额', '应付债券', '当日总市值/负债总计',
       '所有者权益合计', '未分配利润', '流动负债合计', '盈余公积金', '短期借款', '衍生金融负债', '负债合计', '资产总计',
       '长期借款', '非流动负债合计']

clean=data3.copy()

#=======================Process for NAN======================================================
drop_subset=['资产总计','负债合计','所有者权益合计','未分配利润',
             '盈余公积金','流动负债合计','非流动负债合计',
             '当日总市值/负债总计','企业自由现金流量FCFF',
             '固定资产净额','存货净额']
clean=clean.dropna(subset=drop_subset,how='any',axis=0)

#=======================Merge with hp results==============================================
hp=pd.read_csv('hp.csv')
clean['时间']=clean['时间'].astype('int64')
clean=pd.merge(clean,hp,left_on='时间',right_on='Time',how='left')
#========================Separate dataset by===============================================
company=list(clean['证券代码'].value_counts().index)
subset=[]
for i in company:
    subset.append(clean[clean['证券代码']==i])
#=========================Compute function================================================
def compute_add(data):
    data_lag=data.shift(1)
    data_add=data-data_lag
    return data_add

def compute(data):
    data['v8']=data['资产总计'].shift(1)
    data['v11']=compute_add(data['短期借款'])
    data['v4']=compute_add(data['长期借款'])
    data['v13']=compute_add(data['一年内到期的非流动负债'])
    data['v7']=compute_add(data['应付债券'])
    data['DEBT1']=(data['v11']+data['v4']+data['v13']+data['v7'])/data['v8']
    data['v1']=compute_add(data['负债合计'])
    data['DEBT2']=data['v1']/data['v8']
    data['v2']=compute_add(data['所有者权益合计'])
    data['v16']=compute_add(data['未分配利润'])
    data['v9']=compute_add(data['盈余公积金'])
    data['Equity1']=(data['v2']-data['v16']-data['v9'])/data['v8']
    data['Equity2']=data['v2']/data['v8']
    data['v14']=compute_add(data['流动负债合计'])
    data['SL']=data['v14']/data['v8']
    data['v10']=compute_add(data['非流动负债合计'])
    data['LL']=data['v10']/data['v8']
    data['v11']=compute_add(data['短期借款'])
    data['v5']=compute_add(data['以公允价值计量且其变动计入当期损益的金融负债'])
    data['v15']=compute_add(data['衍生金融负债'])
    data['FL']=(data['v10']+data['v11']+data['v13']+data['v5']+data['v15'])/data['v8']
    data['OL']=(data['v14']-data['v11']-data['v13']-data['v5']-data['v15'])/data['v8']
    data['当日总市值/负债总计']=data['当日总市值/负债总计'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
    data['Q']=(data['当日总市值/负债总计']*data['负债合计'])/data['资产总计']
    data['Q']=data['Q'].map(np.log)
    data['v6']=compute_add(data['企业自由现金流量FCFF'])
    data['CF']=data['v6']/data['v8']
    data['CA']=(data['存货净额']+data['固定资产净额'])/data['v8']
    data['Scale']=data['资产总计'].map(np.log)
    data['ROA']=data['净利润']/data['v8']
    data['Cycle']=data['Cycle factor']
    data['Cycle*Q']=data['Cycle'].mul(data['Q'])
    data['Cycle*CF']=data['Cycle'].mul(data['CF'])
    data['Cycle*CA']=data['Cycle'].mul(data['CA'])
    Final=data[['证券代码', '时间','DEBT1', 'DEBT2', 'Equity1', 'Equity2', 'SL', 'LL', 'FL', 'OL',
       'Q', 'CF', 'CA','Cycle','Cycle*Q','Cycle*CF','Cycle*CA','ROA','Scale']]
    Final.columns=['Company', 'Time','Debt1', 'Debt2', 'Equity1', 'Equity2', 'SL', 'LL', 'FL', 'OL',
       'Q', 'CF', 'CA','Cycle','Cycle*Q','Cycle*CF','Cycle*CA','ROA','Scale']
    return Final.iloc[1:,:]
#======================loop for all company======================================================
subset=[compute(i) for i in subset]
analysis=pd.concat(subset,axis=0)
analysis.to_csv('analysis.csv',index=False)    
    
    
