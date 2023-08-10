"""
Program to Swap the contents of two memory locations using bitwise
XOR operation.
"""
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))

print("The value of a and b before swapping are",a,b,"respectively")

a = a^b
b = a^b
a = b^a

print("The value of a and b after swapping are",a,b,"respectively")

