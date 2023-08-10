"""
Suppose the cover price of a book is $24.95, but bookstores get a 40%
discount. Shipping costs $3 for the first copy and 75 cents for each
additional copy. What is the total wholesale cost for 60 copies?
"""
#read the number of books
number = int(input("Enter the number of books to be shipped "))

coverprice = 24.95 #defining the cover price of each copy

#computing total price of the 60 books
total_price = (coverprice-(coverprice*0.4))*number+(3+(number-1)*0.75)

print("The total wholesale cost of",number,"number of books is equal to ${:.2f}"
      .format(total_price))
