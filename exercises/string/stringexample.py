import string
print(list(string.punctuation))
text ='do you love him?please tell him yes or he will die!'
for punct  in list(string.punctuation):
    if punct in text:
        text =text.replace(punct," ")
print(text)
print("a" in text)
print(text.find("g"))