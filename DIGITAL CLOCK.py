from tkinter import *
import tkinter as tk
from tkinter import font
from datetime import *

window = tk.Tk()
window.title("CLOCK")
window.geometry('200x50')
window.iconbitmap('vk.ico')
window.config(bg="black")

f = font.Font(family="TIMES",size=23,weight="bold")

def time():
    current_time = datetime.now().strftime("%H:%M:%S %p")
    a.config(text=str(current_time)) 
    a.after(10,time)

a = Label(window,text="",fg="red",bg="black",font=f)
a.pack()

time()

window.resizable('false','false')
window.mainloop()