## Load the CSV file "sales_data.csv" into
## a DataFrame named sales_df.
## Display the first 5 rows of the DataFrame.
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Gina'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Dallas', 'Seattle']}
df= pd.DataFrame(data)

file = 'data.csv'
df.to_csv(file, index=False)

read = pd.read_csv('data.csv')

print(read.head()) 