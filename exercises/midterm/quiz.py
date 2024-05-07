import pandas as pd

data = {'Year': [2017,2018,2019,2021,2022], 'Revenue': [1400,1700,2300,2500,2800], 'Cost':[1300,1400,2000,2200,2500]}

df = pd.DataFrame(data) #dataframe kuruyoruz

df['Profit']= 3 * df['Revenue'] * df['Revenue'] -1.5 * df['Cost'] * df['Cost']

print(df)
