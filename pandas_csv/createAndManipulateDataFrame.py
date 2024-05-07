import  numpy as np
import pandas as pd

student_info= {"Name":["ana","mariam","niko"],
               "subject1":[72,62,94],
               "subject2":[88,62,94],
               "subject3":[71,62,94],
               }
student_table = pd.DataFrame(student_info)
student_table["Average"] =(student_table["subject1"]+student_table["subject2"]+student_table["subject3"])/3
print(student_table.head())

print("-------------------") ## manipulate column content
student_table.columns= ["Firstname", "Python", "Calculus","Math","Total"]
print(student_table.head())

print("-------------------") ## manipulate exact column content
student_table.rename(columns={"Math":"Linear Algbra"}, inplace=True)
print(student_table.head())

print("-------------------") ## manipulate exact column content with index number
student_table.columns.values[0]="Hi"
print(student_table.head())

print("-------------------") ## delete wanted column from table
student_table.drop("Total", axis="columns", inplace=True) ## axis could be also index
print(student_table.head())

print("-------------------") ## manipulate with adding extra column
student_dataframe= pd.DataFrame(student_info)
student_dataframe= student_dataframe.assign(Statistics =[90,22,52])
student_dataframe.insert(4,"Algebra",[67,90,100])
print(student_dataframe.head())

print("-------------------") ## add extra row
student_dataframe= student_dataframe._append({"Name": "Dato","subject1":51, "subject2":51,"subject3":51,"Algebra": 100, "Statictics":50, "new":50},ignore_index=True)
print(student_dataframe.head())
