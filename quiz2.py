from tkinter import *
import re

def check_age():
    email = email_entry.get()
    year_match = re.search(r'(\d{4})@', email)

    if year_match:
        birth_year = int(year_match.group(1))
        current_year = 2024
        age = current_year - birth_year

        if age < 18:
            result_label.config(text="User is under 18 years old.")
        else:
            result_label.config(text="User is 18 years old or older.")
    else:
        result_label.config(text="Invalid email format.")

master = Tk()
master.geometry('400x200')
master.title('Detect Fake Mails')
master.config(bg='lightgray')

email_label = Label(master, text="Enter Email:", font=("Arial", 12))
email_label.pack(pady=10, padx=20)

email_entry = Entry(master, width=30, font=("Arial", 12))
email_entry.pack(pady=10)

check_button = Button(master, text='Check Age', width=15, font=("Arial", 12), command=check_age)
check_button.pack(pady=10)

result_label = Label(master, text="", font=("Arial", 12), fg='green', bg='lightgray')
result_label.pack(pady=10)

master.mainloop()
