"""
Purpose: Python program for the problem statement -
N students take K apples and distribute them among each other evenly.
The remaining (the undivisible) part remains in the basket. How many
apples will each single student get? How many apples will remain in
the basket?
"""
n = int(input("Enter the number of students "))
k = int(input("Enter the number of apples "))

v = k//n #number of apples each student will get
r = k%n #number of remaining apples

print("Number of apples each student gets = ",v)
print("Number of remaining apples = ",r)
