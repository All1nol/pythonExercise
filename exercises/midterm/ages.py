from bs4 import BeautifulSoup
import re

#part 1 :  read html file  in variable
with open("Ages.html",'r') as f:
    content =f.read() # this will  read html as string

#convert to  actual html  format
content =BeautifulSoup(content,'html.parser')
ages =content.find_all("p") # this will read all p
print(ages)
ages =[float(re.findall(r'\d+',age.text)[0]) for age in ages ]
print(ages)
print(sum(ages)/len(ages))