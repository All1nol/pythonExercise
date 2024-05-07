import pandas as pd
import numpy as np
# Create a DataFrame
d = {
    'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
             'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
    'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],
    'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]}

df = pd.DataFrame(d)
print(df.head(12))
print("-------")

print(df.loc[0,:])

print("-------")
print(df.loc[df["Name"]=="Alisa"])
print("-------")
print(df.loc[df["Score"].idxmin()]) ## idxmax
print("-------")
print(df[(df["Score"]>60)&(df["Score"]<70)])