def bmi(ma,he):
    b = ma/he
    print("\nYOUR BMI : ",b)
    if b<=18.5:
        print("YOUR ARE THIN!!")
    elif b>=25:
        print("YOU ARE UNDER OVERWEIGHT CONDITION!!")
    else:
        print("YOU ARE NORMAL, NOTHING TO WORRY!!")
    
print("----------BODY MASS INDEX----------")
z = input("DO YOU KNOW YOUR HEIGHT IN METERS ? ")
if z=="yes" or z=="y" or z=="YES" or z=="Y":
    h = float(input("ENTER YOUR HEIGHT (in meters) : "))
elif z=="no" or z=="n" or z=="NO" or z=="N":
    h = float(input("ENTER YOUR HEIGHT (in centimeters) : "))
    h *=0.01
    h = h**2
    
x = input("\nDO YOU KNOW YOUR WEIGHT IN KGS ? ")
if x=="yes" or x=="y" or x=="YES" or x=="Y":
    m = float(input("ENTER YOUR WEIGHT (in kgs) : "))
elif x=="no" or x=="n" or x=="NO" or x=="N":
    m = float(input("ENTER YOUR WEIGHT (in pounds or lbs) : "))
    m *=0.454
    
bmi(m,h)
