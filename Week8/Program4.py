"""
Create integer list, write user defined function to sort in descending order

"""

def bubble_sort(list1):
    for j in range(n-1):
        for k in range(0,n-j-1):
            if list1[k] > list1[k+1]:
                temp = list1[k]
                list1[k] = list1[k+1]
                list1[k+1] = temp
            
    print("The list after sorting is ",list1)

list1=[]
n = int(input("Enter the number of elements in the list "))

for i in range(n):
    x = int(input("Enter the element: "))
    list1.append(x)
print("Before sorting the list is ",list1)

bubble_sort(list1)

