"""
String encoding 
i)the first letter of each word is printed at the end.
"""
s = "practice problems for students"

list1 = s.split() #converting value into a list
s1 = ""
for i in list1:
    s1 = s1 + i + i[0]+" "
print(s1)


#ii)After each character, a 'p' is added
list2=[]
for i in list1:
    x = ""
    for j in i:
        x = x + j + "p"
    list2.append(x)
print(" ".join(list2))


#b)reverse a string, input:nice place to study is library
value = "nice place to study is library"
list1 = value.split()
print("The given string is:",value)
x=[]
l = len(list1)
for i in range(l-1,-1,-1):
    x.append(list1[i])

print("The reversed string is:"," ".join(x))
