from random import *
from tkinter import *
import tkinter as tk
from tkinter import font,messagebox

window = tk.Tk()
window.title("NUMBER GUESSING GAME")
window.geometry("270x100")
window.iconbitmap('vk.ico')
window.config(bg="grey")

def r():
    no = n.get()
    no = int(no)
    number = randint(1,101)
    if no<number and no>number : 
        re = "THAT IS NOT EVEN CLOSE!! RETRY!"
    elif number==no-1 or number==no+1:
        re = "SOO CLOSE.. TRY AGAIN!!"
    elif number==no:
        re = "YAAY!!! YOU GUESSED RIGHT!!"
    else:
        re = "TRY AGAIN!!"
        
    messagebox.showinfo("RESULT",re)
n = IntVar()        
f = font.Font(family="TIMES",size = 10,weight='bold')
l = Label(window,text="ENTER A NUMBER : ",font=f,relief="flat",bg="grey").grid(row=0,column=0)
e = Entry(window,textvariable=n,width=20).grid(row=0,column=1)
r = Button(window,text="RESULT",font=f,bg="grey",relief="raised",command=r).grid(row=1,column=0)


window.resizable('false','false')
window.mainloop()