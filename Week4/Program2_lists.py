#A
l1=[1,2,"hello",(5,8,9),10.5,[6,7],3.5,(1,2,3),[11,12],{23,34},"aaa"]

#creating empty lists for every data type
l_int = []
l_float = []
l_str = []
l_tuple = []
l_list = []
l_set = []

#checking data type of elements
for i in l1:
    c = type(i)
    if(c == int):
        l_int.append(i)
    elif(c == float):
        l_float.append(i)
    elif(c == str):
        l_str.append(i)
    elif(c == tuple):
        l_tuple.append(i)
    elif(c == list):
        l_list.append(i)
    elif(c == set):
        l_set.append(i)

print("List of integers",l_int)
print("List of floating point numbers",l_float)
print("List of strings",l_str)
print("List of tuples",l_tuple)
print("List of lists",l_list)
print("List of sets",l_set)


#B

strlist=['aaa','xxx','bbb','abs','xyz','bcd']
numlist=[23,12,34,56,26,33,22]

#organising list in ascending and descending order respectively	   
strlist.sort()
print("The string in ascending order is",strlist)
strlist.sort(reverse=True)
print("The string in descending order is",strlist)
	   
numlist.sort()
print("The numbers in ascending order is",numlist)
numlist.sort(reverse=True)
print("The numbers in descending order is",numlist)
	   
