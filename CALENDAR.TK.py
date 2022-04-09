from tkinter import *
import tkinter as tk
from tkinter import font,ttk
import calendar

window = tk.Tk()
window.title("CALENDAR")
window.geometry("450x300")
window.iconbitmap("vk.ico")
window.config(bg="#F59E8B")

def c():
    year = n.get()
    month = m.get()
    if month=="JANUARY":
        me=1
    elif month=="FEBURARY":
        me=2
    elif month=="MARCH":
        me=3
    elif month=="APRIL":
        me=4
    elif month=="MAY":
        me=5
    elif month=="JUNE":
        me=6
    elif month=="JULY":
        me=7
    elif month=="AUGUST":
        me=8
    elif month=="SEPTEMBER":
        me=9
    elif month=="OCTOBER":
        me=10
    elif month=="NOVEMBER":
        me=11
    else:
        me=12
        
    cal = calendar.month(year,me)
    r.config(text=cal)
    
global r,m 
n=IntVar()
m=StringVar()

f = font.Font(family="TIMES",weight='bold',slant='italic',underline=1)
f2 = font.Font(family="arial",size=15,weight='bold')
l = Label(window,text = "ENTER THE YEAR : ",font=f,relief="flat",bg='#F59E8B').grid(row=0,column=0)
e = Entry(window,textvariable=n,width=25).grid(row=0,column=1)
l2 = Label(window,text="ENTER THE MONTH : ",font=f,relief="flat",bg='#F59E8B').grid(row=1,column=0)

values = {
    "JANUARY":1,
    "FEBRUARY":2,
    "MARCH":3,
    "APRIL":4,
    "MAY":5,
    "JUNE":6,
    "JULY":7,
    "AUGUST":8,
    "SEPTEMBER":9,
    "OCTOBER":10,
    "NOVEMBER":11,
    "DECEMBER":12
}
comboboxvalues = "\n".join(values.keys())

e2 = ttk.Combobox(window,textvariable=m,values=comboboxvalues,width=25)
e2.current(0)
e2.grid(row=1,column=1)

b = Button(window,text="GET CALENDAR",font =f,borderwidth=2,command=c,bg='black',fg='white',relief="raised")
b.grid(row=2,column=1)

r = Label(window,font=f2,borderwidth=4,relief="flat",bg='#F59E8B',fg='black')
r.grid(row=3,column=1)

window.resizable('false','false')
window.mainloop()

