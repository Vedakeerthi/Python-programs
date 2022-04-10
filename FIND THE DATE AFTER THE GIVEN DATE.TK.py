from tkinter import *
import tkinter as tk
from tkinter import font
from datetime import *
import datetime as dt

window = tk.Tk()
window.geometry('630x100')
window.iconbitmap('vk.ico')
window.title('DATE CALCULATOR')
window.config(bg="gray")

def gd():
    da = n.get()
    das = d+dt.timedelta(days=da)
    re = str(das)+" IS THE DATE AFTER "+str(da)+" DAYS"
    Label(window,text=re,bg="black",fg="red",font=("times",10,'bold')).grid(row=3,column=0)

f = font.Font(family="TIMES",size=10,weight='bold',underline=1)
d = dt.date.today()
n = IntVar()
Label(window,text="CURRENT DATE : "+str(d),fg="black",bg="gray",font=f).grid(row=0,column=0)
Label(window,text="ENTER THE NUMBER OF DAYS TO BE CALCULATED FROM THE CURRENT DATE : ",fg="black",bg="gray",font=f).grid(row=1,column=0)
Entry(window,textvariable=n,width=15).grid(row=1,column=1)
Button(window,text="GET DATE",command=gd,fg="black",bg="white",relief='groove').grid(row=2,column=1)

window.resizable('false','false')
window.mainloop()

