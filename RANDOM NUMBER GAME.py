import random as r
def randg(i):
    n = r.randint(1,10)
    if n>i and n<i:
        print("NOT EVEN CLOSE, TRY AGAIN!!")
    elif n==i+1 or n==i-1:
        print("SOO CLOSE!! THE NUMBER IS ",n)
    elif n==i:
        print("YAY!! CONGRATS YOU FOUND IT!!")
    else:
        print("TRY AGAIN!")

if __name__ == '__main__':
    print("----------RANDOM NUMBER GAME----------")
    a = int(input("ENTER A NUMBER FROM 1-10 : "))
    randg(a)
