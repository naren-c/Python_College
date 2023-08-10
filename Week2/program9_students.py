"""
Given the number of students in each class, print the smallest possible number
of desks that can be purchased. Given that two people can sit on each bench
"""
a = int(input("Enter the number of students in section A "))
b = int(input("Enter the number of students in section B "))
c = int(input("Enter the number of students in section C "))

"""
if 'a' is the number of students in a class, then 
a//2 will give the total number of benches required,
with two students in each bench
a % 2 will give the extra bench required if the number
of students is an odd number
"""
numa = (a//2)+(a%2)   
numb = (b//2)+(b%2)
numc = (c//2)+(c%2)
print("Number of benches for A=",numa)
print("Number of benches for B=",numb)
print("Number of benches for C=",numc)
