name = "mohanDas Karamchand gandhi"
print(name)
name_list = name.split()

#1)m K gandhi
x = ""
for i in name_list[:2]:
    x = x+(i[0])+" "

print(x+name_list[2])


#2)M K GANDHI  
c = ""
for i in name_list[:2]:
    c = c+(i[0].upper())+" "
c = c+name_list[2].upper()
print(c)

#3)M K Gandhi   
b = c.title()
print(b)

#4)Mohandas Karamchand Gandhi
print(name.title())



s = "bad python bad teacher bad lecture"

#i)Replace all occurrences of bad to good
s1 = s.replace("bad","good")
print(s1)

#ii)Replace first occurrence of bad to good
s2 = s.replace("bad","good",1)
print(s2)

#iii)find the leftmost bad
s3 = s.find("bad",0)
print(s3)

#iv)find the second bad from left
s4 = s.find("bad",1)
print(s4)

#v)Replace the second bad to worst and display from that point of string and also display the whole string
list1 = s.split()
count = 0
ele = None
newstr = " "
for i in range(len(list1)):
    if list1[i]=="bad":
        count+=1
        ele = i
    if count == 2:
        break

list1[ele] = "worst"
print(newstr.join(list1))
newstr1 = " "
print(newstr1.join(list1[ele:]))

