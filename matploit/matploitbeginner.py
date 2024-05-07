import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s =pd.Series([67,90,89,56,66,45],name="Marks")
Marks_dataframe =pd.DataFrame(s)
plt.plot(Marks_dataframe["Marks"])
plt.show()
print(Marks_dataframe["Marks"].mode()[0]) ## std() mean()

