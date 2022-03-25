alice = 0
bob = 0

x = []
y = []
n = int(input("ENTER THE NUMBER OF ELEMENTS TO BE STORED IN BOTH THE ARRAYS : "))
print("Enter the elements of the first array")
for i in range(0,n):
    r1 = int(input("enter the element : "))
    x.append(r1)
print("Now enter the elements of the second array")
for j in range(0,n):
    r2 = int(input("enter the element : "))
    y.append(r2)

for k in range(0,n):
    if x[k] > y[k]:
        alice = alice + 1
    elif x[k] < y[k]:
        bob = bob+1

print("THE MARKS OBTAINED BY ALICE IS : ",alice)
print("THE MARKS OBTAINED BY BOB IS : ",bob)
