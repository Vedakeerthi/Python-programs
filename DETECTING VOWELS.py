vowels_list = ['a','e','i','o','u','A','E','I','O','U']
st = input("ENTER A STRING : ")
vowels_s=[]
vowels=0
for i in st:
    for j in vowels_list:
        if i==j:
            vowels=vowels+1
            vowels_s.append(i)
        

print("THE NUMBER OF VOWELS IN THE GIVEN STRING IS : ",vowels )
print("THE VOWELS IN THE GIVEN STRING ARE : ",vowels_s)