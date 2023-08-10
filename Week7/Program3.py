def double(x):
    x = 2*x
    print("The value of the given number, doubled is",x)

def triple(y):
    y = 3*y
    print("The value of the given number, tripled is",y)

def find(z,num):
    z(num)

a = int(input("Enter a given number "))
find(double,a)
find(triple,a)

