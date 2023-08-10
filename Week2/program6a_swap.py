"""
Swap the contents of two memory locations using temporary variable.
"""
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
print("Value of x and y before swapping are",x,y,"respectively")
temp = x  #assigning value of x to temporary variable
x = y     #assigning value of y to x
y = temp  #assignig value of temporary variable to y
print("Value of x and y after swapping are",x,y,"respectively")

"""
Swap the contents of two memory locations without using temporary
variable.
"""
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
print("Value of x and y before swapping are",x,y,"respectively")
x = x-y
y = x+y
x = y-x
print("Value of x and y after swapping are",x,y,"respectively")
