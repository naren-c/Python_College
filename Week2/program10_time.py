"""
Given the integer N - the number of seconds that is passed since midnight -
how many full hours and full minutes are passed since midnight? The program
should print two numbers: the number of hours (between 0 and 23) and the
number of minutes (between 0 and 1339). For example, if N = 3900, then 3900
seconds have passed since midnight. Therefore, the time now is 1:05am. So the
program should print 1 65 -
1 full hour is passed since midnight, 65 full minutes passed since midnight.
"""
t = int(input("Enter the number of seconds passed since midnight: "))
hours = t//3600     #calculate number of hours by dividing t with 3600
minutes = ((t%3600)//60) #calculate number of minutes from remaining t
seconds = ((t%3600)%60) #gives remaining number of seconds
print("Hours=",hours)
print("Minutes=",minutes)
print("Seconds=",seconds)
