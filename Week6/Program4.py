"""
Read movie data from mov1.csv file. CSV file mov1.csv has three columns c1 has
year,c2 has rating,c3 has movie name.
"""


file1 = open('mov1.csv','r') #opening file mov1.csv in read mode
x = file1.read() #reading the entire contents of the file
print(x)
file1.close()

"""
write the year of release and movie name from mov1.csv to a text file
"""

file2 = open('mov1.csv','r')
file3 = open('newmov1.txt','w') #creating a new file to store the values year of release and movie name

#read one line at a time, extract the year of release and movie name and
#write these values to the file newmov1.txt
line = file2.readline() 
while line:
    line = line.strip() #remove extra characters and \n
    y = line.split(',') 
    print(y[0],y[-1], file = file3) #write year of release and movie name to file newmov1.txt
    line = file2.readline()

# close the files
file2.close()
file3.close()
