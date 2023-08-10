"""
To find the simple interest for given inputs by the user
"""
#read the values of principal amount, rate and time from the user
p = float(input("Enter the value for principal amount")) 
r = float(input("Enter the value for rate"))
t = int(input("Enter the number of years"))

si = (p*r*t)/100 #formula to calculate the simple interest

print("The simple interest for the principal amount",p,
      "for rate",r,"years",t,"is equal to",si)
