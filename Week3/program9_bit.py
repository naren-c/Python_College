"""
Python Program to Clear the Rightmost Set Bit of a Number
"""
#read a value of a number
a = int(input("Enter the value of a number whose rightmost bit needs to be cleared: "))
bit = int(input("Enter the bit to clear: "))
value = a & ~(1<<bit)
print(bin(a))
print(bin(value))


