#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install num2words


# In[3]:


#converting number to words using module

from num2words import *
a = int(input("ENTER A NUMBER : "))
b = num2words(a,lang="en")
print(b.upper())


# In[12]:


def num_words(num_int,num_len):
    
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
    hundreds = ['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred',
           'eight hundred','nine hundred']
    thousand = ['','one thousand','two thousand','three thousand','four thousand','five thousand','six thousand','seven thousand',
           'eight thousand','nine thousand']
    
    
    if num_len==4 :
        for i in range(num_len):
            if i==0:
                a = num_int[3]
                a = int(a)
                s = ones[a]
            elif i==1:
                b = num_int[2]
                b = int(b)
                s1 = tens[b]
            elif i==2:
                c = num_int[1]
                c = int(c)
                s2 = hundreds[c]
            elif i==3:
                d = num_int[0]
                d = int(d)
                s3 = thousand[d]
                print(s3+s2 +s1+" "+s)
    elif num_len==3 :
        for i in range(num_len):
            if i==0:
                a = num_int[2]
                a = int(a)
                s = ones[a]
            elif i==1:
                b = num_int[1]
                b = int(b)
                s1 = tens[b]
            elif i==2:
                c = num_int[0]
                c = int(c)
                s2 = hundreds[c]
                print(s2 +s1+" "+s)
            
    elif num_len==2:
        for i in range(num_len):
            if i==0:
                d = num_int[1]
                d = int(d)
                s3 = ones[d]
            elif i==1:
                e = num_int[0]
                e = int(e)
                s4 = tens[e]
                print(s4+s3)
    else :
        num_int = int(num_int)
        print(ones[num_int])

num_int = input("ENTER A NUMBER : ")
num_len = len(num_int)
num_words(num_int,num_len)

