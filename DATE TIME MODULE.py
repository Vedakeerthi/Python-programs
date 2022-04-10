# ## INSTALLING THE MODULE USING PIP

pip install datetime

# ## IMPORTING THE MODULE AND PRINTING TODAY'S DATE

from datetime import *
import datetime as dt
today = dt.date.today()

print(today)


# ## THIS IS USED TO CALCULATE THE DIFFERENCE OF THE DATES:

my_bday = dt.date(2020,1,25)
til = today - my_bday
print("THE NUMBER OF DAYS TILL MY BIRTHDAY : {}".format(til))
til_sec = til.total_seconds()
print("THE NUMBER OF SECONDS TILL MY BIRTHDAY : {}".format(til_sec))
af3 = today + dt.timedelta(days=3)
print("THE DATE AFTER THREE DAYS : {}".format(af3))


# ## THIS IS USED TO DISPLAY A DATE:

td = dt.date(2020,1,25)
print(td)

print(td.year)    #I AM DISPLAYING THE GIVEN YEAR SEPARATELY
print(td.day)     #I AM DISPLAYING THE GIVEN DAY SEPARATELY
print(td.month)   #I AM DISPLAYING THE GIVEN MONTH SEPARATELY


# ## THIS IS USED TO DISPLAY A TIME

t = dt.time(0,3,0,0)  #RAILWAY TIMINGS
print(t)


print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


# ## THIS IS USED TO DISPLAY A DATE AND THE TIME:

d = dt.datetime(2020,1,25,23,4,5)
print(d)
print(d.weekday())
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)


# ## THIS IS USED TO PRINT THE CURRENT DATE AND TIME

print(dt.datetime.now())