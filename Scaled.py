import pandas as pd
import numpy as np
from sklearn import preprocessing

data=pd.read_excel('test.xlsx')
scaled_Characters=preprocessing.MinMaxScaler(data['Characters'].values)
scaled_Characters=pd.DataFrame(scaled_Characters)
scaled_Original_examples=preprocessing.normalize(data['Original examples'])
scaled_Original_examples=pd.DataFrame(scaled_Original_examples)
scaled=pd.concat([data,scaled_Characters,scaled_Original_examples],axis=1)
scaled.columns=['Dynasty', 'Characters','Original examples','scaled_Characters',
                'scaled_Original_examples']
order=['Dynasty', 'Characters','scaled_Characters','Original examples',
                'scaled_Original_examples']
scaled=scaled[order]
scaled.to_csv('scaled.csv')