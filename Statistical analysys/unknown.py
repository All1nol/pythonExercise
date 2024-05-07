import  pandas  as pd
import numpy as np
student_info ={"Name":["Michael","John","David","George","Nick"],"Python":[78,77,88,91,56],
               "Calculus":[98,66,77,87,88],"Statistics":[90,56,63,65,45]}
student_dataframe =pd.DataFrame(student_info)
print(student_dataframe.describe())

student_info ={"Name":["Michael","John","David","George","Nick"],"Python":[78,77,88,91,56],
               "Calculus":[98,66,77,87,88],"Statistics":[90,56,63,65,45]}
student_dataframe =pd.DataFrame(student_info)
student_dataframe=student_dataframe.set_index("Name")
print("-------------")
print(student_dataframe.mean(axis=1))