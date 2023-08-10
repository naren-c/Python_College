x=input("Enter the comma separated values ")
print(x)

#using split function to separate the input values
y=list(x.split(','))
print("The comma separated list is",y)

z=tuple(x.split(','))
print("The comma separated tuple is",z)
