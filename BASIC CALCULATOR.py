def add(c,d):
    return c+d
def subtract(c,d):
    return c-d
def multiply(c,d):
    return c*d
def divide(c,d):
    return c/d
def power(c,d):
    return c**d
def mod(c,d):
    return c%d
def fact(c):
    if(c==1):
        return 1
    elif(c==0):
        return 1
    else:
        return c*fact(c-1)

print("--------------BASIC OPERATIONS---------------")
print("PRESS 1 FOR ADDITION")
print("PRESS 2 FOR SUBTRACTION")
print("PRESS 3 FOR MULTIPLICATION")
print("PRESS 4 FOR DIVISION")
print("PRESS 5 FOR POWER")
print("PRESS 6 FOR MODULUS")
print("PRESS 7 FOR FACTORIAL")

n = int(input("ENTER THE OPERATION TO BE PERFORMED: "))

if(n==1):
    a = int(input("ENTER THE OPERAND 1: "))
    b = int(input("ENTER THE OPERAND 2: "))
    print("THE SUM OF THE TWO NUMBERS ARE : ",add(a,b))
elif(n==2):
    a = int(input("ENTER THE OPERAND 1: "))
    b = int(input("ENTER THE OPERAND 2: "))
    print("THE SUBTRACTION OF THE TWO NUMBERS ARE: ",subtract(a,b))
elif(n==3):
    a = int(input("ENTER THE OPERAND 1: "))
    b = int(input("ENTER THE OPERAND 2: "))
    print("THE MULTIPLICATION OF THE TWO NUMBERS ARE: ",multiply(a,b))
elif(n==4):
    a = int(input("ENTER THE OPERAND 1: "))
    b = int(input("ENTER THE OPERAND 2: "))
    print("THE DIVISION OF THE TWO NUMBERS ARE: ",divide(a,b))
elif(n==5):
    a = int(input("ENTER THE BASE ELEMENT : "))
    b = int(input("ENTER THE POWER ELEMENT: "))
    print("THE POWER OF THE NUMBER ARE: ",power(a,b))
elif(n==6):
    a = int(input("ENTER THE OPERAND 1: "))
    b = int(input("ENTER THE OPERAND 2: "))
    print("THE MODULUS OF THE NUMBER IS: ",mod(a,b))
elif(n==7):
    a = int(input("ENTER THE NUMBER TO FIND THE FACTORIAL: "))
    print(fact(a))
else:
    print("!ENTER A VALID NUMBER!")

