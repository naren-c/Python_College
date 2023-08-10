"""
Find length of the constructed list using a user defined function

"""

def length(list1):
    count = 0
    for i in list1:
        count=count+1

    return count


list1=[]

type1 = input("Enter the data type of the list elements: int, float ")
if type1 != "int" and type1 != "float":
    print("Invalid data type")
else:   
    x = int(input("Enter the element, enter s to quit: "))

    while x!='s':
        if type1 == "int":
            list1.append(int(x))
        elif type1 == "float":
            list1.append(float(x))
        x = input("Enter the element, enter s to quit: ")
    y = length(list1)
    print("The length of the list is ",y)
