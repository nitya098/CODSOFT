from tkinter import *
from tkinter import messagebox
operation="NONE"
def calculate():
    global operation
    if len(i_first.get())>0 or len(i_second.get())>0:
        if operation!="NONE":
            first = int(i_first.get())
            second = int(i_second.get())
            if operation=="ADD":
                val=first+second
            elif operation=="SUB":
                val=first-second
            elif operation=="MUL":
                val=first*second
            elif operation=="DIV":
                if second==0:
                    messagebox.showerror(title="Error", message="Divide by zero error")
                val=first/second
            l_val.config(text=str(val))
        else:
            messagebox.showerror(title="Error", message="Please choose an operation")
            reset()
    else:
        messagebox.showerror(title="Error", message="Please enter both the numbers")
        reset()
def add():
    global operation
    operation="ADD"
    b_plus.config(border=5)
def sub():
    global operation
    operation="SUB"
    b_min.config(border=5)
def mul():
    global operation
    operation="MUL"
    b_mul.config(border=5)
def divi():
    global operation
    operation="DIV"
    b_div.config(border=5)
def reset():
    i_first.delete(0,"end")
    i_second.delete(0,"end")
    b_plus.config(border=0)
    b_min.config(border=0)
    b_mul.config(border=0)
    b_div.config(border=0)
    l_val.config(text="0")
window=Tk()
window.title("Simple Calculator")
window.config(padx=10,pady=5,borderwidth=0)
canvas=Canvas(width=400,height=80)
calc=PhotoImage(file="Images/calculator.png")
plus=PhotoImage(file="Images/plus.png")
mult=PhotoImage(file="Images/multiply.png")
min=PhotoImage(file="Images/minus.png")
div=PhotoImage(file="Images/divide.png")
canvas.create_image(220,40,image=calc)
canvas.grid(column=1,row=1,columnspan=5)
l_first=Label(text="First No:",font=('Ariel',16))
l_first.grid(column=1,row=2,pady=20)
l_oper=Label(text="Operation:",font=('Ariel',16))
l_oper.grid(column=1,row=3,pady=20)
b_plus=Button(image=plus,command=add)
b_plus.grid(column=2,row=3,pady=20,padx=20)
b_min=Button(image=min,command=sub)
b_min.grid(column=3,row=3,pady=20,padx=20)
b_mul=Button(image=mult,command=mul)
b_mul.grid(column=4,row=3,pady=20,padx=20)
b_div=Button(image=div,command=divi)
b_div.grid(column=5,row=3,pady=20,padx=20)
l_second=Label(text="Second No:",font=('Ariel',16))
l_second.grid(column=1,row=4,pady=20)
i_first=Entry(width=45)
i_first.grid(column=2,row=2,columnspan=4)
i_first.focus()
i_second=Entry(width=45)
i_second.grid(column=2,row=4,columnspan=4)
i_second.focus()
b_calc=Button(text="CALCULATE",font=('Ariel',22,'bold'),command=calculate)
b_calc.grid(column=1,row=5,columnspan=5)
l_ans=Label(text="Answer:",font=('Ariel',22))
l_ans.grid(column=1,row=6)
l_val=Label(text="0",font=('Ariel',30,'bold'))
l_val.grid(column=2,row=6,pady=20)
b_reset=Button(text="RESET",font=('Ariel',16),command=reset)
b_reset.grid(column=4,row=6,columnspan=2)
window.mainloop()