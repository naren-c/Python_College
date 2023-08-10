def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

Str = input("Enter a string ")
print(reverse(Str))




def towerofHanoi(n, source, destination, aux):
    if n==1:
        print("move disc 1 from", source, "tower", destination, "tower")
        return
    towerofHanoi (n-1, source, aux, destination)
    print("Move disc ",n,"from",source,"tower",destination,"tower")
    towerofHanoi(n-1,aux,destination,source)

num = int(input("Enter number of discs "))
towerofHanoi(num,"left","right","middle")




def power(n,b):
    if n==0:
        return 1
    else:
        return b*power(n-1,b) 


n = int(input("Enter the value of power "))
b = int(input("Enter the value of base "))
a = power(n,b)
print(a)






                  
