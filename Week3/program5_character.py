"""
Write a program to read 4 characters separately  from the user. Convert
every character to its next alphabet.
"""
#reading the value of 4 characters
character1 = input("Enter any character ")
character2 = input("Enter any character ")
character3 = input("Enter any character ")
character4 = input("Enter any character ")

#incrementing the value of character1,character2,character3 and character4
#to the next character

character1 = chr(ord(character1)+1)
character2 = chr(ord(character2)+1)
character3 = chr(ord(character3)+1)
character4 = chr(ord(character4)+1) 

print("The incremented four characters are",character1,character2,character3,
      character4)
