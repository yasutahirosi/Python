import pandas as pd
import numpy as np
api_key='170d0f988a515fec69429f9c5adff203'

#==========================Clean Frame========================
data=pd.read_excel(r'/Users/law/SASUniversityEdition/myfolders/Python/Tasks/20200723/data of dissertation.xlsx',
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

#=======================Process for NAN=======================
drop_subset=['资产总计','负债合计','所有者权益合计','未分配利润',
             '盈余公积金','流动负债合计','非流动负债合计',
             '当日总市值/负债总计','企业自由现金流量FCFF',
             '固定资产净额','存货净额']
clean=clean.dropna(subset=drop_subset,how='any',axis=0)

clean['Debt1']=(clean['净利润']+clean['长期借款']+clean['衍生金融负债']+clean['资产总计'])/clean['盈余公积金']
clean['Debt2']=clean['负债合计']/clean['盈余公积金']
clean['Equity1']=(clean['所有者权益合计']-clean['固定资产净额']-clean['非流动负债合计'])/clean['盈余公积金']
clean['Equity2']=clean['所有者权益合计']/clean['盈余公积金']
clean['CL']=clean['未分配利润']/clean['盈余公积金']
clean['NCL']=clean['短期借款']/clean['盈余公积金']
clean['FL']=(clean['短期借款']+clean['净利润']+clean['衍生金融负债']+clean['以公允价值计量且其变动计入当期损益的金融负债']+clean['存货净额'])/clean['盈余公积金']
clean['当日总市值/负债总计']= clean['当日总市值/负债总计'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
clean['OL']=(clean['未分配利润']-clean['净利润']-clean['衍生金融负债']-clean['以公允价值计量且其变动计入当期损益的金融负债']-clean['存货净额'])/clean['盈余公积金']
clean['Tobin Q']=(clean['当日总市值/负债总计'] - clean['负债合计'])/clean['盈余公积金']
clean['CF']=clean['企业自由现金流量FCFF']/clean['盈余公积金']
clean['CA']=(clean['存货净额']+clean['固定资产净额'])/clean['盈余公积金']
clean['ES']=clean['资产总计'].map(np.log)
clean['ROA']=clean['净利润']/clean['盈余公积金']
hp=pd.read_csv('/Users/law/SASUniversityEdition/myfolders/Python/Tasks/20200723/hp results.csv')
clean['时间']=clean['时间'].astype('int64')
clean=pd.merge(left=clean,right=hp,left_on='时间',right_on='Time',how='left')
clean['EC']=clean['Cycle'].map(lambda x: 1 if x>0 else 0)
Final=clean[['证券代码', '时间','Debt1', 'Debt2', 'Equity1', 'Equity2', 'CL', 'NCL', 'FL', 'OL',
       'Tobin Q', 'CF', 'CA', 'ES', 'ROA','EC']]
Final.columns=['Company', 'Time','Debt1', 'Debt2', 'Equity1', 'Equity2', 'CL', 'NCL', 'FL', 'OL',
       'Q', 'CF', 'CA', 'Scale', 'ROA','Cycle']
Final['Cycle*Q']=Final['Cycle'].mul(Final['Q'])
Final['Cycle*CF']=Final['Cycle'].mul(Final['CF'])
Final['Cycle*CA']=Final['Cycle'].mul(Final['CA'])
Final.to_csv('final.csv',index=False)
      