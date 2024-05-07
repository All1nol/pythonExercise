import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")
data["status"] = data["Student"].map( lambda x : x.split(',')[1]
                                      .split('.')[0])
data.groupby("status")["Salary"].mean().plot(kind = "bar")
plt.show()
print(data)


