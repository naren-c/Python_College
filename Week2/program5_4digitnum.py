"""
Given a 4-digit integer number, display the individual digits & also
compute the sum of digits.
"""
num = int(input("Enter the four digit number: "))
fourthdigit = num%10 #gives the last digit of the number
num = num//10 #assigns a new value to num, excluding the last digit
thirddigit = num%10 #gives the third digit of the number
num = num//10 #assigns a new value to num, excluding the last two digit
seconddigit = num%10 #gives the second digit of the number
num = num//10#assigns a new value to num, excluding the last three digit
firstdigit = num%10

#calculates the sum of all digits
sum = firstdigit + seconddigit + thirddigit + fourthdigit   
print("First digit= ",firstdigit)
print("Second digit= ",seconddigit)
print("Third digit= ",thirddigit)
print("Fourth digit= ",fourthdigit)
print("The sum of digits in the number is", sum)
