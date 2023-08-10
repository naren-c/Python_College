"""
Write a Python program 
A) To get a single random character from a specified string.
B) Write a program to:
i) shuffle students in a class. (Assume no of students in a class are 10)
ii) to choose one student who would become a Class representative.
iii) to create a random sample of size 2 from the available number of population who are the potential candidates to become event coordinators. 
C) Calculate multiplication of two random float numbers
D) To generate a floating-point number within a range.
E) Generates a random integer number from the given range.
F) To generate the same random number every time.
G) Roll a dice in such a way that every time you get the same number.
"""
import random

#A
x = input("Enter a string ")
print(random.choice(x))

#B) Let students in the class be represented by roll numbers from 1 to 10

# i)
students = [1,2,3,4,5,6,7,8,9,10]
(random.shuffle(students))
print(students)

# ii)
print(random.choice(students))

#iii)
print(random.sample(students,2))

#C
f1 = (random.random())
f2 = (random.random())
f = f1*f2
print(f)

#D
x = int(input("Enter the start range "))
y = int(input("Enter the end range "))
print(random.uniform(x,y))

#E
a = int(input("Enter the start range "))
b = int(input("Enter the end range "))
print(random.randint(a,b))

#F
random.seed(3)
print(random.randint(1,10))
random.seed(3)
print(random.randint(1,10))

#F using for loop
for i in range(2):
    random.seed(3)
    print(random.randint(1,10))

#G
x = int(input("Enter the number of times the dice should be rolled "))
for i in range(x):
    random.seed(3)
    print(random.randint(1,6))

