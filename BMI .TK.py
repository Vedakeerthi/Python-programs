from tkinter import * 
import tkinter as tk
from tkinter import messagebox,ttk
window = tk.Tk()
window.title("BMI CALCULATOR")
window.iconbitmap(r'vk.ico')
window.geometry('550x300')
window.config(bg="black")

    
def kg():
    e = Entry(f,font="TIMES",fg='red',textvariable=wkg).grid(row=1,column=1)    
def g():
     e1 = Entry(f,font="TIMES",fg='red',textvariable=wg).grid(row=2,column=1)

def feet():
    e2 = Entry(f,font="TIMES",fg='red',textvariable=hf).grid(row=5,column=1)
def inches():
    e3 = Entry(f,font="TIMES",fg='red',textvariable=hi).grid(row=6,column=1)
def centimeters():
    e4 = Entry(f,font="TIMES",fg='red',textvariable=hc).grid(row=7,column=1)
def meters():
    e5 = Entry(f,font="TIMES",fg='red',textvariable=hm).grid(row=8,column=1)
    
def bmi():
    weight_kg=0
    weight_g=0
    
    weight_kg = wkg.get()
    weight_g = wg.get()
    
    if weight_g==0:
        weight = weight_kg
    else:
        weight = weight_g*0.001
   
    height_feet=0  
    height_inches=0
    height_centimeters=0
    height_meters=0
    
    height_feet = hf.get()
    height_inches = hi.get()
    height_centimeters = hc.get()
    height_meters = hm.get()
    
    if height_feet==0 and height_inches==0 and height_centimeters==0 :
        height = height_meters
    elif height_feet==0 and height_inches==0 and height_meters==0 :
        height = height_centimeters*0.01
    elif height_feet==0 and height_meters==0 and height_centimeters==0 :
        height = height_inches*0.0254
    elif height_inches==0 and height_meters==0 and height_centimeters==0 :
        height = height_feet*0.3048
           
    bmi = weight/(height**2)
    bmi = round(bmi,2)
    if bmi<=18.5:
        re = "     YOU ARE IN AN UNDERWEIGHT CATEGORY, TAKE CARE!!     "
    elif bmi>18.5 and bmi<24.9:
        re = "     GOOD! YOU ARE IN AN NORMAL CONDITION     "
    else:
        re = "     YOU ARE UNDER OBESE CATEGORY, TAKE CARE!!     "
        
        
    messagebox.showinfo("RESULT","YOUR BMI IS : "+str(bmi)+re )
    
    
wkg = DoubleVar()
wg = DoubleVar()
hf= DoubleVar()
hi= DoubleVar()
hc= DoubleVar()
hm= DoubleVar()
f = Frame(window,width=100,highlightbackground='black',highlightcolor='red',highlightthickness=3).grid(row=0,column=0)

l =Label(f,text = "IN WHICH UNIT YOU KNOW YOUR WEIGHT : ",font = "TIMES",bg="black",fg='red').grid(row= 0,column=0)
r1 = Radiobutton(f,text="kg",font="TIMES",padx=2,pady=2,command=kg,justify=LEFT,fg="white",bg="black").grid(row=1,column=0)
r2 = Radiobutton(f,text="g",font="TIMES",padx=2,pady=2,command=g,justify=LEFT,fg="white",bg="black").grid(row=2,column=0)

l1 = Label(f,text="IN WHICH UNIT YOU KNOW YOUR HEIGHT : ",font="TIMES",bg="black",fg='red').grid(row = 4,column =0)
r3 = Radiobutton(f,text="feet",font="TIMES",padx=2,pady=2,command=feet,justify=LEFT,fg="white",bg="black").grid(row=5,column=0)
r4 = Radiobutton(f,text="inches",font="TIMES",padx=2,pady=2,command=inches,justify=LEFT,fg="white",bg="black").grid(row=6,column=0)
r5 = Radiobutton(f,text="centimeters",font="TIMES",padx=2,pady=2,command=centimeters,justify=LEFT,fg="white",bg="black").grid(row=7,column=0)
r6 = Radiobutton(f,text="meters",font="TIMES",padx=2,pady=2,command=meters,justify=LEFT,fg="white",bg="black").grid(row=8,column=0)

bt = Button(f,text="CALCULATE BMI",font="TIMES",fg='red',relief="raised",command=bmi).grid(row=9,column=0)



window.resizable('false','false')
window.mainloop()
