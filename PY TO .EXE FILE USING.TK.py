from tkinter import *
import tkinter as tk
import tkinter.font as font 
window = tk.Tk()
window.title(".py to .exe")
window.iconbitmap(r'vk.ico')
window.geometry("670x400")
window.configure(bg = "yellow")

myfont = font.Font(family="Times New Roman",size = 13,weight='bold',slant='italic',underline=1)
myfont2 = font.Font(family = "Lobster", size=10, weight='bold',slant='italic',underline=0)

heading = Label(window, text = "THE STEPS TO CONVERT A .py FILE TO .exe FILE, ARE: ", font=myfont,fg="black",bg = "yellow").place(x=0,y=0)
step1 = Label(window, text="STEP 1   : pip install pyinstaller", font=myfont2, fg="green",bg = "yellow").place(x=0,y=50)
step2 = Label(window, text="STEP 2   : Go into the directory where your ‘.py’ file is located", font=myfont2,bg = "yellow", fg="red").place(x=0,y=75)
step3 = Label(window, text="STEP 3   : Press the shift and the right mouse button simultaneously, and you will get a drop down box", font=myfont2, fg="green",bg = "yellow").place(x=0,y=100)
step4 = Label(window, text="STEP 4   : Click on 'Open PowerShell window' in the box ", font=myfont2, fg="red",bg = "yellow").place(x=0,y=125)
step5 = Label(window, text="STEP 5   : Type the command given below in that PowerShell window. pyinstaller --onefile -w 'filename.py'", font=myfont2, fg="green",bg = "yellow").place(x=0,y=150)
step6 = Label(window, text="STEP 6   : In case you get an error try this,'.\pyinstaller --onefile -w 'filename.py''", font=myfont2, fg="red",bg = "yellow").place(x=0,y=175)
step7 = Label(window, text="STEP 7   : Press enter", font=myfont2, fg="green",bg = "yellow").place(x=0,y=200)
step8 = Label(window, text="STEP 8   : Open ‘dist’ folder above. Here you will get your ‘.exe’ file", font=myfont2,bg = "yellow", fg="red").place(x=0,y=225)
step9 = Label(window, text="STEP 9   : You can see an spec file, you can even delete that it is of no use", font=myfont2, bg = "yellow", fg="green").place(x=0,y=250)
step10 = Label(window, text="STEP 10 : YAY! YOUR EXE FILE IS READY NOW!!", font=myfont2, fg="red",bg = "yellow" ).place(x=0,y=275)


window.resizable('false','false')
window.mainloop()