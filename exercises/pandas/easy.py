## Creating a Series:
## Create a Pandas Series named s with
## the following values: 10, 20, 30, 40, 50. Print the series.
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series([10,20,30,40,50], name= "s")
print(s)

## Accessing Elements:
## From the series s created in question 1, print the element at index 3.
print(s[3])

## Slicing:
## From the series s created in question 1, print elements from index 1 to index 3.
print(s[1:4])

## Create a Pandas DataFrame named df with the following data:
## Name    Age    Score
## John    25     90
## Sara    30     85
## Mike    28     88

table = {"Name":["John", "Sara","Mike"], "Age":[25,30,28],"Score":[90,85,88]}
df = pd.DataFrame(table)
print(df.head())

## Column Access:
## From the DataFrame df created in question 4, print the "Age" column.
print(df["Age"])
print("------------")

## Adding a Column:
## Add a new column named "Grade" to the DataFrame df with
## the values "A", "B", "C"
## corresponding to each row. Print the updated DataFrame.
print("------------")
df['Grade'] = ['A', 'B', 'C']
print("Updated DataFrame:\n", df)

## Filtering Rows:
## From the DataFrame df created in question 6,
## print the rows where the "Score" is greater than 85.
print("------------")
print(df[df["Score"]>85])

## Sorting:
## Sort the DataFrame df based on the "Age"
## column in descending order. Print the sorted DataFrame.
print("------------")
sorted_df=df.sort_values(by="Age", ascending=False)
print(sorted_df.head())

## Calculations:
## Calculate the average age and average score from the DataFrame df.
print(df["Age"].mean())
print(df["Score"].mean())

## Statistical Summary:
## Print the statistical summary (mean, min, max, etc.) for the DataFrame df.
print(df.describe())