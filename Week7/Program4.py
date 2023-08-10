def increment(x,n):
    def increment1():
        print(x+(n*5))
    return increment1
x = int(input("Enter the given number "))
n = int(input("Enter the number of times the number should be incremented by 5 "))
y = increment(x,n)
y()


def root(u,v):
    def nth_root():
        print((u)**(1/v))
    return nth_root
u = int(input("Enter the given number "))
v = int(input("Enter the root value "))
w = root(u,v)
w()
