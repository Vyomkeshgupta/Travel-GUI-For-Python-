from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.configure(bg="#3498db")
# root.configure(bg="#ffdd59")
root.iconbitmap("images.jfif")
f1=Frame(root,bg="red",borderwidth=3).grid()
def submitform():
    name1=""
    nameval=name_value.get()
    numberval=number_value.get()
    tomonthval=to_month_value.get()
    frommonthval=to_month_value.get()
    paymentval=payment_mode_value.get()
    if nameval==name1:
        messagebox.showerror("Error","Enter Name")
    elif len(numberval)!= 10:
        messagebox.showerror("Error","Enter Number")
    elif frommonthval not in months:
        messagebox.showerror("Error","Enter From Date ")
    elif paymentval not in payment_mode:
        messagebox.showerror("Error","Enter Payment Mode")
    elif tomonthval not in months:
        messagebox.showerror("Error","Enter To Date ")
    else:
        with open("travelsubmittions","a") as e:
            e.write(f"name:{nameval} , Number:{numberval} , To Month:{tomonthval} , From Month: {tomonthval} , PaymentMode:{paymentval} \n")
        messagebox._show("Submitted","Your Info Has Been Submitted To The File 'travelsubmittions' ")


root.geometry("490x258")
# root.maxsize(350,158)
# root.minsize(350,158)
root.title("Travel")
travel=Label(text="Travel",font="Times 15 bold").grid(row=0,column=2)
name=Label(text="Name",font="Times 9 bold").grid()
number=Label(text="Number",font="Times 9 bold").grid()
from_date=Label(text="From Date",font="Times 9 bold").grid()
to_date=Label(text="To Date",font="Times 9 bold").grid()
payment_mode=Label(text="Payment Mode",font="Times 9 bold").grid()


name_value=StringVar()
name_entry=Entry(root,textvariable=name_value).grid(row=1,column=1)
number_value=StringVar()
number_entry=Entry(root,text="+91",textvariable=number_value).grid(row=2,column=1)
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
payment_mode=[
    "Card",
    "Cash"
]
to_month_value=ttk.Combobox(root,value=months)
# to_month_value.current(0)
to_month_value.bind("<<ComboboxSelected>>")
to_month_value.grid(row=4,column=1)



from_month_value=ttk.Combobox(root,value=months)
# from_month_value.current(0)
from_month_value.bind("<<ComboboxSelected>>")
from_month_value.grid(row=3,column=1)
payment_mode_value=ttk.Combobox(root,value=payment_mode)
# payment_mode_value.current(0)
# payment_mode_value.bind("<<ComboboxSelected>>")
payment_mode_value.grid(row=5,column=1)
submit=Button( text="Submit",command=submitform)
# exit=Button(text="Exit",font="Times 9",command=exit).grid(column=2)
exit=Button(text="Exit",command=exit)
submit.grid(row=6,column=3)
root.mainloop()