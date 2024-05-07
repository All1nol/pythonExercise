import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = {'Experience': [1,5,3], 'Sale':[150,200,400]}
df= pd.DataFrame(data)
file = 'Sale.csv'
df.to_csv(file, index=False)

df = pd.read_csv('Sale.csv')

df['Experience'] = np.log(df['Experience'])

scaler = StandardScaler()

df['Sale'] = scaler.fit_transform(df[['Sale']])

print(df)
