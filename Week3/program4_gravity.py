"""
Python Program to Find the Gravitational Force Acting Between Two Objects
"""
#read values of mass of object 1 and 2 and the distance between them
mass1 = float(input("Enter the value of mass of object 1 "))
mass2 = float(input("Enter the value of mass of object 2 "))
distance = float(input("Enter the distance between the two objects "))

g = 6.67*10**-11 #value of constant g

f = (g*(mass1*mass2))/(distance)**2 #formula to calculate the gravitational force

print("The gravitational force acting between the two objects is",f)
