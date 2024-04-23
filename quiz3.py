from tkinter import *


def calculate_total_price():
    distance_a_to_b = float(aTob_entry.get())
    distance_b_to_c = float(bToc_entry.get())
    total_distance = distance_a_to_b + distance_b_to_c
    total_distance_entry.delete(0, 30)

    total_price = distance_a_to_b * 60 + distance_b_to_c * 50
    total_distance = distance_a_to_b + distance_b_to_c

    if total_distance > 200:
        total_price += total_price * 10 / 100
    total_price_entry.insert(0, str(total_price))
    total_distance_entry.insert(0, str(total_distance))


master = Tk()
master.geometry('300x220')
master.title('Distance and Price Calculator')
master.config(bg='lightgray')

labels_and_entries = [
    ("Distance from A to B", 20, 20),
    ("Distance from B to C", 20, 60),
    ("Total Distance", 20, 100),
    ("Total Price", 20, 140)
]

for label_text, x, y in labels_and_entries:
    label = Label(master, text=label_text, font=16)
    label.place(x=x, y=y)

aTob_entry = Entry(master, width=10, font=16)
aTob_entry.place(x=210, y=20)

bToc_entry = Entry(master, width=10, font=16)
bToc_entry.place(x=210, y=60)

total_distance_entry = Entry(master, width=10, font=16)
total_distance_entry.place(x=210, y=100)

total_price_entry = Entry(master, width=10, font=16)
total_price_entry.place(x=210, y=140)

calculate_button = Button(master, text="Calculate Total Price", command=calculate_total_price)
calculate_button.place(x=100, y=180)

master.mainloop()
