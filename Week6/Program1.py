x = int(input("Enter a number till when you want to find its cube to "))
d = dict() #creating anew dictionary

for i in range(1,x+1): 
    d[i] = pow(i,3) #using pow function to find cube of the number

print(d)
