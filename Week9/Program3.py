"""
a)Given a list of tuples containing two integers, remove all tuples where
second element in tuple is not a factor of first element.
b)Find intersection of two given lists
"""

l=[(10,2), (4, 3), (12, 4), (15, 4), (24, 5)]

def factor(b):
    if b[0]%b[1] == 0:
        return 1
    else:
        return 0

x = list(filter(lambda a:factor(a),l))
print(x)




c = [10, 11, 12, 14, 16, 18, 20]
d = [10, 20, 16, 18, 19]


y = list(filter(lambda e: e in c,d))
print(y)
