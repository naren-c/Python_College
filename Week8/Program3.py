"""
Given a string write a user defined function to display the first longest string
with its length

"""




def find_len(str1):
    count = 0
    for j in str1:
        count = count+1
    return count
        
a = input("Enter a string to find the longest word ")
list1 = a.split()

max_len = -1
for i in list1:
    b = find_len(i)
    if b>max_len:
      max_len = b
      x = i

print(max_len,x)
