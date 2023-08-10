"""
WAP to create a homogeneous list and define a user defined function to find
minimum in a given list of data
"""



def min1(list1):
    min = list1[0]
    for i in list1:
        if i < min :
            min = i
    return min

list1 = []
num = int(input("Enter an integer number "))
while num > -1:
    list1.append(num)
    num = int(input("Enter an integer number (to stop input a negative value) "))
   
print("The minimum value in the list is", min1(list1))
