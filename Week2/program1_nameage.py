"""
Purpose:Program that has two parameters namely name and their age.
And that tells them the year that they will turn 100 years old.
"""

print("What is your name? ")
name=input()
print("What is your age? ")
age=int(input())

#calculate the year the person will be 100 years old
#assume the current year is 2020
year=2020+(100-age)

print(name," will be 100 years old in the year ",year)
