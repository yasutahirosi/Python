#Pandas Tricks
import pandas as pd

#1 Select_dtypes()
data=pd.read_csv('/Users/law/OneDrive/文档/测试数据/Gapminder.csv')
data.dtypes.value_counts()
data.select_dtypes(include=['object'])

#2 columns to list
cols=data.columns.tolist()

#3
