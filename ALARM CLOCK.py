import datetime as dt
from pygame import mixer
from plyer import notification

def time():
    current_time = dt.datetime.now().strftime("%H:%M:%S %p")
    return current_time

print("----------ALARM----------")
print("\nTHE CURRENT TIME IS : ",time())
hours = int(input("ENTER THE HOURS TO KEEP THE ALARM AT : "))
minutes = int(input("ENTER THE MINUTES TO KEEP THE ALARM AT : "))
ampm = input("ENTER WHETHER AM/PM : ")
your_alarm = dt.time(hours,minutes,0)

if (ampm=="PM") or (ampm=="pm") or (ampm=="Pm"):
    if hours < 12 :
        hours = hours+12
    
print("\n\nwaiting for alarm....")
        
while(True):
    
    if (hours==dt.datetime.now().hour) and (minutes==dt.datetime.now().minute):
        mixer.init()
        mixer.music.load('D:\SONGS\Maara Theme.mp3')
        mixer.music.play()
        mixer.music.set_volume(100)
        notification.notify(title="ALARM CLOCK",message="WAKE UP BUDDY!! IT'S TIME TO LEARN..",app_icon='a.ico',timeout=10)
        stop = input("\nPRESS S TO STOP THE ALARM : ")
        if stop=="S" or stop=="s":
            mixer.music.stop()
        break
        
        

