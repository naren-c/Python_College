"""
Program to
a)Convert temperature in celsius to fahrenheit
b)Convert temperature in fahrenheit to celsius
"""
c = float(input("Enter the value of temperature in Celsius "))
f = (c*9/5)+32    #using Fahrenheit to Celsius formula

print(c,"degree Celsius is equal to",f,"degree Fahrenheit")

f = float(input("Enter the value of temperature in Fahrenheit "))
c = (f-32)*5/9    #using Celsius to Fahrenheit formula
print(f,"degree fahrenheit is equal to",c,"degree Celsius")
