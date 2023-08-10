"""
Python Program to Clear the Rightmost Set Bit of a Number
"""
#read a value of a number
a = int(input("Enter the value of a number whose rightmost bit needs to be cleared: "))
print("The binary value of",a,"is",bin(a)) 
b = a>>1 #right shifting the value of a to clear the rightmost bit
b = b<<1 #left shifting value of b to bring back all bits to original position

print("Binary value of the number after clearing the rightmost bit is",bin(b))
