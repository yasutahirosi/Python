import pandas as pd
#==========================Clean Frame========================
data=pd.read_excel('/Users/law/Downloads/data.xlsx',
                   sheet_name='Sheet1')
data1=data.iloc[[0]+list(range(3,1363)),:]
data1.columns=data1.iloc[0,:]
data1.columns=list(data1.iloc[0,:])
data1=data1.iloc[1:,:]
data1.index=data1.iloc[:,0]
data1=data1.iloc[:,1:]
ind=list(data1.index)
index=[i.split()[0]+" "+i.split()[2] for i in ind]
data1.index=index
data2=data1.T
#=======================Process for NAN=======================
data3=data2.fillna(0)
drop_subset=['资产总计','负债合计','所有者权益合计','未分配利润',
             '盈余公积金','流动负债合计','非流动负债合计',
             '当日总市值/负债总计','企业自由现金流量FCFF',
             '固定资产净值','存货净额']
data2_=data2.dropna(subset=drop_subset,how='all',axis=0)

