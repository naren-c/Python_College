"""
Program to calculate the distance between two points.
"""
import math
x1 = int(input("Enter the x coordinate value for point 1 "))
y1 = int(input("Enter the y coordinate value for point 1 "))
x2 = int(input("Enter the x coordinate value for point 2 "))
y2 = int(input("Enter the y coordinate value for point 2 "))

#using distance formula
distance = float(math.sqrt((x1-x2)**2+(y1-y2)**2))

print("The distance between the two points is ",distance)
      
