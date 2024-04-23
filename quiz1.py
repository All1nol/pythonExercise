from tkinter import *
import re

def calculate_revenue():
    first_price = first_entry.get()
    first_price = re.findall(r'\d+', first_price)

    second_price = second_entry.get()
    second_price = re.findall(r'\d+', second_price)

    total_revenue = int(first_price[0]) + int(second_price[0])
    output_entry.config(state='normal')
    output_entry.delete(0, END)
    output_entry.insert(0, total_revenue)

master = Tk()
master.geometry('400x300')
master.title('Revenue Calculator')
master.config(bg='lightblue')

Label(master, text="First Price:", font=("Arial", 12), bg='lightblue').grid(row=0, column=0, padx=10, pady=10)
Label(master, text="Second Price:", font=("Arial", 12), bg='lightblue').grid(row=1, column=0, padx=10, pady=10)
Label(master, text="Total Revenue:", font=("Arial", 12), bg='lightblue').grid(row=2, column=0, padx=10, pady=10)

first_entry = Entry(master, width=20, font=10)
first_entry.grid(row=0, column=1, padx=10, pady=10)

second_entry = Entry(master, width=20, font=10)
second_entry.grid(row=1, column=1, padx=10, pady=10)

output_entry = Entry(master, width=20, font=10, state='readonly')
output_entry.grid(row=2, column=1, padx=10, pady=10)

revenue_button = Button(master, text='Calculate Revenue', width=20, command=calculate_revenue)
revenue_button.grid(row=3, column=0, columnspan=2, pady=20)

master.mainloop()
