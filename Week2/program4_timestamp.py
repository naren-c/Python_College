"""
Given two timestamps of the same day: a number of hours, minutes and
seconds for both of the timestamps. Calculate how many seconds passed
between them.
"""
h1 = int(input("Enter hour value for timestamp 1: "))
m1 = int(input("Enter minute value for timestamp 1: "))
s1 = int(input("Enter second for timestamp 1: "))
h2 = int(input("Enter hour value for timestamp 2: "))
m2 = int(input("Enter minute value for timestamp 2: "))
s2 = int(input("Enter second value for timestamp 2: "))

#finding the difference between two timestamps by converting
#both the timestamps into seconds
seconds = (((h2*3600)+(m2*60)+s2)-((h1*3600)+(m1*60)+s1)) 
print("The difference in timestamp is",seconds, "seconds")
