"""
Given the distance between 2 cities in kilometers. A program to convert it
into meters, centimeters, feet and inches and display the result.
"""
distance = float(input("Enter the distance between two points in kilometers "))
meter = distance*1000 #converting kilometer into meter
centimeter = meter*100 #converting kilometer into centimeters using meters
feet = 3.2808399*meter #converting kilometer into feet using meters
inches = 39.3700787*meter #converting kilometer into inches using meters
print("Distance in meters= ",meter)
print("Distance in centimeter= ",centimeter)
print("Distance in feet= ",feet)
print("Distance in inches= ",inches)

