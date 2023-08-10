values = [("Rashma",8105731555,"rashma@gmail.com","bangalore"),
         ("Saritha",9582161900,"saritha@gmail.com","Mangalore"),
         ("Bharathi",9276895311,"bharathi@yahoo.com","Coimbatore"),
         ("deepthi",8976885553,"deepthi@gmail.com","bangalore"),
         ("kakoli",8816121598,"kakili@gmail.com","dispur")]

d = dict(enumerate(values,1)) #raed values to dictionary one by one
print("The phone book is \n",d,"\n")

# i) Add new number to phone book
#adding the new value at the end of the dictionary
d[len(d)+1] = [('sreenath', 9872345670, 'sreenath@pes.edu', 'kolar')]
print("The phone book after adding a new number to the phone book is \n",d,"\n")



# ii) Delete an entry based on the key entered by user

key = int(input("Enter the phone book entry to be deleted "))
if key in d: #condition to check if input key is present in the dictionary
    del d[key] #deleting key from dictionary
else:
    print("Key not found")
    
print("After deleting key from the phone book, the phone book is \n",d)





