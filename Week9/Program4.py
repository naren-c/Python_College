"""
Write a function mymap which takes a callback and an iterable, creates a list,
applies the callback to each element of the iterable and puts the result into
list and returns the list. mymap should mimic map.
Test this with the following calls.
a)Given a list of words, return a list of words with ing appended to it.
b)Given a list of words, return a list of tuples having the word and its length.

"""

def mymap(func,wlist):
    list1 = []
    for i in wlist:
        b = func(i)
        list1.append(b)
    return list1

def mymap1(str1):
    a = str1+"ing"
    return a


def mymap2(str1):
    return str1,len(str1)


    
my_list = ['skipp', 'jump', 'stretch', 'pull']

c = mymap(mymap1,my_list)
print(c)

d = mymap(mymap2,my_list)
print(d)
