"""
Write a Python program which accepts the radius of a sphere and computes
the volume and surface area of a sphere.
"""
radius = float(input("Enter the value of radius of a sphere "))

volume = (4/3)*3.14*radius**3 #formula to compute volume of sphere
surface_area = 4*3.14*radius**2 #formula to compute surface area of sphere

print("The volume of the sphere of radius ",radius,"is {:.2f}".format(volume))
print("The surface area of the sphere of radius",radius,"is {:.2f}".format(surface_area))

