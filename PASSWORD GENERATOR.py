from random import *

n = int(input("ENTER THE NUMBER OF PASSWORD LENGTH : "))
num = "1234567890"
low = "abcdefghijklmnopqrstuvwxyz"
hig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym = "`~!@#$%^&*()_+=-/.,<>?;:'""'[]{}| "

result = num+low+hig+sym
a = "".join(sample(result,n))
print(a)

