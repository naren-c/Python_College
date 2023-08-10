def func(outer):
    x = outer()
    print("nth Fibonnaci number= ",x)

@func
def outer():
    a=1
    b=1
    n = int(input("Enter n to find nth Fibonnaci number: "))
    for i in range(2,n):
        a,b = b,b+a
    return b

print(outer)
