from tkinter import * 
import tkinter as tk
from calendar import *
from tkinter import font

window = tk.Tk()
window.title("2020 CALENDAR")
window.geometry("900x750")
window.iconbitmap('vk.ico')
window.config(bg="black")

n = IntVar()
def c():
    y = n.get()
    cal = calendar(y)
    r.config(text=cal)
    


f = font.Font(family="TIMES",weight='bold',size=15)
m = font.Font(family="ARIAL")
l = Label(window,text = "ENTER THE YEAR : ",font=f,bg="black",fg="white").grid(row=0,column=0)
e = Entry(window,textvariable=n,font=f).grid(row=0,column=1)
b = Button(window,text = "GET CALENDAR", font=f,command=c)
b.grid(row=1,column=1)
r = Label(window,font=m,bg="black",fg="white")
r.grid(row=2,column=1)

window.mainloop()

