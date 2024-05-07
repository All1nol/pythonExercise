import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s =pd.Series([67,90,89,56,66,45],name="Marks")
print(s) ##print(s[1:4])

d=pd.Series([67,90,89,66,45], name ="Marks")
Marks_dataframe = pd.DataFrame(d)
print(Marks_dataframe.head())

print("----------")
y =pd.Series([67,90,89,56,66,45],name="Marks")
Marks_dataframe =pd.DataFrame(y)
print(Marks_dataframe["Marks"])

