"""
WAP to create a homogeneous list and define a user defined function to find
maximum in a given list of data
"""

"""

Step 1: Start
Step 2: Create empty list called list1
Step 3: Read integer values to list
Step 4: set max = list1[0]
Step 5: for i in list:
           if i > max:
              max = i
Step 6: Print the value of max 

"""

def max1(list1):
    max = list1[0]
    for i in list1:
        if i > max :
            max = i
    return max

list1 = []
num = int(input("Enter an integer number "))
while num > -1:
    list1.append(num)
    num = int(input("Enter an integer number (to stop input a negative value) "))
   
print("The maximum value in the list is", max1(list1))
