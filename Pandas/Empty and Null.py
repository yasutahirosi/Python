import pandas as pd

path=r"C:\Users\luoz14\Desktop\pic4qg1.sas7bdat"

data=pd.read_sas(path,encoding='latin1')

for i in data.columns: