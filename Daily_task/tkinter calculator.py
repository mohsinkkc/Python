from tkinter import *
from tkinter import messagebox as msg

cal=Tk()
cal.title("Calculater")
cal.geometry('500x500')
cal.resizable(False,False)
#-------------------function=========

def add():
    if name1_entry.get()=="" or name2_entry.get()=="":
        msg.showinfo("Alert","the input can't be blank")
    else:
        num1=int(name1_entry.get())
        num2=int(name2_entry.get())
        msg.showinfo("status",f"{num1+num2}")
def sub():
    if name1_entry.get()=="" or name2_entry.get()=="":
        msg.showinfo("Alert","the input can't be blank")
    else:
        num1=int(name1_entry.get())
        num2=int(name2_entry.get())
        msg.showinfo("status",f"{num1-num2}")

def mul():
    if name1_entry.get()=="" or name2_entry.get()=="":
        msg.showinfo("Alert","the input can't be blank")
    else:
        num1=int(name1_entry.get())
        num2=int(name2_entry.get())
        msg.showinfo("status",f"{num1*num2}")
def div():
    if name1_entry.get()=="" or name2_entry.get()=="":
        msg.showinfo("Alert","the input can't be blank")
    else:
        num1=int(name1_entry.get())
        num2=int(name2_entry.get())
        msg.showinfo("status",f"{num1/num2}")

header=Label(cal,text="Welcome to the worl of Calculator",fg="orange",bg="black",font=('Arial 20'))
header.place(x=50,y=50)

name1=Label(cal,text="enter the num 1:",font=('Arial 12'))
name1.place(x=50,y=150)
name1_entry=Entry(cal,)
name1_entry.place(x=200,y=150)

name2=Label(cal,text="enter the num 2:",font=('Arial 12'))
name2.place(x=50,y=200)
name2_entry=Entry(cal,)
name2_entry.place(x=200,y=200)

button=Button(cal,text="+",font="Arial",command=add)
button.place(x=50,y=250)
button=Button(cal,text="-",font="Arial",command=sub)
button.place(x=100,y=250)

button=Button(cal,text="*",font="Arial",command=mul)
button.place(x=150,y=250)

button=Button(cal,text="/",font="Arial",command=div)
button.place(x=200,y=250)
