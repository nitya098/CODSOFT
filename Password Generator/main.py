import random
from tkinter import *
from tkinter import messagebox
import pyperclip
password=""
def generator():
    b_generate.config(state="disabled")
    global password
    if len(i_length.get())<=0:
        messagebox.showerror(title="ERROR", message="Please enter the desired password length")
        b_generate.config(state="active")
        return
    length=int(i_length.get())
    if length<8:
        messagebox.showerror(title="ERROR",message="The length should be greater or equal to 8")
        b_generate.config(state="active")
        return
    elif length>=8 and length<12:
        symbols=2
        number=2
        capital=2
        small=length-6
    elif length >= 12 and length <= 20:
        symbols = 3
        number = 3
        capital = 3
        small = length - 9
    else:
        messagebox.showerror(title="ERROR", message="The length should be lesser than or equal to 20 characters")
        b_generate.config(state="active")
        return
    sym=['!', '#', '$', '%', '&', '(', ')', '*', '+']
    num=['0','1','2','3','4','5','6','7','8','9']
    cap=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z']
    sml=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
    chosen=[]
    for i in range(symbols):
        choice=random.choice(sym)
        chosen.append(choice)
    for i in range(number):
        choice=random.choice(num)
        chosen.append(choice)
    for i in range(capital):
        choice=random.choice(cap)
        chosen.append(choice)
    for i in range(small):
        choice=random.choice(sml)
        chosen.append(choice)
    random.shuffle(chosen)
    for ele in chosen:
        password+=ele
    l_pass.config(text=password)
def copy():
    global password
    pyperclip.copy(password)
def redo():
    global password
    password=""
    generator()
window=Tk()
window.title("Password Generator")
window.config(padx=15,pady=15)
icon=PhotoImage(file="Images/icon.jpg")
canvas=Canvas(height=150,width=150)
canvas.create_image(75,75,image=icon)
canvas.grid(column=1,row=1,columnspan=2,pady=10)
l_length=Label(text="Password Length:",font=('Ariel',25))
l_length.grid(column=1,row=2)
i_length=Entry(width=10,font=('Ariel',25))
i_length.grid(column=2,row=2)
b_generate=Button(text="GENERATE",font=('Ariel',25),command=generator)
b_generate.grid(column=1,row=3,columnspan=2,pady=10)
l_password=Label(text="Password:",font=('Ariel',26))
l_password.grid(column=1,row=4,pady=10)
l_pass=Label(text="",font=('Ariel',22))
l_pass.grid(column=2,row=4,pady=10)
b_copy=Button(text="Copy",font=('Ariel',25),command=copy)
b_copy.grid(column=1,row=5)
b_regenerate=Button(text="Regenerate",font=('Ariel',25),command=redo)
b_regenerate.grid(column=2,row=5,padx=40)
window.mainloop()