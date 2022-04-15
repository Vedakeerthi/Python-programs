from tkinter import *
import tkinter as tk
from tkinter import ttk,font
import random as r


window = tk.Tk()
window.title("STONE PAPER SCISSOR")
#window.iconbitmap('vk.ico')
window.config(bg="black")
window.geometry('600x600')

def sps():
    man = n.get()
    image_list = [STONE,PAPER,SCISSOR]
    shuffle = r.randint(0,2)
    comp = image_list[shuffle]
    if man == "SCISSOR":
        man = 2
    elif man=="PAPER":
        man=1
    elif man=="STONE":
        man=0
    l1 = Label(window,image=comp,bg="black",width=250,height=450).grid(row=3,column=1)
    if (man==0 and shuffle==0) or (man==1 and shuffle==1) or (man==2 and shuffle==2):
        res = Label(window,text="IT'S A TIE",width=15,fg="red",bg="white",font=f1).grid(row=4,column=1)
        
    elif (man==0 and shuffle==2) or (man==1 and shuffle==0) or (man==2 and shuffle==1):
        res = Label(window,text="YOU WON!!",width=15,fg="red",bg="white",font=f1).grid(row=4,column=1)
       
    else:
        res = Label(window,text="YOU LOSE..",width=15,fg="red",bg="white",font=f1).grid(row=4,column=1)

    
STONE = PhotoImage(file="My_personal_files/CODING FILES/MY PROGRAMS/PYTHON/MY PROJECTS/STONE PAPER SCISSOR GAME IMAGES/rock.png")
PAPER = PhotoImage(file="My_personal_files/CODING FILES/MY PROGRAMS/PYTHON/MY PROJECTS/STONE PAPER SCISSOR IMAGES/paper.png")
SCISSOR = PhotoImage(file="My_personal_files/CODING FILES/MY PROGRAMS/PYTHON/MY PROJECTS/STONE PAPER SCISSOR IMAGES/scissor.png")
f = font.Font(family="Times",size=10,weight='bold',slant='italic',underline=0)
f1 = font.Font(family="Times",size=10,weight='bold',underline=1)
n=StringVar()
l1 = Label(window,text="IT'S YOUR TURN : ",fg="red",bg="black",font=f).grid(row=0,column=0)
values=['STONE','PAPER','SCISSOR']
v = ttk.Combobox(window,values=values,textvariable=n).grid(row=0,column=1)

b = Button(window,text='spin',command=sps,relief='groove').grid(row=1,column=1)

window.resizable('false','false')
window.mainloop()