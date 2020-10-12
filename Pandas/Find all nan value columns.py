import pandas as pd
path=r"C:\Users\luoz14\Desktop\qc.sas7bdat"
data=pd.read_sas(path,encoding='latin1')
a=data.isnull().sum()[data.isnull().sum()==len(data)].index
b=" ".join(list(a))

