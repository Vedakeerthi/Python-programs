from tkinter import *
import tkinter as tk
from tkinter import font,Radiobutton
from random import *

window = tk.Tk()
window.title("PASSWORD GENERATOR")
window.geometry('600x250')
window.iconbitmap('vk.ico')
window.config(bg="#ffffff")

def l():
    z = m.get()
    y = n.get()
    if z==1:
        num = "1234567890111213141516"
        re = sample(num,y)
        a.config(text=re)
    elif z==2:
        sm = "abcdefghijklmnopqrstuvwxyz"
        re = sample(sm,y)
        a.config(text=re)
    elif z==3:
        sm = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        re = sample(sm,y)
        a.config(text=re)
    elif z==4:
        sm = "`~!@#$%^&*()_+=-/.,<>?;:'""'[]{}| "
        re = sample(sm,y)
        a.config(text=re)
    


n = IntVar()
m = IntVar()
f = font.Font(family="times",size=10,weight="bold",slant="italic",underline=0)


a1_1 = Label(window,text="ENTER THE LENGTH OF YOUR PASSWORD : ",font=f,bg="#ffffff",fg="black").grid(row=0,column=0)
a1 = Entry(window,width=15,textvariable=n).grid(row=0,column=1)
a1_2 = Label(window,text="INCLUDE: ",font=f,fg="black",bg="#ffffff").grid(row=1,column=1)
w = Radiobutton(window,text="NUMBERS",font=f,variable=m,value=1,bg="#ffffff").grid(row=2,column=2)
w1 = Radiobutton(window,text="SMALL CASE LETTERS",font=f,variable=m,value=2,bg="#ffffff").grid(row=3,column=2)
w2 = Radiobutton(window,text="LARGE CASE LETTERS",font=f,variable=m,value=3,bg="#ffffff").grid(row=4,column=2)
w3 = Radiobutton(window,text="SYMBOLS",font=f,variable=m,value=4,bg="#ffffff").grid(row=5,column=2)


a2 = Button(window,text="GET PASSWORD",width=15,font=f,relief='flat',bg="red",fg="white",command=l).grid(row=6,column=2)
a = Label(window,width=0,bg="#ffffff")
a.grid(row=7,column=2)

window.resizable('false','false')
window.mainloop()