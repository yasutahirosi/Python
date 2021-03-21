from sklearn import datasets
import pandas as pd

data=pd.DataFrame(datasets.load_boston()['data'])
data.columns=datasets.load_boston()['feature_names']


data.columns

#Select specific cols
exp1=data.filter(['CRIM',"ZN","INDUS"])

#Select cols with specific charcters
exp2=data.filter(regex="^C",axis='columns')

exp3=data.filter(regex="I",axis='columns')

exp4=data.filter(regex="S$",axis='columns')