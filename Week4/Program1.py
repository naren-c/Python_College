#Fibonacci Series
n = int(input("Enter the number of terms in Fibonacci series "))

fib1 = 0 #assigning first term in Fibonacci as 0
fib2 = 1 #assigning first term in Fibonacci as 1
print(fib1)
print(fib2)
i = 3 #Set counter as 3 as two terms are already printed 

while i<=n:
    fib3 = fib1+fib2 #assign next fibonacci term as the sum of previous two terms
    print(fib3)
    #changing values of fib1 and fib2 to the next values
    fib1 = fib2 
    fib2 = fib3
    i+=1


#Factorial of a number

m = int(input("Enter a positive number to find its factorial "))

j = 1 #counter
factorial = 1 #assigning factorial as 1, as 0 and 1 factorial is 1

while j<=m:
    factorial = factorial*j #calculating factorial
    j+=1
print("The factorial of the number is",factorial)


#Prime numbers

p = int(input("Enter a positive number to print all prime number "))

print("Prime numbers between 2 to",p,"are")
for num in range(2,p):
    k = 2 
    isPrime = True #assuming all numbers to be prime
    while k<num:
        if num%k == 0:  
            isPrime = False #segregating prime numbers from non prime numbers
            break
        k+=1
    if(isPrime):
        print(num)
