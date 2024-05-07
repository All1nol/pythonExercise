from tkinter import *

def bill():
    quantity_khinkali =float(khinkali_entry.get())
    quantity_mwvadi =float(mwvadi_entry.get())
    cost =quantity_khinkali*0.70+quantity_mwvadi*18
    if len(result_entry.get())!=0:
        # result_entry.config(state='disabled')
        result_entry.insert(0, "")
    result_entry.insert(0,str(cost))
master =Tk()
master.geometry("700x700")
master.title("Resturants")
master.config(bg="green")


khinkali_label =Label(master,text="Buy khinkali",font=14)
khinkali_label.place(x=70,y=70)
khinkali_entry =Entry(master,width=10,font=20)
khinkali_entry.place(x=160,y=70)



mwvadi_label =Label(master,text="Buy mwvadi",font=14)
mwvadi_label.place(x=70,y=110)
mwvadi_entry =Entry(master,width=10,font=20)
mwvadi_entry.place(x=160,y=110)



result_label =Label(master,text="calculate total price",font=14)
result_label.place(x=70,y=160)
result_entry =Entry(master,width=10,font=20)
result_entry.place(x=210,y=160)

calc_button =Button(master,text="calculate bill",command=bill)
calc_button.place(x =300,y =220)

master.mainloop()