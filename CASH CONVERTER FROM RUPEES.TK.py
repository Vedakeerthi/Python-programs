from tkinter import *
from tkinter import font,ttk
import tkinter as tk


window = tk.Tk()
window.title("CURRENCY CONVERTER")
window.iconbitmap("vk.ico")
window.config(bg="black")
window.geometry("650x650")
v = font.Font(family="TIMES",size=10,slant='italic',weight='bold',underline=0)
fon = font.Font(family="ARIAL",size=10,weight='bold',underline=0)
def convert():
    ru = n.get()
    converto = ss.get()
    if converto == "US Dollar":
        cv = ru*0.013411
        Label(window,text="THE US DOLLAR OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=3,column=0)
    elif converto == "Euro":
        cv = ru*0.011336
        Label(window,text="THE EURO OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=4,column=0)
    elif converto == "British Pound":
        cv = ru*0.010177
        Label(window,text="THE BRITISH POUND OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=5,column=0)
    elif converto == "Australian Dollar":
        cv = ru*0.018467
        Label(window,text="THE AUSTRALIAN DOLLAR OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=6,column=0)
    elif converto == "Canadian Dollar":
        cv = ru*0.017658
        Label(window,text="THE CANADIAN DOLLAR OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=7,column=0)
    elif converto == "Singapore Dollar":  
        cv = ru*0.018072
        Label(window,text="THE SINGAPORE DOLLAR OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=8,column=0)
    elif converto == "Swiss Franc":
        cv = ru*0.012240
        Label(window,text="THE SWISS FRANC OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=9,column=0)
    elif converto == "Malaysian Ringgit":
        cv = ru*0.055286
        Label(window,text="THE MALAYSIAN RINGGIT OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=10,column=0)
    elif converto == "Japanese Yen":
        cv = ru*1.402339
        Label(window,text="THE JAPANESE YEN OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=11,column=0)
    else:
        cv = ru*0.088587
        Label(window,text="THE CHINESE YUAN RENMINBI OF "+str(ru)+" INDIAN RUPEES IS : "+str(cv),font=v,fg="black",bg="red").grid(row=12,column=0)
   
ss = StringVar()
n = IntVar()
a = Label(window,text="SELECT THE OTHER CURRENCY TO BE CONVERTED TO : ",font=v,fg="white",bg="black").grid(row=0,column=0)
aa = [
      "US Dollar",
      "Euro",
      "British Pound",
      "Australian Dollar",
      "Canadian Dollar",
      "Singapore Dollar",
      "Swiss Franc",
      "Malaysian Ringgit",
      "Japanese Yen",
      "Chinese Yuan Renminbi"
      ]

t = ttk.Combobox(window,font=fon,width=15,values=aa,textvariable=ss)
t.grid(row=0,column=1)
l = Label(window,text="ENTER THE INDIAN RUPEES TO BE CONVERTED : ",font=v,fg="white",bg="black").grid(row=1,column=0)
e = Entry(window,fg="red",textvariable=n,width=15).grid(row=1,column=1)
b = Button(window,text="Convert",fg="black",bg="white",relief="raised",font=fon,width=15,command=convert).grid(row=2,column=1)
window.resizable('false','false')
window.mainloop()

