#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = int(input("ENTER A NUMBER FROM 1-26 FOR LETTERS :"))
a += 64
if 63<a<91:
    print(chr(a))
else:
    print("INVALID NUMBER..")

