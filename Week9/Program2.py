"""
Write a Write a Python program using map/reduce/filter and lambda.
a)To find palindromes in a given list of strings
b) Given a list of strings, remove all strings having first character as digit
"""

x = ['ws3sw', 'C++', 'Python', 'ada', 'daa', 'FAAF']

def palindrome(str1):
    list1 = list(str1)
    list2=[]
    n = len(list1)
    for i in range(n-1,-1,-1):
        list2.append(list1[i])
    s = ""
    str2 = s.join(list2)
    if str1 == str2:
        return 1
    else:
        return 0

y = list(filter(lambda p:palindrome(p),x))
print(y)



w = ['DIGICOM', '4GB', 'RAM', '16TB', 'HD', 'LCD']

def digit(w):
    if w[0] in ["0","1","2","3","4","9"]:
        return 0
    else:
        return 1

v = list(filter(lambda d: digit(d),w))
print(v)
