def bin_oct_hex(n):
    print("THE BINARY NUMBER IS : ",bin(n).replace("0b",""))
    print("THE OCTAL NUMBER IS : ",oct(n).replace("0o",""))
    print("THE HEXA-DECIMAL NUMBER IS : ",hex(n).replace("0x",""))
    
def dec_oct_hex(n):#000111
    dec = []
    a = len(n)-1
    for i in range(0,len(n)):
        b = abs(i-a)
        value =int(n[b])*pow(2,i)
        z =int(value)
        dec.append(z)
    dec = sum(dec)
    print("THE DECIMAL NUMBER IS : ",dec)
    print("THE OCTAL NUMBER IS : ",oct(dec).replace("0o",""))
    print("THE HEXA-DECIMAL NUMBER IS : " ,hex(dec).replace("0x",""))
    
def dec_bin_hex(n):
    dec = []
    for i in range(0,len(n)):
        s = len(n)-1
        a = abs(i-s)
        v = int(n[a])*pow(8,i)
        dec.append(v)
    dec = sum(dec)
    print("THE DECIMAL NUMBER IS : ",dec)
    print("THE BINARY NUMBER IS : ",bin(dec).replace("0b",""))
    print("THE HEXA-DECIMAL NUMBER IS : ",hex(dec).replace("0x",""))

def dec_bin_oct(n):
    dec = int(n,16)
    print("THE DECIMAL NUMBER IS : ",dec)
    print("THE BINARY NUMBER IS : ",bin(dec).replace("0b",""))
    print("THE OCTAL NUMBER IS : ",oct(dec).replace("0o",""))


if __name__ == "__main__":
    while(True):
     print("----------CONVERTER----------")
     print("PRESS 1 FOR DECIMAL INPUT ")
     print("PRESS 2 FOR BINARY INPUT ")
     print("PRESS 3 FOR OCTAL INPUT ")
     print("PRESS 4 FOR HEXA-DECIMAL INPUT ")
     n = int(input().strip())
     if n==1: 
        x = int(input("ENTER THE DECIMAL NUMBER, TO CONVERT IT TO OTHER FORMATS : "))
        bin_oct_hex(x)
     elif n==2 : 
        x = input("ENTER THE BINARY NUMBER, TO CONVERT IT TO OTHER FORMATS : ")
        dec_oct_hex(x)
     elif n==3 : 
        x = input("ENTER THE OCTAL NUMBER, TO CONVERT IT TO OTHER FORMATS : ")
        dec_bin_hex(x)
     else : 
        x = input("ENTER THE HEXA-DECIMAL NUMBER, TO CONVERT IT TO OTHER FORMATS : ")
        dec_bin_oct(x)

    

