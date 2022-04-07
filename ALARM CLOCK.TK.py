from tkinter import *
import tkinter as tk
from tkinter import font,ttk,filedialog
from datetime import *
import datetime as dt
from plyer import notification
from pygame import mixer


window = tk.Tk()
window.geometry('600x600')
window.title("ALARM CLOCK")
window.iconbitmap('vk.ico')
window.config(bg="black")

def time():
    current_time = datetime.now().strftime('%H:%M:%S %p')
    cl.config(text="CURRENT TIMINGS :"+ str(current_time))
    cl.after(10,time)

def s(hs,mi):
    hours = hs
    minutes = mi
    am = ap.get()
    h = datetime.now().hour
    m = datetime.now().minute
    Label(window,text="waiting for alarm.....",fg="red",bg="black").pack()
    if (am == "pm") or (am=="PM") or (am=="Pm"):
        if hours<12:
            hours +=12

    while(True):
        if (hours==h) and (minutes==m):
            mixer.init()
            url = filedialog.askopenfile(title="SELECT THE ALARM SOUND",
                                         initialdirectory="/",
                                         filetype = ("sound file","*.mp3*")
                                         )
            mixer.music.play(url)
            notification.notify(title='ALARM CLOCK',text="WAKE UP BUDDY!! LOT TO GO...",app_icon='a.ico',timeout=30)
            Label(window,text="PRESS S TO STOP THE ALARM : ",fg="red",bg="black").pack()
            Entry(window,textvariable=st).pack()
            stop = st.get()
            if stop=="s" or stop=="S":
                mixer.music.stop()
            break

h = IntVar()
m = IntVar()
ap = StringVar()
st = StringVar()
hou = 0
minu = 0
Label(window,text="ALARM CLOCK",fg="red",bg="black").pack()
cl = Label(window,text ="",fg="red",bg="black")
cl.pack()

time()
Label(window,text="ENTER THE HOUR TO BE ALARMED : ",fg="red",bg="black").pack()

Entry(window,fg="black",textvariable=h).pack()
hou = h.get()

Label(window,text="ENTER THE MINUTES TO BE ALARMED : ",fg="red",bg="black").pack()

Entry(window,fg="black",textvariable=m).pack()
minu = m.get()

Label(window,text="ENTER WHETHER AM/PM : ",fg="red",bg="black").pack()

a = ttk.Combobox(window,values=['am','pm'],textvariable=ap).pack()

Button(window,text="SET ALARM!",fg="black",bg="white",command=s(hou,minu),relief="raised").pack()



window.resizable('false','false')
window.mainloop()


